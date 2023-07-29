from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.by import By

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


    # So let's try match, shall we ... 
    if useChrome:

        driver.get("https://www.match.com/profile/me/edit")

        userName = driver.find_element(By.XPATH, '//*[@id="profile-edit-layout"]/div[2]/div[2]/div/section/div/div[1]/div/div[1]/div[1]/h2')
        myName = userName.text
        assert myName == "Rob"

        # 'View more' button
        viewMore_button = driver.find_element(By.XPATH, '//*[@id="profile-edit-layout"]/section[1]/div/div[2]/div[2]/button')
        viewMore_button.click()

        # now select the summary
        summary = driver.find_element(By.XPATH, '//*[@id="profile-edit-layout"]/section[1]/div/div[2]/div[1]/span')
        mySummary = summary.text

        # click VIEW
        VIEW_button = driver.find_element(By.XPATH, '//*[@id="profile-edit-layout"]/div[1]/div[1]/div/ul/li[1]/a/span')
        VIEW_button.click()

        # click the photo carousel ..
        photo_carousel_button = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[1]/div[2]/div/button')
        photo_carousel_button.click()

        # photo carousel right arrow ...
        photo_carousel_right_arrow_button = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/button[2]/span/span')

        # figure out how many pictures they have ...
        image_count = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/span')
        no_of_images = image_count.text # '1/5'
        noiList = no_of_images.split('/')
        totalImages = int(noiList[1])

        photo_carousel_image = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/figure/div[2]/button/img')
        photo_carousel_caption = driver.find_element(By.XPATH, '//*[@id="lightbox-image-caption"]/div/span')

        for _ in range(totalImages):
            image_text = photo_carousel_caption.text
            photo_carousel_right_arrow_button.click()    


        # close the photo carousel
        photo_carousel_close_button = driver.find_element(By.XPATH, '//*[@id="modalHeader"]/button/span')
        photo_carousel_close_button.click()
        

        # Right arror button ...
        # /html/body/div[5]/div/div/section/div/button[2]/span/span

        # shows how many images ... "1" "/" "5"
        # //*[@id="lightbox-image-caption"]/span

        # X to close the photo carousel ...
        # //*[@id="modalHeader"]/button/span


        
   

        print("Match Success!")




    driver.quit()

test_eight_components()
