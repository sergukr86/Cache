from django.shortcuts import render, get_object_or_404

from .models import Blog


def view_blog(request, blog_id: int):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "blog.html", {"blog": blog})
