from selenium import webdriver
driver = webdriver.Chrome()
email = "dylan_bakr@comcast.net"
password = "D3vi!8oy007"
driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F")
driver.find_element_by_id("login-username").send_keys(email)
driver.find_element_by_id("login-password").send_keys(password)
driver.find_element_by_id("login-button").click()
driver.get("open.spotify.com/collection/tracks")
 
