from browser.playwright_wrapper import BrowserWrapper

def run_scripted():
    browser = BrowserWrapper()
    browser.open("https://www.w3schools.com/html/html_forms.asp")

    browser.fill("input[name='firstname']", "Nida")
    browser.fill("input[name='lastname']", "Fathima")
    browser.click("input[type='submit']")

    input("Press Enter to close...")
    browser.close()
