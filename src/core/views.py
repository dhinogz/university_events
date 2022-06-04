from django.shortcuts import render


def frontpage_view(request):

    context = {}

    return render(request, "frontpage.html", context)
