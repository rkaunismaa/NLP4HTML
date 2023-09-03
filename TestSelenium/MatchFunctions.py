from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pickle

import time
from datetime import date

# Match Search pages
targetSearchPages = [
    ('Top Picks' ,     'https://www.match.com/search?sortBy=1',  True),
    ('Photo Count' ,   'https://www.match.com/search?sortBy=2',  True),
    ('Age' ,           'https://www.match.com/search?sortBy=3',  True),
    ('Activity Date' , 'https://www.match.com/search?sortBy=4',  True),
    ('Newest First' ,  'https://www.match.com/search?sortBy=6',  True),
    ('Mutual Search' , 'https://www.match.com/search?sortBy=9',  True),
    ('Reverse Search' ,'https://www.match.com/search?sortBy=10', True),
    ('Distance' ,      'https://www.match.com/search?sortBy=11', True)
]

def createNewDriver():

    try :

        chromedriver_path = '/usr/local/bin/chromedriver'
        chromeService = ChromeService(executable_path=chromedriver_path)

        chromeOptions = ChromeOptions()
        chromeOptions.headless = True
        chromeOptions.binary_location = '/usr/bin/brave-browser'
        chromeOptions.add_argument('--remote-debugging-port=9224') 

        driver = webdriver.Chrome(options = chromeOptions,  service=chromeService)

    except Exception :

        # something failed, return nothing
        driver = None 

    return driver

def scanProfiles4MatchId(profileMaster, matchId):

    bFound = False
    for profile in profileMaster:
        profilePage = profile[0]
        ppSplit = profilePage.split('/')
        ppId = ppSplit[-1]

        if (ppId == matchId):
            bFound = True
            break
    
    return bFound


# Scan a match search page
def scanSearchPage(driver, profileIDS, userList):

    # select all the "css-1trsig2" css selectors 
    profiles = driver.find_elements(By.CLASS_NAME, "css-1trsig2")

    for profile in profiles:

        personName = ''
        try:

            url = profile.get_attribute("href")
            urlParts = url.split("?")
            profilePage =urlParts[0]

            profilePageParts = profilePage.split("/")
            profileId = profilePageParts[-1]

            try:
                imageUrl = profile.find_element(By.CLASS_NAME, "css-103b9rp").get_attribute("src")
            except NoSuchElementException:
                print('imageUrl NoSuchElementException!')
                imageUrl = ''

            try:
                personName = profile.find_element(By.CLASS_NAME, "css-1jab1x0").text
            except NoSuchElementException:
                print('personName NoSuchElementException!')
                personName = ''

            try:
                personAgeLocation = profile.find_element(By.CLASS_NAME, "css-3g75q9").text
            except NoSuchElementException:
                print('personAgeLocation NoSuchElementException!')
                personAgeLocation = ''

            try:
                personAgeLocationHidden = profile.find_element(By.CLASS_NAME, "css-17ertmd").text
            except NoSuchElementException:
                print('personAgeLocationHidden NoSuchElementException!')
                personAgeLocationHidden = ''

            try:
                images = profile.find_element(By.CLASS_NAME, "css-1r6f8km").text
            except NoSuchElementException:
                print('images NoSuchElementException!')
                images = ''

            # only load profiles we have not yet loaded
            if not profileId in profileIDS:
                userList.append( (personName, profilePage, profileId, personAgeLocation, personAgeLocationHidden, imageUrl, images) )
                profileIDS.append(profileId)
                print(f'New User {personName} => {profileId} added to userList!')
            else:
                print(f'We have already scanned {personName} => {profileId}!')
            

        except NoSuchElementException:
            print(f'{personName} => NoSuchElementException!')

        except Exception:
            print('Exception!')


# Scan the profile page of a user
def scanProfilePage(userNumber, userCount, driver, userProfiles, profilePage):

    personName = ""

    try: 

        # Set an explicit wait of 10 seconds for the carousel button to be clickable
        carouselButtonXPATH = '//*[@id="mainContent"]/article/div[2]/div[1]/div[2]/div/button'
        try:
            wait = WebDriverWait(driver, 10)
            photo_carousel_button = wait.until(EC.element_to_be_clickable((By.XPATH, carouselButtonXPATH)))
        except StaleElementReferenceException:
            photo_carousel_button = driver.find_element(By.XPATH, carouselButtonXPATH)

        try:
            personName = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[1]/div[1]/div/h6').text
        except NoSuchElementException:
            print('personName NoSuchElementException!')
            personName = ""
        try:
            personAgeLocation = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[2]/span').text
        except NoSuchElementException:
            print('personAgeLocation NoSuchElementException!')
            personAgeLocation = ""
        
        try:
            personSubscriber = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[2]/div/span/span/span/div/div/b').text
        except NoSuchElementException:
            print('personSubscriber NoSuchElementException!')
            personSubscriber = ""

        try:
            personLastActive = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[4]/span').text
        except NoSuchElementException:
            print('personLastActive NoSuchElementException!')
            personLastActive = ""

        try:
            personBannerHeading = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[6]/blockquote/h2').text
        except NoSuchElementException:
            print('personBannerHeading NoSuchElementException!')
            personBannerHeading = ""

        try:
            personBannerText = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[6]/blockquote/div/div/span').text
        except NoSuchElementException:
            print('personBannerText NoSuchElementException!')
            personBannerText = ""

        try:
            personSummary = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/section[1]/div/div/div/div[1]/span').text    
        except NoSuchElementException:
            print('personSummary NoSuchElementException!')
            personSummary = ""

        photo_carousel_button.click()

        # Set an explicit wait of 5 seconds for the carousel button to be clickable
        carouselCloseButtonXPATH = '//*[@id="modalHeader"]/button/span'
        try:
            wait = WebDriverWait(driver, 5)
            photo_carousel_close_button = wait.until(EC.element_to_be_clickable((By.XPATH, carouselCloseButtonXPATH)))
        except StaleElementReferenceException:
            photo_carousel_close_button = driver.find_element(By.XPATH, carouselCloseButtonXPATH)

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

        photo_carousel_close_button.click()

        userProfiles.append( (profilePage, personName, personAgeLocation, personSubscriber, personLastActive, personBannerHeading, personBannerText, personSummary, imageList) )

        print(f'{userNumber}/{userCount} Page scan for {personName} Success!')

    except Exception:
        # something failed ... move on ..
        print(f'{userNumber}/{userCount} Page scan for {personName} failure! ... move on!')