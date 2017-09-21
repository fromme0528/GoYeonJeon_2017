from django.shortcuts import render
from django.utils import timezone
from .models import Post, Video, Cheeringsongs, Message
from .models import Video
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .forms import PostForm, MessageForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
#	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	posts = Post.objects.all()
	messages = Message.objects.all()
	return render(request, 'blog/post_list.html', {'posts':posts} )

def post_detail(request, pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request, 'blog/post_detail.html',{'post':post})

def score_history(request):
	return render(request, 'blog/score_history.html')

def cheeringsongs(request):
	songs = get_list_or_404(Cheeringsongs)
	return render(request, 'blog/cheeringsongs.html',{'songs' : songs})

def videos(request):
    video_list = get_list_or_404(Video)
    return render(request, 'blog/videos.html', {'videos': video_list})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def message_detail(request, pk):
	message = get_object_or_404(Message,pk=pk)
	return render(request, 'blog/message_detail.html',{'message':message})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)     
        post = form.save()
        post.save(update_fields=["score_k"])
        post.save(update_fields=["score_y"])
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def message_new(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save(update_fields=["title"])
            post.save(update_fields=["text"])
            messages = Message.objects.all()
            return redirect('message_detail', pk=post.pk)
    else:
        form = MessageForm()
    return render(request, 'blog/message_edit.html', {'form': form})

def message_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})