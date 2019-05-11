from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import Word
from utilities import http, result_codes, messages


# Create your views here.
def test_word(request):
    return render(request, "test/test_word.html", {})


@http.json_response()
def test_show_word(request):
    try:
        word = Word.objects.last()
    except ObjectDoesNotExist:
        return http.code_response(
            code=result_codes.BAD_REQUEST,
            message=messages.NOT_FOUND)
    return {
        'word': word.json(),
    }

