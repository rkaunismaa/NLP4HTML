import scrapy

class LoginSpider(scrapy.Spider):

    name = 'login_spider'
    # start_urls = ['https://www.match.com/login/?regflow=https://www.match.com/cpx/en-us/match/IndexPage']
    start_urls = ['https://www.match.com/login']

    def parse(self, response):

        # Identify the login form fields and adjust the data as necessary
        form_data = {
            'email': 'youremail',
            'password': 'yourpassword',
            'reactivateUrl': 'reactivateAccount',
            'rememberMe' : 'true',
            'submitted' : 'false'
        }

        # Submitting the login form using a POST request
        yield scrapy.FormRequest.from_response(
            response,
            formdata=form_data,
            callback=self.two_factor
        )

    def two_factor(self, response):

        # Select the Text radio button, then click continue
        # //*[@id="Mjc6OlNNUw2"]
        # //*[@id="Mjc6OlNNUw2-radio-button__label"]
        # #Mjc6OlNNUw2
        # <input type="radio" class="css-mhkgdc" name="verifyType" id="Mjc6OlNNUw2" data-verifytype="1" value="xxx-xxx-8721">

        # radio button verifyType
      
        # /html/body/div[1]/div[2]/div/div/main/form/div/div/div/div[2]/div[1]/div/label[1]/input

        # Email radio button
        # //*[@id="Mjc6OkVtYWls0"]
        # //*[@id="Mjc6OkVtYWls0-radio-button__label"]
        # <input type="radio" class="css-mhkgdc" name="verifyType" id="Mjc6OkVtYWls0" data-verifytype="2" value="r*****s@gmail.com">

        # Continue Button
        # //*[@id="mainContent"]/form/div/div/div/div[2]/button
        # //*[@id="mainContent"]/form/div/div/div/div[2]/button

        form_data = {
            'verifyType': 'xxx-xxx-8721'
        }
         
        # Submitting the login form using a POST request
        yield scrapy.FormRequest.from_response(
            response,
            formdata=form_data,
            callback=self.enter_Code
        )

    def enter_Code(self, response):

        # Prompt the user for input
        codes = input("Enter in the 4 numbers you received on your phone, with spaces in between them, then hit enter ...")
        code_list = codes.split()

        form_data = {'verify-first': code_list[0],
                     'verify-second':code_list[1],
                    'verify-third':code_list[2],
                    'verify-fourth':code_list[3]  
                    }
        
        # Submitting the login form using a POST request
        yield scrapy.FormRequest.from_response(
            response,
            formdata=form_data,
            callback=self.after_login
        )

    def after_login(self, response):
        # Check if login is successful by examining the response.
        # You can check for a particular element or text on the page.
        if "Your Profile" in response.text:
            self.logger.info("Login successful!")
            # From here, you can continue with your authenticated crawling.
            # For example, yield a request to a protected page:
            yield scrapy.Request(url='https://www.match.com/profile/me/edit', callback=self.parse_protected_page)
        else:
            self.logger.error("Login failed!")

    def parse_protected_page(self, response):
        # Parse the protected page after successful login
        # Your parsing logic here
        pass
