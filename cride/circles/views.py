"""Circle views."""

# from django.http import HttpResponse
# from django.http import JsonResponse

from cride.circles.models import Circle

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Serializers
from cride.circles.serializers import CircleSerializer, CreateCircleSerializer

# def list_circles(request):
#     """LIst Circle """
#     return HttpResponse('hola')

# def list_circles(request):
#     """LIst Circle """
#     circles = Circle.objects.all()
#     public = circles.filter(is_public=True)
#     data = []
#     for circle in public: #aki se se hace el query (lazy)
#         # print(circle)
#         data.append({
#             'name':circle.name,
#             'slug_name':circle.slug_name,
#             'rides_taken':circle.rides_taken
#         })

#     return JsonResponse(data,safe=False)

# @api_view(['GET'])
# def list_circles(request):
#     """List Circle """
#     circles = Circle.objects.filter(is_public=True)
#     data = []
#     for circle in circles: #aki se se hace el query (lazy)
#         data.append({
#             'name':circle.name,
#             'slug_name':circle.slug_name,
#             'rides_taken':circle.rides_taken
#         })

#     return Response(data)


# @api_view(['GET'])
# def list_circles(request):
#     """List Circle """
#     circles = Circle.objects.filter(is_public=True)
#     data = []
#     for circle in circles: #aki se se hace el query (lazy)
#         serializer = CircleSerializer(circle)
#         data.append(serializer.data)

#     return Response(data)


@api_view(['GET'])
def list_circles(request):
    """List Circle """
    circles = Circle.objects.filter(is_public=True)
    # many=True > porque va traer un arrelgo de varios registros
    serializer = CircleSerializer(circles,many=True)

    return Response(serializer.data)


# @api_view(['POST'])
# def create_circle(request):
#     """Create Circle """
#     name = request.data['name']
#     slug_name = request.data['slug_name']
#     about = request.data.get('about','')
#     circle = Circle.objects.create(name=name,slug_name=slug_name,about=about)
#     data = {
#         'name':circle.name,
#         'slug_name':circle.slug_name,
#         'rides_taken':circle.rides_taken,
#         'rides_offered':circle.rides_offered,
#         'members_limit':circle.members_limit
#     }
#     return Response(data)


@api_view(['POST'])
def create_circle(request):
    """Create Circle """
    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.data
    circle = Circle.objects.create(**data)
    return Response(CircleSerializer(circle).data)