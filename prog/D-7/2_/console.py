'''
=========================================== 2018/01/29 17:08:31
pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_

python -m pip list


pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL
python -m virtualenv env

        C:\WORKS_2\WS\WS_Others\prog\D-7\2_>pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL
        python -m virtualenv env
        
        
        C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL>Using base prefix 'C:\\WORKS_2\\Programs\\Python\\Python_3.5.1'
        New python executable in C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL\env\Scripts\python.exe
        C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL\envInstalling setuptools, pip, wheel...Collecting setuptools
          Using cached setuptools-38.4.0-py2.py3-none-any.whl
        Collecting pip
        Collecting wheel
          Using cached wheel-0.30.0-py2.py3-none-any.whl
        Installing collected packages: setuptools, pip, wheel
        Successfully installed pip-9.0.1 setuptools-38.4.0 wheel-0.30.0
        done.

env\Scripts\activate.bat

python -m pip install django==1.10

        C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL>env\Scripts\activate.bat
        
        
        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL>python -m pip install django==1.10
        
        Collecting django==1.10
          Using cached Django-1.10-py2.py3-none-any.whl
        Installing collected packages: django
        Successfully installed django-1.10

python

import django
django.get_version()

------------------------------------------------------ 2018/01/29 17:18:34
pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL
django-admin startproject admin_MindMapFiles

pushd admin_MindMapFiles

python manage.py runserver

pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL
env\Scripts\activate.bat

pushd admin_MindMapFiles
python manage.py migrate > migrate.log

(env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL>pushd admin_MindMapFiles
python manage.py migrate > migrate.log

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL\admin_MindMapFiles>Operations to perform:
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

## 'mm' ---> mindmap manager
python manage.py startapp mm


------------------------------------------------------ 2018/01/29 17:25:56
#ref install at once https://stackoverflow.com/questions/9956741/how-to-install-multiple-python-packages-at-once-using-pip
pip install sympy numpy matplotlib

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL\admin_MindMapFiles>pip list
        DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
        cycler (0.10.0)
        Django (1.10)
        matplotlib (2.1.2)
        mpmath (1.0.0)
        numpy (1.14.0)
        pip (9.0.1)
        pyparsing (2.2.0)
        python-dateutil (2.6.1)
        pytz (2017.3)
        setuptools (38.4.0)
        six (1.11.0)
        sympy (1.1.1)
        wheel (0.30.0)

------------------------------------------------------ 2018/01/29 17:50:45
C/P ---> C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\admin_CakeIFM_11


pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL
python -m virtualenv env2

env2\Scripts\activate.bat

python -m pip install django==1.10
        (env2) C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL>python -m pip install django==1.10
        
        Collecting django==1.10
          Using cached Django-1.10-py2.py3-none-any.whl
        Installing collected packages: django
        Successfully installed django-1.10






'''
