<h1>Friendly Fitness</h1>

<img src="assets/readme_images/all-devices-black.png">

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

 <details>
  <summary>Screenshots Desktop</summary>

  ![Header](assets/readme_images/header.PNG)

  - The header was kept as minimal as possible and I chose to keep the services section without any drop downs as the low amount of services currently being offered meant it was un necessary to do additional steps for navigation

  ![Desktop Footer](assets/readme_images/footer.PNG)

  - I chose to keep the footer only to the Home page as it felt intrusive on other pages and could potentially lead customers away from their main aim of the site which is to purchase personal training sessions. For that reason I kept navigation away for the site to a minimum.

  ![Desktop Main Home Image](assets/readme_images/main_image.PNG)

  - I wanted to main website image to be something both striking and also which easily gave the viewer a snapshot of the site aim. I chose the image I chose because it tailors to a wider audience as is in the Marketing startegy. 

  ![Desktop Pricing Section](assets/readme_images/pricing_section.PNG)

  - The pricing section was added to give a bit of authenticity and personality to the site. Letting customers see a justification of the services pricing before purchasing for those who would not already be familiar to the trainer they are about to work with.

  ![Desktop Services Page](assets/readme_images/services_view.PNG)

  - The services page was kept to the same level of mimimal design as the home. Providing only the necessary details of the service and choosing imagery which spoke to a wide audience. I choose to categorize and order the services and left room for additional services without the page being excessively long. Any more than 3 services and I would then choose to break down the service section and add the additonal required navigation through the site.

  ![Desktop Services Detail](assets/readme_images/service_detail.PNG)

  - For the service detail, I experimented with the footer also being present here but after user feedback, they felt there was very little to get confused about on this page and made for a more likely addition to the shopping cart. They felt the layout was clean and easy to read and felt the flow was laid out nicely.

  ![Desktop Shopping Cart](assets/readme_images/shopping_cart.PNG)

  - The shopping cartm while having the update and delete functionality, still does not feel over bearing to the user and I wanted to appearance to look and feel familiar to the previous pages bu while also being ditinct enough to know that you are nearing the final stage of completing your purchase.

  ![Desktop Checkout](assets/readme_images/checkout.PNG)

  - The checkout, while having a bit more information to it that the previous steps, feels like it has enough familiarity to other ecommerce stores that users will have enough intuition to navigate through it successfully and user feddback clarified that. While I think there are some changes that can be made, I would prefer to use a larger audience to dictate those changes.

  ![Desktop Sign In](assets/readme_images/Sign_in.PNG)

  - The sign in page, just needed enough changes to set the same feel, thrugh colours, fonts and layouts, that it did not feel like you were in any way using a third party or navigatin away from the site whilst you are about to provide personal information.

  ![Desktop Sign Up](assets/readme_images/sign_up.PNG)

  - For the sign up, the main aim was that the fields be easy to read and easy to understand what was required. Of course having allauth provide the heavy lifting meant all that was required was colour coding and directing successfully to make it a pleasant esperience. 

  ![Desktop Confirmation Page](assets/readme_images/confirmation.PNG)

  - For the confirmation receipt, I just wanted to have all the information clearly displayed to the user and have a thankful message diplayed to them. Ensuring that mobile, tablet and desktop views all gave a similar experience was important and so I compared recipts of other sites to mobile versions too and found that they kept a similar style and made users scroll for info instead of minimizing it to have to zoom

  </details>

Please use the Drop down above to expand out the Dekstop Images  

## Colour Scheme 

The colour scheme for the site was based off colours which evoke the emotions typically associated to health and wellnes and physical activity. Colours can be seen to similar to well know fitness brands like Anytime Fitness, Orange Theory, Fitness First and others.

------------- Enter colour palette here -----------------------

## Font Choice

I chose the roboto and Lato as they are two of the most popular fonts currently used and having familiarity in the site can help build a sense of trust in the user. I had experimented with other fonts but found that the two complimented each other well and givent that there is not a great deal of text through the site, the fonts felt easy on the eye to avoid any strain for the user.

- #5C0F3E
- #FFA500
- #D3D3D3
- #000
- #fff

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
## **Manual Testing based on User Stories**
### Admin
As an admin I would like to be able to review recent purchases
(Recent purchases send through to the admin panel as expected with necessary details)
As an admin I would like to be able to add to the list of services available
(Services can easily and successfully be added to the site throuh the Services Management page)
As an admin I would like to be able to update and/or delete services as necessary
(Services can easily and effectively be edited or deleted when viewing on the Services page)
As an admin I would like to be able to see new users that have been created for the store
(New users are successfully added to the database and can be viewed in the admin panel for review)


### **Shopper**
As a User I would like to be able to find services on the page easily and quickly
(Tested and worked as designed and felt the process simple and easy and no errors on multiple test)
As a User I would like to be able to find services on the page easily and quickly
(Navigation bar worked as Designed and was easily accessbible on various devices. No failed attempts)
As a User I would like to be able to add services to my cart for review before purchasing
(Cart was successfully updated with products and view was rendering as easily readabale and understandable)
As a User I would like to be able to clearly be able to see the services I am purchasing and price
(List of services displayed as expected both in the cart and checkout pages of the app and were easily recognised)
As a User I would like to be able to browse the site easily with no unnecessary clutter
(Site was kepy minimal and from additional user testing, were able to navigate through the serives easily and understand site objective)
As a User I would like to be able to I would like to be able to store my information for the future
(Information saved to user profiles when saving through the checkout page and by adding through the profile section)
As a User I would like to be able to review my details and payment before completing my purchase
(Checkout page is easily read through form fields to be able to understand and read the details provided along with validating checks)
As a User I would like to be able to receive confirmation of my purchase
(Confirmation email and receipts successfully sent with correct details after completing payment)
As a User I would like to be able to Opt in for further information from the business
(Mail chimp form is successfully adding users to the Mailchimp contacts for further updates)
As a User I would like to be able to review my previous purchases from the Store
(Previous purchases are displaying in the profile section for the user and displaying correct values)
As a User I would like to be able to understand the services I am purchasing and their pricing
(Pricing page and descriptions of services allow users information on the services they are purchasing and the reasons behind it)
As a User I would like to be able to checkout securely and safely
(Stripe payment is successfully validating cards and asking for verification when required)


# Validator Testing

- The HTML templates were validated using [W3 Validator](https://validator.w3.org/nu/#textarea). No major errors were returned for the HTML segments.
- The CSS style sheet was validated using [W3C Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) and no errors were returned.
- The JavaScript files were run through [JSHint](https://jshint.com/) and no errors were found apart from a few missing semi-colons which were added. Also, the project was run through whilst checking for any issues in the console. No errors were found.
- The code was validated using [PEP8](http://pep8online.com/). Some Line too long errors were returned but in the interest of time, I did not change all of these.
- The finished project was also run through [Wave](https://wave.webaim.org/) to check for issues with contrast styling and HTML structure. 

# Responsive Testing

Responsive Testing dont mainly through Developer Tools for the following-

- iPhone 12
- iPhone 6/7/8
- Samsung Galaxy S20 Ultra
- Samsung Galaxy S8+
- Pixel 5
- iPad Air
- IPad Mini
- 4k 27" Screens
- 1080p 24" Screens
- 1080p 18" Screens


# Bugs Found 


# User Feedback 

 
# Search Engine Optimisation (SEO)
To find the relevant keywords for my project I made the following searches on [Google](www.google.co.uk) and [Word Tracker](www.wordtracker.com)  along with a few combinations:



Also, I included ‘Handmade Jewellery’ within the homepage message’ along with a subheading of ‘Find the perfect gift today!’ 

# Deployment 

This project was deployed using Heroku.

See the following steps to deploy below:

1. Log into Heroku and Create a New App.

2. Give the App a name, it must be unique, and select a region closest to you. 

3. Click on 'Create App'. This will take you to a page where you can deploy your project. 

4. Next, click on the 'Resources' tab and search for 'Heroku Postgres' in the Add-ons section to add the Heroku Postgres database to the project. 

5. Click on the 'Settings' tab at the top of the page. The following steps must be completed before deployment.

6. Within the settings.py file you need to import os and import dj_database_url at the top. Then, in the command line install dj_database_url and psycopg2 along with Gunicorn so that we can use Postgres. Freeze these installs into the requirements.txt file.

7. Scroll down to Config Vars (also known as Environment Variables) and click 'Reveal Config Vars'. Store the database URL in the Config Vars

Using an if statement in settings.py (see below) ,when our app is running in Heroku, we connect to Postgres but in our local environment, we connect to SQLite:

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

11. Next, I created a Procfile to tell Heroku to create a web dyno that will run Gunicorn and serve our Django app.

Within this file add the following:

    web: gunicorn friendly-fitness.wsgi


12. I then told Heroku temporarily disable collectstatic by using the Heroku config set, disable collectstatic = 1.

13. Then add the hostname of our Heroku app to 'Allowed Hosts' in settings.py as well as localhost so that GitPod will still work too.

14. Along with these steps, it was also required to do a Json Dump to re uplaod the static and media files to the new database as they were not initially done through a fixtures file. During these steps there were some issues, including Django updating to the latest version which needed to be reversed and through the process, some additional files were created.

15. I opted to keep the files in case they may be required for future testing or development of the site or in the instance of a re deploy. 

16. I then committed and pushed these changes into my GitHub repository so that I could start my first deployment. Once complete, log into Heroku using the following command in the terminal, **heroku login -i**,  and enter your login details.

17. Once logged in, add a remote to your local repository with the Heroku git:remote command and your Heroku app’s name: **heroku git:remote -a clay-and-fire**

18. Finally, deploy using the following command: **git push heroku main**. Once deployed you can open the app from the command line to ensure it was successfully deployed.

- To deploy and host the images and static files through AWS, I followed the videos from the Boutique Ado walkthrough project, along with the updated PDF that was posted to Dev Tips in the slack channel for the 5th Project.


# Credit
## Content 

I used the Code Institutes Boutique Ado Follow Along project to help with building this project along with the following websites:

- [Mini Web Tool](https://miniwebtool.com/django-secret-key-generator/) to generate a new Django Secret Key.


### Styling
- [Unsplash](https://unsplash.com/)
- [Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [Bootstrap](https://getbootstrap.com/docs/4.2/)

### Product Images
All media files were used from Unsplash from a variety of artists, which all had images under the titles of 'workout' training' and 'exercise'.
- [Unsplash](https://unsplash.com/)


# Acknowledgments
