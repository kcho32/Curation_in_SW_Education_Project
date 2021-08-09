from django.db import models
from common.models import CustomUser as User


class Category(models.Model):
    class_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return '/lecture/category/{0}'.format(self.slug)

    class Meta:
        verbose_name_plural = 'Categories'


class Lecture(models.Model):
    class_name = models.CharField(max_length=300)
    content = models.TextField()
    level = models.CharField(max_length=30)
    period = models.CharField(max_length=30)
    student = models.CharField(max_length=30, blank=True, null=True)
    subject = models.CharField(max_length=300)
    pre_ready = models.CharField(max_length=300)

    lecture_image = models.ImageField(upload_to='lecture/images/%Y/%m/%d/', blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    member = models.ManyToManyField(User, related_name='member')
    max_member = models.IntegerField(default=10)
    lecture_concern = models.ManyToManyField(User, related_name='concern_lecture')
    lecture_concern_count = models.PositiveIntegerField(db_column="concern_lecture_count", default=0)

    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return f'/lecture/{self.pk}/'
