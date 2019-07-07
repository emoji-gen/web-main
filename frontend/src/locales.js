'use strict'

import ja from '@/locales/ja'
import ko from '@/locales/ko'

export function getLocale() {
  return document.documentElement.lang || 'ja'
}

export function getLocales() {
  return ['ja', 'ko']
}

export function getLocalePath() {
  switch (getLocale()) {
    case 'ko':
      return '/ko'
    default:
      return ''
  }
}

export const messages = {
  ja,
  ko,
}
