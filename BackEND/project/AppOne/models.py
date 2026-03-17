from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)

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
        db_table = "users"


class ClubMember(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='club_member',
        verbose_name='Хэрэглэгч'
    )
    course = models.PositiveIntegerField(verbose_name='Курс')
    joined_at = models.DateField(verbose_name='Клубт элссэн огноо')
    bio = models.TextField(blank=True, null=True, verbose_name='Товч танилцуулга')

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"

    class Meta:
        verbose_name = "Клубийн гишүүн"
        verbose_name_plural = "Клубийн гишүүд"
        db_table = "club_members"


class Project(models.Model):
    id = models.AutoField(primary_key=True)

    PROJECT_STATUS_CHOICES = [
        ('planning', 'Төлөвлөж байгаа'),
        ('ongoing', 'Хийгдэж байгаа'),
        ('completed', 'Дууссан'),
    ]

    title = models.CharField(max_length=200, verbose_name='Төслийн нэр')
    description = models.TextField(verbose_name='Төслийн тайлбар')
    status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS_CHOICES,
        default='planning',
        verbose_name='Төслийн төлөв'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Төсөл"
        verbose_name_plural = "Төслүүд"
        db_table = "projects"


class ProjectMember(models.Model):
    id = models.AutoField(primary_key=True)

    ROLE_CHOICES = [
        ('leader', 'Багийн ахлагч'),
        ('backend', 'Backend хөгжүүлэгч'),
        ('frontend', 'Frontend хөгжүүлэгч'),
        ('fullstack', 'Full Stack хөгжүүлэгч'),
        ('designer', 'UI/UX дизайнер'),
        ('tester', 'Тестлэгч'),
        ('pm', 'Төслийн менежер'),
        ('other', 'Бусад'),
    ]

    member = models.ForeignKey(
        ClubMember,
        on_delete=models.CASCADE,
        related_name='project_members',
        verbose_name='Гишүүн'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_members',
        verbose_name='Төсөл'
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        verbose_name='Үүрэг'
    )
    responsibility = models.TextField(
        blank=True,
        null=True,
        verbose_name='Хариуцсан ажил'
    )

    def __str__(self):
        return f"{self.member} - {self.project} ({self.get_role_display()})"

    class Meta:
        verbose_name = "Төслийн гишүүн"
        verbose_name_plural = "Төслийн гишүүд"
        db_table = "project_members"
        unique_together = ('member', 'project', 'role')