from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('list/', views.list, name="list"),
    path('<int:movie_pk>/', views.detail, name="detail"),
    path('<int:movie_pk>/likes/', views.movie_likes, name="movie_likes"),
    path('<int:movie_pk>/favorites/', views.favorites, name="favorites"),
    path('<int:movie_pk>/reviews/', views.reviews, name="reviews"),
]
