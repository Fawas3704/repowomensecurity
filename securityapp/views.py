from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from securityapp.models import ComplaintTable, FeedbackTable, LoginTable, UserTable

# Create your views here.
class Loginpage(View):
    def get(self,request):
        return render(request,"adminstration/login.html")
    def post(self,request):
        username = request.POST['username']
        password =request.POST['password']
        login_obj = LoginTable.objects.get(Username=username,Password=password)
        if login_obj.TYPE =="admin":
            return HttpResponse('''<script>alert("welcome to admin home");window.location="/navigation"</script>''')
# ///////////////////////////// ADMIN  ///////////////////////////////////  
class complaintpage(View):
    def get(self,request):
        obj=ComplaintTable.objects.all()
        return render(request,"adminstration/complaint2.html",{'obj':obj})
    
class sendreply(View):
    def get(self,request,id):
        obj=ComplaintTable.objects.get(id=id)
        return render(request,"adminstration/reply.html",{'obj':obj})
    def post(self,request,id):
        obj=ComplaintTable.objects.get(id=id)
        form=Addreplyform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('complaint')

        

class feedbackpage(View):
  def get(self,request):
        obj=FeedbackTable.objects.all()
        print(obj)
        return render(request,"adminstration/feedback2.html",{'obj':obj})
class manage_user(View):
    def get(self,request):
        obj=UserTable.objects.all()
        return render(request,"adminstration/manage_user.html",{'obj':obj})
    
class AcceptUser(View):
    def get(self,request, login_id):
        login_obj=LoginTable.objects.get(id=login_id)
        login_obj.TYPE="user"
        login_obj.save()
        return HttpResponse('''<script>alert("User Accepted");window.location="/manage_user"</script>''')
class RejectUser(View):
    def get(self,request, login_id):
        login_obj=LoginTable.objects.get(id=login_id)
        login_obj.TYPE="reject"
        login_obj.save()
        return HttpResponse('''<script>alert("You are rejected");window.location="/manage_user"</script>''')
class navigation(View):
    def get(self,request):
        return render(request,"adminstration/navigation.html")
    





























