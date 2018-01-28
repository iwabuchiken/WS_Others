'''
====================================== 2018/01/28 07:11:32
python -m virtualenv env

        C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL>python -m virtualenv env
        Using base prefix 'C:\\WORKS_2\\Programs\\Python\\Python_3.5.1'
        New python executable in C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\env\Scripts\python.exe
        C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\envInstalling setuptools, pip, wheel...Collecting setuptools
          Using cached setuptools-38.4.0-py2.py3-none-any.whl
        Collecting pip
        Collecting wheel
          Using cached wheel-0.30.0-py2.py3-none-any.whl
        Installing collected packages: setuptools, pip, wheel
        Successfully installed pip-9.0.1 setuptools-38.4.0 wheel-0.30.0
        done.

python -m pip --version

        C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL>python -m pip --version
        
        pip 9.0.1 from C:\WORKS_2\Programs\Python\Python_3.5.1\lib\site-packages (python 3.5)

pushd C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL
env\Scripts\activate.bat

pip list

        pip list
        
        
        C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL>
        (env) C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL>DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
        pip (9.0.1)
        setuptools (38.4.0)
        wheel (0.30.0)

deactivate

        (env) C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL>deactivate
        
        C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL>

pushd C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL
env\Scripts\activate.bat

python -m pip install django==1.10

        (env) C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL>python -m pip install django==1.10
        
        Collecting django==1.10
          Using cached Django-1.10-py2.py3-none-any.whl
        Installing collected packages: django
        Successfully installed django-1.10

## https://overiq.com/django/1.10/installing-django/#testing-the-installation
pushd C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL
python

import django
django.get_version()

------------------------------------------------ 2018/01/28 08:58:26
pushd C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL
django-admin startproject admin_CakeIFM_11
cd admin_CakeIFM_11

python manage.py runserver

pushd C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\admin_CakeIFM_11
python manage.py migrate > migrate.log

    (env) C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL>pushd C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\admin_CakeIFM_11
    python manage.py migrate > migrate.log


    (env) C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\admin_CakeIFM_11>Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying sessions.0001_initial... OK

python manage.py startapp im


### https://overiq.com/django/1.10/handling-static-content-in-django/
http://127.0.0.1:8000/static/aaa.jpg
http://127.0.0.1:8000/im/static/aaa.jpg    #=> Page not found (404)





'''
