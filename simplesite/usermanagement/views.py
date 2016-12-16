from django.shortcuts import render
from .models import Users
from .forms import PostForm


# Create your views here.
def post_list(request):
    return render(request, 'usermanagement/post_list.html', {})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        form = PostForm()
    else:
    	form = PostForm()
    return render(request, 'usermanagement/post_edit.html', {'form': form})
def list_all(request):
	users = Users.objects.all()
	return render(request, 'usermanagement/list_all.html', {'users': users})