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
    


# //////////////////////////////////////// API ////////////////////////////////////////////////////////////////

class UserReg(APIView):
    def post(self,request):
        print("###############",request.data)
        user_serial=UserSerializer(request.data)
        login_serial=LoginSerializer(data=request.data)
        data_valid=user_serial.is_valid()
        login_valid=login_serial.is_valid()

        if data_valid and login_valid:
           print("&&&&&&&&&&&&&&&&&")
           password=request.data['password']
           login_profile=login_serial.save(user_type='USER', password=password)
           user_serial.save(LOGIN=login_profile)
           return Responce(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': login_serial.errors if not login_valid else None,
                         'user_error': user_serial.errors if not data_valid else None}, status=status.HTTP_400)























