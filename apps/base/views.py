from django.views import generic


class HandBookView(generic.TemplateView):
    template_name = 'handbook.html'
