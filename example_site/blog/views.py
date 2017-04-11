# coding: utf8
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail
# Create your views here.
def post_list(request):
	object_list = Post.published.all()
	paginator = Paginator(object_list, 3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})
	# posts = Post.published.all()
	# return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
	return render(request, 'blog/post/detail.html', {'post': post})


class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 4
	template_name = 'blog/post/list.html'

def post_share(request, post_id):
	post = get_object_or_404(Post, id=post_id, status='published')
	sent = False
	if request.method == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			post_url = request.build_absolute_uri(post.get_absolute_url())   # 构建一个包含Http schema 和主机名 的完整的url
			subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], (cd['comments']).encode('utf8'))
			send_mail(subject, message, 'wangwei101108@foxmail.com', [cd['to']])
			sent = True
	else:
		form = EmailPostForm()
	return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})