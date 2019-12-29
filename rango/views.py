from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
# Create your views here.

from django.http import HttpResponse
def index(request): 
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {}
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	context_dict['categories'] = category_list
	return render(request, 'rango/index.html', context_dict)
def about(request):
	#return HttpResponse("About says you're here!")
	#context_dict = {'boldmessage':'This tutorial has been put together by Echocherish'}
	#return render(request,'rango/about.html', context=context_dict)
	print(request.method)
	print(request.user)
	return render(request, 'rango/anout.html',{})
def show_category(request,category_name_slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug=category_name_slug)
		pages = Page.objects.filter(Category=category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['category'] =None
		context_dict['pages'] = None
	return render(request,'rango/category.html', context_dict)
def add_category(request):
	form = CategoryForm()
	if request.method =='POST':
		form = CategoryForm(request.POST)
	if form.is_valid():
		form.save(commit=True)
		return index(request)
	else:
		print(form.errors)
	return render(request, 'rango/add_category.html',{'form':form})