'use strict'

import merge from 'lodash.merge'

import en from '@/locales/en'
import ja from '@/locales/ja'
import ko from '@/locales/ko'

import { EXTRA_MESSAGES } from '@/src/initial_state'

// --------------------------------------------------------

export const DEFAULT_LOCALE = 'ja'
export const LOCALES = ['en', 'ja', 'ko']

export function getLocale() {
  const locale = document.documentElement.lang || DEFAULT_LOCALE
  if (LOCALES.includes(locale)) {
    return locale
  }
  return DEFAULT_LOCALE
}

export function toLocalizedPath(unlocalizedPath, locale) {
  const _locale = locale || getLocale()
  if (_locale !== DEFAULT_LOCALE && LOCALES.includes(_locale)) {
    return '/' + _locale + unlocalizedPath
  }
  return unlocalizedPath
}

export function toUnlocalizedPath(localizedPath) {
  for (const locale of LOCALES) {
    if (locale !== DEFAULT_LOCALE) {
      if (localizedPath.startsWith('/' + locale + '/')) {
        return localizedPath.substring(locale.length + 1)
      }
    }
  }
  return localizedPath
}

export function setLocale(locale) {
  document.documentElement.lang = locale
}


export const MESSAGES = {
  en: merge(en, EXTRA_MESSAGES.en),
  ja: merge(ja, EXTRA_MESSAGES.ja),
  ko: merge(ko, EXTRA_MESSAGES.ko),
}
