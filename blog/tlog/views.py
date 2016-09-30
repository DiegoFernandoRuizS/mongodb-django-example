from django.shortcuts import render

from django.shortcuts import render
from .models import User, Post


# Create your views here.

def index(request):
    user = User.objects.create(
        email="diegofruizs@diego.com",
        first_name="Diego Fernando",
        last_name="Ruiz Sanchez"
    )
    user.save()
    post = Post.objects.create(
        title="Mi primer post prueba",
        author=user
    )
    post.save()
    return_info()
    print("Ok - Guardado")
    return render(request, 'index.html', {})


def return_info():
    for post in Post.objects:
        print(post.title)
        if isinstance(post.author, User):
            print(post.author.email)
