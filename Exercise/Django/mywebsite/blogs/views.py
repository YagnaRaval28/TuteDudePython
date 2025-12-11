from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse
blog_names={
    "python-basic":"Python intro page",
    "django":"Django basic page",
    "regex":"Regular expression in Python"
}
def home_page(request):
    return HttpResponse("<h1>Home Page</h1>")
def blogposts(request):
    list_item=""
    blog_list=list(blog_names.keys())
    for b in blog_list:
        blog_path=reverse("blog-post",args=[b])
        list_item+=f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'
    res_data=f"<ul>{list_item}</ul>"
    return HttpResponse(res_data)
def python_intro(request):
    return HttpResponse("Python intro page")
def django_basics(request):
    return HttpResponse("Django basic page")
def blog_post(request,blog):
    try:
        res=blog_names[blog]
    except:
        return HttpResponseNotFound("<h1>Blog not found</h1>")       
    return HttpResponse(res)
def blog_post_by_number(request,blog):
    return HttpResponse(blog)
