from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import imageupload

def firstone(request):
    return HttpResponse("welcome")
def form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        image=request.FILES.get('image')
        imageupload.objects.create(name=name,age=age,image=image)
        return HttpResponse('okay')
    return render(request,'card.html')

def view(request):
    context=imageupload.objects.all()
    return render(request,'form.html',{'detail':context})

def delete(request, pk):
    obj = get_object_or_404(imageupload, pk=pk)
    
    if request.method == 'POST':
        obj.delete()
        return redirect('card') 
    
    return render(request, "del.html", {'detail': obj})



       



