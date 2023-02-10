from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view

from watchmate_app.models import Movie


from .serializers import MovieSerializer

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    
    return Response(serializer.data)