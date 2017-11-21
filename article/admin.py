from django.contrib import admin

# Register your models here.
from article.models import Article,Category

class ArticleAdmin(admin.ModelAdmin):
  list_display = ('pk','title','content','category')

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('pk','name')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)