from django.db import models
import random
import string

# Create your models here.


class ShortURL(models.Model):
    id_user = models.ForeignKey('auth.User')
    url_hash = models.CharField(max_length=50)
    url_redirect = models.CharField(max_length=300)
    count_redirects = models.IntegerField(default=0)

    def __str__(self):
        return self.url_hash

    def get_hash(self):
        tokens = string.ascii_lowercase + string.ascii_uppercase + string.digits
        max_char = 5
        hash = ''

        hash += hash.join(random.choice(tokens) for y in range(max_char))

        while ShortURL.objects.filter(url_hash=hash):
            hash += hash.join(random.choice(tokens) for y in range(max_char))

        return hash
