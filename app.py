# coding=utf-8
import gzip
import re
import urllib2
from StringIO import StringIO

from bs4 import BeautifulSoup


def do_rep(html):
    soup = BeautifulSoup(html, features='html')
    for script in soup(["script", "style", "img"]):
        script.extract()  # rip it out
    text = soup.body.get_text()
    # text = decode_heuristically(text)
    words = set()
    rgx = re.compile('[,\.\?!()\*\[\]\{\}\'";:/\+-_@#\$%\^&\s<>][\w]{6}[,\.\?!()\*\[\]\{\}\'";:/\+-_@#\$%\^&\s<>]', re.UNICODE)
    for word in rgx.findall(text):
        word = re.sub('[,\.\?!\(\)\*\[\]\{\}\'\";:/\+\-_@#\$%\^&\s<>]', '', word)
        if len(word) == 6 and re.match(r"[\w]+", word, re.UNICODE):
            words.add(word)
    for word in words:
        for found in soup.findAll(text=re.compile('[,\.\?!()\*\[\]\{\}\'";:/\+-_@#\$%\^&\s<>]'+word+'[,\.\?!()\*\[\]\{\}\'";:/\+-_@#\$%\^&\s<>]')):
            st = found.string
            st = st.replace(word, word + u"\u2122")
            found.replace_with(st)
    return str(soup)


def application(environ, start_response):
    habra_path = 'http://habrahabr.ru'  # /company/yandex/blog/258673/
    path = environ.get('PATH_INFO')
    # print 'path:', path
    if path == '/' or path == '':
        path = '/company/yandex/blog/258673/'
    req = urllib2.Request(habra_path + path)
    req.add_header('Accept-encoding', 'gzip')
    if environ.get('HTTP_REFERER', None):
        req.add_header('Referrer', environ.get('HTTP_REFERER').replace('localhost:8080', 'habrahabr.ru'))
    response = urllib2.urlopen(req)
    status = '%s %s' % (response.code, response.msg)
    response_headers = [('Content-type', response.headers.dict.get('content-type'))]
    start_response(status, response_headers)
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        html = f.read()
    else:
        html = response.read()
    if 'text/html' in response.headers.dict.get('content-type'):
        html = do_rep(html)
    return [html]


if __name__ == '__main__':
    from wsgiref.handlers import BaseHandler
    from wsgiref.simple_server import make_server

    try:
        BaseHandler.http_version = '1.1'
        import webbrowser

        webbrowser.open('http://localhost:8080/company/yandex/blog/258673/')
        make_server('', 8080, application).serve_forever()
    except KeyboardInterrupt:
        pass