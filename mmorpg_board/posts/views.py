from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings



@login_required
def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            subject = 'Новый комментарий к вашему посту'
            message = f'Здравствуйте, {post.author.username}! На ваш пост "{post.title}" оставили новый комментарий.'
            recipient_list = [post.author.email]
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'posts/create_comment.html', {'form': form})


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


@login_required
def private_page(request):
    user = request.user
    comments = Comment.objects.filter(post__author=user)

    selected_post = request.GET.get('post')

    if selected_post:
        # Фильтруем комментарии на основе выбранного поста
        comments = comments.filter(post__title__icontains=selected_post)

    return render(request, 'posts/private_page.html', {'comments': comments})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author == request.user:
        comment.delete()
    return redirect('private_page')


@login_required
def accept_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.post.author == request.user:
        comment.is_accepted = True
        comment.save()
        subject = 'Ваш комментарий принят'
        message = f'Здравствуйте, {comment.author.username}! Ваш комментарий к посту "{comment.post.title}" был принят автором.'
        recipient_list = [comment.author.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

    return redirect('private_page')





