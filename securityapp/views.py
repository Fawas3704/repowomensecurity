from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View

from women_security.serializer import FriendlistEditSerializer, LoginSerializer, UserSerializer
from .forms import *
from securityapp.models import ComplaintTable, FeedbackTable, FriendTable, LoginTable, UserTable
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
        user_serial=UserSerializer(request.data)
        login_serial=LoginSerializer(data=request.data)
        data_valid=user_serial.is_valid()
        login_valid=login_serial.is_valid()

        if data_valid and login_valid:
           print("&&&&&&&&&&&&&&&&&")
           password=request.data['password']
           login_profile=login_serial.save(user_type='USER', password=password)
           user_serial.save(LOGIN=login_profile)
           return Response(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': login_serial.errors if not login_valid else None,
                         'user_error': user_serial.errors if not data_valid else None}, status=status.HTTP_400)
    
class FriendlistAPIView(APIView): 
    # GET: List all friends or retrieve a single friend by ID
    def get(self, request, pk=None):
        user_id = request.query_params.get("user_id")  # Extract user_id from query parameters

        if pk:  # Retrieve a specific friend by ID
            try:
                friend = FriendTable.objects.get(pk=pk)
                serializer = FriendtableSerializer(friend)
                return Response(serializer.data)
            except FriendTable.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        elif user_id:  # Retrieve all friends for a specific user_id
            friends = FriendTable.objects.filter(user_id=user_id).all()
            serializer = FriendtableSerializer(friends, many=True)
            return Response(serializer.data)
        else:  # Retrieve all friends if no filter is provided
            friends = FriendTable.objects.all()
            serializer = FriendtableSerializer(friends, many=True)
            return Response(serializer.data)
    
    # POST: Create a new friend entry
    def post(self, request):
        print("$$$$$$$$", request.data)
        serializer = FriendtableSerializer(data=request.data)
        if serializer.is_valid():
            s=serializer.save()
            # s.user_id=Userprofile.objects.get(i)
            # s.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # PUT: Update an existing friend entry
    def put(self, request, pk):
        print(request.data)
        try:
            friend = FriendTable.objects.filter(pk=pk).first()
        except FriendTable.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FriendlistEditSerializer(instance=friend, data=request.data)
        if serializer.is_valid():
            print("dddd")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # DELETE: Delete a specific friend entry
    def delete(self, request, pk):
        try:
            friend = FriendTable.objects.get(pk=pk)
        except FriendTable.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        friend.delete()
        return Response({"detail": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

























