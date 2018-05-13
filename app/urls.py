
from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('blog_details/<int:id>', views.Blog_details.as_view(), name='blog_details'),
    path('create_blog', views.Create_blog.as_view(), name='create_blog'),

    # ============== Author
    path('author_post/<name>', views.Author_post.as_view(), name='author_post'),
    path('author_dashboard/<name>', views.Author_dashboard.as_view(), name='author_dashboard'),
    path('new_admin', views.New_admin.as_view(), name='new_admin'),
    path('login', views.Login_admin.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),

    # ================== Category
    path('category_all', views.Category_all.as_view(), name='category_all'),
    path('single_category/<name>,', views.Single_category.as_view(), name='single_category'),
    path('create_category', views.Create_category.as_view(), name='create_category'),
    path('edit_category/<name>', views.Edit_category.as_view(), name='edit_category'),
    path('delete_category/<name>', views.Delete_category.as_view(), name='delete_category'),
]