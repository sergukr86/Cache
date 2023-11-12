import time

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.cache import cache_page

from .models import Blog


@cache_page(5)
def view_blog(request, blog_id: int):
    start_time = timezone.now()
    time.sleep(2)
    blog = get_object_or_404(Blog, id=blog_id)
    end_time = timezone.now()
    total_time = end_time - start_time
    print(total_time)
    return render(request, "blog.html", {"blog": blog})
