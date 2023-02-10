from django.urls import path, include
#from .views import movie_list, movie_detail
from .views  import MovieListAV, MovieDetailAV

urlpatterns = [
    # path('list/', movie_list, name="movie-list"),
    # path('<int:pk>/', movie_detail, name="movie-details")

    path('list/', MovieListAV.as_view(), name="movie-list"),
    path('<int:pk>/', MovieDetailAV.as_view(), name="movie-details")
]
