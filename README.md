## Emoji Generator
[![CircleCI](https://circleci.com/gh/emoji-gen/web-main/tree/master.svg?style=shield)](https://circleci.com/gh/emoji-gen/web-main/tree/master)
[![dependencies Status](https://david-dm.org/emoji-gen/web-main/status.svg)](https://david-dm.org/emoji-gen/web-main)
[![devDependencies Status](https://david-dm.org/emoji-gen/web-main/dev-status.svg)](https://david-dm.org/emoji-gen/web-main?type=dev)

:tada: Ultimate Emoji Generator
<br>
<br>

## Requirements

  - Python `$(cat .python-version)`
  - Node `$(cat .node-version)`
  - MySQL 5.7

## Libraries

- [aiohttp](https://github.com/aio-libs/aiohttp) - Server-side framework
- [Vue](https://vuejs.org/) - Frontend framework
- [Skia](https://skia.org/) - Graphics library

## Getting Started

- [Server-side setup document](server/README.md)

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
