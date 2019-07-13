'use strict'

import merge from 'lodash.merge'

import ja from '@/locales/ja'
import ko from '@/locales/ko'
import zhHans from '@/locales/zh-Hans'
import en from '@/locales/en'

import { EXTRA_MESSAGES } from '@/src/initial_state'


// --------------------------------------------------------
// Locale utilities
// --------------------------------------------------------

export const DEFAULT_LOCALE = 'ja'
export const LOCALES = ['ja', 'ko', 'zh-Hans', 'en']

export const INITIAL_LOCALE = getLocale()

export function detectLocale(localizedPath) {
  for (const locale of LOCALES) {
    if (locale !== DEFAULT_LOCALE) {
      if (localizedPath.startsWith('/' + locale + '/')) {
        return locale
      }
    }
  }
  return DEFAULT_LOCALE
}

export function getLocale() {
  const locale = document.documentElement.lang || DEFAULT_LOCALE
  if (LOCALES.includes(locale)) {
    return locale
  }
  return DEFAULT_LOCALE
}

export function setLocale(locale) {
  document.documentElement.lang = locale
}

export function toLocalizedPath(unlocalizedPath, locale) {
  const _locale = locale || getLocale()
  if (_locale !== DEFAULT_LOCALE && LOCALES.includes(_locale)) {
    return '/' + _locale + unlocalizedPath
  }
  return unlocalizedPath
}

export function toUnlocalizedPath(localizedPath) {
  const locale = detectLocale(localizedPath)
  if (locale === DEFAULT_LOCALE) {
    return localizedPath
  }
  return localizedPath.substring(locale.length + 1)
}


// --------------------------------------------------------
// Localized messages
// --------------------------------------------------------

export const MESSAGES = {
  ja: merge(ja, EXTRA_MESSAGES.ja),
  ko: merge(ko, EXTRA_MESSAGES.ko),
  'zh-Hans': merge(zhHans, EXTRA_MESSAGES['zh-Hans']),
  en: merge(en, EXTRA_MESSAGES.en),
}
