from django.contrib import admin
from django import forms
from .models import News, Category, Author, NewsCategory
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content_text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


# admin.site.register(News)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(NewsCategory)


@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    form = NewsAdminForm
