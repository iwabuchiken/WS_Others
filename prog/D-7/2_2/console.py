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


=========================================== 2018/01/30 16:24:08
pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL\Admin_Projects

python manage.py runserver

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL\Admin_Projects>python manage.
        y runserver
        Unhandled exception in thread started by <function check_errors.<locals>.wrappe
         at 0x00000000040387B8>
        Traceback (most recent call last):
          File "C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\env\lib\site-packages\djan
        o\utils\autoreload.py", line 226, in wrapper
            fn(*args, **kwargs)
          File "C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\env\lib\site-packages\djan
        o\core\management\commands\runserver.py", line 113, in inner_run
            autoreload.raise_last_exception()
          File "C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\env\lib\site-packages\djan
        o\utils\autoreload.py", line 249, in raise_last_exception
            six.reraise(*_exception)
          File "C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\env\lib\site-packages\djan
        o\utils\six.py", line 685, in reraise
            raise value.with_traceback(tb)
          File "C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\env\lib\site-packages\djan
        o\utils\autoreload.py", line 226, in wrapper
            fn(*args, **kwargs)
          File "C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\env\lib\site-packages\djan
        o\__init__.py", line 27, in setup
            apps.populate(settings.INSTALLED_APPS)
          File "C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\env\lib\site-packages\djan
        o\apps\registry.py", line 85, in populate
            app_config = AppConfig.create(entry)
          File "C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\env\lib\site-packages\djan
        o\apps\config.py", line 90, in create
            module = import_module(entry)
          File "C:\WORKS_2\WS\WS_Others\prog\D-34\5_\VIRTUAL\env\lib\importlib\__init__
        py", line 126, in import_module
            return _bootstrap._gcd_import(name[level:], package, level)
          File "<frozen importlib._bootstrap>", line 986, in _gcd_import
          File "<frozen importlib._bootstrap>", line 969, in _find_and_load
          File "<frozen importlib._bootstrap>", line 956, in _find_and_load_unlocked
        ImportError: No module named 'im'

------------------------------------------------------ 2018/01/30 16:24:08
(env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL\Admin_Projects>pip list
        DEPRECATION: The default format will switch to columns in the future. You can us
        e --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.con
        f under the [list] section) to disable this warning.
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


pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL
python -m virtualenv env

        C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL>python -m virtualenv env
        Using base prefix 'C:\\WORKS_2\\Programs\\Python\\Python_3.5.1'
        New python executable in C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL\env\Scripts
        \python.exe
        Installing setuptools, pip, wheel...done.
        
env\Scripts\activate.bat

python -m pip install django==1.10

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL>python -m pip install django==
        1.10
        Collecting django==1.10
          Using cached Django-1.10-py2.py3-none-any.whl
        Installing collected packages: django
        Successfully installed django-1.10

pip install sympy numpy matplotlib

        (env) C:\WORKS_2\WS\WS_Others\prog\D-7\2_\VIRTUAL>pip install sympy numpy matplotlib
        Collecting sympy
        Collecting numpy
          Using cached numpy-1.14.0-cp35-none-win_amd64.whl
        Collecting matplotlib
          Using cached matplotlib-2.1.2-cp35-cp35m-win_amd64.whl
        Collecting mpmath>=0.19 (from sympy)
        Collecting python-dateutil>=2.1 (from matplotlib)
          Using cached python_dateutil-2.6.1-py2.py3-none-any.whl
        Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib)
          Using cached pyparsing-2.2.0-py2.py3-none-any.whl
        Collecting cycler>=0.10 (from matplotlib)
          Using cached cycler-0.10.0-py2.py3-none-any.whl
        Collecting pytz (from matplotlib)
          Using cached pytz-2017.3-py2.py3-none-any.whl
        Collecting six>=1.10 (from matplotlib)
          Using cached six-1.11.0-py2.py3-none-any.whl
        Installing collected packages: mpmath, sympy, numpy, six, python-dateutil, pyparsing, cycler, pytz, matplotlib
        Successfully installed cycler-0.10.0 matplotlib-2.1.2 mpmath-1.0.0 numpy-1.14.0 pyparsing-2.2.0 python-dateutil-2.6.1 pytz-2017.3 six-1.11.0 sympy-1.1.1














'''
