from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
#model 사용하겠다는 거 알려줘야 함

def home(request):
    blogs = Blog.objects
    #모델로부터 받아 처리할 수 있게끔
    #쿼리셋(을 기능적으로 처리하게 해주는 방법 --> 메소드)
    #모델이름.쿼리셋(objects).메소드()
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id)) #pylint: disable=E1101
    # render가 '요청이 들어오면 이 html 파일을 보여줘 라는 녀석'이였다면, redirect는 '요청을 들어오면 저쪽 url로 보내버려' 하는 녀석
