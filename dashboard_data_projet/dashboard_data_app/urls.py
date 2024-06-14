from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_view, name = 'index'),
    path('login', views.login_view, name = 'login'),
    path('add_sales', views.add_sales_view, name = 'add_sales'),
    path('performance', views.performance_view, name = 'performance'),
    path('upload_files', views.upload_view, name = 'upload_files'),
    path('logout', views.logout_view, name='logout'),
    path('summary', views.summary_view, name='summary'),

]