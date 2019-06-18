"""Circle views."""

# from django.http import HttpResponse
from django.http import JsonResponse

from cride.circles.models import Circle

# def list_circles(request):
#     """LIst Circle """
#     return HttpResponse('hola')

def list_circles(request):
    """LIst Circle """
    circles = Circle.objects.all()
    public = circles.filter(is_public=True)
    data = []
    for circle in public: #aki se se hace el query (lazy)
        # print(circle)
        data.append({
            'name':circle.name,
            'slug_name':circle.slug_name,
            'rides_taken':circle.rides_taken
        })

    return JsonResponse(data,safe=False)






