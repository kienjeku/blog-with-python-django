from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
        {
        'title' : 'Post1',
        'author': 'John Doe',
        'date_posted': 'September 22, 2022',
        'post_content': 'ccontent by John Doe'
        },
        {
        'title' : 'Post2',
        'author': 'sylvia Mumo',
        'date_posted': 'September 23, 2022',
        'post_content': 'content by Sylvia Mumo' 
        }
]

def home(request):

    context = {'posts': posts}
    return  render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})