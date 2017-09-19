from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Video
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
#	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request, 'blog/post_detail.html',{'post':post})

def score_history(request):
	return render(request, 'blog/score_history.html')

def cheeringsongs(request):
	return render(request, 'blog/cheeringsongs.html')

def videos(request):
    full_list = Video.objects.all()
    return render_to_response('blog/video.html', {'full_list': full_list})

