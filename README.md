Emoji-Web
---------
:tada: Ultimate Emoji Generator

## Requirements

  - Python 3.5
  - Node 6.9.1
  - memcached
  - Redis

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
v6.9.1

$ npm i -g yarn
$ yarn --version
0.16.1

$ yarn
$ yarn start     # for development
$ yarn run build # for production
```

## License
Copyright (C) 2016 Emoji Generator.
