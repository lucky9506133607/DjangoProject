from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):  # new
    template_name = "about.html"
    
if request.method == 'POST' and 'run_script' in request.POST:
    # import function to run 
    import seleniumcode 
 
    # call function 
    hrms()  
 
    # return user to required page 
    #return HttpResponseRedirect(reverse('registered'))
    
        
