from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import SnippetView


router = SimpleRouter(trailing_slash=False)
router.register('snippets', SnippetView, basename='snippets')

urlpatterns = []

urlpatterns += router.urls