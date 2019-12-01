from django.contrib import admin

from .models import (
    category ,
    post ,
    comment ,
)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title' ,'content' ,'num_viwes' ,'timestamp' ,'categories')
    lis_display_link = ('image')
    list_filter = ('user', 'title' ,'content' ,'num_viwes' ,'timestamp' ,'category')
    search_fields = ['category' , 'title' , 'user']
    list_per_page =15

    def categories(self, obj):
        return " , ".join([c.category for c in obj.category.all()])



class CategoryAdmin(admin.ModelAdmin):
    list_display =('category' ,)
    list_filter = ('category' ,)
    search_fields = ('category' ,)
    list_per_page = 15

class CommentAdmin(admin.ModelAdmin):
    list_display =('user' , 'post' , 'txt' ,'timestamp')
    list_filter = ('user' , 'post' , 'txt' ,'timestamp')
    list_per_page =15
    search_fields =('user' , 'post' , 'txt' ,'timestamp')

admin.site.register(post ,PostAdmin)
admin.site.register(category ,CategoryAdmin)
admin.site.register(comment ,CommentAdmin)
