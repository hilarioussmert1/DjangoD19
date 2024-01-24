from .views import NewsList
from django.urls import path


urlpatterns = [
    path('', NewsList.as_view(), name='news_list')
]