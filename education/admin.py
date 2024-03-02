from django.contrib import admin

from education.models import Product, Lesson, Group
from users.models import User


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_data', 'cost', 'owner')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')

