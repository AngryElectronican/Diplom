from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
# Create your views here.
increment=0
def basic_view(request):
    if(request.method=="POST"):
        global increment
        
        if "button_form" in request.POST:
            print('button_form+{}'.format(request.POST['data']))
            increment=request.POST['data']
            msg=Message(message="{}".format(request.POST['data']),module_id="{}".format(request.POST['ID']))
            msg.save()
        elif "button_not_form" in request.POST:
            print('button_not_form+{}'.format(request.POST['button_not_form']))
            increment=request.POST['button_not_form']
        
        return render(request,'Trening/base.html',{'inc':increment})

    return render(request,'Trening/base.html',{})

def Request_Handler(request):
    if(request.method=="GET"):
        module_id=request.GET["module_id"]
        data={'data':"N"}
        message=Message.objects.all().filter(module_id=module_id,cheked=False).order_by('sending_date')
        for msg in message:
            msg.cheked=True
            msg.save()
            data={'data':msg.message}
            break

        return JsonResponse(data)
