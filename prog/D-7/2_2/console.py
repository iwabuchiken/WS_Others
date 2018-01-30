'''
=========================================== 2018/01/30 17:49:44
pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL

python -m virtualenv env

        C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL>python -m virtualenv env
        Using base prefix 'C:\\WORKS_2\\Programs\\Python\\Python_3.5.1'
        New python executable in C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\env\Script
        s\python.exe
        Installing setuptools, pip, wheel...done.

env\Scripts\activate.bat

python -m pip install django==1.10

        env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL>python -m pip install django
        1.10
        ollecting django==1.10
         Using cached Django-1.10-py2.
         py3-none-any.whl
        nstalling collected packages: django
        uccessfully installed django-1.10

django-admin startproject Admin_Projects

pushd Admin_Projects

python manage.py runserver

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects>python manage.
        py runserver
        Performing system checks...
        
        System check identified no issues (0 silenced).
        
        You have 13 unapplied migration(s). Your project may not work properly until you
         apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        January 30, 2018 - 17:55:50
        Django version 1.10, using settings 'Admin_Projects.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

#ref C:\WORKS_2\WS\WS_Others\prog\D-34\5_\console.py
python manage.py migrate > migrate.log

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects>python manage.py migrate > migrate.log
        
        Operations to perform:
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

python manage.py startapp mm

pip install sympy numpy matplotlib

(env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects>pip install sympy numpy matplotlib

        Collecting sympy
        Collecting numpy
          Using cached numpy-1.14.0-cp35-none-win_amd64.whl
        Collecting matplotlib
          Using cached matplotlib-2.1.2-cp35-cp35m-win_amd64.whl
        Collecting mpmath>=0.19 (from sympy)
        Collecting cycler>=0.10 (from matplotlib)
          Using cached cycler-0.10.0-py2.py3-none-any.whl
        Collecting python-dateutil>=2.1 (from matplotlib)
          Using cached python_dateutil-2.6.1-py2.py3-none-any.whl
        Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib)
          Using cached pyparsing-2.2.0-py2.py3-none-any.whl
        Collecting six>=1.10 (from matplotlib)
          Using cached six-1.11.0-py2.py3-none-any.whl
        Collecting pytz (from matplotlib)
          Using cached pytz-2017.3-py2.py3-none-any.whl
        Installing collected packages: mpmath, sympy, numpy, six, cycler, python-dateutil, pyparsing, pytz, matplotlib
        Successfully installed cycler-0.10.0 matplotlib-2.1.2 mpmath-1.0.0 numpy-1.14.0 pyparsing-2.2.0 python-dateutil-2.6.1 pytz-2017.3 six-1.11.0 sympy-1.1.1
















'''
