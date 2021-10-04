from django.contrib import admin
from .models import Student_information

# admin.site.register(Student_information)





class Student_informationAdmin(admin.ModelAdmin):

      list_per_page = 15
list_display = ['Name','RollNo', 'address', 'Branch', 'CGPA']
    


admin.site.register(Student_information,Student_informationAdmin)




