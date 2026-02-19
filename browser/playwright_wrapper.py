from playwright.sync_api import sync_playwright

class BrowserWrapper:
    def __init__(self):
        self.playwright = sync_playwright().start()
        # Try to launch the system Chrome browser via Playwright's "chrome" channel.
        # Falls back to bundled Chromium if the channel isn't available.
        try:
            self.browser = self.playwright.chromium.launch(channel="chrome", headless=False)
        except TypeError:
            # Older playwright versions may not accept `channel` parameter; fall back.
            self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def open(self, url):
        print(f"Opening {url}")
        self.page.goto(url)

    # Compatibility aliases expected by existing code
    def open_page(self, url):
        return self.open(url)

    def type_text(self, selector, text):
        return self.fill(selector, text)

    def new_page(self):
        """Return the underlying Playwright Page object for compatibility."""
        return self.page

    def click(self, selector):
        print(f"Clicking {selector}")
        self.page.click(selector)

    def fill(self, selector, text):
        print(f"Filling {selector}")
        self.page.fill(selector, text)

    def get_text(self, selector):
        return self.page.inner_text(selector)

    def close(self):
        self.browser.close()
