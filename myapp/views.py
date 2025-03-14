from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import Userform,Taskform,Loginform

from myapp.models import User,TaskModel

from django.contrib.auth import authenticate,login,logout

from django.utils.decorators import method_decorator

# Create your views here.

def is_user(fn):

    def wrapper(request,**kwargs):

        id=kwargs.get("pk")

        obj=TaskModel.objects.get(id=id)

        if obj.user_id==request.user:

            return fn(request,**kwargs)
        
        else:

            return redirect('login')
        
    return wrapper



class RegistrationView(View):

    def get(self,request):

        form=Userform

        return render(request,'register.html',{'form':form})
    
    def post(self,request):
        
        form=Userform(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            User.objects.create_user(**form.cleaned_data)

        form=Userform

        return redirect('login')
    

class LoginView(View):

    def get(self,request):

        form=Loginform

        return render(request,'login.html',{'form':form})
    
    def post(self,request):

        form=Loginform(request.POST)

        if form.is_valid():

            username=form.cleaned_data.get("username")

            password=form.cleaned_data.get("password")

        user=authenticate(request,username=username,password=password)

        if user:

            print('Valid credentials')

            login(request,user)

            print(request.user)

            form=Taskform

            return redirect('create')

        else:

            print('user not found')

            form=Loginform

            return render(request,'login.html',{'form':form})
        
class TaskaddView(View):

    def get(self,request):

        form=Taskform

        data=TaskModel.objects.filter(user_id=request.user)

        return render(request,'task.html',{'form':form,'data':data})
    
    def post(self,request):

        form=Taskform(request.POST)

        if form.is_valid():

            TaskModel.objects.create(**form.cleaned_data,user_id=request.user)

            data = TaskModel.objects.filter(user_id=request.user)

            print("task added")

        return redirect("alltask")

            # return render(request,'task.html',{'form':form,'data':data})
        
class Taskall(View):

    def get(self,request):

        data=TaskModel.objects.filter(user_id=request.user).order_by('is_completed','created_date')
        
        return render(request,'alltask.html',{"data":data})
    

@method_decorator(decorator=is_user,name='dispatch')  
class TaskUpdate(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        data=TaskModel.objects.get(id=id)

        form=Taskform(instance=data)

        return render(request,'taskupdate.html',{'form':form})
    
    def post(self,request,**kwargs):

        id=kwargs.get("pk")

        data=TaskModel.objects.get(id=id)

        form=Taskform(request.POST,instance=data)

        if form.is_valid():

            form.save()

        return render(request,'taskupdate.html',{'form':form})
    

# task detail view
# lh:8000/detail/<int:pk>
@method_decorator(decorator=is_user,name='dispatch')
class TaskDetail(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        data=TaskModel.objects.get(id=id)

        return render(request,'taskdetail.html',{'data':data})
    

class TaskDelete(View):


    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        data=TaskModel.objects.get(id=id)
        
        if data.user_id==request.user:

            data.delete()

            return redirect('alltask')
    
        else:

            print('get out')
    
        return redirect('login')


class TaskEdit(View):

    def get(self,request,**kwargs):

        id= kwargs.get("pk")

        data=TaskModel.objects.get(id=id)

        if data.is_completed == False:

            data.is_completed = True

            data.save()

        return redirect("alltask")
    

class Signout(View):

    def get(self,request):

        logout(request)

        return redirect('login')
    

class CompletedView(View):

    def get(self,request):

        data = TaskModel.objects.filter(user_id=request.user,is_completed=True)

        return render(request,"complete.html",{'data':data})



class UserdetailsView(View):

    def get(self,request):

        total = TaskModel.objects.filter(user_id=request.user).count() #total task of a user

        completed = TaskModel.objects.filter(user_id=request.user,is_completed=True).count() #completed task

        incomplete = total - completed

        return render(request,'userdetail.html',{'total':total,'completed':completed,'incomplete':incomplete})


        





    


        