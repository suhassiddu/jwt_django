from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Public, Protected

urlpatterns = [
    path('public/', Public.as_view()),
    path('protected/', Protected.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

