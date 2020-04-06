# jitney

* Prerequisites:
	- Python && pip
	- npm && node
	- venv


```bash
$ python -m venv jitney/
$ source jitney/bin/activate
$ (jitney) export FLASK_APP=jitney
$ (jitney) cd jitney/ && pip install -r requiremnets.py && npm install && npm run build
$ (jitnet) cd ..
$ (jitney) flask init-db
$ (jitney) flask run
```

There are some environment variables that will need to be set, namely:

- the database
- the app secret key

