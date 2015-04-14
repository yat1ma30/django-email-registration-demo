# Django Email Registration Demo

This is a small demo project using email and password authentication.
This project depens on [django-registration v1.2](https://github.com/macropin/django-registration).


## Features

This demo contains following features.

* Email as an username
* Registration with sending activation key
* Login
* Logout


## Running this app

You can run this app easily.

```
$ git clone https://github.com/ottatiyarou/django-email-registration-demo.git
$ cd django-email-registration-demo
$ pip install -r requirements.txt
$ ./manage.py syncdb
$ ./manage.py runserver
```

Then open the browser and navigate to http://localhost:8000


## Running SMTP server on Python for dev

```
$ python -m smtpd -n -c DebuggingServer localhost:1025
```
