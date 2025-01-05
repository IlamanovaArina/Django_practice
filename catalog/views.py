from django.shortcuts import render

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
    return render(request, 'contacts.html')
