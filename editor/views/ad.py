from urllib.parse import parse_qs

from django.views.decorators.http import require_http_methods, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..models import Ad
from .. import storage
from . import resp


@require_GET
@login_required
def ad_view(request, id):
    try:
        ad = Ad.objects.get(id=id)
    except Ad.DoesNotExists:
        return resp.error_not_found(id=id)

    storage.increase_ad_views(id, request.user.id)

    views_count = len(storage.get_ad_views(id))
    
    return render(request, 'ad_view.html', context={
        'ad':          ad,
        'views_count': views_count
    })

@require_GET
@login_required
def ads_list(request):
    return render(request, 'ads_list.html', context={
        'ads': Ad.objects.all()
    })

@require_http_methods(['GET', 'POST'])
@login_required
def new_ad(request):
    if request.method == 'GET':
        return render(request, 'ad_editor.html')
    
    elif request.method == 'POST': 
        try:
            title   = request.POST['title']
            content = request.POST['content']
        except KeyError as e:
            return resp.error_missed_form_field(e.args[0]) 

        Ad.objects.create(
            title=title,
            content=content
        )

        return redirect('/ads')

@require_http_methods(['GET', 'PATCH', 'DELETE'])
@login_required
@csrf_exempt
def ad_edit(request, id): 
    try: 
        ad = Ad.objects.get(id=id)
    except Ad.DoesNotExists:
        return resp.error_not_found(id=id)  

    if request.method == 'GET':               
        return render(request, 'ad_editor.html', context={
            'ad': ad
        })
        
    elif request.method == 'PATCH':
        req_data = parse_qs(request.body.decode())

        if 'csrfmiddlewaretoken' in req_data:
            del req_data['csrfmiddlewaretoken']

        for k,v in req_data.items():
            setattr(ad, k, v[0])

        ad.save()

        return resp.ok()

    elif request.method == 'DELETE':
        ad.delete()

        return resp.ok() 
