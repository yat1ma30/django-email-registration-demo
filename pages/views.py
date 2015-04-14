from django.shortcuts import render


def index_view(request, template_name="pages/index.html"):
    context = ()
    return render(request, template_name, context)
