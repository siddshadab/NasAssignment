from django.http import HttpResponse
from rest_framework.views import exception_handler
from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled


def process_exception(self, request):
    detail = 'Something went wrong, please contact a Support Team.'
    return HttpResponse('{"detail":"%s"}' % detail, content_type="application/json", status=500)

def custom_exception_handler_throttle(exc, context):
    response = exception_handler(exc, context)
    if isinstance(exc, Throttled):
        custom_response_data = {
            'message': 'request limit exceeded',
            'availableIn': 'Please return after some time'
        }
        response.data = custom_response_data
        return response

