from django.urls import path
from .views import TypingViewSet

urlpatterns = [
    path("typing/",TypingViewSet.as_view()),
]