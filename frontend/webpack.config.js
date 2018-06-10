'use strict'

const { join } = require('path')
const webpack = require('webpack')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const VueLoaderPlugin = require('vue-loader/lib/plugin')

const isDev = ~process.argv.indexOf('--watch')
const mode = isDev ? 'development' : 'production'

module.exports = {
  mode,

  // Entry and Context
  context: __dirname,
  entry: {
    desktop: './src/desktop/index.js',
  },

  // Output
  output: {
    filename: 'js/[name].js',
    path: join(__dirname, '../server/public'),
  },

  // Module
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
        },
      },
      {
        test: /\.js$/,
        loader: 'babel-loader'
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'postcss-loader',
          {
            loader: 'sass-loader',
            options: {
              includePath: [
                join(__dirname, 'src'),
              ],
            },
          },
        ],
      }
    ]
  },

  // Resolve
  resolve: {
    extensions: ['.js', '.vue', '.scss'],
    modules: [
      join(__dirname, 'src'),
      'node_modules',
    ],
  },

  // Plugins
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'css/[name].css',
    }),
    new webpack.DefinePlugin({
      DEBUG: isDev,
    }),
    new VueLoaderPlugin()
  ],

  // Watch and WatchOptions
  watchOptions: {
    poll: true,
  },
}
