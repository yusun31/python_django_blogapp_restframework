from rest_framework.viewsets import ModelViewSet

from blog.models import Post, Comment
from blog.serializers import PostSerializer, CommentSerializer
from django.utils import timezone


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # login 되어 있는 상태에서만 잘 동작
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, published_date = timezone.now())


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
