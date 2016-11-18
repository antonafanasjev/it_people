# it_people

Language: python 3.5 

## Usage

### Add new user

Run shell: 
```
python3 manage.py shell
```

And type: 
```
from django.contrib.auth.models import User
User.objects.create_user('name', 'email@something.com', 'password')
```

## Deploy

Tested deploy: NGINX + uwsgi

NGINX config sample: 
```
server {
  listen 80;
  server_name mysite.com;
  
  location / {
    include uwsgi_params;
    uwsgi_pass unix:/tmp/ads.sock
  }
  
  location /static {
    alias /your/project/path/ads/editor/static; 
  }
}
```

UWSGI .ini sample: 
```
[uwsgi]
chdir = /your/project/path/
home = /your/virtualenv/dir
module = ads.wsgi

socket = /tmp/ads.sock
chmod-socket=666
vacuum = true
```
