from django.contrib import admin
from .models import User, ClubMember, Project, ProjectMember


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'last_name',
        'first_name',
        'student_code',
        'course',
        'major',
        'phone_number',
        'gender',
        'created_at',
    )
    list_display_links = ('id', 'last_name', 'first_name')
    search_fields = (
        'last_name',
        'first_name',
        'student_code',
        'major',
        'phone_number',
    )
    list_filter = ('gender', 'course', 'major', 'created_at')
    ordering = ('id',)
    list_per_page = 20


@admin.register(ClubMember)
class ClubMemberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_last_name',
        'get_first_name',
        'get_student_code',
        'joined_at',
    )
    list_display_links = ('id', 'get_last_name', 'get_first_name')
    search_fields = (
        'user__last_name',
        'user__first_name',
        'user__student_code',
        'bio',
    )
    list_filter = ('joined_at',)
    ordering = ('id',)
    list_per_page = 20

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Овог'
    get_last_name.admin_order_field = 'user__last_name'

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'Нэр'
    get_first_name.admin_order_field = 'user__first_name'

    def get_student_code(self, obj):
        return obj.user.student_code
    get_student_code.short_description = 'Оюутны код'
    get_student_code.admin_order_field = 'user__student_code'


class ProjectMemberInline(admin.TabularInline):
    model = ProjectMember
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('status',)
    ordering = ('id',)
    list_per_page = 20
    inlines = [ProjectMemberInline]


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_last_name',
        'get_first_name',
        'get_student_code',
        'get_project_title',
        'role',
    )
    list_display_links = ('id', 'get_last_name', 'get_first_name')
    search_fields = (
        'member__user__last_name',
        'member__user__first_name',
        'member__user__student_code',
        'project__title',
        'responsibility',
    )
    list_filter = ('role', 'project')
    ordering = ('id',)
    list_per_page = 20

    def get_last_name(self, obj):
        return obj.member.user.last_name
    get_last_name.short_description = 'Овог'
    get_last_name.admin_order_field = 'member__user__last_name'

    def get_first_name(self, obj):
        return obj.member.user.first_name
    get_first_name.short_description = 'Нэр'
    get_first_name.admin_order_field = 'member__user__first_name'

    def get_student_code(self, obj):
        return obj.member.user.student_code
    get_student_code.short_description = 'Оюутны код'
    get_student_code.admin_order_field = 'member__user__student_code'

    def get_project_title(self, obj):
        return obj.project.title
    get_project_title.short_description = 'Төсөл'
    get_project_title.admin_order_field = 'project__title'