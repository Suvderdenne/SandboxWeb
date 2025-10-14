from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Эр'),
        ('F', 'Эм'),
    ]

    last_name = models.CharField(max_length=50, verbose_name="Овог")
    first_name = models.CharField(max_length=50, verbose_name="Нэр")
    age = models.PositiveIntegerField(verbose_name="Нас")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Хүйс")
    phone_number = models.CharField(max_length=20, verbose_name="Утасны дугаар")
    course = models.PositiveIntegerField(verbose_name="Курс")
    major = models.CharField(max_length=100, verbose_name="Мэргэжил")
    student_code = models.CharField(max_length=20, unique=True, verbose_name="Оюутны код")
    skills = models.TextField(blank=True, null=True, verbose_name="Чадварууд")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Бүртгэгдсэн огноо")

    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.student_code}"

    class Meta:
        verbose_name = "Оюутан"
        verbose_name_plural = "Оюутнууд"
