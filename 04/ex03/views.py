from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "shades": [
            "{:02X}".format(int(i * 255 / 50)) for i in range(50)
        ].__reversed__()
    }
    return render(request, 'ex03/index.html', context)
