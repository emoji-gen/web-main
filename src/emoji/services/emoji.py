
def generate_emoji(text,font,color,back_color, \
                    size_fixed = False, \
                    align = 'center', \
                    stretch = True):
    global cache
    hash_text = text + \
            ':' + color +\
            ':' + back_color +\
            ':' + font +\
            ':' + ('true' if size_fixed else 'false') +\
            ':' + align +\
            ':' + ('true' if stretch else 'false') +\
            ':' + str(config.cache_version)
    r = int(color[0] +color[1],16)
    g = int(color[2] +color[3],16)
    b = int(color[4] +color[5],16)
    if len(color) == 6:
        a = 0xff
    elif len(color) == 8:
        a = int(color[6] + color[7],16)
    br = int(back_color[0] + back_color[1],16)
    bg = int(back_color[2] + back_color[3],16)
    bb = int(back_color[4] + back_color[5],16)
    if len(back_color) == 6:
        ba = 0xff
    elif len(back_color) == 8:
        ba = int(back_color[6] + back_color[7],16)
    cache_id = hashlib.md5(hash_text.encode('utf-8')).hexdigest()
    img_png = cache.get(cache_id)
    if img_png is None:
        lines = text.splitlines()

        if len(text) > 100: # XXX: 100 文字以上
            return None

        if len(lines) == 1 and len(lines[0]) > 10: # XXX: 1 列 10 文字以上
            return None

        if len(lines) > 10: # XXX: 10 行以上
            return None

        emoji = String2emoji(lines, 'assets/fonts/' + font,(r,g,b,a),(br,bg,bb,ba))
        if not size_fixed:
            emojiMode = emoji.MODE_NOMAL
        elif size_fixed:
            emojiMode = emoji.MODE_FONTSIZE_FIXED
        else :
            emojiMode = emoji.MODE_NOMAL
        img = emoji.getEmoji(emojiMode,align,stretch)
        output = io.BytesIO()
        img.save(output,format='png')
        img_png = output.getvalue()
        cache.set(cache_id,img_png)
    return img_png
