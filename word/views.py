from django.shortcuts import render

from .models import Word


# Create your views here.
def test_word(request):
    return render(request, "test/test_word.html", {})


# @http.json_response()
# def test_show_word(request):
# 	try:
#         word = Word.objects.latest('id')
#     except ObjectDoesNotExist:
#         return http.code_response(code=codes.BAD_REQUEST, message=messages.USER_NOT_FOUND)
#     return {
#         "user": word.json(),
#     }

