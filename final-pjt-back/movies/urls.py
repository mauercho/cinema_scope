from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('list/', views.list, name="list"),
    path('<int:movie_pk>/', views.detail, name="detail"),
    path('<int:movie_pk>/likes/', views.movie_likes, name="movie_likes"),
]
