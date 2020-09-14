from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

class MovieIndexView(View):
    def get(self, request):
        return render(request, 'movie/movie_dashboard.html')

    def post(self, request):
        return render(request, 'movie/movie_registration.html')

class MovieRegistrationView(View):
    def get(self, request):
        return render(request, 'movie/movie_registration.html')