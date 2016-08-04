import path from 'path'
import webpack from 'webpack'
import WebpackNotifierPlugin from 'webpack-notifier'
import UnminifiedWebpackPlugin from 'unminified-webpack-plugin'

module.exports = {
  context: __dirname,
  entry: path.join(__dirname, 'view/index.js'),
  output: {
    filename: 'static/js/bundle.min.js',
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
  plugins: [
    new webpack.optimize.UglifyJsPlugin({
      compress: { warnings: false }
    }),
    new UnminifiedWebpackPlugin(),
    new WebpackNotifierPlugin({ alwaysNotify: true }),
  ],
  resolve: {
    extensions: ['', '.js', '.json'],
  },
  watchOptions: {
    poll: true
  },
  postcss: function () {
    return [
      require('autoprefixer'),
      require('precss'),
      require('postcss-clearfix'),
      require('postcss-calc'),
    ];
  },
}
