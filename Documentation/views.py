from django.contrib import messages
from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from .forms import ContactUsMessage
# Create your views here.

def link(request):
    qs = DocLinks.objects.all() or None
    return render(request , 'DocsLinks.html' , {"item":qs})

class DocsList(ListView):
    template_name = 'Docs.html'

    def get_queryset(self):
        request=self.request
        all = DocLinks.objects.all()
        print(request.GET)
        our_query = request.GET.get('q')
        if our_query is not None:
            return Docs.objects.search(our_query)
        return all


def contact_us(request):
    qs = ContactInfo.objects.filter(active = True).first() or None
    form = ContactUsMessage(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        subject = form.cleaned_data.get('subject')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        Message.objects.create(name = name , subject = subject , email = email , message = message)
        form = ContactUsMessage()
        messages.success(request, 'پیام شما با موفقیت دریافت شد')
    context = {
        "qs" : qs,
        "form":form
    }
    return render(request,'shared/ContactUs.html',context)