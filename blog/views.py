from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from .models import Blog

from faker import Faker


@cache_page(60)
def view_blog(request, blog_id: int):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "blog.html", {"blog": blog})


# fake = Faker()
# Faker.seed(0)
#
#
# def fill_in(request, blog_id: int):
#     if blog_id >= 1:
#         for i in range(blog_id + 1):
#             Blog.objects.create(
#                 title=fake.sentence(nb_words=6),
#                 content=fake.text(max_nb_chars=200),
#                 updated_at=fake.date(),
#             )
#     return redirect("view_blog", blog_id=1)
