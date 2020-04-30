# Milestone Project 4
***
[![Build Status](https://travis-ci.org/auxfuse/Milestone4.svg?branch=master)](https://travis-ci.org/auxfuse/Milestone4)

## Table of Contents:
* [What does it do and what does it need to fulfill?](#what-does-it-do-and-what-does-it-need-to-fulfill)
* [Functionality of Project](#functionality-of-project)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Design](#design)
        * [1. Font](#1-font)
        * [2. Color Scheme](#2-color-scheme)
        * [3. Logo](#3-logo)
        * [4. Geometry](#4-geometry)
        * [5. Wireframing & Proposed/Implemented Functionality per Page](#5-wireframing--proposedimplemented-functionality-per-page)
* [Technology Used](#technology-used)
* [Database](#database)
* [Features](#features)
    * [Future Features](#future-features)
    * [Defensive Design](#defensive-design)
* [Testing](#testing)
    * [Found Bugs & Fixes](#found-bugs--fixes)    
* [Deployment](#deployment)
* [Credits](#credits)
    * [Special Thanks & Acknowledgements](#special-thanks--acknowledgements)

***

## Welcome to PHP Barbell!

<p align="center">
    <img src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/img/logo.png" alt="PHP Logo">
</p>

***

## What does it do and what does it need to fulfill?
This Milestone project creation is the culmination of learning and study from all modules of the Full Stack Developer Course, culminating in the creation of this Full Stack Framework Django project. This Application will allow an admin to store and manipulate data records and also allow users to create, read, update, delete & purchase memberships for this newly create local barbell club called, <a href="https://php-barbell.herokuapp.com/">PHP Barbell</a>.

<p align="center">
    <img src="https://raw.githubusercontent.com/auxfuse/Milestone4/master/Milestone4/static/img/favicon.ico" alt="PHP Favicon">
</p>

### Functionality of Project
The application uses Django 3 to encourage rapid development, by following a model-template-view architecture pattern. The project uses Separation of Concern amongst the applications to utilise the Django Framework effectively.

Alongside using Django, sqlite was used in the Project's inception phase as a test database for local testing. Sqlite is self-contained highly reliable, SQL database engine that features all the normal relational database management. Once I was ready I switch to using PostGreSQL (aka Postgres), for my Development Database to ensure that any data entered was visible in my deployed application. Postgres is open source and boosts a fully technical and easy to use Object relational database management system.

Using Django and the above Database methods an administrator for the application (in this case the owner of PHP Barbell), has complete access to a completely custom styled Admin dashboard where they can Create, Read, Update and Delete records in the each proposing application model if appropriate. For example: The owner access the admin dashboard to update staff records, which is a totally separate and completely custom Django application made specifically for this purpose.

The project is version controlled via Git & Github and is deployed via Heroku. All environment variables & secret variables are stored in an env.py file which is then held in a git ignored file to ensure project integrity is held to a high secure present day and project requirements standard.

[Back to top](#table-of-contents)

## User Experience:

#### User Stories:
_Generic (Guest/Public) User:_
* As a Generic User, I want to be able to view the site on any device I may have, (mobile/tablet/desktop).
* As a Generic User, I want to have the ability to register to the site.
* As a Generic User, I want to have the ability to research the business and anything associated with same through the application.
* As a Generic User, I want to have the ability to view the established Accessibility Statement & Privacy Policy if any.
* As a Generic User, I want to be able to view available Membership prices.
* As a Generic User, I want to be able to get in contact with the business owner through the website.
* As a Generic User, I want to have the ability to see the established social accounts coupled with the business, eg: Facebook, Instagram etc.
* As a Generic User, I want to have information available as to the directions of the business site.

_Registers (Logged in) User:_
* As a Registered User, I want to have the ability to Login to the site via my registered details.
* As a Registered User, I want to be able to view the Community Forum posts and interact and comment on same.
* As a Registered User, I want to have the ability to search through the Forum to find specific categorised Posts.
* As a Registered User, I want to be able to Create, Edit and Delete my own Forum Posts for discussion amongst the Community.
* As a Registered User, I want to have the ability to review membership options and but one.
* As a Registered User, I want to be able to view my Cart and any items I currently have awaiting payment in my Cart.
* As a Registered User, I want to be able to items currently added to my Cart.
* As a Registered User, I want to have the ability to Logout of the application.

_Application Owner/Administrator User:_
* As a Site Administrator, I want to be able to login to an administration panel.
* As a Site Administrator, I want to have the ability to update site content, such as Forum Posts, User details, Staff & Membership packages etc etc.
* As the Owner, I want to ensure any user navigating to my site has a positive User experience between content and responsive design to theming.
* As the Owner, I want to show any user navigating to my site the facilities, services & pricing available.
* As the Owner, I to showcase the new premises location on a map embedded into one of the public pages.

_Developer:_
* As a Developer, I want to demonstrate my growing abilities as a budding Full Stack Software developer during my time on the CI course.
* As a Developer, I want a project that I can proudly showcase to potential employers via my Github Repository.
* As a Developer, I want to create a project that is fully scalable and can be expanded upon as I continue to grow as a developer.

#### Design
I rather enjoy learning new ways to style my projects and I feel more and more that Front End Development and Design is my calling in this profession. Earlier this year I saw an article on the rising trend of Neumorphism in the industry and I was hooked. I knew from then that I was going to try and utilise this methodology in my final project as it really brings an application to life.

It is a by-product of recent trendsetting Skeumorphism which takes a material polish approach to creating good user experience. For example, using symbolism to portray an act or action, eg: the recycle bin icon or making a particular element's background have a textile styling that would be familiar to a User. But Neumorphism uses imaginary light sources and their respective highlights & shadowing from same to make the elements on show look as if they are still part of the background from which they are almost protruding or sinking into. It's nickname in the industry today is _**Soft UI**_. 

For this project, I imagined a light source installed in the top left corner of the webpage. This allowed me to visualise where the light would hit on these elements causing highlights and shadows. Then using the css property of `box-shadow` to impact the element based on the above to create the shadows & highlights necessary. This css property uses horizontal & vertical offsetting along with blur and spread and finally the color of the shadow itself to produce the desired effect.  

By using rounded edges on the components, eg: cards, and removing conventional borders entirely it allowed for some very creative visuals, almost as if it were one seamless plastic moulding being rendered for the user.

As an example of putting all of the above to use the following is the Login Form card with Neumorphism styles in place:

<p align="center">
    <img src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/neumorphismExample.PNG" alt="Neumorphism Styled Form">
</p>

##### 1. Font
The project has a main font of <a href="https://fonts.google.com/specimen/Roboto+Condensed">Roboto Condensed</a> which is used for primary texts and headers, and a secondary font of <a href="https://fonts.google.com/specimen/Lato">Lato</a>, both of which greatly complement each other throughout the site.
  
“Sans-Serif” is used as the default backup font in cases where these fonts have difficulty loading. "Roboto Condensed" consists of a dual nature, sporting a mechanical skeleton and character form is largely geometric, and at the same time featuring friendly and open curves. This allows for a more natural reading Rhythm more commonly found with humanist and serif fonts. This made it a clear choice in terms of primary font as the website ideology is that of natural form and geometric positioning.

 "Lato" is the secondary font used to compliment the primary font. Again, this typeface is of the serif family, contains classical proportions (particularly in upper case), but holds a strong structure providing stability and seriousness. It reads well alongside "Roboto Condensed" and ultimately was a great fit with the overall theme of the application.

##### 2. Color Scheme
This project was actually inspired by a friend of mine and his new venture as a local gym, that gym is called <a href="https://precisionhealthperformance.com/">Precision, Health & Performance</a> and they specialise in doing exactly what the name says. There is already a commercial website in place and the color scheme for it is monotone in nature with color only added via images noted throughout the site. The guys at PHP were kind enough and offered me their commercially built website as my project medium. I noticed that although it was incredibly intricate and quite simple and pleasing on the eye it needed something to just separate the monotone coloring. The theme of the site was light to begin with. It stayed this particular theme until very recently. As you can see from the the next few images, it had a soft UI neumorphism incorporated trend and it's color scheme incorporated these colors (or shade variants of same):

<details>
<summary>Original Light Theme of Application Example:</summary>

[![Image from Gyazo](https://i.gyazo.com/3a30228222f75f1a0ea2363aa860642a.gif)](https://gyazo.com/3a30228222f75f1a0ea2363aa860642a)

* ![#efeeee](https://placehold.it/15/efeeee/000000?text=+) `#efeeee` - Primary color
* ![#323232](https://placehold.it/15/323232/000000?text=+) `#323232` - Secondary color
* ![#432344](https://placehold.it/15/432344/000000?text=+) `#432344` - Tertiary color
* ![#ffc03d](https://placehold.it/15/ffc03d/000000?text=+) `#ffc03d` - Supplementary color
* ![#ff2525](https://placehold.it/15/ff2525/000000?text=+) `#ff2525` - Supplementary color 2
   
</details>

After attempting to implement a darkmode switch for this project, I had put in some amount of time creating the dark theme in a differing CSS file. The darkmode plan didn't work out, and is parked as a future feature for now, but after the darkmode theme got such a positive response from my Peers in Slack and from my test audience the color scheme was switched to that permanently. 

* ![#323232](https://placehold.it/15/323232/000000?text=+) `#323232` - Primary color
* ![#432344](https://placehold.it/15/432344/000000?text=+) `#432344` - Secondary color
* ![#ffc03d](https://placehold.it/15/ffc03d/000000?text=+) `#ffc03d` - Tertiary color
* ![#efeeee](https://placehold.it/15/efeeee/000000?text=+) `#efeeee` - Supplementary color
* ![#ec9e9e](https://placehold.it/15/ec9e9e/000000?text=+) `#ec9e9e` - Supplementary color 2

The primary color of ![#323232](https://placehold.it/15/323232/000000?text=+) `#323232` was used to denote key componentry used in the application such as the Navbar & Footer. It's almost charcoal grey color emulates the color of the knurling found in many modern barbells and it ultimately was only a hue percentage off the logo dominate color that it became the obvious choice. It is also the default background for the entire application. It allowed for a greater Neumorphism effect to be implemented over the light theme and ultimately really showed off this Modern design Trend and the presence of the Brand itself.

The secondary color of ![#432344](https://placehold.it/15/432344/000000?text=+) `#432344` is used throughout the site as Primary call to actions, such as the Login/Register buttons, Create Posts/Comment buttons etc and change hue and directional gradient when hovered & pressed. It is the introduction of some monochromatic coloring on elements in the website as multiple hues of lightening or darkening tints are used to create the animations and the gradients.

The Tertiary color of ![#ffc03d](https://placehold.it/15/ffc03d/000000?text=+) `#ffc03d` and again monochromatic techniques are used for animating the navigational elements in the navbar & footer partial components on hover, and also providing a bright contrast on some of the custom horizontal block dividers. It is used to show the user via highlight the current page being viewed in the navbar. And provides the background hover effect to denote the clickable action on a Forum Post or Membership Plan.

The first Supplementary color of ![#efeeee](https://placehold.it/15/efeeee/000000?text=+) `#efeeee` is used as the default font color and is easy on the eye for the user against the background Primary color above.

The second Supplementary color of ![#ec9e9e](https://placehold.it/15/ec9e9e/000000?text=+) `#ec9e9e` is used as a visual indicator for the user detailing warnings/error messages such as the Stripe errors, or permanent Call to actions such as deleting a Post or Clearing the Cart. This hue of the color red was used to improve the contrast ratio against the dark theme of the site allowing greater User Experience to take place.

##### 3. Logo
The logo was provided by Dean Roche, the owner of PHP as a complimentary gesture to help and aid me in the development of this site and the content within. Without this asset, I would of spent a lengthy period of time creating a logo to my liking. the logo itself was not only used as the Branding image in the Navbar but also used as a Horizontal Visual Page Break and is rendered on every template to ensure consistency throughout the application.

<p align="center">
    <img src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/img/logo.png" alt="PHP Logo">
</p>

##### 4. Geometry

The applications geometrical aspects feature aesthetically modern components such as rounded edges and Neumorphism styling. Plenty of whitespace was used to allow the user to flick to important context and features much easier with little strain provoked in their eyes.

A rule of symmetrical grouping was used horizontally and the rule of thirds was implemented vertically on most pages where content would allow. For example, most pages feature a descriptive context for the user, a branding logo as separation but also to invoke that brand in the user's mind-eye when remembering from reference and the actual content necessary for that page.

Form inputs were kept label-less to keep with the Neumorphism trend and all form inputs use a placeholder as form label to still direct the user as to the information that the field requires and maintaining the centrally aligned component Geometry found throughout the application. 

##### 5. Wireframing & Proposed/Implemented Functionality per Page

Wireframing for this project began with Pen and paper as all my projects tend to start, but ultimately Wireframes were created using Balsamiq. Each page or view of the application was rendered as a wireframe in both Small and Medium-Large viewports to show the difference between the aesthetics and showing how the elements per page would react to differing viewport sizes. Each element planned out in this stage has made it into the physical build of the application with not much deviation occurring from the original wireframe plans.

* Base Template:

   The base.html parent template contained all the default components for each child template to inherit from. All links were provided to third party icon providers, frameworks, stylesheets and script links. The navbar & footer partial components were created in their own html files and inserted into the base.html via the Jinja `include` statement to ensure separation of concern could occur for ease of scalability of the application elements. 
   
   The navbar partial template component contains all primary relevant navigation throughout the site. The navbar uses Bootstrap and the jQuery & Popper.js library to ensure it stays repsonsive and collapses into a toggler on medium screen sizes or less thus ensuring Mobile first design. The navigational items change depending on whether a user is logged in or not to ensure that the flow of the application is upheld. Each `nav-item` of the navbar highlights when the user navigates to a specific page, this is actually achieved through the view method of each template by passing the `active` class into the context of the render via an expression tag in the navbar, see example code; `{{ membership_page }}` passed into the class attribute actually renders as `active` when the view is in focus to the user:
   
   ```html
   <li class="nav-item {{ membership_page }}">
      <a class="nav-link" aria-label="Membership" href="{% url 'membership' %}">Membership</a>
   </li>
   ```
  
  The footer partial template component contains supplementary information pertaining to the website such as Privacy policy, Accessibility & Socials, and some information about myself as the Developer and it's intended use and purpose for `educational purposes`.

  Where appropriate, `block` statements were used for the Page titles, the main inheritance portion in the body and finally for any bespoke scripts that needed to be loaded on specific pages.
  ```html
  {% block content %}
  {& endblock %}
  ```

   <details>
   <summary>Base Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Base.png" alt="Base template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Base.png" alt="Base template tablet-desktop wireframe">
   </p>
   </details>

***

* Home (Index) Page:

   The home (Index) page is our primary landing page and has two call to actions based on whether a User is logged in or not. If they are not logged in the two call to actions are to Register/Login. This is essential to our users as we want to ensure high numbers of first time visitors register for the site and that all recurring registered users have multiple places to login from.
   
   If the user is already logged in the content of the call to action cards change to reflect the logged in status. This time around notifying the user of the Forum and Membership pages. This change was implemented after the wireframes were created due to a defensive design issue where it was unnecessary to show a user registration/login if they already have logged in, and as such does not appear in the wireframes.
   
   The home page also contains the `_alerts.html` partial to deliver success messaging to the User on Registration, Login & Logout aswell as any error messages to be displayed to the user when attempting to access restricted content as an example.
   
   The home page contains a custom javascript element in the form of the Hero image typewriter animation. This custom js function was separated into it's own javascript file and then it was injected via the jinja statement block tags added in the `base.html` template to ensure that this file only runs when the index template is rendered.

   <details>
   <summary>Home (Index) Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Index.png" alt="Home (Index) template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Index.png" alt="Home (Index) template tablet-desktop wireframe">
   </p>
   </details>

***

* About Page:

   The About page features information regarding the Barbell club. The coaches section is rendered directly from the coaches app and model. The owner/administrator of the website has the ability to add/edit or remove coach/staff information, which will appear in this section for users to see.
   
   This page also hosts a carousel to showcase the Facility and the Facility being used by members of the Gym. This is a staple integration of marketing techniques as it shows the facility in use. The Carousel code is referenced from the Bootstrap Framework and using custom CSS ensures that the images held within and displayed in the component maintain there aspect ratio proportionally throughout the applications responsive behaviour from mobile devices and up. A snippet of the css is shown here:
   
  ```css
  .carousel img {
      object-fit: contain;
      margin: 1rem 0;
      height: 400px;
      min-width: 100%;
      max-width: none;
  }
  ```
   
   As well as the carousel to promote the Facility, I wanted to implement an interactive map to display to the user how easy it was to find the premises and how central it was to the City. Using Leaflet.js it was quite easy to embed a map into the `about.html` template, which was suggested to me by <a href="https://github.com/TravelTimN">Tim Nelson</a>, who during his time as Interactive Frontend Lead in Slack had done an extensive set of documentation on using the JavaScript Library as well as providing an example project to reference again. The documentation and example site can be found <a href="https://github.com/TravelTimN/ci-ifd-lead/tree/master/week4-leafletjs">Here</a>. Using Leaflet.js over Google Maps considerably reduced my work time in implementing the function, including but not restricted to not having to set an API key to set up the map itself and using a bespoke map tile provider in the form of ArcGIS. The map is responsive thanks to Bootstrap's utilisation of the Grid and a custom map marker was added in keeping with the Brand of the application and business. This custom js code was separated into it's own javascript file ensuring separation of concern and then it was injected via the jinja statement block tags added in the `base.html` template to ensure that this file only runs when the about template is rendered. 

   <details>
   <summary>About Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-About.png" alt="About template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-About.png" alt="About template tablet-desktop wireframe">
   </p>
   </details>

***

* Membership Template:

   This template is comprised of some context pertaining to the services offered with membership options, branding throughout and an image to break up the flow of the page a bit. Each payment plan detailed on this template can be controlled by the Admin in the Admin panel of the site, but for examples sake of the project submission, 3 Membership Plans have been created and displayed. 
   
   These plans are returned to the template by querying the database table "Membership" and grabbing all the available objects within. A filter was placed on this aswell to ensure the cheapest options were placed on the left of the screen, or on top for mobile and then in ascending order by price.
   
   ```python
   memberships = Membership.objects.all().order_by('price')
   ```
  
  The wireframe initially had a button to add a plan to the Cart but during application development I utilised the anchor element & empty span method combo as detailed previously to add a cart to the user. Users can only add a plan to a cart if they are logged in, or if they are logged & their cart is empty. This idea behind this is that as these plans are monthly subscription based it was to ensure a user would never buy multiple plans for the forthcoming 30-day period. A user can re-buy a Plan at their leisure right now in separate transactions, with a future implementation being they can only buy one plan in any 30-day period.
  
  When a plan is in the cart, the anchor & empty span link is removed via a jinja template expression checking for the total price of the cart is greater than 0, as well as swapping out the helper text located at the bottom of each membership plan card. This acts as a small defensive element so a user cannot add more than one plan to the cart at any one time. There are also defensive measures added to the `add_to_cart` function as part of the cart app that we will take about later. If a user attempts to add a plan to a cart while the cart already has a plan added or if the user is not logged in, an error message to suit each action is thrown. Otherwise, a success message is thrown to the user detailing successful addition to cart.

   <details>
   <summary>Membership Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Membership.png" alt="Membership template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Membership.png" alt="Membership template tablet-desktop wireframe">
   </p>
   </details>

***

* Register Template:

   The Registration template contains some directional text, the brand image to break up the page a bit and the Registration Form. As with the Login form below, the Registration form is created as a class and is a built-in form from <a href="https://docs.djangoproject.com/en/3.0/topics/auth/default/#module-django.contrib.auth.forms">Django Contrib Auth ~ UserCreationForm</a> and was created using reference from the Django documentation linked.
   
   By default the `UserCreationForm` has 3 fields, username, password1 and password2. As planned for this project I also added fields for First Name, Last Name and Email to be captured and added to the User table in the database. All fields are required and a user cannot register by leaving any of the fields blank. Labels are excluded from the Registration form in keeping with the clean aesthetic of the application and in keeping with common design trends of late. Placeholders are used in-place of labels and this theme is consistent throughout all form fields rendered in the application.
   
   The original helper text that accompanies the `UserCreationForm` has been excluded also as it added an unnecessary dis-pleasing aesthetic to the form that personal preference from myself did not like, I also asked several of my peers for their direction with this design approach and it was positively received. Removing the helper text proved problematic at first but using <a href="https://stackoverflow.com/questions/13202845/removing-help-text-from-django-usercreateform">this post</a> from StackOverflow gave me the answer needed. As the original fields of the `UserCreationForm` had `username` as the default autofocus field, I also used the same dunder init method to set the default autofocus to the First Name field.
   
   ```python
  """Disable help text of User Creation Form & set default autofocus to 
   first_name."""
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for fieldname in ['username', 'password1', 'password2']:
           self.fields[fieldname].help_text = None
       self.fields['first_name'].widget.attrs['autofocus'] = True
       self.fields['username'].widget.attrs['autofocus'] = False   
   ```
   
   During Peer-code-review of my project it was pointed out that a User could register with a Password of 1 character. This was an unintended consequence of extending the UserCreationForm class and thanks to Peer and Fellow student, <a href="">Johan de Leeuw</a> for pointing out that my view and method of checking for defensive supports in the view were flawed. Using the `.is_valid()` method to ensure the UserCreationForm's built-in validators worked did the trick and ultimately allowed me to compress and refactor my code easily. I used the <a href="https://docs.djangoproject.com/en/3.0/ref/forms/validation/#form-and-field-validation">Django docs for Form & field validation</a> as provided by Johan to help me implement the method.
      
   Additional Defensive design is implemented in ensuring that emails used are unique by using the `clean_<fieldname>()` method directly in the Form class. Coupled with the below jinja expression statement to check if a user is already logged in or not. If they are, we produce the `_error.html` partial indicating that they have attempted to navigate to this template in error and are potentially already logged in.
   
   ```html
   {% if user.is_authenticated %}
        {% include 'partials/_error.html' %}
   {% else %}
        <!-- Render normal Login template html -->
   {% endif %}
   ```
  
  Lastly, to ensure users are met with the appropriate flow of the application, if they have already registered there is a link directing them to the `login.html` template which is available just under the "Register" button on the form.

   <details>
   <summary>Registration Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Register.png" alt="Register template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Register.png" alt="Register template tablet-desktop wireframe">
   </p>
   </details>

***

* Login Template:

   The Login Template is simple, some text, the brand image to break up the page a bit and the login form. The login form itself is generated via a Django Form class. It takes two fields, Username & Password. It checks the username submitted versus the list of Registered users to the site which is held via the PostGres Database, and the password for that user. If both are met entry to the application is permitted. If not, an error alert is displayed detailing that login details were submitted incorrect, and that is produced by passing a message to be stored in the Django Messages Framework and outputting same to the included partial `_alerts.html` on the `login.html` template.
   
   As with the registration page, defensive design elements are achieved in the login template itself using Jinja expression syntax to produce the `_error.html` partial template instead of the default `login.html` template if the expression returns `True` meaning the User is already logged into the application. This step is crucial in maintaining that a user cannot attempt to login multiple times resulting in poor User Experience of the site.

   Lastly, in an attempt to direct users to the appropriate section of the application, included under the form "Submit" button is a link to the Registration page allowing users who have yet to register for the application navigate to same and register.
   
   <details>
   <summary>Login Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Login.png" alt="Login template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Login.png" alt="Login template tablet-desktop wireframe">
   </p>
   </details>

***

* Accessibility Template:

   The Accessibility template is a completely static page. It encompasses the use of the card component from the Bootstrap framework as it is inherent throughout the site. It is a secondary accompanying page to the application that professional brands and established businesses will have included. The content within was obtained from Dean Roche, the owner of Precision Health Performance as an added asset when approached on the subject of what I could use for my project. 

   <details>
   <summary>Accessibility Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Accessibility-Statement.png" alt="Accessibility template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Accessibility-Statement.png" alt="Accessibility template tablet-desktop wireframe">
   </p>
   </details>

***

* Privacy Policy Template:

   As with The Accessibility template, the Privacy Policy is a completely static page. It encompasses the use of the card component from the Bootstrap framework as it is inherent throughout the site. It is a secondary accompanying page to the application that professional brands and established businesses will have included. The content within was obtained from Dean Roche, the owner of Precision Health Performance as an added asset when approached on the subject of what I could use for my project. 

   <details>
   <summary>Privacy Policy Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Privacy-Policy.png" alt="Privacy Policy template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Privacy-Policy.png" alt="Privacy Policy template tablet-desktop wireframe">
   </p>
   </details>

***

* Cart Template:

   The cart template is only accessible to those who have logged in, and shows a user if the cart has something to checkout or not. If it is empty and the user navigates to this template, some helpful short text is displayed to the user detailing same. If the cart has had a plan added to it, then the Cart will display that plan and also a small asterisk symbol will appear in the Navbar alongside the `Cart` Nav-item. For as long as the user is currently logged in, without checking out or clearing the basket, this asterisk symbol will persist, highlighted in yellow across all pages.
   
    If the user wants to checkout, then clicking on the checkout button displayed in the cart card will navigate the user onto same, however, as with the edit-post.html template, a two factor visual cue delete is in play. When a user clicks on `Click here to Clear Cart`, a dialog box slides open with some warning text as to the permanency of this action. If the user wants to continue, a final click on the `Clear` button will clear the cart and navigate the user back to the membership template. As the cart is now clear, the asterisk also disappears from view denoting to the user that their cart is empty.

   <details>
   <summary>Cart Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Cart.png" alt="Cart template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Cart.png" alt="Cart template tablet-desktop wireframe">
   </p>
   </details>

***

* Checkout Template:

   The checkout template is only accessible to a logged in user, and if a Cart has had an item added to it and then if the user has selected to Checkout that Cart. It will detail the currently selected plan for checkout as a secondary visual inspection for the user to ensure they are getting exactly what they want. And it will also have the Payment form. The Payment details form rendered on the checkout.html template is comprised of two seperate Django forms. One for capturing the Payment details pertaining to the card being used and the other to capture the necessary information for the Order.
   
   There are multiple defensive elements at play for this particular form, from ensuring that the user cannot leave any fields blank to ensuring the correct length of digits is entered for the Credit Card No. & CVV number.
   
   Once a user clicks to buy, and if successful payment is made, the user is redirected back to the Memberships page displaying a success message, and the cart is cleared. If there are any errors detected on submission, the Stripe Error messages will appear detailing the found error, or the normal HTML field warnings will show per field if a field is left blank etc.   

   <details>
   <summary>Checkout Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Checkout.png" alt="Checkout template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Checkout.png" alt="Checkout template tablet-desktop wireframe">
   </p>
   </details>

***

* Forum Template:

   Being the forefront page for the Forum itself, the Forum template utilises multiple call to actions. User can only navigate and use any of the functionality of the Forum after they Login. If an attempt to navigate to the Forum is made without Logging in first, the check of `user.is_authenticated` returns False and renders the `_error.html` partial instead, otherwise the normal flow of the page is rendered and exposes the functionality within to the logged in User. The primary cta for this page is to Navigate a user to create a Post.
   
   Included in this template is also a Fitlering system. This is a single field form with a select element containing all the possible categories a Post could be. A user cannot submit a filter request without ensuring a category is selected beforehand, and if an attempt to do so is made an error alert is displayed via the `_alerts.html` partial template embedded in the template. The categories in the select field are rendered via a jinja expression `for` loop, which has been passed to the template in the context of the form view function. We check for both key and value of the key-value pair of the categories and render the `{{ value }}` of the category to the user in the template, while the `{{ key }}` is the check in our function that we pass into our querset when rendering the `filtered-posts.html` template.

   ```html
   {% for key,value in categories %}
        <option value="{{ key }}">{{ value }}</option>
   {% endfor %}
   ```
  
  The physical user posts are rendered on the page in Ascending Date Order, meaning that the most recent post will be rendered first and the oldest post will be last. If there are no posts to display, a small helper text is displayed to the user detailing same. Each Post is rendered with an anchor element and blank span overlaid over the Post Card, and when clicked will trigger the function view `view_post` and navigate the user to view that particular post in it's entirety and any comments it may have etc.
  
  As this page is the repository for all Posts made, the page is capped at '6' posts before switching to a Paginated view to ensure that the `never-ending` scrolling scenario is not a feature of the design. Pagination is implemented and custom styled inline with the Application's theme and branding prevalent throughout, and using Pagination keeps User Experience at a maximum.

   <details>
   <summary>Forum Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Forum.png" alt="Forum template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Forum.png" alt="Forum template tablet-desktop wireframe">
   </p>
   </details>

***

* Create Post Template:

   Navigation to the Create Post Template is locked behind an initial check to ensure that the user is first logged in. If not logged in, as with other similar pages, the `_error.html` partial will display instead of the normal page flow for when a user is logged in. The form itself is generated as a Django Form class and comprises of several input fields of `Post title`, `Post Details` and `Post Category` for the user to detail and two that populate on Post Submission of `Date Posted` and `Post Originator`.
   
   As detailed in the Database Schema, the `Date Posted` is autopopulated to the current date/time of the post submission and the `Post Originator` is a foreign key into the Users table to get the current Logged in User. The `Post Category` field choices are imported from the `categories` dict available in the models.py file of the app.  
   
   Each visible form field to the user has the required attribute assigned to them in the forms.py class Form `CreatePost`, including the Select Dropdown field of `Post Category` using the following dunder init method, which was needed as the Select widget attributes can only be set this way due to the nature of the choices import:
   
  ```Python
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['category'].widget.attrs['class'] = 'form-control'
    self.fields['category'].label = ''
    self.fields['category'].required = True 
  ``` 
  
  Upon successful creation of a post, the user is navigated back to the `forum.html` template and a success message is rendered detailing the successful action.

   <details>
   <summary>Create Post Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Create-Post.png" alt="Create Post template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Create-Post.png" alt="Create Post template tablet-desktop wireframe">
   </p>
   </details>

***

* Filtered Posts Template:

   This template returns a filtered queryset of Posts dependent on the category selected by the user on the `forum.html` template. If no posts are available for that category, a small amount of text is detailed to the user to show same, otherwise the posts for the queryset are rendered with pagination in tow to ensure that similar design standards are concurrent throughout the application and saving on vital visual real estate of the page.
   
   As with the `forum.html` clicking on any of the posts returned in the queryset rendered will navigate the user to the `view-post.html` template to view, comment, and access the edit/delete settings for the post if they own same.

   <details>
   <summary>Filtered Posts Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Filter-Posts.png" alt="Filter Posts template mobile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Filter%20Posts.png" alt="Filter Posts template tablet-desktop wireframe">
   </p>
   </details>

***

* View Post Template:

   Navigating to the `view-post.html` template can be achieved once a user is logged into the system and has clicked on any post in the `forum.html` or `filter-posts.html` templates. As with all other templates, we still check to ensure that a user is logged in before rendering the normal flow of the view, if a user is not logged in and attempts to gain access to this page, the `_error.html` template partial is rendered instead.
   
    If the user who is currently logged in clicks to view a post that they are the originator for, there is extra functionality added to the `view-post.html` template. There is some additional helper text along with a <a href="https://fontawesome.com/icons/cog?style=solid">Font Awesome Icon</a> of a Cog-wheel to denote how to access the post for editing/deletion.
    
    If the user who is currently logged does not own the post they are currently viewing then the Post renders without the originator functionality. The template itself plays host to some common elements shared between the types of users. For one, the `post originator` is displayed in the page-title at the top of the page and the entire post is displayed in a card, with the `title`, `post details`, `category` and `post date`.
    
    Comments are displayed under the brand image, and is paginated to 8 comments per page. Each comment is separated into their own card and has a differing color box-shadow to contrast the comments against the Post itself of ![#ff2525](https://placehold.it/15/ff2525/000000?text=+) `#ff2525`. This is against what was planned in the wireframes but after seeing both stand-points I settled on this layout as it kept the content to the top portion of the view and the call-to-action add comment section to the bottom portion.
    
    The comment field is a single field for the user to add their comment details for the post and the model comprises a total of 4 fields, 3 of which are auto-populated on submission of a comment, `date_commented` which is set to the current datetime, a foreign key to the users table for the `commenter` field and then another foreign key into the Post table linking the comments to the current respective `post`. When a comment is added to the Post it is automatically added to the top of the list of comments, with the user redirected back to the same `view-post.html` template and a success message relayed to the user detailing the comment being added to the Post.
    
   <details>
   <summary>View Post Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-View-Post.png">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-View-Post.png">
   </p>
   </details>

***

* Edit Post Template:

   Access and navigation to this template is locked behind several defensive design elements. Firstly in the template itself we are checking to ensure that the user is logged in before attempting to navigate to this template, as before, if not logged in the `_error.html` partial template is rendered in place of the normal flow of the template. 
   
   Then as previously mentioned on the `view-post.html` template the icon `cog` to access the `edit-post.html` template is also hidden unless the currently logged in user is equal to the `post originator`. And even then any attempt to navigate to the `edit-post.html` template via a URL browser injections is met with a check on whether or not the currently logged in user is the Post originator, if not, then the user is redirected to the `index.html` template with an error message displayed to the user that they are not the owner of that post.
   
   When a user is the Post originator, the `edit-form.html` template renders with the `CreatePost` form and any values that it previously had originally via passing the `instance=post` keyword argument, in the form fields for editing. The only fields that can be edited are the same three fields visible to the user when creating a Post, `title`, `post_text` and `category`. When clicking Update the record will save the details to the database and redirect the user back to the `view-post.html` template with a success message displaying to the user of the update.
   
   The `edit-post.html` template also contains the only user delete function for a particular post. As a permanent irreversible action this action is behind a two-check and dual-confirmation in the form of a user needs to click on `Delete Post` link first which expands out a warning dialog under the `edit-post` form and then click a second highly contrasted in warning color of the supplementary color #2 ![#ff2525](https://placehold.it/15/ff2525/000000?text=+) `#ff2525` to delete the post. Once the post is deleted the user is redirected back to the `forum.html` template with a success message as to the action just performed. Again as with each element of the Forum, there is a check in place to ensure that the currently logged in user is the `post.originator`, if not or a user somehow manages to not be logged in, they are redirected back to the `index.html` template with an error message returned and displayed via `_alerts.html` partial. 

   <details>
   <summary>Edit Post Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Edit-Post.png">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Edit-Post.png">
   </p>
   </details>

***

[Back to Top](#table-of-contents)

## Technology Used

#### Languages, Frameworks, Editors & Version Control:

* HTML, CSS & Python ~ core languages used to create this multi-page CRUD application.
* <a href="https://getbootstrap.com/"> Bootstrap Framework</a> ~ Used as the core structuring layout for the application, ensuring mobile-first design and screen size fluidity.
* Bootstrap's <a href="https://getbootstrap.com/docs/4.3/getting-started/introduction/#js">Imported Javascript & JQuery</a> ~ For the Modal and Responsive Navbar expand & collapse functionality.
* <a href="https://www.jetbrains.com/pycharm/">PyCharm IDE</a> ~ PyCharm was used as the preferred IDE for this project.
* PyCharm built-in Terminal ~ Used to commit to local repository and further push to Github Repo ensuring adequate version
controlling throughout the life-cycle of the project build.
* <a href="https://git-scm.com/">Git</a> ~ Installed on local device and integrated to PyCharm as a Plugin to enable version controlling.
* <a href="https://github.com/auxfuse/Milestone1">Github</a> ~ Used to host the repository of all previous versions of the build and linked to Heroku to push the latest changes to the deployed build version held there.
* <a href="https://www.heroku.com/">Heroku</a> ~ A cloud platform as a service enabling deployment for this CRUD application.

#### Tools Used:

* <a href="">PostgreSQL</a> ~ A free and open-source relational database management system emphasizing extensibility and technical standards compliance. Designed to handle high range of workloads including Web services with many concurrent users.
* <a href="https://mycolor.space/">ColorSpace</a> ~ Used to find complimentary color schemes used throughout the application.
* <a href="http://eye-dropper.kepi.cz/">Eye Dropper (Color Picker)</a> ~ Open Source Google Chrome Extension used to obtain hexadecimal/rgba/hsl values of colours. Built by Kepi (<a href="https://github.com/kepi">Kepi's Github</a>)
* Google Chrome DevTools ~ Used to test the application's functionality, the responsiveness of same, and the CSS visualisation, as well as assisting in such tasks as figuring out the correct style properties to override Bootstraps user agent styling.
* <a href="https://balsamiq.com/">Balsamiq</a> ~ Used for the creation of my pre-build wireframes showing the main elements and differences in size of same through small to large screen sizes.
* <a href="https://realfavicongenerator.net/">Favicon Generator</a> ~ Used to create favicon from custom Logo I created for the project.
* <a href="https://validator.w3.org/">W3C HTML Validator</a> & <a href="https://validator.w3.org/">W3C CSS Validator</a> & <a href="https://jshint.com/">JSHint</a> ~ Used to check the validity and efficiency of my code.
* <a href="https://autoprefixer.github.io/">Autoprefixer CSS Online</a> ~ Used to check for possible webkits required in the applications stylesheet ensuring Cross-browser support.
* <a href="http://pep8online.com/">PEP 8 Online Validator</a> ~ to check my python code to be consistent with PEP8 requirements.
* Adobe Photoshop ~ to create the custom long and short variations of the Logo for this application.
* <a href="https://fontawesome.com/icons?d=gallery">Font Awesome Icons</a> ~ For social icons used in Footer.

## Database

#### Database Schema:

Detail the db schema here....images, thoughts behind fks etc

## Features

The project boasts several key features:
* Create: ...

[Back to Top](#table-of-contents)

#### Future Features:

* Detail future implementations here...

#### Defensive Design

Defensive design for this application was...

* On registration & login functions, several defensive elements are at play. Between checking the unique fields are in fact unique, to testing if the user is logged in already when attempting to get to both of these views via a browser url injection. Error messaging and the use of a partials components work in conjunction with each other to detail to the user the type of error they have.
    
    For example, if a user is already logged in, and attempts to acces the login page via `https://php-barbell.herokuapp.com/accounts/login` they are met with a custom partial `_error.html` template and an error message within detailing that they are already logged in and to use the navigation elements in the navbar to return to the normal flow of the site.

## Testing

Testing was ...

#### Found Bugs & Fixes:

During manual testing...

1. When implementing Travis (at the inception of my project), I ran into a rather bespoke bug whereas the build would not pass even though I had what seemed to be the correct code (see below):
    ```yaml
    language: python
    python:
      - "3.8"
    # command to install dependencies
    install:
      - "pip3 install -r requirements.txt"
    # command to run tests
    script:
      - SECRET_KEY="whatever" ./manage.py test
    ```
   The error appeared in the logs whenever the script would attempt to run and pass the secret_key. With help from <a href="https://github.com/10xOXR">Chris Quinn</a> in the <a href="https://code-institute-room.slack.com/archives/C7HS3U3AP/p1583432481074600">Slack Full Stack Frameworks</a> channel, I was able to rectify this issue thanks to his guidance. Chris also explained to me the reason why this was happening. It is down to a default linux permission of 644 being set on my basic `./manage.py` meaning it is not executable via the script. Changing this to `python manage.py test` allowed Python to call and run the file circumventing Travis now potentially enforcing file permissions when testing builds. 

2. When developing the Privacy Policy & Accessibility Statement templates, I encountered a strange visual bug where overflow-x was persistent even though the flow of the code followed the Bootstrap structure to the letter, `container > row > col`. This was caused by my use of auto margin on the `.content` section element. I was using margin to push the content down away from the navbar as this project uses a sticky property to fix the navbar to the top of the viewport at all times, regardless of scroll position. After a lengthy period of time debugging and turning to Slack for help, <a href="https://code-institute-room.slack.com/archives/C7HS3U3AP/p1583710151076600">Simen Daehlin</a> pointed out the issue could be potentially coming from my `.content` css code block of:
    ```css
    .content {
        margin: 77px auto 0;
        -webkit-box-flex: 1;
                -ms-flex: 1;
                    flex: 1;
    }
    ```
   After which I turned my attention to the code block in question and using devtools was able to narrow down my search to the left and right auto margin property being the culprit. For some reason it was causing the site and the actual components injected inside the block content to no longer be responsive. Removing the `auto` value rectified this visual bug.
  
3. Text here.....

[Back to Top](#table-of-contents)

## Deployment

Detail deployment here...

[Back to Top](#table-of-contents)

## Credits

* <a href="https://github.com/10xOXR">Chris Quinn</a> ~ For his guidance and solution on setting up Travis correctly. <a href="https://code-institute-room.slack.com/archives/C7HS3U3AP/p1583432481074600">Link to solution</a>.

[Back to Top](#table-of-contents)

#### Special Thanks & Acknowledgements:

* Those in Slack, Tutor Support and my Mentor Spencer Barriball for assisting with me with countless queries since starting on this journey until now.

###### <i>Disclaimer: This project was created for educational use only as part of the Code Institute Full Stack Software Development Course for Milestone 4 Grading!</i>

[Back to Top](#table-of-contents)

<p align="center">
    <img src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/img/logo.png" alt="PHP Logo">
</p>

# Notes: Delete before submission

- default coach image obtained from https://static.thenounproject.com/png/363639-200.png and is a free to use vector download from the noun project.

- Flickr used to host images and then using urlfield in model to pass it to the template img src attribute for the admin of the website to update the coach information.

- Success cards in Stripe V2 Test get accepted even if a
CVV field is left blank. This was brought to the attention in
a Slack Thread after I had found that what should of been an
incorrect card number length of 12-digits (424242424242) was
allowing skipping the try block in our views.py file in the
checkout app. Link to slack post:
https://code-institute-room.slack.com/archives/C7HS3U3AP/p1587987242043500
After more defensive steps taken in the forms.py file of the checkout app,
they were also deemed insufficient to stop this from happening, so with
thanks to Slack user DaveL for pointing out the correctional defensive measures
should be made in the stripe.js file to suit.