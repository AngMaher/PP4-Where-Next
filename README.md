# Table of Contents

- [User Experience](#user-experience)

  - [User Goals](#user-goals)

  - [Developer Goals](#developer-goals)

- [Logic and Features](#logic-and-features)

  - [Logic](#logic)

  - [Database Structure](#database-structure)

  - [Features](#features)

    - [Main Menu](#main-menu)

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


# User Experience

## User Goals


## Developer Goals



# Logic and Features

## Logic


## Database structure


## Features




# Technology

## Languages Used

- [Python](https://www.python.org/) - high level programming language
- [Markdown](https://www.markdownguide.org/cheat-sheet) - language used to write README and TESTING documents.

## Software Used

- [LucidChart](https://lucidchart.com) - LucidChart was used to create flowchart for the project.
- [Git](https://git-scm.com/) - Git was used for version control by using the Gitpod terminal to commit to Git and push to Github.
- [Github](https://github.com/) - Github was used to write and store the projects code.
- [Google Sheets](https://www.google.com/sheets/about/) - Used to store all the data from the program.
- [Heroku](https://www.heroku.com/home) - Heroku was used to deploy the project.
- [Text ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - Used to create the logo for the project.

## Python Libraries/Modules

- [gspread](https://docs.gspread.org/en/v5.7.0/) - used for control of Google Sheets 
- [OAuthLib](https://oauthlib.readthedocs.io/en/latest/) - needed to access google sheets
- [os](https://www.geeksforgeeks.org/os-module-python-examples/) - used to write the clear screen function
- [time](https://docs.python.org/3/library/time.html) - python module - used to pause screen before continuing
- [sys](https://superfastpython.com/exit-process/#What_is_sysexit) - Python Module used to exit the program
- [random](https://www.w3schools.com/python/ref_random_random.asp) - Python Module used to generate random numbers for raffle
- [tabulate](https://www.statology.org/create-table-in-python/) - Used to create the table to print the data from the player worksheet
- [colorama](https://pypi.org/project/colorama/) - Used to colour the text in terminal output.

# Testing

## Validation

### PEP8

- [PEP8CI](https://pep8ci.herokuapp.com/) - This was used test the code. No errors where found in the code. 

![PEP8CI](/assets/images/pep8.png)

## Manual Testing

Please find manual testing file here: [TESTING.md](/TESTING.md)

## Bugs/known issues


# Deployment

## Git and GitHub
- Code Institute template was used to create GitHub public repository PP4-WHERE_NEXT.

- I developed programm, often commiting changes using terminal commands.

- I made sure that all my libraries and packages are listed in requirements.txt.

- When program was ready for further deployment I visited heroku.com website to deploy on heroku.



## Deployment to Heroku
- I visited https://heroku.com/ and opened dashboard. Then I clicked button "New" and selected "Create new app" button.

- I entered my app name as "PP4-Where-Next", region to Europe and clicked on "Create app" button

- The next step was to go to "Deploy" tab and then to "Deployment method" section to authorize and connect my GitHub account.

![connect github](/assets/images/connectgithub.png)

- When succesfully connected I selected main branch from "PP4-WHERE-NEXT " repository.

- Then I went to "Settings" tab

- In the next step I went to "Config Vars" section and added KEY "CREDS" with value of my credentials file creds.json (copy all and paste).

![config vars](/assets/images/configvars.png)

- Next to "Buildpacks" section. In the next step I added pyhton and nodejs buildpacks, making sure python was first then nodejs.

![buildpacks](/assets/images/buildpacks.png)

- In the next step I went back to "Deploy" tab and decided to use manual mode, however automatic mode is also available to deploy, which I done at a later time.

![connected screen](/assets/images/connected.png)

- The link to my deployed app was shown on screen: [Live Link](https://st-mochtas-fc.herokuapp.com/)

## Local Deployment
- To make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- git clone 

## To Fork the Repository
- To make a copy or ‘fork’ the repository
  - Log into GitHub and locate the repository
  - Select the ‘fork’ option to create and copy the original
  Link to Github repository: ![Github](https://github.com/AngMaher/St-Mochtas-FC)

# Future Development


# Credits

## Code

## Media

- [Text ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - to create my logo

## Resources

 - Websites used along with course material were [StackOverFlow](https://stackoverflow.com/questions/18754276/python-for-beginners), and [W3Schools](https://www.w3schools.com/python/)

 # Acknowledgements
  
- I would like to thank my mentor Jubril for his guidance through the project and my many testers (family and friends).