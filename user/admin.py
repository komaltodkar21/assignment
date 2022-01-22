from django.contrib import admin
from user.models import User, Post

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','username','email','password')
admin.site.register(User,UserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display=('id','text','created_at','updated_at')
admin.site.register(Post,PostAdmin)