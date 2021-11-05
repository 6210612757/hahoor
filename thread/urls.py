from django.urls import path

from . import views

app_name = 'thread'
urlpatterns = [ path("", views.index, name="index"),
                path("<int:thread_id>", views.thread,name = "thread"),
                path("my_thread",views.my_thread,name = "my_thread"),
                path("create_thread",views.create_thread,name = "create_thread"),
                path("reply_thread/<int:thread_id>", views.reply_thread,name = "reply_thread"),
                path("report_thread/<int:thread_id>", views.report_thread,name = "report_thread"),
                path("report_sub_thread/<int:sub_thread_id>", views.report_sub_thread,name = "report_sub_thread"),
               ]
