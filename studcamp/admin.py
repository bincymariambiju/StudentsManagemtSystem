from django.contrib import admin
from . models import Contact,Signup,Course,Staff,Feedback,Session


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone","desc")

admin.site.register(Contact)
class SignupAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone","qualification","course","password","cpassword")

admin.site.register(Signup)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("cid","cname","duration","fee")

admin.site.register(Course)
class Staffdmin(admin.ModelAdmin):
    list_display = ("sid","sname","email","phone","address","qualification","subject","salary")

admin.site.register(Staff)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name","email","desc")

admin.site.register(Feedback)

class SessionAdmin(admin.ModelAdmin):
    list_display = ("session","shr","msg")

admin.site.register(Session)




