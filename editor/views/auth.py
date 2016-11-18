from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from . import resp


@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        try: 
            url_args = request.get_full_path().split('?')[1].split('&')
            url_args = {k:v for k, v in map(lambda arg: arg.split('='), url_args)}
        except IndexError:
            next_url = None
        else:
            next_url = url_args.get('next')
            
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError as e:
            return resp.error_missed_form_field(e.args[0])

        user = authenticate(username=username, password=password) 

        if user is None:
            return HttpResponse(status_code=401)
        else:
            login(request, user)

        if next_url is not None:
            return redirect(next_url)
        
        return redirect('/ads') 
