djangomx-python-flask-2014-10-22
================================


This app was used in DjangoMX 2014-10-22 to show how to create a charge and an app using Flask.

To run, execute the following commands:

```bash
virtualenv venv --distribute
source venv/bin/activate
pip install Flask gunicorn conekta
```
If you are using Heroku + Foreman

```bash
gem install foreman
foreman start
#open http://127.0.0.1:5000
```

License
-------
Developed by [Conekta](https://www.conekta.io). Available with [MIT License](LICENSE).
