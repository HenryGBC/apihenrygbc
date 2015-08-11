from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'resume', 'image', 'content', 'fecha', 'usuario', 'url' )

