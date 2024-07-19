from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import PostForm 
#from django.contrib.auth.decorators import login_required

from .filters import PostFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post , Tag

def posts(request):
	posts = Post.objects.filter(active=True)

	#Adding Filter as Search Box
	myFilter = PostFilter(request.GET, queryset=posts)
	posts = myFilter.qs


	context = {'posts':posts , 'myFilter':myFilter }
	return render(request, 'base/posts.html',context)

def post(request,slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		PostComment.objects.create(
			author=request.user.profile,
			post=post,
			body=request.POST['comment']
			)
		messages.success(request, "You're comment was successfuly posted!")

		return redirect('post', slug=post.slug)


	context = {'post':post}
	return render(request, 'base/post.html', context)


def createPost(request):
	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST ,request.FILES)
		if form.is_valid():
			form.save()
		return redirect('posts')

	context = {'form':form}
	return render(request, 'base/post_form.html',context)

def updatePost(request,slug):
	post = Post.objects.get(slug=slug)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST ,request.FILES ,instance=post)
		if form.is_valid():
			form.save()
		return redirect('posts')

	context = {'form':form}
	return render(request, 'base/post_form.html',context)

def deletePost(request,slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		post.delete()
		return redirect('posts')

	context = {'post':post }
	return render(request, 'base/delete.html',context)
