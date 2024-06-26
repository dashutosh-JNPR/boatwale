from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Tag
from django.views.generic import ListView

# Create your views here.
def blog(request):
    content_category = Category.objects.all()
    content_posts = Post.objects.all()
    context = {
        'title': "Boatwale Blog - Stories, Tips, and Insights on Varanasi Boating",
        'description': 'Stay updated with the latest stories, tips, and insights about boating in Varanasi on the Boatwale blog, curated for both enthusiasts and travelers.',
        'keywords': "Varanasi boating, boatwale blog, Ganges River stories, boating tips, boat tour insights, Varanasi travel guide, boatwale updates",
        'categories': content_category,
        'posts': content_posts,
        'thumnail': '../static/images/banner/boat-mountain-lake-boat-in-mountain-lake.webp'
    }
    return render(request, 'blog.html', context=context)

def post(request, slug):
    post_content = get_object_or_404(Post, slug=slug)
        
    context = {
        'title': post_content.title,
        'description': post_content.description,
        'content': post_content,
        'thumnail': post_content.featured_image
    }
    
    return render(request, 'single-blog.html', context=context)

class CategoryDetailView(ListView):
    model = Post
    template_name = 'category_detail.html'  # Replace with your template name
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
    
class TagDetailView(ListView):
    model = Post
    template_name = 'tag_detail.html'  # Replace with your template name
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context