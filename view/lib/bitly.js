import queryString from 'query-string'

const baseUrl = 'https://api-ssl.bitly.com/v3/'
const baseQuery = {
  access_token: '1af5c5aa6d54b824861bfe77d3566be1f6548a7b'
}

module.exports = {
  shorten: function (longUrl) {
    const query = Object.assign({ longUrl: longUrl })
    const xhr   = new XMLHttpRequest()
    xhr.open('GET', `${baseUrl}shorten?${queryString.stringify(query)}`)
  },
}
