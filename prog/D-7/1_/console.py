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









