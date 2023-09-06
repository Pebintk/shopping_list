from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name' : 'Muhammad Pendar Bintang Kasdiono',
        'class' : 'PBP E'
    }

    return render(request, 'main.html', context)