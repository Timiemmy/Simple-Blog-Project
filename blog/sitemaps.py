from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):  # This retuen the Querysets of objects to be included in the sitemap
        return Post.published.all()

    def lastmod(self, obj):  # This recieves each objet return by items and return the last time the object was updated
        return obj.updated
