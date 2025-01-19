AUTHOR = 'su'
SITENAME = 'chess.jp'
SITEURL = ''

PATH = "content"
STATIC_PATHS = ['images', 'extra']

TIMEZONE = 'Japan'

DEFAULT_LANG = 'en'

THEME = '/pelican-themes/new-bootstrap2'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("チェスのこと", "https://chessjpjp.blogspot.com/")
)
# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
