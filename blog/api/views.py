
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from blog.models import Blog
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from blog.api.serializers import BlogSerializer, UserSerializer

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

"""
SERIALIZERS USING GENERIC CLASS BASED VIEWS
"""

class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class BlogEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field='url'




"""
SERIALIZERS OF USERS USING GENERIC CLASS BASED VIEWS
"""

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, TokenHasReadWriteScope)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

