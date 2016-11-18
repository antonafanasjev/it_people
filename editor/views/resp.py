from django.http import HttpResponse


def ok(code=200):
    assert isinstance(code, int)
    
    return HttpResponse('OK', status=code)

def error(code, msg):
    assert isinstance(code, int)
    assert isinstance(msg,  str)
    
    return HttpResponse(msg, status=code)

def error_missed_form_field(field_name):
    return error(400, 'Missed required form filed: {}'.format(field_name))

def error_not_found(**kw):
    return error(404, 'Couldn\'t find item ({})'.format(', '.join([str(k) + '=' + str(v) for k,v in kw.items()])))
