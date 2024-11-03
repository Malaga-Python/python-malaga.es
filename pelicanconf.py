AUTHOR = 'Python Málaga'
SITENAME = 'Python Málaga'
SITEURL = ""

WELCOME_MESSAGE = "Comunidad Python Málaga"

PATH = "content"

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("Asociación", "/asociacion/"),
    ("Empresas", "/empresas/"),
    ("Código conducta", "/codigo-conducta/"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "theme"

MENU_LINKS = LINKS

DESCRIPTION = "Comunidad de lenguaje de programación Python en Málaga, España. Eventos, charlas, talleres y mucho más."
KEYWORDS = ("Python, Málaga, Malaga, España, Spain, Programación, Desarrollo Software, Comunidad, Charlas, Talleres, "
            "Eventos")

# SEO configuration
# SEO_REPORT = True  # SEO report is enabled by default
# SEO_ENHANCER = True  # SEO enhancer is disabled by default
# SEO_ENHANCER_OPEN_GRAPH = True  # Subfeature of SEO enhancer
# SEO_ENHANCER_TWITTER_CARDS = True  # Subfeature of SEO enhancer
