<h1>ChatGPT Terminal</h1>

<h3>Summary</h3>
This project is designed to be run in the users terminal. I decided to design this application to be run in a TMUX window while working on code and thought it would help to intergrate ChatGPT directly into my developer environment.  Feel free to share and create PR's to help improve the codebase.

<h3> Installation</h3>
First checkout the repository using Git:
<br>
<code> git checkout https://github.com/SkylarCastator/chatgpt-terminal-extension.git </code>

Make sure to install Python. My Venv is using version 3.11 but should work on different versions.
Also make sure you have pip setup as part of your python package. 
Next cd into the project directory and run:
<br>
<code> pip install requirements.txt </code>

Once this code is ran you should have the venv set up to run the project. You can test by running:
<br>
<code> python3 main.py </code>

Once you have tested that you can run the application link it to an alias like the command below.
<br>
<code> alias gpt='python3 {path-to-chatgpt-project}/main.py' </code>

<h3>Onboarding Process</h3>
The onboarding process will request you to create a token for chatgpt and to enter it into the prompt. This will load the token into a saved location on your machine.
If you need to edit this setting any time, enter {/user} into the prompt and follow the instructions to alter the token file.

Creating the token for ChatGPT can be done by going the the chat gpt website : 

https://platform.openai.com

Create an account and then go to the keys page here:

https://platform.openai.com/account/api-keys

Copy the key and then enter it into the prompt. This will allow you to start using the application.

<h3> Basic Usage </h3>
The ">>" prompt is there to helpo the user to understand what level they are using the application.
When it doesnt have any extra contact before the prompt you are using the main layer that allows you to prompt ChatGPT.

The other command tha can be used currently include:

- <b>/help</b> : Shows the list of options for the application to be ran.
- <b>/user</b> : Allows the user to change the user pref file
- <b>/chatgpt</b> : Allows the user to change the chatgpt prompt inputs.
- <b>/exit</b> : Allows the user to exit the application