ALLOWED_HOSTS = ["*"]

APIS = {
    'authentication': 'http://localhost:8000',
    'base': 'http://localhost:8000',
    'booth': 'http://localhost:8000',
    'census': 'http://localhost:8000',
    'mixnet': 'http://localhost:8000',
    'postproc': 'http://localhost:8000',
    'store': 'http://localhost:8000',
    'visualizer': 'http://localhost:8000',
    'voting': 'http://localhost:8000',
}

BASEURL = 'http://localhost:8000'

DATABASES = {
    'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'covid19analyzer',
        'USER': 'c19auser',
        'PASSWORD': 'complexpassword',
        'HOST': 'localhost',
        'PORT': '5432',
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256