import re
import os
import markdown
import pypandoc

s = r'''\begin{theorem}[Weierstrass Approximation] \label{wapprox}

but not match

\begin{theorem}[Weierstrass Approximation]
\label{wapprox}'''

regex=r'(\\(?:begin|end)(?=((?:{[^}]*}|\[[^]]*])*))\2)[^\S\n]*(?=\S)'
tbl_regex='|(?:([^\r\n|]*)\\|)+\r?\n\\|(?:(:?-+:?)\\|)+\r?\n(\\|(?:([^\r\n|]*)\\|)+\r?\n)+'
math_regex='\\${1,2}.*?(?<!\\\\)\\${1,2}'
tbl_p = re.compile(tbl_regex)
math_p = re.compile(math_regex)
#s_p=re.compile(s)
regex_p=re.compile(regex)


def convert_markdowntable2html(md_table):
    conv=markdown.markdown(md_table[0], extensions=['markdown.extensions.tables'])
    if len(conv)>0:
        #print('table html: {}'.format(conv))
        pass
    return conv


def convert2mathml(txt):
    print("type: {}, txt: {}".format(type(txt), txt))
    filters = [
        #'--citeproc'
    ]

    pdoc_args = [
        #'--mathjax'
        #,'-smart'
        '--mathml'
    ]
    output = pypandoc.convert_text(txt[0],
                                   to='html5',
                                   format='md',
                                   extra_args=pdoc_args,
                                   filters=filters)
    out= output.split('<p>')[1].split('</p')[0]
    print("math: {}".format(out))
    return out


def preprocess(buf):
    if len(buf) > len(re.sub(tbl_regex, '', buf)):
        buf = tbl_p.sub(convert_markdowntable2html, buf)
    buf = math_p.sub(convert2mathml, buf)
    return buf
