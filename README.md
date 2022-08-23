<h1>Friendly Fitness</h1>

<img src="assets/readme_images/responsive.png">

### **Live Site**
[Frinedly Fitness Live Site](https://friendly-fitness.herokuapp.com/)

### **Repository:**
[Friendly Fitness Github Repository](https://github.com/StephenKennyGains/FriendlyFitness)

# About
An E-commerce site for selling Personal Training services for those working in the fitness indusrty selling One to One personal Training and Online Training Services.

# Table of Contents

[User Experience](#user-experience)

- [Marketing Audience](#marketing-plan)

- [User Stories](#user-stories)

- [Features](#features)

- [Structure](#structure)
    - [Databases](#databases)
    - [Design Plan](#design-plan)


[Marketing Strategy](#marketing-strategy)

[Features](#features)

[Additional Future Features](#additional-future-features)

[Technologies Used](#technologies-used)

[User Testing](#user-testing)

[Validator Testing](#validator-testing)

[Design Testing](#design-testing)

[Known Bugs](#known-bugs)

[User Feedback](#user-feedback)

[Search Engine Optimisation](#search-engine-optimisation)

[Deployment](#deployment)

[Credits](#credits)

[Acknowledgments](#Acknowledgments)

# User Experience

# Marketing Audience

This website was built based on my own experiences from 10 years working in the fitness industry modelled as a B2C structure. The aim of the site is to allow a Personal Trainer to advertise, market and sell their Personal Training services for both in Person and Online training. 

From experience in the industry, many trainers will work as independant contractors to the gym in which they operate or operate their business by going to people's homes, public training spaces or through online services. With that in mind, selling, advertising and maing their services accesible is a challenge to those in the industry who are in heavy competition to have a larger brand reach and ease of access to their services.

For selling services such as Personal Training, the target adience can be quite broad as it caters to both a male and female demographic along with a wide age range anywhere from 18-50 for online services. With the broad age range, the site needed to be both visually appealing, high speed and a very simplistic navigation and ease of use for the older demographic. Given the broad age range, the site also needs to be as visually appealing in mobile and tablet views.

The general target of advertising personal training would be for 35-50 as the ideal target market given the higher likelihood of being able to afford the services, have the scheduling time for avialing of them and the higher need for more tailored advice for health reasons and the overall impacts of age. With the high trend rates of gym, fitness and personal training related content, the market has expanded to the younger demographic and with that, the imagery, fonts and colour scheme is intended to be both appealing to navigate the site for older users and be visually appealing to younger users.

# User Stories

The User stories for the project can be found in the following link-[here](https://github.com/users/StephenKennyGains/projects/2).



# Features

To ensure the project User Stories were completed and met, the site required the following:

- Site Navigation which was simple and minimal for quick and easy navigation

- A landing page which outlined the Pricing and allowed easy access to site services

- A services page which was user friendly, easy to access, easy to use and visually appealing

- Service images, descriptions, pricing, and easy selection of

- A cart page which allows users to store services in their account while they continue to browse

- A checkout page so that users can review their information and the services they are purchasing

- A confirmation page for reviewing their purchase

- Login, registration, account and confirmation pages for account creation

- Custom 404 Error Page

# Structure

The site is strctrure in a simple and effective way leaving very mimimal choice to steer users directly to the services section of the page and 

The option is open for both users and non-users to purchase from the site to leave open access to all users

The website is made of the following apps:
1. Home
2. Serices
3. Profile
4. Cart
5. Checkout

## Databases

For the live site, I connected Heroku's Postgres Database and for the local environment, it remains connected to Sqlite/
Below is the entity rleationship diagram of the site:

<img src="assets/readme_images/FriendlyFitnessERD.png">

### Category

The Category is the options for the User and Admin to select Services in a filtered way. Admins can add and update categories through the admin panel and Users will be filtered services based by category

### Products
Products can be added by the admin from both the site and admin panel along with updating and deleting. Services can be selected by the user to add to their cart.

### Order & Order Line Items
Order Line Items are created by the User by adding the service to their Cart. Their Order is based on the total services along with their User and purchase information.

### User
User profiles are created by the user for speed in purchasing services. Users can save their details and Login to use those details in future purchases.
 

## Wireframes

Wireframes were created on Adobe XD and have been updated after initial views in a Live format. [Balsamiq](https://balsamiq.com/).


# Marketing Strategies

For the Marketing of the website I want to be able to reach both ends of the spectrum for the target audience and be able to cater towards all genders and the various personality types of potential clients. with the age gap between the newer demographic of younger people and the tragte demogrpahic of older people, Facebook and Intagram are the 2 platforms of choice to market through alongside email marketing. While Tiktok is the largest growing audience and highest growing spend rate amongst marketers, the saturation of low quality content may be conflicting for the type of training aimed at being provided. 

Tiktok although it has a large audience and is a huge growing market and is now becoming the leading social media platform, it stil has a younger target audience and content quality on the platorm in the Fitness and training space can be low so it was ruled out as Facebook and Instram can be targetted on One post and thus saves time in marketing towards multiple channels which cannot yet be managed.

To combine the aim of Facebook, Instagram and Email Marketing, a platform like HubSpot with a starter marketing plan and CRM plan would allow for large scale MArketing campaigns, social media posting, traffic analytics for the site using their HuBSpot Tracking code and scheduling and managing posts in one system. Along with that, User purchases and plans could be tracked and invoiced from the same system, alongside multiple integrations available. This would be my go to for Marketing and would allow for a smaller based team such as a One man Peronal Training business to still operate effectively and effeciently. 

### MailChimp

Users can currently subscribe to the Newsletter through the Mailchimp form in the footer of the site but this would also be able to managed through HubSpot if the Marketing and Social content was migrated there.


# Features

## Homepage

### Logo / Shop Name

<img src="assets/readme_images/logo.png" width="50%">

### Search Bar 

<img src="assets/readme_images/search.png" width="50%">

### My Account 

<img src="assets/readme_images/my-account.png" width="50%">

### Shopping Bag 

<img src="assets/readme_images/bag-icon.png" width="20%">

### Bootstrap Toast

<img src="assets/readme_images/success-toast.png" width="50%">

<img src="assets/readme_images/alert-toast.png" width="50%">

### Product Navigation

<img src="assets/readme_images/navigation.png" width="100%">

### Delivery Banner

<img src="assets/readme_images/delivery-banner.png" width="100%">

### Homepage Message

<img src="assets/readme_images/homepage.png" width="750%">

## My Account

### Account Registration

<img src="assets/readme_images/registration.png" width="50%">

### Login

<img src="assets/readme_images/login.png" width="50%">

### My Profile

- Delivery Information

<img src="assets/readme_images/default-delivery.png" width="50%">

- Order History

<img src="assets/readme_images/order-history.png" width="50%">

- Order Confirmation

<img src="assets/readme_images/checkout-success.png" width="50%">


### Logout

<img src="assets/readme_images/logout.png" width="50%">

## Products Page 

<img src="assets/readme_images/products.png" width="75%">

## Product Details 

<img src="assets/readme_images/add-favourites.png" width="75%">

## Product Favourited 

<img src="assets/readme_images/added-favourites.png" width="50%">

## Product Review

Visable on the bottom of the Product Details Page

Logged in as Superuser and with reviews:

<img src="assets/readme_images/review-section-1.png" width="75%">

Not logged in and without reviews:

<img src="assets/readme_images/review-section-2.png" width="75%">

## Edit Review Form

<img src="assets/readme_images/edit-review.png" width="75%">

## Delete Review Confirmation

<img src="assets/readme_images/delete-review.png" width="50%">

## Favourited Products (Wishlist)

<img src="assets/readme_images/my-favourites.png" width="75%">

## Shopping Bag

<img src="assets/readme_images/shopping-bag.png" width="50%">

## Checkout

<img src="assets/readme_images/checkout.png" width="50%">

## Add Coupon Form

<img src="assets/readme_images/add-coupon.png" width="50%">


## Coupon Added / Remove Coupon

<img src="assets/readme_images/added-coupon.png" width="50%">


## Checkout Success

<img src="assets/readme_images/checkout-success.png" width="50%">

## Order Confirmation Email

<img src="assets/readme_images/email-confirm.png" width="50%">

## Footer

<img src="assets/readme_images/footer.png" width="100%">

## Help

### FAQs

<img src="assets/readme_images/faq.png" width="50%">


### Shipping and Returns

<img src="assets/readme_images/shipping.png" width="50%">

## Company
### About Us

<img src="assets/readme_images/about.png" width="50%">

### Privacy Policy

<img src="assets/readme_images/privacy.png" width="50%">

## Contact Form

<img src="assets/readme_images/contact.png" width="50%">

The following email is sent via the contact form:

<img src="assets/readme_images/contact-form-email.png" width="50%">


## 404 Error Page

<img src="assets/readme_images/error.png" width="50%">

## Admin Features

### Product Management
<img src="assets/readme_images/add.png" width="50%">

### Edit Products
<img src="assets/readme_images/edit.png" width="50%">

### Delete Products
<img src="assets/readme_images/delete.png" width="50%">

## Colour Scheme 

The colour scheme for the site was based off colours which evoke the emotions typically associated to health and wellnes and physical activity. Colours can be seen to similar to well know fitness brands like Anytime Fitness, Orange Theory, Fitness First and others.

------------- Enter colour palette here -----------------------

## Font Choice

I chose the roboto and Lato as they are two of the most popular fonts currently used and having familiarity in the site can help build a sense of trust in the user. 

## Favicon 
-------------Create Favicon and Enter here ------------------- 


# Features to be Implemented
The following features may prove useful to the site with a larger audience and further market research

- A blog of content related to health and wellness so the newsletter can direct traffic back to the site

- With additional services potentially being brought in the future, additonal partitioning of the services through available categories in the navigation will make for easier use for the user but with a small group of categoreis to choose from, having the user navigate through the options shows the user what is available and make it look like a larger operation.

- At present, users can buy multiple packages of personal training which makes sense for the 6 and 10 session pacages as a user may want 12 or 20 sessions in a package but if any noticeable errors came through in orders, limiting users to 1 service of each type per purchase may be a required feature. 

# Technologies Used

- HTML
- CSS
- Python
- JavaScript
- GitHub
- GitPod
- Herokuutilised/tested. 
- Django
- Bulma
- Bootstrapresponsive across multiple devices and screen sizes.
- Font Awesome
- Adobe XD
- Lucid Chart
- Google Fonts

# Testing
## **Manual Testing by User Story**
### **Superuser / Admin**
### 1. As a Site Owner, I want to be able to add a product so that I can add more items to my store.

### 3.	As a Site Owner, I want to be able to delete a product so that I can remove items that are no longer available.

### 4.	As a Site Owner, I want to be able to send emails to customers with a subscription, notifying customers of any deals, sale and new arrivals.

### 5.	As a Site Owner, I want to be able to remove reviews from the site without deleting them so that they can still be available if required.

### 6. As a Business Owner I want to Create discount codes for customers so that I can reward loyal customers.


### **Shopper**
### 1. As a Shopper, I want to be able to view a list of items so that I can add them to my basket.


###	2. As a shopper, I want to be able to click into an item so that I can view a product description and add to the basket.


### 3. As a shopper, I want to be able to add items to my basket so that I can keep track of what I am spending.


### 4. As a shopper, I want to be able to be able to adjust the quantity of products in my basket so that I can make changes to my purchases before checkout.


### 5. As a shopper, I want to be able to be able to enter payment information so that I can check out quickly and hassle free.


### 6. As a shopper, I want to be able to be able to feel that my personal and payment details are safe and secure so that I can confidently carry out my purchase.


### 7. As a shopper, I want to be able to be able to view an order confirmation so that I can verify my order is correct.


### 8. As a shopper, I want to be able to receive an email confirmation of my order so that I have proof of my order for my records.


### 9. As a shopper, I want to be able to be able to order without creating an account so that I can make one-off orders.


### 10. As a shopper, I want to be able to be able to sort a specific category of a product so that I can find the best price quickly for the product I am looking for.

### 12. As a shopper, I want to be able to be able to easily see what I’ve searched for and the number of results so that I can quickly see whether the product is available.

### 13. As a shopper, I want to be able to be able to easily register for an account so that I can have a personal account and view my profile and purchase history.


### 14. As a shopper, I want to be able to be able to recover my password so that I can recover my account access.


### 15. As a shopper, I want to be able to be able to receive a registration confirmation email so that I can confirm registration.


### 16. As a shopper, I want to be able to be able to sign up for emails so that I can be notified of new releases, deals, and upcoming sales.


### 17. As a shopper, I want to be able to be able to contact the site owner so that I can ask about my order or for further information not contained within the Footer Pages.


### 18. As a shopper, I want to be able to be able to review products purchased on the site so I can share my thoughts with other shoppers and the business.


### 19. As a shopper, I want to be able to be able to edit and remove my reviews of products purchased so I can share or remove my reviews if my opinions change.


### 20. As a Shopper I want to save Items to my favourites so that I can purchase them later without having to search for them.


# Validator Testing

- The HTML templates were validated using [W3 Validator](https://validator.w3.org/nu/#textarea). No major errors were returned for the HTML segments.
- The CSS style sheet was validated using [W3C Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) and no errors were returned.
- The JavaScript files were run through [JSHint](https://jshint.com/) and no errors were found apart from a few missing semi-colons which were added. Also, the project was run through whilst checking for any issues in the console. No errors were found.
- The code was validated using [PEP8](http://pep8online.com/). No errors were returned.
- The finished project was also run through [Wave](https://wave.webaim.org/) to check for issues with contrast styling and HTML structure. 

# Responsive Testing

I also tested this project's responsiveness across multiple devices including:

- iPhone X
- iPhone 8
- Samsung S21 FE
- Samsung S10+
- Samsung Galaxy Z Flip3
- iPad Pro 9.7"
- MacBook Pro 13"

I also used Google developer tools to check responsiveness across multiple other devices and screen sizes. 

# Bugs Found 

I encountered the following issues whilst building this project:
- The Footer wasn't sticking to the bottom on some of the pages. To fix this I added an 'h-100' Bootstrap class to the container divs or set the minimum height within media queries. 

- The Success Message wasn't working when removing items from the cart. To fix this I needed to get the product ID to identify which Item was being deleted in the message

- The Shopping bag was repeating the 'Continue Shopping' and 'Add to Bag' buttons after every item in the bag. To fix this I moved the {% endfor %} for the {% if bag_items %} to be before the buttons.

- Incorrect Stripe public key in checkout view. I accidentally wrote the public key in the context in capitals. 

- I was able to add products to categories that were not on the dropdown list. To fix this I had to remove the non-existing categories in the admin panel and remove/change to category of the products added to these categories.

- Deploy not completing - message received: ERROR: Could not find a version that satisfies the requirement python-apt==2.0.0+ubuntu0.20.4.7 (from versions: 0.0.0, 0.7.8). To fix this I removed the un-required installs from requirements.txt file.

- The Webhook for the live site was generating a 301 error. To fix this I had to add a / at the end of the URL that the webhook was set up to.

- The delivery confirmation page image wasn't Loading on the deployed site. To fix this I changed the image source to the images [AWS](https://aws.amazon.com/?nc2=h_lg) URL to display the image.

- Stripe was sending a Server 500 error in the Webhooks, this was an error on Stripes part which I could not control. I believe this is fixed now. All Webhooks are currently sending as expected. 

# User Feedback 

- Make the price on the Product Card bolder.
- Change 'Quantity' to 'Qty' on the Product Details page and Shopping Bag page.
- Add a slight margin to the bottom of the Product Cards.
- Center the Product Cards on the Products page.
- Change the button styling so that the call to action is toward purchasing items.

**Peer Code Review Feedback**

My project was shared on Slack with other Code Institute students. The feedback received was: 

- Add some weight to the font or make it larger as it is difficult to read on some of the pages, particularly the FAQs and About Us pages.

All feedback received was implemented throughout the project.
 
# Search Engine Optimisation (SEO)
To find the relevant keywords for my project I made the following searches on [Google](www.google.co.uk) and [Word Tracker](www.wordtracker.com)  along with a few combinations:

-	Clay Jewellery
-	Polymer Clay Jewellery
-	Baked Clay Jewellery
-	Handmade jewellery
-	Handmade clay jewellery
-	Handmade gifts
-	Ladies handmade gifts
-	Gift ideas for woman

Of the above, the top combination of searches  I found were:

-	Handmade Polymer Clay Jewellery
-	Handmade Jewellery Gifts 
-	Handmade Women’s Jewellery
-	Handmade Jewellery UK
-	Handmade Jewellery

Of the above searches, Handmade Polymer Clay Jewellery best suited what my project is selling and had the highest search rate of all keywords attempted. With that in mind, I have selected the following to be included in my projects metadata:

-	Handmade Jewellery Gifts
-	Handmade Polymer Clay Jewellery
-	Handmade Jewellery
-	Polymer Clay Jewellery

Also, I included ‘Handmade Jewellery’ within the homepage message’ along with a subheading of ‘Find the perfect gift today!’ 

# Deployment 

This project was deployed using Heroku. At the time of deployment, Heroku was facing a security issue, therefore this project was deployed via the command line in GitPod and those are the steps detailed below. As this was the case I was unable to allow automatic deployments in Heroku each time a commit was pushed into the repository.

See the following steps to deploy below:

1. Log into Heroku and Create a New App.

2. Give the App a name, it must be unique, and select a region closest to you. 

3. Click on 'Create App'. This will take you to a page where you can deploy your project. 

4. Next, click on the 'Resources' tab and search for 'Heroku Postgres' in the Add-ons section to add the Heroku Postgres database to the project. 

5. Click on the 'Settings' tab at the top of the page. The following steps must be completed before deployment.

6. Within the settings.py file you need to import os and import dj_database_url at the top. Then, in the command line install dj_database_url and psycopg2 so that we can use Postgres. Freeze these installs into the requirements.txt file.

7. Scroll down to Config Vars (also known as Environment Variables) and click 'Reveal Config Vars'. Here the database URL is stored to run my app on Heroku. 

I used an if statement in settings.py (see below) so that when our app is running in Heroku, we connect to Postgres but in our local environment, we connect to sequel light:

    development = os.environ.get('DEVELOPMENT', False)

    if development:

            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }

        else:

            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }

Development is set in gitpod's environment variables as True.

8. Next I ran the migrations again to set up my Postgres Database by running **Python 3 manage.py migrate** within the command line and then create a Superuser using **python3 manage.py create superuser**.

9. Following setting up the database I generated a new Secret Key, to replace the insecure key that was in settings.py and added: **os.environ.get('SECRET_KEY')**. I then added the newly generated key to the Config Vars on Heroku. 

10. We must then install Gunicorn, which will act as our webserver and freeze that into our requirements file.

11. Next, I created a Procfile to tell Heroku to create a web dyno that will run Gunicorn and serve our Django app.

Within this file add the following:

    web: gunicorn clay_and_fire.wsgi

Web tells Heroku to allow web traffic, whilst Gunicorn is the server installed earlier, a web services gateway interface server (wsgi). This is a standard that allows Python services to integrate with web servers.

12. I then told Heroku temporarily disable collectstatic by using the Heroku config set, disable collectstatic = 1. I added this via Heroku's Config Vars but this can also be added via the command line. This was to prevent Heroku from attempting to deploy the static files, causing an error, until Amazon Web Services was set up. 

13. Then add the hostname of our Heroku app to 'Allowed Hosts' in settings.py as well as localhost so that GitPod will still work too.

14. I then committed and pushed these changes into my GitHub repository so that I could start my first deployment. Once complete, log into Heroku using the following command in the terminal, **heroku login -i**,  and enter your login details.

15. Once logged in, add a remote to your local repository with the Heroku git:remote command and your Heroku app’s name: **heroku git:remote -a clay-and-fire**

16. Finally, deploy using the following command: **git push heroku main**. Once deployed you can open the app from the command line to ensure it was successfully deployed.

17. Once we can confirm the app deployed successfully, we need to set up Amazon Web Services as this will be where my media and static files are stored. To do this I first created an account with Amazon Web Services. Then, I searched for the service, S3, using the search bar at the top of the page. 

18. Click into it and then click the orange 'Create a Bucket' button. I named this bucked to match my clay-and-fire Heroku app name to keep things simple. Then, I selected my region and changed the 'Object Ownership' setting to **ACLs enabled**. Then, I unchecked block all public access, acknowledged that the bucket will be public, and clicked on the 'Create Bucket' button.

19. Next, on the properties tab, I scrolled to the bottom and turned on static website hosting.
This gave me a new endpoint that I can use to access it from the internet. For the index and error document, I filled in some default values and then clicked Save.

20. Now on the permissions tab I pasted in the following coors configuration:

    [
        
        {
            "AllowedHeaders": [
            "Authorization"
            ],

            "AllowedMethods": [
            "GET"
            ],

            "AllowedOrigins": [
            "*"
            ],

            "ExposeHeaders": []
        }
        
    ]

which is going to set up the required access between our Heroku app and this s3 bucket.

21. Next I'll go to the bucket policy tab a select, policy generator so we can create a security policy for this bucket. The policy type is going to be s3 bucket policy and then allow all principals by using a '*' and the action will be, get object. Next, I copied the ARN which stands for Amazon resource Name from the other tab and paste it into the ARN box at the bottom. I then clicked 'Add statement' and then 'Generate Policy'.

22. I then copied this policy into the bucket policy editor. I then added '/*' at the end of the resource key to allow access to all resources in this bucket and then saved it.

23. Finally, to complete configuration, I went to the 'access control list' tab and checked edit and enable List for Everyone (public access), and accepted the warning box.

24. Next I created a group and a user to access the bucket by searching for the service IAM (Identify and Access Management). I clicked on 'User Groups' and then 'Create User Group' giving it the name 'manage-clay-and-fire'. 

25. I then created the Policy used to access our bucket by clicking 'Policies' and then 'Create Policy'. I clicked onto the JSON tab and then selected import managed policy to import one that AWS has pre-built for full access to s3.

26. I searched for s3 and then import the s3 full access policy. I then got the bucket ARN from the bucket policy page in s3 and pasted that into the 'Resource' section on the JSON tab.

I then clicked the 'Next' buttons until I reached 'Review Policy'. I gave it a name and a description and then clicked 'Create Policy'. This took me back to the policies page.

27. Next I attached the policy to the Group I created by returning to the Create User Group page and refreshing the Policies box. I then was able to attach the new policy created by selecting it and finally clicking 'Create Group'.

28. Finally I created a user to put in the group by going to the User's page and clicking 'Add User'. I created a user named **clay-and-fire-static-files-user**, gave them Programmatic Access, and clicked 'Create User'. 

29. I then downloaded the CSV file which contained this User's Access Key and Secret Access Key which I used to authenticate them from my Django app. It is important to download this file as you cannot be re-downloaded and contains the new user's credentials which I next add to the Config Vars on Heroku.

30. Next, I connected Django to the new S3 bucket. To do this I installed two new packages:
- boto3
- django-storages 

31. I then pip3 freeze these to the requirements.txt file to ensure they're installed on the next Heroku Deploy and added **storages** to our installed apps in settings.py. 

32. To connect Django to S3 (only on Heroku) I then added the following in if statement settings.py:

        if 'USE_AWS' in os.environ:
            # Bucket Config
            AWS_STORAGE_BUCKET_NAME = 'clay-and-fire'
            AWS_S3_REGION_NAME = 'eu-west-2'
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
            AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

            # Static and media files
            STATICFILES_STORAGE = 'custom_storages.StaticStorage'
            STATICFILES_LOCATION = 'static'
            DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
            MEDIAFILES_LOCATION = 'media'

            # Override static and media URLs in production
            STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
            MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


33. I then added the following to our Config Vars on Heroku:
- USE_AWS = True
- AWS_ACCESS_KEY_ID, taken from the new user credentials
- AWS_SECRET_ACCESS_KEY, taken from the new user credentials

and removed:
- Remove staticcollect=1 from congifvars within Heroku 

I also set DEBUG to 'DEVELOPMENT' in os.environ as for security it cannot be set to True on the deployed version. 

34. The next step is to tell Django that in production we want to use s3 to store our static files whenever someone runs collectstatic and that we want any uploaded product images to go there also. To do that I created a file called custom_storages.py.

35. Within this file I imported both our settings from django.conf and the s3boto3 storage class from Django Storages. Then I created custom classes for static storage and media storage which inherited the imported class from Django Storages to give it all its functionality. Then I set the class to store static and media files in the location specified in the USE_AWS if statement within settings.py.

36. Finally, to complete the deployment of the AWS setup, I committed the changes and pushed them to GitHub. In the command line I then typed the following command: **git push heroku main**. If you need to login to Heroku again complete steps 14 - 16 to re-deploy. Once Heroku is allowing users to connect to their GitHub accounts you can set up automatic deploys which will remove the need to repeat these steps.
# Credit
## Content 

I used the Code Institutes Boutique Ado Follow Along project to help with building this project along with the following websites:

- [Mini Web Tool](https://miniwebtool.com/django-secret-key-generator/) to generate a new Django Secret Key.

- [Sculpey Blog Post](https://www.sculpey.com/create/blog/10-surprising-facts-about-polymer-clay#:~:text=Polymer%20clay%20is%20non%2Dtoxic,use%20around%20children%20and%20pets.) was used to gather information about polymer clay for the FAQs page.

- I used [H&M](https://hmgroup.com/about-us/our-values/), [Oysho](https://www.oysho.com/gb/company.html), and [Accessorize](https://www.accessorize.com/uk/our-brand.html) to see how they shared their Policies and Frequently Asked Questions with their customers for content ideas.

- [GDPR Privacy Policy Generator](https://www.privacypolicygenerator.info/) was used to generate the Privacy Policy that was added to the footer.

- [Scottish Coder YouTube Tutorial](https://www.youtube.com/watch?v=1DcySa35fXw) was used to help with creating a working contact form view.

- I used the following YouTube Tutorials to help with creating the Error404 page:

    - [Custom 404 Error Page. Python Django Web Framework Course. #16](https://www.youtube.com/watch?v=3SKjPppM_DU)
    - [Python Django 3 0 7 Create Show Custom 404 Error Page](https://www.youtube.com/watch?v=ZhwkddfqUTY)

<br>

- [XML Sitemap Generator](https://www.xml-sitemaps.com/) was used this to generate the sitemap for my project.

- The following videos were used to help create the review functionality:
    - [Rathan Kumar - Review and Rating System in Django Python Part 1](https://www.youtube.com/watch?v=3KCBN7WJXMY)
    - [Rathan Kumar - Review and Rating System in Django Python Part 2](https://www.youtube.com/watch?v=Zkmu93lMLPs)
    - [Rathan Kumar - Review and Rating System in Django Python Part 3](https://www.youtube.com/watch?v=gDtsAWMA3Jo)
    - [Rathan Kumar - Review and Rating System in Django Python Part 4](https://www.youtube.com/watch?v=eIN1nZCt7Ww)

- [Stack Overflow](https://stackoverflow.com/questions/16244821/how-to-stop-sticky-footer-from-covering-content) was used to fix the footer covering the review form.

- [Stack Overflow](https://stackoverflow.com/a/666407) was used to help with the cancel button for the confirm delete review template.

- [GitHub Django Allauth Issues](https://github.com/pennersr/django-allauth/issues/3037) was used to help fix email subject by adding ACCOUNT_EMAIL_SUBJECT_PREFIX to my settings.

- The following video was used to help create the coupon functionality:
    - [freeCodeCamp.org - How to Build an E-commerce Website with Django and Python](https://www.youtube.com/watch?v=YZvRrldjf1Y&t=10194s)

- The following helped with putting together the favourites functionality:
    - [Stackoverflow](https://stackoverflow.com/questions/64720982/modeling-favorites-in-django-from-two-different-models)
    - [Very Academy Python Django Ecommerce Customer Wish List](https://github.com/veryacademy/django-ecommerce-project/blob/main/Part-07%20Wish%20List/account/views.py)
    - [American Ale House](https://github.com/Steven-Dawson18/american-ale-house/tree/main/favourites)

### Styling
- [Unsplash - Landing Image](https://unsplash.com/photos/uRuF9ABj0NY)
- [Logo Font - Google Fonts](https://fonts.google.com/specimen/Raleway?query=raleway)
- [Font Awesome Icons](https://fontawesome.com/)
- [CSS-Tricks - Flexbox Sticky Footer](https://css-tricks.com/couple-takes-sticky-footer/), for the sticky footer code.
- [Bootstrap](https://getbootstrap.com/docs/4.2/components/spinners/) - Overlay Spinner on checkout page.

### Product Images
- 'noimage.png' taken from Code Institutes Boutique Ado Follow Along Project
- [Pexels - Carpe Jugulum](https://www.pexels.com/photo/orange-and-black-ladybug-on-green-leaf-5035921/)
- [Pexels - Lisa Fotios](https://www.pexels.com/photo/a-woman-with-a-face-shaped-earring-7016917/)
- [Pexels - cottonbro](https://www.pexels.com/photo/close-up-shot-of-a-woman-wearing-a-blue-earring-8541542/)
- [Unsplash - Svitlana](https://unsplash.com/photos/J7ydFF1WyGQ)
- [Unsplash - Kate Hliznitsova](https://unsplash.com/photos/P6NiFTyI294)
- [Unsplash - Sincerely Media](https://unsplash.com/photos/8WebmlRgMp0)
- [Unsplash - Gabrielle Henderson](https://unsplash.com/photos/YGIPzuiD1jc)
- [Unsplash - Gabrielle Henderson](https://unsplash.com/photos/YbA4hHxkSrg)
- [Unsplash - Gabrielle Henderson](https://unsplash.com/photos/O7l3PmbGxF0)
- [Unsplash - Gabrielle Henderson](https://unsplash.com/photos/fR3PIa-WtBg)

The images used in this project were also compressed using (OptimiZilla)[https://imagecompressor.com/].

### Website Images
- [Pexels - Delivery Image](https://www.pexels.com/photo/person-holding-green-and-white-floral-book-5486791/)

- [Favicon Generator](https://favicon.io/favicon-converter/) used to generate a favicon image from a jpg image.

# Acknowledgments
Thank you to all who encouraged and supported me as I created my first full-stack E-Commerce website. Thank you to the Tutors at Code Institute for always helping to figure out issues I encountered that I was unable to solve myself. I'd especially like to thank my mentor at Code Institute, Antonio, for his guidance, patience, encouragement, and constant support.