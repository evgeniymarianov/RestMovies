from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MovieListSerializer
from .models import Movie

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
