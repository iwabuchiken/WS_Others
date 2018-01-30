'''

### copied from : C:\WORKS_2\WS\WS_Others\prog\D-7\1_\console.py

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

        # import django
        # django.get_version()
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
          Rendering model statesDONE
          Applying contenttypes.0001_initialOK
          Applying auth.0001_initialOK
          Applying admin.0001_initialOK
          Applying admin.0002_logentry_remove_auto_addOK
          Applying contenttypes.0002_remove_content_type_nameOK
          Applying auth.0002_alter_permission_name_max_lengthOK
          Applying auth.0003_alter_user_email_max_lengthOK
          Applying auth.0004_alter_user_username_optsOK
          Applying auth.0005_alter_user_last_login_nullOK
          Applying auth.0006_require_contenttypes_0002OK
          Applying auth.0007_alter_validators_add_error_messagesOK
          Applying auth.0008_alter_user_username_max_lengthOK
          Applying sessions.0001_initialOK

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

------------------------------------ 
pushd C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB
env\Scripts\activate.bat

cd django_project

python manage.py shell

from django import template
t = template.Template("We are learning {{ name }}")
c = template.Context({'name': 'Django'})
print(t.render(c))

c2 = template.Context({'name': 'a new web framework'})
print(t.render(c2))

c = template.Context()
print(t.render(c))

t2 = template.Template("We are learning {{ name }} with {{name}}")
c2 = template.Context({'name': 'a new web framework'})
print(t2.render(c2))

t2 = template.Template("We are learning {{ name }} with {{name2}}")
dic = {'name': 'a new web framework', 'name2': 'framework'}
c2 = template.Context(dic)
print(t2.render(c2))

/------------------------------------ 2018/01/25 18:10:47
------------------------------------ 
framework = {
'first': 'Django',
'second': 'Laravel',
'third': 'Spring',
'fourth': 'CodeIgniter'
}

t = template.Template("We are learning {{ framework.first }}")
c = template.Context({'framework': framework})
print(t.render(c))

------------------------------------ 
import datetime
now = datetime.datetime.now()
now.day

now.month

now.year



t = template.Template("Date is {{ now.day }}-{{ now.month }}-{{ now.year }}")
c = template.Context({'now':now})
print(t.render(c))

name = "django"
name.capitalize()

name.upper()

name


t = template.Template("{{ var.capitalize }} learning {{ var.upper }}")
c = template.Context({'var': name})
print(t.render(c))

def abc() : print("abc")
c = template.Context({'now':now})
t = template.Template("{{ var.capitalize }} learning {{ var.upper }}")


list = ['Ruby on Rails', 'Django', 'Laravel']
t = template.Template("We are learning {{ list.1 }} ")
t = template.Template("We are learning {{ list.1 }}, but we love {{list.0}}")
c = template.Context({'list': list})
print(t.render(c))

==================================== 2018/01/26 07:06:41
pip install sympy

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB\django_project>pip install sympy
        Collecting sympy
        Collecting mpmath>=0.19 (from sympy)
        Installing collected packages: mpmath, sympy
        Successfully installed mpmath-1.0.0 sympy-1.1.1

pushd C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB
env\Scripts\activate.bat

cd django_project

pip install numpy

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB\django_project>pip install numpy
        
        Collecting numpy
          Downloading numpy-1.14.0-cp35-none-win_amd64.whl (13.4MB)
            100% |################################| 13.4MB 74kB/s 
        Installing collected packages: numpy
        Successfully installed numpy-1.14.0

pip install matplotlib

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\1_\TGDB\django_project>pip install matplotlib
        
        Collecting matplotlib
        
            100% |################################| 8.7MB 113kB/s 
        Collecting pytz (from matplotlib)
          Using cached pytz-2017.3-py2.py3-none-any.whl
        Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib)
          Using cached pyparsing-2.2.0-py2.py3-none-any.whl
        Collecting six>=1.10 (from matplotlib)
          Using cached six-1.11.0-py2.py3-none-any.whl
        Collecting python-dateutil>=2.1 (from matplotlib)
          Using cached python_dateutil-2.6.1-py2.py3-none-any.whl
        Collecting cycler>=0.10 (from matplotlib)
          Using cached cycler-0.10.0-py2.py3-none-any.whl
        Requirement already satisfied: numpy>=1.7.1 in c:\works_2\ws\ws_others\prog\d-7\1_\tgdb\env\lib\site-packages (from matplotlib)
        Installing collected packages: pytz, pyparsing, six, python-dateutil, cycler, matplotlib
        Successfully installed cycler-0.10.0 matplotlib-2.1.2 pyparsing-2.2.0 python-dateutil-2.6.1 pytz-2017.3 six-1.11.0










'''
