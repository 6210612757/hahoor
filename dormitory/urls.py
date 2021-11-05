from django.urls import path

from . import views

app_name = 'dormitory'
urlpatterns = [
                path("", views.index, name="index"),
                path("dormitories", views.dormitories, name="dormitories"),
                path("<str:dorm_title>", views.dormitory,name = "dormitory"),
                path("dormitory/create_dormitory",views.create_dormitory,name = "create_dormitory"),
                path("dormitory/my_dormitory",views.my_dormitory,name = "my_dormitory"),
                path("dormitory/remove_dormitory/<int:dormitory_id>",views.remove_dormitory,name = "remove_dormitory"),
                path("dormitory/change_status/<int:dormitory_id>",views.change_status_dormitory,name = "change_status_dormitory"),
                path("dormitory/review_dormitory/<int:dormitory_id>",views.review_dormitory,name = "review_dormitory"),
                path('dormitory/review_report/<int:review_id>',views.report_review,name="report_review"),
]
