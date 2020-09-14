from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class CustomerIndexView(View):
    def get(self, request):
        return render(request, 'customer/customer_dashboard.html')
    
    def post(self, request):
        return render(request, 'customer/customer_registration.html')
    
class CustomerRegistrationView(View):
    def get(self, request):
        return render(request, 'customer/customer_registration.html')