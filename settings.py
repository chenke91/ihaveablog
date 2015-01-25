#coding:utf-8
bind = 'unix:/var/run/gunicorn.sock'

workers = 4

# you should change this
user = 'root'

# maybe you like error
loglevel = 'warning'
errorlog = '-'

secure_scheme_headers = {
    'X-SCHEME': 'https',
}
x_forwarded_for_header = 'X-FORWARDED-FOR'

### gunicorn -c settings.py -b 0.0.0.0:9000  wsgi:app
