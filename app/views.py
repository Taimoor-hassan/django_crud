from django.shortcuts import render,HttpResponseRedirect
from .forms import entryform
from .models import student


# Create your views here.

def home (request):
    if request.method == 'POST':
       form = entryform(request.POST)
       if form.is_valid:
        form.save()
    else:
        form = entryform()
    record=student.objects.all()
    data={
        'f':form,
        'r':record,
    }
    return render(request,'index.html',data)

def edit (request,id):
    if request.method == 'POST':
        de = student.objects.get(pk=id)
        form= entryform(request.POST, instance=de)
        if form.is_valid:
            form.save()
    else:
        de = student.objects.get(pk=id)
        form = entryform(instance=de)

    record=student.objects.all()
    data={
        'f':form,
        'r':record,
    }
    return render(request,'update.html',data)


def delete (request,id):
    if request.method == 'POST':
        de = student.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/')
