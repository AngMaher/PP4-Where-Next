# Where Next?

## About

This website is a Travel Blog, a travel blog with a difference. There are lots of different blog articles to read to inspire your next adventure. 
Not only that! You can set up your own private Travel Bucket List, and also plan how to make each one a reality!!

The User has access to all the blogs on the site, once registered and logged in, they can interact with the each blog by liking and commenting. 

This site also allows them to store their very one Travel Bucket List, They can:
  - Create new items on their list.
  - Edit any of their ideas.
  - Delete any they longer want to achieve.
  - Mark off as done, when they have completed them.
  
Then they can take it a little further....
For each Item on their Bucket List, lets say "Want to travel to Rome". They can:
  - Add extra content. This is to make their wish into a reality and plan their trip. Any images they find, or links to hotels, flights etc. 
  Any information they come across can be stored here. Or a list of items they need to buy etc. Its like an online mood board 
  - They can view their plan, without going into edit mode, to see their plan come together.


You can find the live appliaction here: <a href ='https://pp4-where-next.herokuapp.com/'>Where Next?</a>

![Am I responsive](/media/readme/amiresponsive.png)



## Table of Contents

- [User Experience](#user-experience)

  -[Wireframes](#wireframes)

  - [Colour Scheme](#colour-scheme)

  - [User Goals](#user-goals)

  - [Developer Goals](#developer-goals)

- [Logic and Features](#logic-and-features)

  - [Logic](#logic)

  - [Database Structure](#database-structure)

  - [Features](#features)

    - [main menu](#main-menu)

    - [Player Menu](#player-menu)

    - [Enter Player Details](#enter-player-details)

    - [Delete a Player](#delete-a-player)

    - [List of Outstanding Fees](#list-of-outstanding-fees)

    - [Pay Fees](#pay-fees)

    - [Check Kit Sizes](#check-kit-sizes)

    - [Raffle Menu](#raffle-menu)

    - [Finishing Screen](#finishing-screen)

- [Technology](#technology)

  - [Lanuages Used](#languages-used)

  - [Software Used](#software-used)

  - [Python Libraries/Modules](#python-librariesmodules)

- [Testing](#testing)

  - [Validation](#validation)

    - [PEP8CI](#pep8)

  - [Manual Testing](#manual-testing)

  - [Bugs/Known Issues](#bugsknown-issues)

- [Deployment](#deployment)

  - [Git and Github](#git-and-github)

  - [Deployment to Heroku](#deployment-to-heroku)

- [Future Development](#future-development)

- [Credits](#credits)

- [Acknowledgements](#acknowledgements)


## User Experience

I wanted to keep the design clean, clear and simple to show a contempary and uncluttered design.  The site is mainly off white for the background and blue a colour to premote travel.

### Wireframes

![blog page](/media/readme/blogview.png)
![blog content](/media/readme/blogcontent.png)
![bucketlist](/media/readme/bucketlist.png)
![sign-in page](/media/readme/signin.png)

### Colour Scheme

I decided to keep the website bright with a main colur of blue throughout the site. 

  - #343434 - Jet, this colour is used a on the majority of the text throughout the site, and the footer.
  - #5799E1 - Blue, this is used on many features, buttons and highlighting links etc.
  - #FDF8F4 - Off white, this is used as the main background colour of the site.
  - #E64141 - Orange, this colour is used for the many massages.


![colours used](/media/readme/Where-Next-Colours.png)

I used [coolors.co](https://coolors.co/343434-5799e1-fdf8f4-e64141) to pick my colours.

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
    --main-blue: #5799e1;
    --dark-gray: #343434;
    --background-colour: #fdf8f4;
    --messages: rgb(230, 65, 65, 0.6);
}
```


## Agile 

### The Ideal User/Persona



**Who**

**What**:

**Why**: :

### User Goals
  - As a Site User I can view a list of posts so that I can choose which post I want to view. `(MUST HAVE)`
  - As a Site User I can create and account so that Extend the features of the website to comment/like and create my own bucket list. `(MUST HAVE)`
  - As a Site User/ Admin I can view likes on posts so that I can see which posts are popular. `(MUST HAVE)`
  - As a Site User I can comment on a post so that I can feel part of the conversation. `(MUST HAVE)`
  - As a Site User I can create my own bucket list so that I can keep track of goals. `(MUST HAVE)`
  - As a Site User I can edit and delete items from my bucket list so that I can interact with the list. `(SHOULD HAVE)` `(MUST HAVE)`
  - As a Site User /Admin I can view comments on an individual post so that I can read the conversation. `(MUST HAVE)`
  - As a Site User I can like/unlike posts so that I can interact with the content. `(SHOULD HAVE)`
  - As a Site User I can mark of what I have achieved on my bucket list so that I can see my progress. `(COULD HAVE)`
  - As a Site User I can view an more detailed version of the post so that I can read the article in full. `(MUST HAVE)`
  - As a Site User I can create a mood-board/plan for each item on my bucket list so that I have a place 
      to store all the details I need to make my goal a reality. `(SHOULD HAVE)`
  - As a Site User I can View mood-board/plan so that I can view my plan so far without having to go into edit mode. `(SHOULD HAVE)`
  - As a Site User I can call up all blogs for a certain category so that I can filter the blogs to my needs `(SHOULD HAVE)`

### Developer Goals

 - As a Site Admin I can create, read and delete posts so that I can manage my blog content. `(MUST HAVE)`
 - As a Site Admin I can approve and disapprove comments so that I can filter out objectionable comments. `(SHOULD HAVE)`
 - As a Site Admin I can create draft posts so that I can finish writing the content later. `(SHOULD HAVE)`
 - As a Site Admin I can access the admin from a link on the web page so that I have easier access. `(SHOULD HAVE)`
 - As a Site Admin I can filter the comments by approved and not approve so that I can have a list of all unapproved comments together `(MUST HAVE)`
 - As a Site Admin I can search through posts, comments and Bucket List Items so that I can find what I am looking for with ease `(MUST HAVE)`

 ### Goals not completed

 - As a Site User I can save a post onto my account so that I can have a list of the most relevant posts to read later `(COULD HAVE)`





## Logic and Features

### Logic


### Database structure


### Features




## Technology

<img height="50" src="docs/readme/python_django.png">  <img height="50" src="README/elephantsql.png">  <img height="50" src="README/cloudinary.png"> <img height="50" src="README/html.png">  <img height="50" src="README/css.png">  <img height="50" src="README/bootstrap.png">  <img height="50" src="README/js.png">  <img height="50" src="README/gitpod.png">  <img height="50" src="README/github.png">

### Languages Used

- [HTML](https://www.w3schools.com/html/) - Used for the main site.
- [Markdown](https://www.markdownguide.org/cheat-sheet) - language used to write README and TESTING documents.
- [CSS](https://www.w3schools.com/css/) - Styling language, used for the styling of the website.
- [Python](https://www.python.org/) - high level programming language, used of the back end programming language.


### Software Used

- [LucidChart](https://lucidchart.com) - LucidChart was used to create flowchart for the project.
- [Git](https://git-scm.com/) - Git was used for version control by using the Gitpod terminal to commit to Git and push to Github.
- [Github](https://github.com/) - Github was used to write and store the projects code.
- [Google Sheets](https://www.google.com/sheets/about/) - Used to store all the data from the program.
- [Heroku](https://www.heroku.com/home) - Heroku was used to deploy the project.
- [Text ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - Used to create the logo for the project.

### Python Libraries/Modules

- [gspread](https://docs.gspread.org/en/v5.7.0/) - used for control of Google Sheets 
- [OAuthLib](https://oauthlib.readthedocs.io/en/latest/) - needed to access google sheets
- [os](https://www.geeksforgeeks.org/os-module-python-examples/) - used to write the clear screen function
- [time](https://docs.python.org/3/library/time.html) - python module - used to pause screen before continuing
- [sys](https://superfastpython.com/exit-process/#What_is_sysexit) - Python Module used to exit the program
- [random](https://www.w3schools.com/python/ref_random_random.asp) - Python Module used to generate random numbers for raffle
- [tabulate](https://www.statology.org/create-table-in-python/) - Used to create the table to print the data from the player worksheet
- [colorama](https://pypi.org/project/colorama/) - Used to colour the text in terminal output.

## Testing

### Validation

### PEP8

- [PEP8CI](https://pep8ci.herokuapp.com/) - This was used test the code. No errors where found in the code. 

![PEP8CI](/assets/images/pep8.png)

### Manual Testing

Please find manual testing file here: [TESTING.md](/TESTING.md)

### Bugs/known issues


## Deployment

***
## Deployment

The live deployed application can be found deployed on [Heroku](https://shemmylicious.herokuapp.com).

***
### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: tribe).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

[Back to top &uarr;](#content)

***
### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

[Back to top &uarr;](#content)

***
### Heroku Deployment

[Setting up basic Django Project and Deploying to Heroku CI Doc](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

1. Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
1. Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
1. Further down, to support dependencies, select *Add Buildpack*.
1. The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)
1. From the new app *Settings*, click *Reveal Config Vars*, and set your environment variables.

    
    - CLOUNDINARY_URL: (Enter Cloudinary API URL)
    - DATABASE_URL: (Enter the database URL from ElephantSQL)
    - PORT: 8000
    - DISABLE_COLLECTSTATIC: 1 (must be removed before final deployment)
    - SECRET_KEY: (Enter your secret key)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's *requirements* (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The *Procfile* can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace *app_name* with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select *Automatic Deployment* from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

[Back to top &uarr;](#content)

***
### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "insert your own Cloudinary API key here")
os.environ.setdefault("DATABASE_URL", "insert your own ElephantSQL database URL here")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

[Back to top &uarr;](#content)

***
#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/ShemmyYo/django-shemmylicious) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/AngMaher/PP4-Where-Next.git`
7. Press Enter to create your local clone.


[Back to top &uarr;](#content)

***
#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
To make a copy or ‘fork’ the repository - 

1. Log into GitHub and locate the repository  
2. On the right-hand side of the page select the ‘fork’ option to create and copy the original

Alternatively, if using Gitpod, you can click below to create your workspace using this repository

[Back to top &uarr;](#content)

***


## Future Development


## Credits

### Code

### Media

- [Text ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - to create my logo

### Resources

 - Websites used along with course material were [StackOverFlow](https://stackoverflow.com/questions/18754276/python-for-beginners), and [W3Schools](https://www.w3schools.com/python/)

 ## Acknowledgements
  
- I would like to thank my mentor Jubril for his guidance through the project and my many testers (family and friends).