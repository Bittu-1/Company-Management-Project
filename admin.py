from django.contrib import admin
from CMSApp.models import Department, Employee, Project
from django.utils.html import format_html

# Register your models here.


@admin.register(Department)
class DepartmentAdminPage(admin.ModelAdmin):
    fields = ['departmentname', 'isactive']

    list_display = ['departmentname',  'isactive',  'edit', 'delete']
    list_filter = ['departmentname', 'isactive']

    def edit(self, obj):
        return format_html(f'<a href="{obj.departmentid}/change/" style="color:red;"><i class="fa fa-edit"></i></a>')

    def delete(self, obj):
        return format_html(f' <a href="{obj.departmentid}/delete/"<button style="color:Blue;"><i class="fa fa-trash"></i></button>')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'department', 'isactive']
    list_display = ['name', 'email', 'dateofjoining',
                    'isactive', 'edit', 'delete']
    list_filter = ['name', 'department']

    def edit(self, obj):
        return format_html(f'<a href="{obj.employeeid}/change" style="color:red;"><i class="fa fa-edit"></i></a>')

    def delete(self, obj):
        return format_html(f' <a href="{obj.employeeid}/delete/"<button style="color:Blue;"><i class="fa fa-trash"></i></button>')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ['projectname', 'project_end_date',
              'project_manager_name', 'project_manager_email']
    list_display = ['projectname', 'project_start_date', 'project_end_date',
                    'edit', 'delete']
    list_filter = ['projectname']

    def edit(self, obj):
        return format_html(f'<a href="{obj.projectid}/change" style="color:red;"><i class="fa fa-edit"></i></a>')

    def delete(self, obj):
        return format_html(f' <a href="{obj.projectid}/delete/"<button style="color:Blue;"><i class="fa fa-trash"></i></button>')
