# -*- encoding: utf-8 -*-

import emojilib
import hashlib
from urllib.parse import urlencode, urljoin

class EmojiService():
    def __init__(self, app):
        self._app = app

    def generate(
        self,
        *,
        text,
        width,
        height,
        color,
        background_color,
        size_fixed,
        disable_stretch,
        align,
        font_path,
    ):
        # if len(text) > 100: # XXX: 100 文字以上
        #     return None

        # if len(lines) == 1 and len(lines[0]) > 10: # XXX: 1 列 10 文字以上
        #     return None

        # if len(lines) > 10: # XXX: 10 行以上
        #     return None

        return img_png

# def url_for(
#         text,
#         font,
#         color,
#         back_color,
#         size_fixed = False,
#         align = 'center',
#         stretch = True
#         ):
#     base_url = app.config['SITE_BASE_URL']
#     payload = {
#             'text': text,
#             'font': font,
#             'color': color,
#             'back_color': back_color,
#             'size_fixed': str(size_fixed).lower(),
#             'align': align,
#             'stretch': str(stretch).lower()
#             }
#     return urljoin(base_url, 'emoji') + '?' + urlencode(payload)

# def generate(text,font,color,back_color, \
#                     size_fixed = False, \
#                     align = 'center', \
#                     stretch = True):
#     hash_text = text + \
#             ':' + color +\
#             ':' + back_color +\
#             ':' + font +\
#             ':' + ('true' if size_fixed else 'false') +\
#             ':' + align +\
#             ':' + ('true' if stretch else 'false') +\
#             ':' + str(app.config['CACHE_VERSION'])
#     r = int(color[0] +color[1],16)
#     g = int(color[2] +color[3],16)
#     b = int(color[4] +color[5],16)
#     if len(color) == 6:
#         a = 0xff
#     elif len(color) == 8:
#         a = int(color[6] + color[7],16)
#     br = int(back_color[0] + back_color[1],16)
#     bg = int(back_color[2] + back_color[3],16)
#     bb = int(back_color[4] + back_color[5],16)
#     if len(back_color) == 6:
#         ba = 0xff
#     elif len(back_color) == 8:
#         ba = int(back_color[6] + back_color[7],16)
#     cache_id = hashlib.md5(hash_text.encode('utf-8')).hexdigest()
#     img_png = None #cache.get(cache_id)
#     if img_png is None:
#         lines = text.splitlines()

#         if len(text) > 100: # XXX: 100 文字以上
#             return None

#         if len(lines) == 1 and len(lines[0]) > 10: # XXX: 1 列 10 文字以上
#             return None

#         if len(lines) > 10: # XXX: 10 行以上
#             return None

#         img_png = emojilib.generate(
#             text=text,
#             width=128,
#             height=128,
#             color=color,
#             background_color=back_color,
#             size_fixed=size_fixed,
#             disable_stretch=not stretch,
#             align=align,
#             typeface_file='assets/fonts/' + font,
#             format='png'
#         )
#         # cache.set(cache_id,img_png)
#     return img_png
