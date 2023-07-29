from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pickle

import time

# # Pick a few users ...
# Boyanna = "https://www.match.com/profile/jjLX_J8ZrFwriTXuFyuoyQ2"
# Pat = "https://www.match.com/profile/W5eSN9DQ38U8umJ82C---g2"
# St = "https://www.match.com/profile/4T33D_27J2hcEoPsgTU0aA2"
# Im = "https://www.match.com/profile/xrb0-ZB6LHYG_IhUqPODug2"
# Rita = "https://www.match.com/profile/nhwdQ6YppvWJHY1B_qVCNA2"
# Charlie = "https://www.match.com/profile/TWaXmmkeDcmidIS2aISfPg2"
# Monica = "https://www.match.com/profile/VlqUyWrdoGo6FYYZsfOfjA2"
# Karen = "https://www.match.com/profile/ycWfFU8usvIYvY6jcn0FvA2"
# Rose = "https://www.match.com/profile/3M5shM941vGRKAlF0lD2cg2" # This totally looks like a fishing account
# Sondra = "https://www.match.com/profile/mwS4rT4q-DDi0Zl8XR40FA2"
# Raluca = "https://www.match.com/profile/FVsmTW6T2i5YeLzMZQAjsQ2"


userList = [
    ("Boyanna", "https://www.match.com/profile/jjLX_J8ZrFwriTXuFyuoyQ2"),
    ("Pat", "https://www.match.com/profile/W5eSN9DQ38U8umJ82C---g2"),
    ("St", "https://www.match.com/profile/4T33D_27J2hcEoPsgTU0aA2"),
    ("Im", "https://www.match.com/profile/xrb0-ZB6LHYG_IhUqPODug2"),
    ("Rita", "https://www.match.com/profile/nhwdQ6YppvWJHY1B_qVCNA2"),
    ("Charlie", "https://www.match.com/profile/TWaXmmkeDcmidIS2aISfPg2"),
    ("Monica", "https://www.match.com/profile/VlqUyWrdoGo6FYYZsfOfjA2"),
    ("Karen", "https://www.match.com/profile/ycWfFU8usvIYvY6jcn0FvA2"),
    ("Rose", "https://www.match.com/profile/3M5shM941vGRKAlF0lD2cg2"),
    ("Linda","https://www.match.com/profile/ebunOUTetc9TrOfjDu6D-A2"),
    ("Sondra" ,"https://www.match.com/profile/mwS4rT4q-DDi0Zl8XR40FA2"),
    ("Raluca", "https://www.match.com/profile/FVsmTW6T2i5YeLzMZQAjsQ2"),
    ("Christin", "https://www.match.com/profile/1OZ-5Yxvdn78OMi7R15eJQ2"),
    ("Angela", "https://www.match.com/profile/U6yqKwhgr_QGXl9dAgooJA2"),
    ("Catherine", "https://www.match.com/profile/6N1l1hfUUSuyMWdIqOm4pQ2"),
    ("Shannan", "https://www.match.com/profile/xHc4aGtJAreA1FHiNInBPA2")
]

chromeOptions = ChromeOptions()
chromeOptions.headless = True
chromeOptions.binary_location = '/snap/bin/brave'
chromeOptions.add_argument('--remote-debugging-port=9224') #NOT 9222
driver = webdriver.Chrome(options=chromeOptions)

# This will store all the metadata we want on the user.
userProfiles = []

for testUser in userList:

    profilePage = testUser[1]
    driver.get(profilePage)

    # Set an implicit wait of 10 seconds
    time.sleep(5)
    
    # Set an explicit wait of 5 seconds for the carousel button to be clickable
    carouselButtonXPATH = '//*[@id="mainContent"]/article/div[2]/div[1]/div[2]/div/button'
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, carouselButtonXPATH)))

    userName = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[1]/div[1]/div/h6')
    personName = userName.text

    ageLocation = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[2]/span')
    personAgeLocation = ageLocation.text

    try:
        summary = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/section[1]/div/div/div/div[1]/span')    
        personSummary = summary.text    
    except NoSuchElementException:
        personSummary = ""

    photo_carousel_button = driver.find_element(By.XPATH, carouselButtonXPATH)
    photo_carousel_button.click()

    # Set an implicit wait of 5 seconds
    driver.implicitly_wait(5)

      # Set an explicit wait of 5 seconds for the carousel button to be clickable
    carouselCloseButtonXPATH = '//*[@id="modalHeader"]/button/span'
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, carouselCloseButtonXPATH)))

    image_count = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/span')
    no_of_images = image_count.text # '1/5'
    noiList = no_of_images.split('/')
    totalImages = int(noiList[1])

    # user may only have one image, so no right button
    try:
        photo_carousel_right_arrow_button = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/button[2]')
        nextImageButton = True
    except NoSuchElementException:
        nextImageButton = False

    photo_carousel_image = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/figure/div[2]/button/img')

    imageList = []
    for _ in range(totalImages):

        image_src = photo_carousel_image.get_attribute("src")
        try:
            photo_carousel_caption = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/div/span')
            image_caption = photo_carousel_caption.text
        except NoSuchElementException:
            image_caption = ""

        imageList.append( (image_src, image_caption) )
        if nextImageButton:
            photo_carousel_right_arrow_button.click() 
            # Set an implicit wait of 5 seconds
            driver.implicitly_wait(5)   

    # close the photo carousel
    photo_carousel_close_button = driver.find_element(By.XPATH, carouselCloseButtonXPATH)
    photo_carousel_close_button.click()

    userProfiles.append( (profilePage, personName, personAgeLocation, personSummary, imageList) )

# Save the userProfiles to a local file
fileName = 'matchProfiles.txt'
with open(fileName, "wb") as fp:   #Pickling
    pickle.dump(userProfiles, fp)

print("Match Success!")


driver.quit()


