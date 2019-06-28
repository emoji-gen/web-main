'use strict'

const { join } = require('path')

const webpack = require('webpack')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const EventHooksPlugin = require('event-hooks-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin')
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')
const VueLoaderPlugin = require('vue-loader/lib/plugin')

const isDev = process.argv.includes('--watch')
const mode = isDev ? 'development' : 'production'

module.exports = {
  mode,

  // Entry and Context
  //~~~~~~~~~~~~~~~~~~~~
  context: __dirname,
  entry: './src/main.js',


  // Output
  //~~~~~~~~~
  output: {
    filename: 'script.js',
    path: join(__dirname, '..', 'server/public'),
  },


  // Module
  //~~~~~~~~~
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
        },
      },
      {
        test: /\.html$/,
        loader: 'vue-template-loader',
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules\/(?!vue-color)/,
      },
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: { url: false },
          },
        ],
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: { url: false },
          },
          {
            loader: 'postcss-loader',
          },
          {
            loader: 'sass-loader',
            options: {
              includePaths: [ join(__dirname, 'src') ],
            },
          },
        ],
      },
      {
        test: /\.ya?ml$/,
        use: [
          {
            loader: 'json-loader',
          },
          {
            loader: 'yaml-loader',
          },
        ],
      },
    ]
  },


  // Resolve
  //~~~~~~~~~~
  resolve: {
    alias: {
      '@': __dirname,
      vue: 'vue/dist/vue.runtime.esm.js',
    },
    extensions: ['.js', '.vue', '.yml'],
  },


  // Optimization and Plugins
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~
  optimization: {
    minimizer: [
      new UglifyJsPlugin({
        uglifyOptions: {
          compress: {
            unsafe: true,
            unsafe_comps: true,
            unsafe_Function: true,
            unsafe_math: true,
            unsafe_proto: true,
            unsafe_regexp: true,
            unsafe_undefined: true,
          },
        },
      }),
      new OptimizeCSSAssetsPlugin(),
    ],
    noEmitOnErrors: true,
  },
  plugins: [
    new CleanWebpackPlugin({
      dry: false,
      dangerouslyAllowCleanPatternsOutsideProject: true,
      cleanOnceBeforeBuildPatterns:
        ['js', 'css'].map(v => join(__dirname, '..', `server/public/*.${v}`)),
      verbose: false,
    }),
    new EventHooksPlugin({
      run() { console.log('Mode: ' + mode) },
      watchRun() { console.log('Mode: ' + mode) },
    }),
    new MiniCssExtractPlugin({ filename: 'style.css' }),
    new webpack.DefinePlugin({ DEBUG: isDev }),
    new VueLoaderPlugin()
  ],


  // Watch and WatchOptions
  //~~~~~~~~~~~~~~~~~~~~~~~~~
  watchOptions: {
    poll: true,
    ignored: [ /node_modules/ ],
  },


  // Performance
  //~~~~~~~~~~~~~~~
  performance: {
    hints: false,
  },


  // Stats
  //~~~~~~~~
  stats: {
    entrypoints: true,
    children: false,
    colors: true,
    modules: false,
  },
}
