'use strict'

module.exports = {
  'extends': 'airbnb-base',
  'env': {
    'browser': true,
  },
  'globals': {
    'ga': true,
  },
  'rules': {
    'no-unused-vars': [ 2, { 'args': 'none' } ],
    'no-restricted-syntax': [ 2, 'WithStatement' ],

    'arrow-parens': 1,
    'comma-dangle': 1,
    'no-new': 1,
    'no-else-return': 1,
    'object-shorthand': 1,
    'object-curly-spacing': 1,
    'strict': [ 1, 'global' ],

    'global-require': 0,
    'import/newline-after-import': 0,
    'import/no-extraneous-dependencies': 0,
    'import/first': 0,
    'import/extensions': 0,
    'import/no-unresolved': 0,
    'no-bitwise': 0,
    'no-confusing-arrow': 0,
    'no-multi-spaces': 0,
    'no-nested-ternary': 0,
    'no-underscore-dangle': 0,
    'semi': 0,
  },
}
