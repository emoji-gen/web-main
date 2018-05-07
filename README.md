## Emoji Generator &nbsp;[![CircleCI](https://circleci.com/gh/emoji-gen/web-main/tree/master.svg?style=shield)](https://circleci.com/gh/emoji-gen/web-main/tree/master) [![Dependency Status](https://gemnasium.com/badges/github.com/emoji-gen/Emoji-Web.svg)](https://gemnasium.com/github.com/emoji-gen/Emoji-Web)

:tada: Ultimate Emoji Generator

## Requirements

  - Python `$(cat .python-version)`
  - Node `$(cat .node-version)`
  - MySQL 5.7

## Frameworks

- [aiohttp](https://github.com/aio-libs/aiohttp)
- [Vue](https://vuejs.org/)

## Getting Started
### Server Side

```
$ python --version
Python 3.5.0

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

## Other platforms

- [Emoji-CLI](https://github.com/emoji-gen/Emoji-CLI) (for Console)

## License
GPLv3 &copy; [Emoji Generator](https://emoji-gen.ninja)
