#!/bin/bash

set -eu

cd `dirname $0`

echo 'DROP DATABASE IF EXISTS `emoji`' | mysql -uroot
echo 'CREATE DATABASE `emoji`'         | mysql -uroot
cat table.sql                          | mysql -uroot emoji
