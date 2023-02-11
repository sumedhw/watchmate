from django.urls import path, include
#from .views import movie_list, movie_detail
#from .views  import MovieListAV, MovieDetailAV
#from .views import WatchListListAV, WatchListDetailAV

from .views import ( WatchListListAV, WatchListDetailAV, 
                    StreamPlatformListAV, StreamPlatformDetailAV, 
                    ReviewList, ReviewDetail, ReviewCreate )


urlpatterns = [
    # path('list/', movie_list, name="movie-list"),
    # path('<int:pk>/', movie_detail, name="movie-details")

    # path('list/', MovieListAV.as_view(), name="movie-list"),
    # path('<int:pk>/', MovieDetailAV.as_view(), name="movie-details")

    path('list/', WatchListListAV.as_view(), name="movie-list"),
    path('<int:pk>/', WatchListDetailAV.as_view(), name="movie-details"),

    path('stream/', StreamPlatformListAV.as_view(), name="stream-list"),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name="stream-details"),

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]
