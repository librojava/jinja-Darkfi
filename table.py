import re
import markdown
import os

def convert_markdowntable2html(md_table):
    conv=markdown.markdown(md_table[0], extensions=['markdown.extensions.tables'])
    if len(conv)>0:
        #print('table html: {}'.format(conv))
        pass
    return conv

posts = {}
tbl_regex='|(?:([^\r\n|]*)\\|)+\r?\n\\|(?:(:?-+:?)\\|)+\r?\n(\\|(?:([^\r\n|]*)\\|)+\r?\n)+'
p = re.compile(tbl_regex)
counter =0
for markdown_post in os.listdir('pages'):
    if markdown_post.endswith('md'):
        file_path = os.path.join('pages', markdown_post)
        buf = None
        with open(file_path, 'r') as file:
            buf = file.read()
            if len(buf) > len(re.sub(tbl_regex, '', buf)):
                #print('buf: {}'.format(buf))
                buf = p.sub(convert_markdowntable2html, buf)
                #posts[markdown_post] = buf
        #path='_.'.join(file_path.split('.'))
        f = open(file_path, 'w')
        f.seek(0)
        f.write(buf)
        f.truncate()
        f.close()
