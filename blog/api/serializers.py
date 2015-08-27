from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Blog
        fields = ('id', 'title', 'resume', 'image', 'content', 'date', 'user', 'url' )
        lookup_field='url'




class UserSerializer(serializers.ModelSerializer):
    blog = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'blog')

