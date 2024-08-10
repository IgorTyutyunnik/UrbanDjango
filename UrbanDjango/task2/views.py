from django.shortcuts import render

# Create your views here.
def my_index(request):
    return render(request, 'second_task/index.html')

def my_index2(request):
    return render(request, 'second_task/index2.html')
