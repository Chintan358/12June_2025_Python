

from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name="index"),
    path("reg",reg,name="reg"),
    path("display",display,name="display"),
    path("delete",delete_student,name="delete"),
    path("edit",student_by_id,name="edit"),
    path("update",update_student,name="update"),
    path("home",home,name="home"),


    path("userreg",user_reg,name="userreg"),
    path("userlogin",user_login,name="userlogin"),
    path("userlogout",user_logout,name="userlogout")
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)