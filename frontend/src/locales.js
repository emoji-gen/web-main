'use strict'

import ja from '@/locales/ja'

export function getLocale() {
  return document.documentElement.lang || 'ja'
}

export const messages = {
  ja,
}
