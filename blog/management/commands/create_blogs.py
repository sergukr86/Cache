from django.core.management.base import BaseCommand, CommandError

from blog.models import Blog

from faker import Faker


class Command(BaseCommand):
    help = "Creates as much objects of Blog as needed"

    def add_arguments(self, parser):
        parser.add_argument("number_of_blogs", nargs="+", type=int)

    def handle(self, *args, **options):
        fake = Faker()
        blogs = options.get("number_of_blogs")
        if blogs and blogs[0] > 0:
            for num in range(blogs[0]):
                Blog.objects.create(
                    title=fake.sentence(nb_words=6),
                    content=fake.text(max_nb_chars=200),
                    updated_at=fake.date()
                )
        else:
            raise CommandError("'%s' is less than 1, add a positive number." % blogs)

        self.stdout.write(
            self.style.SUCCESS("Successfully created %s blogs" % blogs[0])
        )
