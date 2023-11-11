from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
