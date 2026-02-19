from browser.playwright_wrapper import BrowserWrapper
import time

browser = BrowserWrapper()
browser.open("https://www.w3schools.com/html/html_forms.asp")

# Wait for 30 seconds to allow manual inspection, then close.
time.sleep(30)
browser.close()
