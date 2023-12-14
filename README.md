# Project 3 - A Python Hangman Game

## Deployment

1. To start with you would need to type this code into your IDE Terminal:

git clone https://github.com/AlistairDriscoll/project-3.git

2. Then create a GitHub repository to host the code and use this command to link
the remote repository location to this repository:

git remote set-url origin <Your GitHub Repo Path>

3. Lastly, push the files to the online repository using the push command:

git push


4. The app was then deployed onto a website called [Heroku](https://heroku.com/),
which specializes in application deployment for back-end languages
such as Python. To deploy, I needed to make an account on their website.
Once I had done this, I needed to press the 'new' button in the top right
corner of my account page and click 'create new app'.

![New App Button](documentation/deployment/new-app-button.png)

5. Following this, a page will come up asking what name you would like for
your app. Select a name that hasn't been chosen before then select your
region in the options section.

![Name App Section](documentation/deployment/name-app-section.png)

6. Next, go to the deploy section.

![Deploy Button](documentation/deployment/deploy-button.png)

7. Now choose GitHub as your way of deploying.

![Deployment Section](documentation/deployment/deployment-section.png)

8. Underneath this, put in the repository you would like to connect to using
the form given.

![Repository Name Section](documentation/deployment/repo-name-section.png)

9. Now click on the settings button.

![Settings Button](documentation/deployment/settings-button.png)

10. In the settings bit go to the Buildpacks section and select python,
then node.js. Please make sure they are ordered correctly, python should be
above node.js.

![Buildpacks Section](documentation/deployment/buildpacks-section.png)

11. Then above the Buildpacks, there should be the Config Vars section.
Click the button to reveal the Config Vars and type in PORT in the key section
and 8000 in the value section.

![Config Vars](documentation/deployment/config-vars.png)

12. Now go back to the deployment and select the 'Deploy branch' button
at the bottom of the page.

![Deploy Page Button](documentation/deployment/deploy-branch-button.png)

13. After a short while, once the website has done everything it needs to,
your app will be a live website! Simply click the open app button in the top
right corner to try it out!

![Open App Button](documentation/deployment/open-app-button.png)

### Local Deployment

- The website can be accessed
with this [link](https://python-hangman-project-3-b49f3ebff2dd.herokuapp.com/)

- Or to deploy it to your IDE you can type this code into the terminal:
git clone https://github.com/AlistairDriscoll/project-3.git

Note: for the code to work you must have the latest version of
Python downloaded as well as Colorama. Download Python from the Python
website, install it then type this line of code into your terminal:

pip install colorama

## Design and Dependencies

- Packages used
- How I structured the code
- Separating packages
- Talk about words file
- Black used for formatting