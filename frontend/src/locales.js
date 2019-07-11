'use strict'

import merge from 'lodash.merge'

import en from '@/locales/en'
import ja from '@/locales/ja'
import ko from '@/locales/ko'

import { MESSAGES } from '@/src/initial_state'

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

export function getLocales() {
  return LOCALES
}

export function getLocalePrefix(locale) {
  const _locale = locale || getLocale()
  if (_locale !== DEFAULT_LOCALE && LOCALES.includes(_locale)) {
    return '/' + _locale
  }
  return ''
}

export function toLocalizedPath(path, locale) {
  return getLocalePrefix(locale) + path
}

export const messages = {
  en: merge(en, MESSAGES.en),
  ja: merge(ja, MESSAGES.ja),
  ko: merge(ko, MESSAGES.ko),
}
