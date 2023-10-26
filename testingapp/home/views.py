from django.shortcuts import render
from .models import place, data


# Create your views here.
def demo(request):
    obj1 = place.objects.all()
    obj2 = data.objects.all()
    context= {
        "place": obj1,
        "data":obj2,
    }

    return render(request, 'index.html', context)

# def devel(request):
#
#     return render(request, 'index.html', {'develop': obj1})
