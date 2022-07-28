from preprocess import preprocess
import os

for markdown_post in os.listdir('../mdpages'):
    if markdown_post.endswith('md'):
        file_path = os.path.join('../mdpages', markdown_post)
        buf = None
        f = open(file_path, 'r')
        buf = f.read()
        buf = preprocess(buf)
        f = open('../pages/'+file_path.split(os.sep)[-1], 'w+')
        f.seek(0)
        f.write(buf)
        f.truncate()
        f.close()
