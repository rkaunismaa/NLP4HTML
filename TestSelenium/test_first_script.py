from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.by import By

import urllib


# Friday, July 28, 2023
# This runs without problems under the conda environment finance on KAUWITB ...
# conda nlp4html or docker container hfpt_July21 ... it does not work. 

def test_eight_components():


    useChrome = True
    useFireFox = not useChrome

    # IF this fails, then try killing any running instances of brave, then try again ... 
    # launch brave from the terminal window using the following command ...
    # brave --remote-debugging-port=9224
    # This needs to be done BEFORE you fire this script! ... 
    if useChrome:
        chromeOptions = ChromeOptions()
        chromeOptions.headless = True
        chromeOptions.binary_location = '/snap/bin/brave'
        chromeOptions.add_argument('--remote-debugging-port=9224') #NOT 9222
        driver = webdriver.Chrome(options=chromeOptions)

    if useFireFox:
        firefoxOptions = FireFoxOptions()
        firefoxOptions.headless = True
        # interesting ... this next line will break this script ... so yeah, don't use it
       # firefoxOptions.binary_location = '/snap/bin/firefox'
        driver = webdriver.Firefox(options=firefoxOptions)


    testSeleniumWebForm = False
    if testSeleniumWebForm :

        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        title = driver.title
        assert title == "Web form"

        driver.implicitly_wait(0.5)

        text_box = driver.find_element(by=By.NAME, value="my-text")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

        text_box.send_keys("Selenium")
        submit_button.click()

        message = driver.find_element(by=By.ID, value="message")
        value = message.text
        assert value == "Received!"
        
        print("Selenium Web Form Success!!")


    testPath = 'MyProfile'
    testPath = "HomePage"
    testPath = "UserProfile"

    # So let's try match, shall we ... 
    if useChrome:

        if testPath == 'MyProfile':

            driver.get("https://www.match.com/profile/me/edit")
            driver.implicitly_wait(0.5)

            userName = driver.find_element(By.XPATH, '//*[@id="profile-edit-layout"]/div[2]/div[2]/div/section/div/div[1]/div/div[1]/div[1]/h2')
            personName = userName.text

            viewMore_button = driver.find_element(By.XPATH, '//*[@id="profile-edit-layout"]/section[1]/div/div[2]/div[2]/button')
            viewMore_button.click()

            summary = driver.find_element(By.XPATH, '//*[@id="profile-edit-layout"]/section[1]/div/div[2]/div[1]/span')
            personSummary = summary.text

            VIEW_button = driver.find_element(By.XPATH, '//*[@id="profile-edit-layout"]/div[1]/div[1]/div/ul/li[1]/a/span')
            VIEW_button.click()

            photo_carousel_button = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[1]/div[2]/div/button')
            photo_carousel_button.click()

            photo_carousel_right_arrow_button = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/button[2]/span/span')

            image_count = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/span')
            no_of_images = image_count.text # '1/5'
            noiList = no_of_images.split('/')
            totalImages = int(noiList[1])

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
                photo_carousel_right_arrow_button.click()    

            # close the photo carousel
            photo_carousel_close_button = driver.find_element(By.XPATH, '//*[@id="modalHeader"]/button/span')
            photo_carousel_close_button.click()


        elif testPath == 'HomePage':

            driver.get("https://www.match.com/home")
            driver.implicitly_wait(0.5)

            userName = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/div/h1')
            personName = userName.text

            viewMore_button = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/div[2]/button')
            viewMore_button.click()

            summary = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/div[1]/span')
            personSummary = summary.text

            photo_carousel_button = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/button')
            photo_carousel_button.click()

            photo_carousel_right_arrow_button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/section/div/button[2]')

            image_count = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/span')
            no_of_images = image_count.text # '1/5'
            noiList = no_of_images.split('/')
            totalImages = int(noiList[1])

            photo_carousel_image = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/section/div/figure/div[2]/button/img')

            imageList = []
            for _ in range(totalImages):
            
                image_src = photo_carousel_image.get_attribute("src")
                try:
                    photo_carousel_caption = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/div/span')
                    image_caption = photo_carousel_caption.text
                except NoSuchElementException:
                    image_caption = ""

                imageList.append( (image_src, image_caption) )
                photo_carousel_right_arrow_button.click()    

            # close the photo carousel
            photo_carousel_close_button = driver.find_element(By.XPATH, '//*[@id="modalHeader"]/button/span')
            photo_carousel_close_button.click()


        elif testPath == 'UserProfile':

            # Pick a few users ...
            Boyanna = "https://www.match.com/highlights/profile/jjLX_J8ZrFwriTXuFyuoyQ2"
            Pat = "https://www.match.com/profile/W5eSN9DQ38U8umJ82C---g2"
            St = "https://www.match.com/profile/4T33D_27J2hcEoPsgTU0aA2"
            Im = "https://www.match.com/profile/xrb0-ZB6LHYG_IhUqPODug2"

            personUrl = Im

            driver.get(personUrl)
            driver.implicitly_wait(0.5)

            userName = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[2]/div[1]/div[1]/div/h6')
            personName = userName.text

            try:
                viewMore_button = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/section[1]/div/div/div/div[2]/button')
                viewMore_button.click()
            except NoSuchElementException:
                personName = userName.text


            summary = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/section[1]/div/div/div/div[1]/span')
            personSummary = summary.text

            photo_carousel_button = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[1]/div[2]/div/button')
            photo_carousel_button.click()

            photo_carousel_right_arrow_button = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/button[2]')

            image_count = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/span')
            no_of_images = image_count.text # '1/5'
            noiList = no_of_images.split('/')
            totalImages = int(noiList[1])

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
                photo_carousel_right_arrow_button.click()    

            # close the photo carousel
            photo_carousel_close_button = driver.find_element(By.XPATH, '//*[@id="modalHeader"]/button/span')
            photo_carousel_close_button.click()


        print("Match Success!")


    driver.quit()

test_eight_components()
