from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):  # new
    template_name = "about.html"

    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    print(data)
