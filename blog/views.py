from django.shortcuts import render,get_object_or_404 ,redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q


from .forms import CommentForm
# Create your views here.

from .models import Category, Post
class PostListView(ListView):
    template_name = 'core/frontpage.html'
    # model = Post
    queryset = Post.objects.filter(status = Post.ACTIVE)
    context_object_name = 'posts'

class PostDetailView(DetailView):
    
    template_name = 'blog/post-detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        post = get_object_or_404(Post, slug=slug,status =  Post.ACTIVE)

        context['post_data'] = post
        context['form'] = CommentForm()
        return context

    
    def post(self, request,*args, **kwargs):

        slug = self.kwargs.get('slug')
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug = slug)
        form = CommentForm()
        return render(request , 'blog/post_detail.html' , {'form':form})



def category(request , slug):
    category = get_object_or_404(Category,slug=slug)
    posts = category.posts.filter(status = Post.ACTIVE)

    return render(request, 'blog/category.html', {'posts' : posts})


def search(request):
    query  = request.GET.get('query','')
    posts = Post.objects.filter(status = Post.ACTIVE).filter(Q(title__icontains= query) | Q(intro__icontains= query) | Q(body__icontains= query))

    return render(request , 'core/frontpage.html' , {'posts': posts, 'query': query})
    