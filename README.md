djangomx-python-flask-2014-10-22
================================


This app was used in DjangoMX 2014-10-22 to show how to create a charge and an app using Flask.

To run, execute the following commands:

```bash
virtualenv venv --distribute
source venv/bin/activate
pip install -r requirements.txt --allow-all-external
```
If you are using Heroku + Foreman

```bash
gem install foreman
foreman start
#open http://127.0.0.1:5000 to test app
heroku create
git push heroku master
#open your heroku app
```

For an live example checkout [this heroku app](https://secret-crag-2820.herokuapp.com/).

For further reading checkout our [docs](https://www.conekta.io/es/docs/tutoriales/pagos-con-tarjeta).

To see your test charges in our [admin](https://admin.conekta.io/es#charges.charge?id=5448327019ce883a43000219).

Cualquier duda que tengas, [mandanos un correo](mailto:soporte@conekta.io)!

License
-------
Developed by [Conekta](https://www.conekta.io). Available with [MIT License](LICENSE).
