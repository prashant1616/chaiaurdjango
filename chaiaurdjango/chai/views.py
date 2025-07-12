from django.shortcuts import render
from .models import Chaivariety
from django.shortcuts import get_object_or_404

# Create your views here.

def all_chai(request):
    chais = Chaivariety.objects.all()
    return render(request,'chai/allchai.html',{'chais':chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(Chaivariety,pk= chai_id)
    return render(request,'chai/chai_details.html',{'chai':chai})