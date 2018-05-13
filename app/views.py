from django.shortcuts import render, get_object_or_404, redirect

from .models import Author, Category, Article, Comments
from .forms import New_admin_form, Comments_form, Create_category_form, Article_form

from django.contrib.auth.models import User

# login
from django.contrib.auth import authenticate, login, logout

# Message
from django.contrib import messages

# paginator
from django.core.paginator import Paginator

# Search
from django.db.models import Q

from django.views import View
# Create your views here.
class Index(View):
    template_name = 'index.html'
    def get(self, request):
        post = Article.objects.all()

        # paginator
        paginator = Paginator(post, 8)
        page = request.GET.get('page')
        paginate = paginator.get_page(page)

        search = request.GET.get('searching')
        if search:
            post = post.filter(
                Q(title__icontains=search)
            )

        context = {
            'post': paginate,
        }
        return render(request, self.template_name, context)

class Blog_details(View):
    template_name = 'blog_details.html'
    def get(self, request, id):
        post = get_object_or_404(Article, pk=id)
        first = Article.objects.first()
        last = Article.objects.last()
        comment = Comments.objects.filter(article_id=id)
        form = Comments_form(request.POST or None)
        related = Article.objects.filter(category=post.category).exclude()[:4]
        context = {
            'post': post,
            'first': first,
            'last': last,
            'form': form,
            'comment': comment,
            'related': related
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        post = get_object_or_404(Article, pk=id)
        form = Comments_form(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_id = post
            instance.save()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

class Create_blog(View):
    template_name = 'create_blog.html'
    def get(self, request):
        if request.user.is_authenticated:
            user = get_object_or_404(Author, current_user= request.user.id)
            form = Article_form(request.POST or None, request.FILES or None)
            context = {
                'user': user,
                'form': form
            }
            return render(request, self.template_name, context)
    def post(self, request):
        if request.user.is_authenticated:
            user = get_object_or_404(Author, current_user= request.user.id)
            form = Article_form(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.article_author = user
                instance.save()
                messages.success(request, 'new Post Created')
                return redirect('blog:index')
            context = {
                'user': user,
                'form': form
            }
            return render(request, self.template_name, context)


# Author

class Author_post(View):
    template_name = 'author_post.html'
    def get(self, request, name):
        post_author = get_object_or_404(User, username=name)
        auth = get_object_or_404(Author, current_user=post_author.id)
        post = Article.objects.filter(article_author=auth.id)
        context = {
            'auth': auth,
            'post': post
        }
        return render(request, self.template_name, context)

class Author_dashboard(View):
    template_name = 'author_dashboard.html'
    def get(self, request, name):
        post_author = get_object_or_404(User, username=name)
        auth = get_object_or_404(Author, current_user=post_author.id)
        post = Article.objects.filter(article_author=auth.id)
        context = {
            'auth': auth,
            'post': post
        }
        return render(request, self.template_name, context)

class New_admin(View):
    template_name = 'new_admin.html'
    def get(self, request):
        form = New_admin_form(request.POST or None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = New_admin_form(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('blog:index')
        return render(request, self.template_name, {'form': form})

class Login_admin(View):
    template_name = 'login.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:index')
        else:
            if request.POST:
                user = request.POST.get('user')
                password = request.POST.get('pass')
                auth = authenticate(request, username=user, password=password)
                if auth is not None:
                    login(request, auth)
                    return redirect('blog:index')
        return render(request, self.template_name)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:index')


# category

class Category_all(View):
    template_name = 'category.html'
    def get(self, request):
        post = Category.objects.all()
        return render(request, self.template_name, {'post': post})

class Single_category(View):
    template_name = 'single_category.html'
    def get(self, request, name):
        cat = get_object_or_404(Category, name=name)
        post = Article.objects.filter(category=cat)
        context = {
            'post': post
        }
        return render(request, self.template_name, context)

class Create_category(View):
    template_name = 'create_category.html'
    def get(self, request):
        if request.user.is_staff or request.user.is_superuser:
            form = Create_category_form(request.POST or None)
            return render(request, self.template_name, {'form': form})
    def post(self, request):
        if request.user.is_staff or request.user.is_superuser:
            form = Create_category_form(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return redirect('blog:category_all')
            return render(request, self.template_name, {'form': form})

class Edit_category(View):
    template_name = 'create_category.html'
    def get(self, request, name):
        if request.user.is_staff or request.user.is_superuser:
            category_id = get_object_or_404(Category, name=name)
            form = Create_category_form(request.POST or None, instance=category_id)
            return render(request, self.template_name, {'form': form})

    def post(self, request, name):
        if request.user.is_staff or request.user.is_superuser:
            category_id = get_object_or_404(Category, name=name)
            form = Create_category_form(request.POST or None, instance=category_id)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request,'Successfully Change')
                return redirect('blog:category_all')
            return render(request, self.template_name, {'form': form})

class Delete_category(View):
    def get(self, request, name):
        name = Category.objects.filter(name=name)
        name.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('blog:category_all')