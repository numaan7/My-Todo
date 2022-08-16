from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo


# Create your views here.
def home(request):
    
    
   
    todos=Todo.objects.filter(completed=False)
    comptodos=Todo.objects.filter(completed=True)
    a=Todo.objects.all()
    b=(len(comptodos)/len(a))*100
    progress=round(b)
    
    return render(request,'todo.html',{'todos':todos,'comptodos':comptodos,'progress':progress})
def add(request):

    if request.method=="POST":
        title=request.POST.get('title')
        details=request.POST.get('details')
        priority=request.POST.get('priority')
        newtodo=Todo(title=title,details=details,priority=priority)
        newtodo.save()
        return redirect('/')
    
    return render(request,'todo.html')
def update(request,id):

    if request.method=="POST":
        todo=Todo.objects.get(id=id)
        title=request.POST.get('title1')
        details=request.POST.get('details1')
        priority=request.POST.get('priority1')
        todo.title=title
        todo.details=details
        todo.priority=priority
        todo.save()
        return redirect('/')
    
    return render(request,'todo.html')
def delete(request,id):
    todo=get_object_or_404(Todo,id=id)
    todo.delete()
    return redirect('/')
   
        
 
def completed(request,id):
    todo=get_object_or_404(Todo,id=id)
    todo.completed=True
    todo.save()
    return redirect('/')
def notcompleted(request,id):
    todo=get_object_or_404(Todo,id=id)
    todo.completed=False
    todo.save()
    return redirect('/')

       
        