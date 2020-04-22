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
        * [5. Wireframing & Proposed Functionality per Page](#5-wireframing--proposed-functionality-per-page)
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
    <img src="" alt="PHP Favicon">
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
This project was actually inspired by a friend of mine and his new venture as a local gym, that gym is called <a href="https://precisionhealthperformance.com/">Precision, Health & Performance</a> and they specialise in doing exactly what the name says. Their is already a commercial website in place and the color scheme for it is monotone in nature with color only added via images noted throughout the site. The guys at PHP were kind enough and offered me their commercially built website as my project medium. I noticed that although it was incredibly intricate and quite simple and pleasing on the eye it needed something to just separate the monotone coloring.

* ![#323232](https://placehold.it/15/323232/000000?text=+) `#323232` - Primary color
* ![#432344](https://placehold.it/15/432344/000000?text=+) `#432344` - Secondary color
* ![#ffc03d](https://placehold.it/15/ffc03d/000000?text=+) `#ffc03d` - Tertiary color
* ![#efeeee](https://placehold.it/15/efeeee/000000?text=+) `#efeeee` - Supplementary color

The primary color of ![#323232](https://placehold.it/15/323232/000000?text=+) `#323232` was used to denote key componentry used in the application such as the Navbar & Footer. It's almost charcoal grey color emulates the color of the knurling found in many modern barbells and it ultimately was only a hue percentage off the logo dominate color that it became the obvious choice.

The secondary color of ![#432344](https://placehold.it/15/432344/000000?text=+) `#432344` is used throughout the site as Primary call to actions, Login/Register buttons, Create Posts/Comment buttons etc and change hue and directional gradient when hovered & pressed. It is the introduction of monochromatic coloring in the website as multiple hues of lightening or darkening tints are used to create the animations and the gradients. It is also used in creating a very light hued version for the shadows on the neumorphic elements.

The Tertiary color of ![#ffc03d](https://placehold.it/15/ffc03d/000000?text=+) `#ffc03d` and again using monochromatic techniques are used for animating the navigational elements in the navbar & footer partial components, and also providing a bright contrast on some of the custom horizontal block dividers. They are also used to show the user via highlight the current page being viewed in the navbar.

Finally the Supplementary color of ![#efeeee](https://placehold.it/15/efeeee/000000?text=+) `#efeeee` is used as the default page body background and also as the font color used when contrast of black text is poor against the monochrome theme of the website, for example: the navigation list items in the navbar and footer.

##### 3. Logo
The logo was provided by Dean Roche, the owner of PHP as a complimentary gesture to help and aid me in the development of this site and the content within. Without this asset, I would of spent a lengthy period of time creating a logo to my liking.

<p align="center">
    <img src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/img/logo.png" alt="PHP Logo">
</p>

##### 4. Geometry

The applications geometrical aspects feature aesthetically modern components such as rounded edges and Neumorphism styling. Plenty of whitespace was used to allow the user to flick to important context and features much easier with little strain provoked in their eyes.

A rule of symmetrical grouping was used horizontally and the rule of thirds was implemented vertically on most pages where content would allow. For example, most pages feature a descriptive context for the user, a branding logo as separation but also to invoke that brand in the user's mind-eye when remembering from reference and the actual content necessary for that page.

Form inputs were kept label-less to keep with the Neumorphism trend and all form inputs use a placeholder as form label to still direct the user as to the information that the field requires. 

##### 5. Wireframing & Proposed Functionality per Page

Wireframing for this project began with Pen and paper as all my projects tend to start, but ultimately Wireframes were created using Balsamiq. Each page or view of the application was rendered as a wireframe in both Small and Medium-Large viewports to show the difference between the aesthetics and showing how the elements per page would react to differing viewport sizes. Each element planned out in this stage has made it into the physical build of the application with not much deviation occurring from the original wireframe plans.

* Base Template:

   The base.html parent template contained all the default components for each child template to inherit from. All links were provided to third party icon providers, frameworks, stylesheets and script links. The navbar & footer partial components were created in their own html files and inserted into the base.html via the Jinja `include` statement to ensure separation of concern could occur for ease of scalability of the application elements. 

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
   
   The home page also contains the `_alerts.html` partial to deliver success messaging to the User on Registration, Login & Logout.
   
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

   The .... 

   <details>
   <summary>Membership Template Wireframes</summary>

   <p align="center">
      <img height="350" src="">
   </p>

   <p align="center">
      <img height="350" src="">
   </p>
   </details>

***

* Registration Template:

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
      
   Defensive design is implemented in ensuring that usernames & emails used are unique aswell as ensuring that passwords 1 & 2 match. Coupled with the below jinja expression statement to check if a user is already logged in or not. If they are, we produce the `_error.html` partial indicating that they have attempted to navigate to this template in error and are potentially already logged in.
   
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
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Register.png">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Register.png">
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
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Mobile-Login.png">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/auxfuse/Milestone4/blob/master/Milestone4/static/wireframes/Ms4-Tablet-Desktop-Login.png">
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

