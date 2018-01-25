'''

#ref https://www.quora.com/How-do-I-install-PIP-in-python-3-5
#ref https://overiq.com/django/1.10/installing-django/#installing-python-virtual-environment "To install virtualenv on Windows"
python -m pip install virtualenv

        C:\WORKS_2\WS\WS_Others\prog\D-7\1_>python -m pip install virtualenv
        Collecting virtualenv
          Downloading virtualenv-15.1.0-py2.py3-none-any.whl (1.8MB)
            100% |################################| 1.8MB 356kB/s
        Installing collected packages: virtualenv
        Successfully installed virtualenv-15.1.0
    

python -m pip list

python -m virtualenv env

        C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB>python -m virtualenv env
        Using base prefix 'C:\\WORKS_2\\Programs\\Python\\Python_3.5.1'
        New python executable in C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB\env\Scripts\py
        thon.exe
        Installing setuptools, pip, wheel...done.
        
python -m pip --version

        C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB>python -m pip --version
        pip 9.0.1 from C:\WORKS_2\Programs\Python\Python_3.5.1\lib\site-packages (python
         3.5)

======================================
#ref https://overiq.com/django/1.10/installing-django/#activating-virtualenv

pushd C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB
env\Scripts\activate.bat

pip list

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB>pip list
        DEPRECATION: The default format will switch to columns in the future. You can us
        e --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.con
        f under the [list] section) to disable this warning.
        pip (9.0.1)
        setuptools (38.4.0)
        wheel (0.30.0)

====================================
https://overiq.com/django/1.10/installing-django/#installing-django

env\Scripts\activate.bat

python -m pip install django==1.10

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB>python -m pip install django==1.1
        0
        Collecting django==1.10
          Downloading Django-1.10-py2.py3-none-any.whl (6.8MB)
            100% |################################| 6.8MB 136kB/s
        Installing collected packages: django
        Successfully installed django-1.10

https://overiq.com/django/1.10/installing-django/#testing-the-installation

python

'''
import django
django.get_version()

        # >>> import django
        # >>> django.get_version()
        # '1.10'

'''
==================================== 2018/01/24 19:34:53
pushd C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB
env\Scripts\activate.bat

django-admin startproject django_project

cd django_project

python manage.py runserver

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB\django_project>python manage.py r
        unserver
        Performing system checks...
        
        System check identified no issues (0 silenced).
        
        You have 13 unapplied migration(s). Your project may not work properly until you
         apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        January 24, 2018 - 19:38:25
        Django version 1.10, using settings 'django_project.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


==================================== 2018/01/25 14:02:03
pushd C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB
cd django_project
python manage.py migrate > migrate.log

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB\django_project>Operations to perform:
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

python manage.py runserver

        Performing system checks...
        
        System check identified no issues (0 silenced).
        January 25, 2018 - 14:02:59
        Django version 1.10, using settings 'django_project.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

------------------------------------ 2018/01/25 14:08:41
pushd C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB
env\Scripts\activate.bat

cd django_project

python manage.py startapp blog

python manage.py runserver

'''
