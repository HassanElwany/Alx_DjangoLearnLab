from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Post  # Assuming a Post model exists in posts app
from .serializers import PostSerializer

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)