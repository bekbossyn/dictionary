from django.shortcuts import render


# Create your views here.
def test_dictionary(request):
    return render(request, "test/test_dictionary.html", {})


