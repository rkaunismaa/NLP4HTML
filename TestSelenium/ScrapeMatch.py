from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pickle

import time
from datetime import date

from MatchFunctions import *

chromeOptions = ChromeOptions()
chromeOptions.headless = True
chromeOptions.binary_location = '/snap/bin/brave'
chromeOptions.add_argument('--remote-debugging-port=9224') 
driver = webdriver.Chrome(options=chromeOptions)

targetSearchPages = [
    ('Top Picks' ,     'https://www.match.com/search?sortBy=1',  True),
    ('Photo Count' ,   'https://www.match.com/search?sortBy=2',  True),
    ('Age' ,           'https://www.match.com/search?sortBy=3',  False),
    ('Activity Date' , 'https://www.match.com/search?sortBy=4',  True),
    ('Newest First' ,  'https://www.match.com/search?sortBy=6',  True),
    ('Mutual Search' , 'https://www.match.com/search?sortBy=9',  True),
    ('Reverse Search' ,'https://www.match.com/search?sortBy=10', True),
    ('Distance' ,      'https://www.match.com/search?sortBy=11', True)
]
 
userList = []
profileIDS = []   
profileCount = 0
exceptionCount = 0

# # Load up one of the specific search pages, then load
# # the profiles into a list
# def scanSearchPage():

#     # select all the "css-1trsig2" css selectors 
#     profiles = driver.find_elements(By.CLASS_NAME, "css-1trsig2")

#     for profile in profiles:

#         try:

#             url = profile.get_attribute("href")
#             urlParts = url.split("?")
#             profilePage =urlParts[0]

#             profilePageParts = profilePage.split("/")
#             profileId = profilePageParts[-1]

#             imageUrl = profile.find_element(By.CLASS_NAME, "css-103b9rp").get_attribute("src")
#             personName = profile.find_element(By.CLASS_NAME, "css-1jab1x0").text
#             personAgeLocation = profile.find_element(By.CLASS_NAME, "css-3g75q9").text
#             personAgeLocationHidden = profile.find_element(By.CLASS_NAME, "css-17ertmd").text
#             images = profile.find_element(By.CLASS_NAME, "css-1r6f8km").text

#             # only load profiles we have not yet loaded
#             if not profileId in profileIDS:
#                 userList.append( (personName, profilePage, profileId, personAgeLocation, personAgeLocationHidden, imageUrl, images) )
#                 profileIDS.append(profileId)

#         except NoSuchElementException:
#             print('NoSuchElementException!')

#         except Exception:
#             print('Exception!')


# Launch the scan of all the target search pages ...
for tsPage in targetSearchPages:

    searchPage = tsPage[1]
    scanThisPage = tsPage[2]

    if scanThisPage == True:

        driver.get(searchPage)

        # Set an implicit wait of 5 seconds
        driver.implicitly_wait(5)

        for _ in range(6):
            # scanSearchPage()
            scanSearchPage(driver, profileIDS, userList)
            driver.execute_script("window.scrollBy(0,2000)","")
            driver.implicitly_wait(5)

# Let's save this list, shall we ...
# Save the userProfiles to a local file
fileName = 'matchLists/matchUserList.txt'
with open(fileName, "wb") as fp:   
    pickle.dump(userList, fp)

# 269 ... 
print(len(userList))

# This will store all the metadata we want on the user.
userProfiles = []

# def scanProfilePage_():

 
#     # Set an explicit wait of 10 seconds for the carousel button to be clickable
#     carouselButtonXPATH = '//*[@id="mainContent"]/article/div[2]/div[1]/div[2]/div/button'
#     try:
#         wait = WebDriverWait(driver, 10)
#         photo_carousel_button = wait.until(EC.element_to_be_clickable((By.XPATH, carouselButtonXPATH)))
#     except StaleElementReferenceException:
#         photo_carousel_button = driver.find_element(By.XPATH, carouselButtonXPATH)

#     userName = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[1]/div[1]/div/h6')
#     personName = userName.text

#     ageLocation = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[2]/span')
#     personAgeLocation = ageLocation.text

#     try:
#         summary = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/section[1]/div/div/div/div[1]/span')    
#         personSummary = summary.text    
#     except NoSuchElementException:
#         personSummary = ""

#   #   photo_carousel_button = driver.find_element(By.XPATH, carouselButtonXPATH)
#     photo_carousel_button.click()

#     # Set an implicit wait of 5 seconds
#     # driver.implicitly_wait(5)

#       # Set an explicit wait of 5 seconds for the carousel button to be clickable
#     carouselCloseButtonXPATH = '//*[@id="modalHeader"]/button/span'
#     try:
#         wait = WebDriverWait(driver, 5)
#         photo_carousel_close_button = wait.until(EC.element_to_be_clickable((By.XPATH, carouselCloseButtonXPATH)))
#     except StaleElementReferenceException:
#         photo_carousel_close_button = driver.find_element(By.XPATH, carouselCloseButtonXPATH)

#     image_count = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/span')
#     no_of_images = image_count.text # '1/5'
#     noiList = no_of_images.split('/')
#     totalImages = int(noiList[1])

#     # user may only have one image, so no right button
#     try:
#         photo_carousel_right_arrow_button = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/button[2]')
#         nextImageButton = True
#     except NoSuchElementException:
#         nextImageButton = False

#     photo_carousel_image = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/figure/div[2]/button/img')

#     imageList = []
#     for _ in range(totalImages):

#         image_src = photo_carousel_image.get_attribute("src")
#         try:
#             photo_carousel_caption = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/div/span')
#             image_caption = photo_carousel_caption.text
#         except NoSuchElementException:
#             image_caption = ""

#         imageList.append( (image_src, image_caption) )
#         if nextImageButton:
#             photo_carousel_right_arrow_button.click() 
#             # Set an implicit wait of 2 seconds
#             # driver.implicitly_wait(2)   

#     # close the photo carousel
#    #  photo_carousel_close_button = driver.find_element(By.XPATH, carouselCloseButtonXPATH)
#     photo_carousel_close_button.click()

#     userProfiles.append( (profilePage, personName, personAgeLocation, personSummary, imageList) )



# def scanProfilePage(userNumber, userCount):

#     personName = ""

#     try: 

#         # Set an explicit wait of 10 seconds for the carousel button to be clickable
#         carouselButtonXPATH = '//*[@id="mainContent"]/article/div[2]/div[1]/div[2]/div/button'
#         try:
#             wait = WebDriverWait(driver, 10)
#             photo_carousel_button = wait.until(EC.element_to_be_clickable((By.XPATH, carouselButtonXPATH)))
#         except StaleElementReferenceException:
#             photo_carousel_button = driver.find_element(By.XPATH, carouselButtonXPATH)

#         userName = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[1]/div[1]/div/h6')
#         personName = userName.text

#         ageLocation = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[2]/span')
#         personAgeLocation = ageLocation.text

#         personSubscriber = ""
#         try:
#             subscriber = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[2]/div/span/span/span/div/div/b')
#             personSubscriber = subscriber.text
#         except NoSuchElementException:
#             personSubscriber = ""

#         personLastActive = ""
#         try:
#             lastActive = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[4]/span')
#             personLastActive = lastActive.text
#         except NoSuchElementException:
#             personLastActive = ""

#         personBannerHeading = ""
#         try:
#             bannerHeading = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[6]/blockquote/h2')
#             personBannerHeading = bannerHeading.text
#         except NoSuchElementException:
#             personBannerHeading = ""

#         personBannerText = ""
#         try:
#             bannerText = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[6]/blockquote/div/div/span')
#             personBannerText = bannerText.text
#         except NoSuchElementException:
#             personBannerText = ""

#         try:
#             summary = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/section[1]/div/div/div/div[1]/span')    
#             personSummary = summary.text    
#         except NoSuchElementException:
#             personSummary = ""

#         photo_carousel_button.click()

#         # Set an explicit wait of 5 seconds for the carousel button to be clickable
#         carouselCloseButtonXPATH = '//*[@id="modalHeader"]/button/span'
#         try:
#             wait = WebDriverWait(driver, 5)
#             photo_carousel_close_button = wait.until(EC.element_to_be_clickable((By.XPATH, carouselCloseButtonXPATH)))
#         except StaleElementReferenceException:
#             photo_carousel_close_button = driver.find_element(By.XPATH, carouselCloseButtonXPATH)

#         image_count = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/span')
#         no_of_images = image_count.text # '1/5'
#         noiList = no_of_images.split('/')
#         totalImages = int(noiList[1])

#         # user may only have one image, so no right button
#         try:
#             photo_carousel_right_arrow_button = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/button[2]')
#             nextImageButton = True
#         except NoSuchElementException:                          
#             nextImageButton = False

#         photo_carousel_image = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/figure/div[2]/button/img')

#         imageList = []
#         for _ in range(totalImages):

#             image_src = photo_carousel_image.get_attribute("src")
#             try:
#                 photo_carousel_caption = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/div/span')
#                 image_caption = photo_carousel_caption.text
#             except NoSuchElementException:
#                 image_caption = ""

#             imageList.append( (image_src, image_caption) )
#             if nextImageButton:
#                 photo_carousel_right_arrow_button.click() 

#         photo_carousel_close_button.click()

#         userProfiles.append( (profilePage, personName, personAgeLocation, personSubscriber, personLastActive, personBannerHeading, personBannerText, personSummary, imageList) )

#         print(f'{userNumber}/{userCount} Page scan for {personName} Success!')

#     except Exception:
#         # something failed ... move on ..
#         print(f'{userNumber}/{userCount} Page scan for {personName} failure! ... move on!')


userNumber = 0
userCount = len(userList)

startTime = time.time()
todaysDate = date.today()

for testUser in userList:

    userNumber += 1
    profilePage = testUser[1]

    driver.get(profilePage)

    # scanProfilePage(userNumber, userCount)
    scanProfilePage(userNumber, userCount, driver, userProfiles, profilePage)


endTime = time.time()
elapsedTime = time.strftime("%H:%M:%S", time.gmtime(endTime - startTime))

print(todaysDate.strftime('# Run Date: %A, %B %d, %Y'))
print(f"# Run Time: {elapsedTime}")

# Save the userProfiles to a local file
fileName = 'matchLists/matchProfiles.txt'
with open(fileName, "wb") as fp:   #Pickling
    pickle.dump(userProfiles, fp)

print("Match Success!")


driver.quit()


