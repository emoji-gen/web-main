'use strict'

import merge from 'lodash.merge'

import ja from '@/locales/ja'
import ko from '@/locales/ko'

import { MESSAGES } from '@/src/initial_state'


export function getLocale() {
  return document.documentElement.lang || 'ja'
}

export function getLocales() {
  return ['ja', 'ko']
}

export function getLocalePrefix() {
  switch (getLocale()) {
    case 'ko':
      return '/ko'
    default:
      return ''
  }
}

export function toLocalizedPath(path) {
  return getLocalePrefix() + path
}

export const messages = {
  ja: merge(ja, MESSAGES.ja),
  ko: merge(ko, MESSAGES.ko),
}
