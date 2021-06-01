from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
#set up chrome options to open headless chrome and perform algorithm
#without seeing the browser steps
# chrome_options=Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#showing browser (set chrome with no options)
actions = ActionChains(driver)
# log in
email = "dylan_bakr@comcast.net"
password = "D3vi!8oy007"
driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F")
time.sleep(1)
driver.find_element_by_id("login-username").send_keys(email)
driver.find_element_by_id("login-password").send_keys(password)
driver.find_element_by_id("login-button").click()
time.sleep(6)
driver.get("https://open.spotify.com/collection/tracks")
time.sleep(2)
#being copying track listings
track_listing = []
while len(track_listing)<4000:
    elements = driver.find_elements_by_css_selector("div[aria-colindex=\"2\"]")
    for x in elements:
        if x.text in track_listing:
            continue
        else:
            track_listing.append(x.text)
            print(x.text)
#scroll to last element so that new elements will load
    actions.move_to_element(elements[-1])
    actions.perform()
    time.sleep(1)
print("*********END**********")
#xpath
#lets see if this works
