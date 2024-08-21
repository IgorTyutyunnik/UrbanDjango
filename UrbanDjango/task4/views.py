from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request, 'fourth_task/menu.html')
def platform(request):
    return render(request, 'fourth_task/index.html')

def games(request):
    games = ["Mass Effect", "Dragon Age", "Cyberpank 2077"]
    context = {
        'games': games,
    }
    return render(request, 'fourth_task/subindex1.html', context)

def card(request):
    return render(request, 'fourth_task/subindex2.html')


