from django.shortcuts import render

info = [
    {
        'name': 'Asel',
        'username':'aselesa',
        'nationality': 'kyrgyz',
        'age': '18'
    },
    {
        'name': 'Yahiko',
        'username':'yoyo',
        'nationality': 'japanese',
        'age': '20'
    }
    
]

def home(request):
    context = {
        'info': info
    }
    return render(request, 'myhole/home.html', context)

def about(request):
    return render(request, 'myhole/about.html', {'title': 'About'})


