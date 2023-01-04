from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,  CreateView, DetailView, ListView, UpdateView
from school.models import School
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SchoolForm

class HomePage(TemplateView):
    template_name = "school/home.html"
    


class registration(LoginRequiredMixin, CreateView):
    model = School
    template_name = "school/registration.html"
    form_class=SchoolForm
    
    success_url = reverse_lazy("form")
    
class FormDetail(LoginRequiredMixin, DetailView):
    model = School
    template_name = "school/formdetail.html"
    context_object_name = "talk"

class FromList(LoginRequiredMixin, ListView):
    model = School
    template_name = "school/form_list.html"
    context_object_name = "book"

class Thank(TemplateView):
    template_name = "school/thank.html"

class Upate(UpdateView):
    model = School
    template_name = "school/update.html"
    fields = "__all__"
    success_url = reverse_lazy("form")


def search_result(request):
    if request.method=="POST":
        searched=request.POST['searched']
        school=School.objects.filter(First_Name__contains=searched)
        return render(request,"school/search_result.html",{'searched':searched,'school':school})
    else:
        return render(request,"school/search_result.html",{})     