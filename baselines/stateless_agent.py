from browser.playwright_wrapper import BrowserWrapper

def run_stateless():
    browser = BrowserWrapper()
    steps = ["open", "fill", "submit"]

    for step in steps:
        if step == "open":
            browser.open("https://www.w3schools.com/html/html_forms.asp")
        elif step == "fill":
            browser.fill("input[name='firstname']", "Test")
        elif step == "submit":
            browser.click("input[type='submit']")

    input("Press Enter to close...")
    browser.close()
