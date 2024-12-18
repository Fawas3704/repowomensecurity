
from django.urls import path

from securityapp.views import *

urlpatterns = [
    path('',Loginpage.as_view(), name="login"),
    path('complaint',complaintpage.as_view(), name="complaint"),
    path('sendreply/<int:id>/',sendreply.as_view(),name='sendreply'),
    path('feedback',feedbackpage.as_view(), name="feedback"),
    path('manage_user',manage_user.as_view(), name="manage_user"),
    path('accept_user/<int:login_id>',AcceptUser.as_view(), name="accept_user"),
    path('reject_user/<int:login_id>',RejectUser.as_view(), name="reject_user"),
    path('navigation',navigation.as_view(), name="navigation"),


    # /////////////////////////////////////// API //////////////////////////////////
    
]

