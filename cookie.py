from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor


host = 'http://www.github.com'
cookies_jar = CookieJar()
opener = build_opener(HTTPCookieProcessor(cookies_jar))
opener.open(host)

cookies = list(cookies_jar)
