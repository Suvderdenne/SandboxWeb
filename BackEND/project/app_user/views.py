import json
import random
from datetime import timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.mail import send_mail
from .models import User


# OTP үүсгэх
def generate_otp():
    return str(random.randint(100000, 999999))


# Email илгээх
def send_otp_email(email, otp):
    send_mail(
        'Баталгаажуулах код',
        f'Таны баталгаажуулах код: {otp}',
        'mandahmts@gmail.com',
        [email],
        fail_silently=False,
    )


@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User.objects.create_user(
                phone_number=data['phone_number'],
                password=data['password'],
                email=data['email'],  # 🔥 email нэмсэн
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', ''),
                age=data.get('age'),
                gender=data.get('gender', ''),
                course=data.get('course', ''),
                major=data.get('major', ''),
                student_code=data.get('student_code', ''),
                skills=data.get('skills', '')
            )
            return JsonResponse({'message': 'User created successfully', 'user_id': user.id}, status=201)
        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def signin_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']

            user = User.objects.filter(email=email).first()

            if user is None:
                return JsonResponse({'error': 'User not found'}, status=404)

            if not user.check_password(password):
                return JsonResponse({'error': 'Invalid password'}, status=401)

            # 🔥 Хэрэв баталгаажаагүй бол OTP илгээнэ
            if not user.is_verified:
                otp = generate_otp()
                user.otp_code = otp
                user.otp_created_at = timezone.now()
                user.save()

                send_otp_email(user.email, otp)

                return JsonResponse({
                    'message': 'OTP sent to email',
                    'requires_verification': True
                }, status=200)

            return JsonResponse({
                'message': 'Login successful',
                'user_id': user.id
            }, status=200)

        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def verify_otp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data['email']
            otp = data['otp']

            user = User.objects.filter(email=email).first()

            if user is None:
                return JsonResponse({'error': 'User not found'}, status=404)

            # ⏱ OTP 5 минут хүчинтэй
            if user.otp_created_at + timedelta(minutes=5) < timezone.now():
                return JsonResponse({'error': 'OTP expired'}, status=400)

            if user.otp_code != otp:
                return JsonResponse({'error': 'Invalid OTP'}, status=400)

            user.is_verified = True
            user.otp_code = None
            user.save()

            return JsonResponse({'message': 'Verified successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)