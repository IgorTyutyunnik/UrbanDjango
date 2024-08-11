from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request, 'therd_task/index.html')

def games(request):
    return render(request, 'therd_task/subindex1.html')

def card(request):
    return render(request, 'therd_task/subindex2.html')


