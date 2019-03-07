from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    #fields = ['task','date','time']
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if(form.is_valid()):
            form.save()
            all_items = List.objects.all
            messages.success(request,('Task has been Added Successfully to Your To-Do List '))

            return render(request,'home.html',{'all_items':all_items})

    else:
        all_items = List.objects.all
        return render(request,'home.html',{'all_items':all_items})

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('ITEM HAS BEEN DELETED !'))
    return redirect('home')

def cross_off(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request,list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,('Task Has Been Edited !'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request,'edit.html',{'item':item})
