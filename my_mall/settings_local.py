# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'my_mall',
            'USER': 'root',
            'PASSWORD': 'ww19971214',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
}