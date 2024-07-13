from django.shortcuts import render
from .models import History
# Create your views here.

def hist(request,hist_id):
    hist = History.objects.get(id = hist_id)
    historys = History.objects.order_by('date_added')
    context = {'historys':historys, 'hist':hist}
    return render(request,'hist.html', context)


def index(request):
    historys = History.objects.order_by('date_added')
    context = {'historys':historys, 'hist':hist}
    return render(request,'index.html', context)