from selenium import webdriver
import time
driver = webdriver.Chrome()
email = "dylan_bakr@comcast.net"
password = "D3vi!8oy007"
driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F")
time.sleep(3)
driver.find_element_by_id("login-username").send_keys(email)
driver.find_element_by_id("login-password").send_keys(password)
driver.find_element_by_id("login-button").click()
time.sleep(3)
driver.get("https://open.spotify.com/collection/tracks")
#find number of songs
numSongs = int(input("how many songs would you like to copy?\n\n"))
#loop to add songs to array tracks
tracks = []

for x in range(numSongs):
    path = '//*[@id="main"]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[4]/div/div[2]/div[2]/div[{}]/div/div/div[2]/div/div/span/span'.format(x+1)
    tracks.append(driver.find_element_by_xpath(path).text)
for x in tracks:
    print(x)

#xpath
#first song '//*[@id="main"]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[4]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/span/span'
#second song '//*[@id="main"]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[4]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/span/span'
#full xpath
#first song '/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[4]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/span/span'
