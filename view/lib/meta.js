function getMetaValue(name) {
  const elem = document.querySelector(`meta[name="${name}"]`)
  return elem ? elem.getAttribute('content') : null
}

module.exports = {
  env: {
    debug: getMetaValue('app:env:debug') === 'true',
    domain: getMetaValue('app:env:domain'),
  },
  feature: {
    history: getMetaValue('app:feature:history') === 'true',
  },
}
