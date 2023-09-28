from django.shortcuts import render,redirect,get_object_or_404
from .forms import TodoForm
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponseBadRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todo_list(request):
    messages = ""
    if request.POST:
        form = TodoForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            title = clean_data['title']
            description = clean_data['description']
            status = clean_data['status']
            Todo.objects.create(title = title, description = description, status = status)
            messages = "Tode is Added"
        else:
            messages = "Something wrong please try later"
    else:
        form = TodoForm()
    
    todo = Todo.objects.order_by("-created")
    data={
        "form":form,
        "messages":messages,
        "todos":todo
    }
    return render(request,'todo_list.html',data)

@login_required
@csrf_exempt
def add_todo(request):
    print("Its coming")
    if request.POST:
        t = request.POST['type']
        id = request.POST['id']
        print(request.POST)
        
        try:
            obj = Todo.objects.get(id = id)
        except:
            return HttpResponseBadRequest
        
        if t == "done":
            obj.status = "d"
            obj.save()
        if t == "delete":
            obj.delete()
            print("deleted")
            
    return JsonResponse({"status":"done"})