import { join } from 'path'
import webpack from 'webpack'
import WebpackFailPlugin from 'webpack-fail-plugin'
import WebpackNotifierPlugin from 'webpack-notifier'
import UnminifiedWebpackPlugin from 'unminified-webpack-plugin'

const isWatch = ~process.argv.indexOf('--watch')
const plugins = [ new WebpackNotifierPlugin({ alwaysNotify: true }) ]

if (!isWatch) {
  plugins.push(
    new webpack.optimize.DedupePlugin(),
    new webpack.optimize.AggressiveMergingPlugin(),
    new webpack.optimize.UglifyJsPlugin({
      compress: { warnings: false },
      sourceMap: false,
    }),
    new UnminifiedWebpackPlugin(),
    WebpackFailPlugin,
  )
}

module.exports = {
  context: __dirname,
  entry: join(__dirname, 'view/index.js'),
  output: {
    filename: isWatch ? '../server/public/js/bundle.js' : '../server/public/js/bundle.min.js',
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel',
        query: {
          presets: ['es2015', 'stage-3']
        },
      },
      { test: /\.css$/, loader: 'style!css!postcss' },
      { test: /\.html$/, loader: 'html' },
      { test: /\.json$/, loader: 'json' },
    ]
  },
  plugins,
  resolve: {
    alias:{
      eg: join( __dirname, 'view'),
    },
    extensions: ['', '.js', '.json'],
  },
  watchOptions: {
    poll: true,
  },
  postcss() {
    return [
      require('postcss-import')({
        path: [ join(__dirname, 'view') ],
      }),
      require('precss'),
      require('postcss-clearfix'),
      require('postcss-calc'),
      require('autoprefixer'),
    ]
  },
}
