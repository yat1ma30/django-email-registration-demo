from django.shortcuts import render


def profile_view(request, template_name="accounts/profile.html"):
    context = {}
    return render(request, template_name, context)
