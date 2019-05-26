from django.http import HttpResponse
from django.shortcuts import redirect

def redirect_blog(request):
    return redirect('posts_list_url',permanent=True)



def hello(request):

    return HttpResponse('<h1>HOP!! HOP!</h1>')
