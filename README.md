# jitney

* Prerequisites:
	- Python && pip
	- npm && node
	- venv


```bash
$ python -m venv jitney/
$ source jitney/bin/activate
$ (jitney) export FLASK_APP=jitney
$ (jitney) pip install -r requirements.py
$ (jitney) flask init-db
... do stuff
$ (jitney) cd jitney && npm install & npm run build
...ensure you are one dir above jitney itself
$ (jitney) flask run
```

