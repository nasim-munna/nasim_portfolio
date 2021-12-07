from django.shortcuts import render,get_object_or_404
from .forms import ContactForm
from django.http import HttpResponseRedirect
from .models import Post, Testimonial,Work,Cv,Client
from django.views import generic
# Create your views here.
def home(request):

    post= Post.objects.all()
    work = Work.objects.all()
    cv = Cv.objects.all()
    client = Client.objects.all()
    testimonial = Testimonial.objects.all()

    if request.method == 'POST':
        
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            
            contact_form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(request.path_info)

    
    
    
    # if a GET (or any other method) we'll create a blank form
    else:
        
        contact_form = ContactForm()

    context={
        'post':post,
        'work':work,
        'cv':cv,
        'client':client,
        'testimonial':testimonial,
    }

    

    return render (request,'portfolio/index.html',context)


def blog_details(request, slug):

    blog = Post.objects.get(slug=slug)
    
    context = {
        'blog': blog,
    }

    return render(request, 'portfolio/post_detail.html', context)
