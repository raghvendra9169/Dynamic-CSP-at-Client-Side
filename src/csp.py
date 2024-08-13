import hashlib
import base64
import os
from bs4 import BeautifulSoup

def generate_nonce():
    return base64.b64encode(os.urandom(16)).decode('utf-8')

def generate_script_hash(script_content):
    hash_object = hashlib.sha256(script_content.encode('utf-8'))
    return f"'sha256-{base64.b64encode(hash_object.digest()).decode('utf-8')}'"

def analyze_clean_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    safe_inline_scripts = []
    inline_styles = []

    for script in soup.find_all('script'):
        if script.string:
            safe_inline_scripts.append(script.string)
        elif 'src' in script.attrs:
            src = script.attrs['src']
            safe_inline_scripts.append(src)
    
    for style in soup.find_all('style'):
        if style.string:
            inline_styles.append(style.string)
    
    return safe_inline_scripts, inline_styles

def get_csp_for_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return ""

    soup = BeautifulSoup(response.content, 'html.parser')

    scripts = {urlparse(script['src']).netloc for script in soup.find_all('script', src=True)}
    styles = {urlparse(link['href']).netloc for link in soup.find_all('link', rel="stylesheet", href=True)}
    images = {urlparse(img['src']).netloc for img in soup.find_all('img', src=True)}
    frames = {urlparse(frame['src']).netloc for frame in soup.find_all('iframe', src=True)}
    objects = {urlparse(embed['src']).netloc for embed in soup.find_all('embed', src=True)}
    fonts = {urlparse(font['src']).netloc for font in soup.find_all('font', src=True)}
    connects = {urlparse(a['href']).netloc for a in soup.find_all('a', href=True) if urlparse(a['href']).scheme in ['http', 'https']}
    medias = {urlparse(source['src']).netloc for source in soup.find_all('source', src=True)}
    workers = {urlparse(worker['src']).netloc for worker in soup.find_all('worker', src=True)}

    csp_directives = {
        'default-src': ["'self'"],
        'script-src': list(scripts) + ["'self'", "'unsafe-inline'", "'unsafe-eval'"],
        'style-src': list(styles) + ["'self'", "'unsafe-inline'"],
        'img-src': list(images) + ["'self'", 'data:'],
        'frame-src': list(frames) + ["'self'"],
        'object-src': ["'none'"],
        'font-src': list(fonts) + ["'self'"],
        'connect-src': list(connects) + ["'self'"],
        'media-src': list(medias) + ["'self'"],
        'worker-src': list(workers) + ["'self'"],
        'child-src': list(frames) + ["'self'"],
        'frame-ancestors': ["'self'"],
        'form-action': ["'self'"]
    }

    csp = []
    for directive, sources in csp_directives.items():
        if sources:
            csp.append(f"{directive} {' '.join(sources)}")

    return "; ".join(csp)

class CustomRequestInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self):
        super().__init__()
        self.csp = ""

    def set_csp(self, csp):
        self.csp = csp

    def interceptRequest(self, info: QWebEngineUrlRequestInfo):
        if self.csp:
            info.setHttpHeader(b'Content-Security-Policy', self.csp.encode('utf-8'))

class CustomWebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interceptor = CustomRequestInterceptor()
        self.profile().setRequestInterceptor(self.interceptor)
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self):
        url = self.url().toString()
        csp = get_csp_for_page(url)
        print(f"CSP for {url}: {csp}")
        self.interceptor.set_csp(csp)
        self.runJavaScript(
            """
            console.log("CSP header should now be in effect.");
            """,
            self.handle_csp_injection
        )

    def handle_csp_injection(self, result):
        print("CSP header injected.")
