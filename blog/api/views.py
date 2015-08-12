
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Blog
from blog.api.serializers import BlogSerializer

"""
SERIALIZERS WITH  CLASS BASED VIEWS USING CLASS APIView
"""

class BlogListView(APIView):
    """
    List all entry blogs or create a new entry
    """

    def get(self, request, format=None):
        entrys = Blog.objects.all()
        serializer = BlogSerializer(entrys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogEntryDetail(APIView):
    """
    Retrieve, update or delete a entry blog
    """
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        entry = self.get_object(pk)
        serializer = BlogSerializer(entry)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        entry = self.get_object(pk)
        serializer = BlogSerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, reqquest, pk, format=None):
        entry = self.get_object(pk)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



"""
SERIALIZERS WITH FUNCTION BASED VIEWS
"""

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
def blog_list(request):
    """
    List all entry blogs or create a new entry
    """
    if request.method == 'GET':
        entrys = Blog.objects.all()
        serializer = BlogSerializer(entrys, many = True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def blog_entry_detail(request, pk):

    """
    Retrieve, update or delete a entry blog
    """

    try:
        entry = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == 'GET':
        serializer = BlogSerializer(entry)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(entry, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        entry.delete()
        return HttpResponse(status=204)

