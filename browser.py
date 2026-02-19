from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def open_page(self, url):
        self.page.goto(url)

    def type_text(self, selector, text):
        self.page.fill(selector, text)

    def click(self, selector):
        self.page.click(selector)
