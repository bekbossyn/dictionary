from django.shortcuts import render


# Create your views here.
def test_user(request):
    return render(request, "test/test_user.html", {})


