from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from drf_util.decorators import serialize_decorator

from apps.blog.models import Category, Blog, Comments
from apps.blog.serializers import CategorySerializer, BlogSerializer, CommentsSerializer, BlogItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        blogs = Blog.objects.all()

        return Response(BlogSerializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogItemSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))

        return Response(BlogItemSerializer(blog).data)


class BlogCreatView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(BlogSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        blog = Blog.objects.create(
            title=validated_data['title'],
            slug=validated_data['slug'],
            body=validated_data['body'],
            category=validated_data['category'],
            enabled=validated_data['enabled'],
        )
        blog.save()

        return Response(BlogSerializer(blog).data)


class BlogCommentsView(GenericAPIView):
    serializer_class = CommentsSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(CommentsSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        comment = Comments.objects.create(
            blog_relation = validated_data['blog_relation'],
            text = validated_data['text'],

        )
        comment.save()

        return Response(CommentsSerializer(comment).data)

"""

class BlogCommentsView(GenericAPIView):
    serializer_class = CommentsSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(CommentsSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        comment = Comments.objects.create(
            blog = validated_data['blog'],
            text = validated_data['text'],

        )
        comment.save()

        return Response(CommentsSerializer(comment).data)

"""