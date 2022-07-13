from django.urls import path
from app import views
urlpatterns = [
    path('book/',views.BookAPIView.as_view()),
    path('book/<int:id>/',views.BookDetialApiView.as_view()),
    path('bookgen/',views.BookGen.as_view()),
    path('bookdegen/<int:pk>/',views.BookDeGen.as_view())
]