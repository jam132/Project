from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q

def post_list(request):
	if request.user.is_superuser or request.user.is_staff:
		today = timezone.now().date()
		queryset_list = Post.objects.active()
		if request.user.is_staff or request.user.is_superuser:
			queryset_list = Post.objects.all()

		query = request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(title__icontains=query) |
				Q(content__icontains=query) |
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
			).distinct()

		paginator = Paginator(queryset_list, 5)
		page = request.GET.get('page')
		try:
			queryset = paginator.page(page)
		except PageNotAnInteger:
			queryset = paginator.page(1)
		except EmptyPage:
			queryset = paginator.page(paginator.num_pages)
	else:
		return render(request, 'login/login.html')
	context ={
		"object_list": queryset,
		"title": "List",
		"today": today,
	}
	return render(request, 'post/list.html', context)
	
def post_create(request):
	if not request.user.is_authenticated():
		return render(request, 'login/login.html')
	elif request.user.is_superuser:
		return HttpResponseRedirect("/posts")
	else:
		form = PostForm(request.POST or None)
		if form.is_valid():
			instance= form.save(commit=False)
			instance.user = request.user
			instance.save()
			messages.success(request, "Successfully Created")
			#return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form": form,
	}
	return render(request, 'post/form.html', context)

def post_update(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None,request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Changes saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"instance": instance,
		"title": instance.title,
		"form":form,
	}
	return render(request, 'post/form.html', context)

def post_delete(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")
	context ={
		"title": "delete"
	}
	return render(request, 'post/delete.html', context)
	
def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404

	context ={
		"instance": instance,
		"title": instance.title,
	}
	return render(request, 'post/detail.html', context)