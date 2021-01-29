from urllib.request import urlparse, urljoin
from urllib.parse import parse_qs, quote, urlunparse, urlencode, urlparse, urljoin


host = 'http://www.github.com?q=urlparse&area=default'
base = 'http://www.debian.org/about'
params = urlparse(host)
query = parse_qs(params.query)
print(query)  # --> {'q': ['urlparse'], 'area': ['default']}
print(params)  # --> ParseResult(scheme='http', netloc='www.github.com', path='', params='', query='', fragment='')

new = urljoin(base, 'info')
print(new)  # --> http://www.debian.org/info
new = urljoin('http://www.debian.org/about/', 'info')
print(new)  # --> http://www.debian.org/about/info
new = urljoin('http://www.debian.org/about/new/', '../info')
print(new)  # --> http://www.debian.org/about/info

# encoding and escaping ascii chars
path = '/images/users/+Zoot+/'
path = quote(path)
print(path)  # --> /images/users/%2BZoot%2B/
# create a dictionary of query parameters
query_dict = {':action': 'search', 'term': 'Are you quite sure this is a cheese shop?'}
query = urlencode(query_dict)
print(query)  # --> %3Aaction=search&term=Are+you+quite+sure+this+is+a+cheese+shop%3F
netloc = 'www.google.com'
new = urlunparse(('https', netloc, path, '', query, ''))
print(new)  # --> https://www.google.com/images/users/%2BZoot%2B/?%3Aaction=search&term=Are+you+quite+sure+this+is+a+cheese+shop%3F
