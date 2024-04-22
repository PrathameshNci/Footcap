from django.contrib import admin
from .models import Category, SubCategory, Prod, Special
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Prod)
admin.site.register(Special)