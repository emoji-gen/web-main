Server-side - Emoji Generator
-----------------------------

## Requirements

  - Python `$(cat .python-version)`
  - MySQL 5.7

### Getting started

```
$ ./script/pip-install.sh
$ python app.py
```

#### Database
Emoji Generator requires MySQL database for saving emoji generated histories.

First, try to type commands as following.

```
$ ./db/setup.sh
```

#### venv

It is recommended that you use the venv.

If in *inux environemnts:

```
$ python -m venv venv
$ source venv/bin/activate

...

$ deactivate # exit
```

