from django.shortcuts import render


# Create your views here.
def test_word(request):
    return render(request, "test/test_word.html", {})


