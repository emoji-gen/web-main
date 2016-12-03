import queryString from 'query-string'
import 'whatwg-fetch'
import meta from './meta'

const baseUrl = 'https://api-ssl.bitly.com/v3/'
const baseQuery = {
  access_token: '1af5c5aa6d54b824861bfe77d3566be1f6548a7b',
}

module.exports = {
  shorten: function (longUrl) {
    let queryLongUrl = longUrl

    // for debug
    if (meta.env.debug) {
      queryLongUrl = queryLongUrl.replace(/localhost:\d+/, meta.env.domain)
    }

    const query   = Object.assign({ longUrl: queryLongUrl, format: 'txt' }, baseQuery)
    const url     = `${baseUrl}shorten?${queryString.stringify(query)}`

    return fetch(url).then(res => res.text())
  },
}
