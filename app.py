# -*- coding: utf-8 -*-

import sys
import os

cwd = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(cwd, 'src')
sys.path.append(src_path)

from emoji import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
