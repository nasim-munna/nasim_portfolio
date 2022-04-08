from django.contrib import admin
from .models import Client, Contact,Post, Testimonial,Work,Cv

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']

admin.site.register(Contact,ContactAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']
  
admin.site.register(Post, PostAdmin)

class WorkAdmin(admin.ModelAdmin):
    list_display= ('title','url')

admin.site.register(Work,WorkAdmin)

admin.site.register(Cv)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('image', 'url')
    search_fields = ['image', 'url']
  
admin.site.register(Client, ClientAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ['name', 'designation']
  
admin.site.register(Testimonial, TestimonialAdmin)