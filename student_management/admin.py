from django.contrib import admin
from .models import Employee
# Register your models here.
admin.site.site_header = "Employee ManageMent"
admin.site.site_title ="Employee ManageMent"
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name","dob","empId","email","mobileNo")
    search_fields=("full_name","firstName", "lastName","dob","empId","email","mobileNo")
    list_filter = ("project",)

    def full_name(self,obj):
        return f"{obj.firstName} {obj.lastName}"