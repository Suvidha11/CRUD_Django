from django.shortcuts import render,HttpResponse,redirect
from .models import student
# Create your views here.
def display(request):
    disp_obj = student.objects.all()
    if not disp_obj:
      msg = "Not data found...please enter atleast one data"
      context={
          'msg':msg
          }
    else:
       context={
          'result': disp_obj
          }   
     
    return render(request, "index.html", context)


def add(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        branch=request.POST['branch']
        add_obj=student(name=name,email=email,branch=branch)
        add_obj.save()
        return redirect('display')
    else:

        return render(request, 'add.html')

def delete(request,id):
    dlt= student.objects.get(stu_id=id)
    dlt.delete()
    return redirect('display')

def update(request,id):
    edit=student.objects.get(stu_id=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        branch=request.POST['branch']
        update_data=student.objects.get(stu_id=id)
        update_data.name=name
        update_data.email=email
        update_data.branch=branch
        update_data.save()
        return redirect('display')
    else:
     return render(request, 'update.html',{'edit':edit})