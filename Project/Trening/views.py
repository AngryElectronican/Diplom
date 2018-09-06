from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
# Create your views here.
increment=0
def basic_view(request):
    if(request.method=="POST"):
        global increment
        increment+=1
        return render(request,'Trening/base.html',{'inc':increment})

    return render(request,'Trening/base.html',{})

def Request_Handler(request):
    if(request.method=="GET"):
        module_id=request.GET["id"]
        message=Message.objects.all().filter(module_id=module_id,cheked=False).order_by('sending_date')
        for msg in message:
            msg.cheked=True
            msg.save()
            data={'data':msg.message}
            break

        return JsonResponse(data)
