from settings import * 

DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'prueba',
        'USER': 'postgres',
        'PASSWORD': 'camilo0210',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
