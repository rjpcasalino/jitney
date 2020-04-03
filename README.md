# jitney

```bash
$ virtualenv jitney/
$ source jitney/bin/activate
$ (jitney) export FLASK_APP=jitney
$ (jitney) flask init-db
... do stuff
$ (jitney) cd jitney && npm install & npm run build
...ensure you are one dir above jitney itself
$ (jitney) flask run
```

