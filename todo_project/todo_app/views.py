from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
from .forms import todo_form
from todo_app.models import todoapp
class listview1(ListView):
    model=todoapp
    template_name ='index.html'
    context_object_name ='todolist'

class detailview1(DetailView):
    model=todoapp
    template_name = 'details.html'
    context_object_name = 'i'

class update1(UpdateView):
    model=todoapp
    template_name = 'update1.html'
    context_object_name = 'task'
    fields=['activity_name','priority','date1']
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={"pk":self.object.id})
class delete1(DeleteView):
    model=todoapp
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

def index(request):
    if request.method=='POST':
        activity_name1=request.POST.get('activity',"")
        priority1=request.POST.get('priority',"")
        date = request.POST.get('date', "")
        list1=todoapp(activity_name=activity_name1,priority=priority1,date1=date)
        list1.save()
    obj1 = todoapp.objects.all()
    return render(request,'index.html',{"todolist":obj1})
def delete(request,taskid):
     if request.method=='POST':
         obj1 = todoapp.objects.get(id=taskid)
         obj1.delete()
         return redirect('/')
     return render(request,'delete.html')
def update(request,tid):
    task1=todoapp.objects.get(id=tid)
    form1=todo_form(request.POST or None,request.FILES,instance=task1)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'update.html',{'form':form1,"id":task1})

