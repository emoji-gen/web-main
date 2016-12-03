'use strict'

module.exports = {
  'extends': 'airbnb-base',
  'env': {
    'browser': true,
  },
  'rules': {
    'no-unused-vars': 2,
    'object-shorthand': 1,
    'comma-dangle': 1,
    'no-new': 1,
    'arrow-parens': 1,
    'object-curly-spacing': 1,
    'strict': [1, 'global'],

    'semi': 0,
    'global-require': 0,
    'no-bitwise': 0,
    'no-multi-spaces': 0,
    'import/newline-after-import': 0,
  },
}
