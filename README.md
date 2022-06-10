# workshops-tests

# how to start
1. install python: https://www.python.org/downloads/
2. make sure that you have pip https://pip.pypa.io/en/stable/installation/

    Usually, pip is automatically installed if you are:
   * working in a virtual environment
   * using Python downloaded from python.org

3. install `pip install virtualenv`
4. run `virtualenv venv` - it will create virtual env, everytime when you open new terminal you should run this to enter into virtualenv
5. make sure that you are in virutalenv
6. process to Install

# install
1. run `pip install -r requirements.txt`
2. run `python manage.py runserver`
3. enter `http://127.0.0.1:8000/` if you see website, you are ready!

# tests
1. run `pytest`