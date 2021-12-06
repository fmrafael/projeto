from django.contrib import admin

# Register your models here.
from .models import Post, TableAffiliate

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ("title", "author", "created","updated")
  prepopulated_fields = {"slug":("title",)}

@admin.register(TableAffiliate)
class TableAffiliateAdmin(admin.ModelAdmin):
  list_display = ("name_affiliate","author")
  

