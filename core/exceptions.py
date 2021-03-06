from rest_framework.views import exception_handler

def core_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['resultCode'] = response.status_code
        response.data['message'] = response.status_text
        response.data['value'] = None
    return response
def _handle_generic_error(exc, context, response):
    # This is the most straightforward exception handler we can create.
    # We take the response generated by DRF and wrap it in the `errors` key.
    response.data = {
        'errors': response.data
    }

    return response