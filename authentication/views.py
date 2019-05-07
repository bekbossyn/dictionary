from django.shortcuts import render


# Create your views here.
def test_authentication(request):
    return render(request, "test/test_authentication.html", {})


