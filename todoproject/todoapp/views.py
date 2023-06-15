from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Tasks
from.forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# 1......create your class base views.
class TasksListView(ListView):
    model=Tasks
    template_name = 'home.html'
    context_object_name = 'task1'
class TasksDetailView(DetailView):
    model=Tasks
    template_name = 'list_details.html'
    context_object_name = 'task'
class TasksUpdateView(UpdateView):
    model=Tasks
    template_name = 'update.html'
    context_object_name = 'task'
    fields= ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TasksDeleteView(DeleteView):
    model = Tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# 2......create your functional base views.
def add(request):
    tasks = Tasks.objects.all()
    if request.method=="POST":
        Name=request.POST.get('task','')
        Priority=request.POST.get('priority','')
        Date=request.POST.get('date','')
        task=Tasks(name=Name,priority=Priority,date=Date)
        task.save()
    return render(request,'home.html',{'task':tasks})
# def details(request):
#     tasks=Tasks.objects.all()
#     return render(request,'details.html',{'task':tasks})

def delete(request,task_id):
    task=Tasks.objects.get(id=task_id)
    if request.method =='POST':
        task.delete()
        return redirect('/')

    return render(request,'delete.html')

def update(request,id):
    tasks=Tasks.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=tasks)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'fo':f,'task':tasks})


