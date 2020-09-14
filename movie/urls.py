from django.urls import path
from . import views

app_name = 'movie';

urlpatterns = [
    path('index', views.MovieIndexView.as_view(), name='movie_view'),
    path('registration', views.MovieRegistrationView.as_view(), name='movie_registration')
    #path('report', views.DvdReportView.as_view(), name='report_view'),
    #path('create', views.DvdCreateView.as_view(), name='create_view'),
    #path('update/<int:id>', views.DvdCreateView.as_view(), name='update_view'),
    #path('view/<int:id>', views.DvdViewView.as_view(), name='view_view'),
    #path('delete/<int:id>', views.DvdDeleteView.as_view(), name='delete_view')
]