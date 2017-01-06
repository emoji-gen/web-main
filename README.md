Emoji-Web
---------
:tada: Ultimate Emoji Generator

## Requirements

  - Python 3.5
  - Node 6.9.2
  - memcached
  - Redis
  - MySQL 5.6

## Frameworks

- [Flask](http://flask.pocoo.org/)
- [Vue](https://vuejs.org/)

## Getting Started
### Server Side

```
$ python --version
Python 3.5.0

$ pip install -r requirements.txt
$ python app.py
```

#### Database
Emoji Generator requires MySQL database for saving emoji generated histories.

First, try to type commands as following.

```
$ ./db/setup.sh
```

#### Job Queue
Emoji Generator use [RQ](http://python-rq.org/) and Redis as job queue.

Try to type command as following.

`$ rq worker high normal low`

#### venv

It is recommended that you use the venv.

If in *inux environemnts:

```
$ python -m venv venv
$ source venv/bin/activate

...

$ deactivate # exit
```

### fonts
You should download used fonts for `assets/fonts` directory.

### Frontend

```
$ node -v
v6.9.2

$ npm i -g yarn
$ yarn --version
0.16.1

$ yarn
$ yarn start     # for development
$ yarn run build # for production
```

## Public API
Emoji Generator has public API for third-party applications.

Please see API references.

- http://docs.emojigeneratorapi.apiary.io/

## License
Copyright (C) 2016-2017 Emoji Generator.
