from django.shortcuts import render
from mes import models
# Create your views here.
def add1(request):
    new_add1 = models.test(
        test1 = request.POST.get('record_no'),
        test2 = request.POST.get('sn'),
        test3 = request.POST.get('board_sn'),
        test4 = request.POST.get('mac1'),
        test5 = request.POST.get('mac2')
    )
    new_add1.save()
    print("success")
