from django.db import models
# Create your models here.


class categories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name="نام دسته بندی")
    slug = models.SlugField(max_length=100)


class subcategories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name="نام دسته بندی")
    parent = models.ForeignKey(categories, verbose_name="دسته بندی", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100 )


class products(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام محصول")
    category = models.ForeignKey(subcategories, verbose_name="دسته بندی", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0, blank=True, verbose_name="تعداد محصول")
    price = models.PositiveIntegerField(verbose_name="قیمت محصول")
    deleted = models.BooleanField(verbose_name="محصول حذف شده", blank=True, default=False)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    description = models.TextField(blank=True)


