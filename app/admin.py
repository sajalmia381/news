from django.contrib import admin

# Register your models here.
from .models import Author, Category, Article, Comments

class Author_admin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['__str__']
    class Meta:
        Molel = Author
admin.site.register(Author, Author_admin)

class Category_admin(admin.ModelAdmin):
    search_fields = ['__str__']
    list_display = ['__str__']
    class Meta:
        Model = Category
admin.site.register(Category, Category_admin)

class Article_admin(admin.ModelAdmin):
    search_fields = ['__str__', 'title', 'posted_on']
    list_per_page = 10
    list_filter = ['posted_on', 'category']
    list_display = ['__str__', 'posted_on']
    class Meta:
        model = Article
admin.site.register(Article, Article_admin)

class Comments_admin(admin.ModelAdmin):
    search_fields = ['__str__', 'comment']
    list_display = ['__str__', 'email']
    list_per_page = 10
    list_filter = ['article_id']
    class Meta:
        model = Comments
admin.site.register(Comments, Comments_admin)