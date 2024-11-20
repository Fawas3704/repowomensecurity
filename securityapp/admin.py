from django.contrib import admin

from securityapp.models import ComplaintTable, FeedbackTable, FriendTable, LoginTable, UserTable

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(UserTable)
admin.site.register(FeedbackTable)
admin.site.register(ComplaintTable)
admin.site.register(FriendTable)
