from django.conf.urls import url
from django.urls import path
from . import views

# urlpatterns = [
#     url(r'^view_list$', views.tutorial_list),
#     url(r'^list$', views.ApiOverview),
#     url(r'^create$', views.createview),
#     url(r'^viewlist/(?P<pk>[0-9]+)$', views.tutorial_detail),
#     url(r'^listpatch/(?P<pk>[0-9]+)$', views.patch_tut),
#     url(r'^listput/(?P<pk>[0-9]+)$', views.put_tut),
#     url(r'^deltut/(?P<pk>[0-9]+)$', views.del_tut)
# ]

urlpatterns = [
    path('tutorial', views.Tutuorialview.as_view()),
    path('tutorial/<int:pk>',views.tutuorialdetailedview.as_view()),
    path('login', views.LoginView.as_view()),
    path('user', views.UserView.as_view())
]