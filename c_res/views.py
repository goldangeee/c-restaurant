from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Category,Food
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(["GET","POST"])
def upoload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url =fs.url(name)
        return HttpResponse(f"File uploaded at {url}")
    return render(request,'upload.html')

# def upload(request):
#     fs = FileSystemStorage()
#     uploaded_file = request.FILES['file']
#     name = fs.save(uploaded_file.name, uploaded_file)
#     url = fs.url(name)
#     return HttpResponse(f"{url}에 저장이 잘 됨")

def add_food(request):
    # get(그냥 주소 입력해서 오면) ->페이지만 보여주고
    # post -> DB에 입력하는 과정을 넣자
    if request.method == "GET":
        return render(request=request,template_name='c_res/add_food.html')
    elif request.method == 'POST':
        # Food.objects.create(name='라떼')
        # request.POST['lion_name']
        # Category 인스턴스 가져오는 영역
        category = Category.objects.get(name=request.POST['category'])

        # Food 내용을 구성 영역

def index(request):
    if request.method == 'POST':
        Category.objects.create(name=request.POST['category']).save()
        Food.objects.create(name=request.POST['name']).save()
    return render(request=request,template_name='c_res/index.html')