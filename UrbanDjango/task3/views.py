from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request, 'therd_task/index.html')

def games(request):
    games = ["Mass Effect", "Dragon Age", "Cyberpank 2077"]
    context = {
        'games': games,
    }
    return render(request, 'therd_task/subindex1.html', context)

def card(request):
    return render(request, 'therd_task/subindex2.html')


