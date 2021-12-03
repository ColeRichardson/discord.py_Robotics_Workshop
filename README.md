# discord.py_Robotics_Workshop
Contains slides, links, and source code used when presenting my learn to code a discord bot with python workshop hosted with UTM Robotics club.
as a quicks tarter on some of the best pratices for setting up the bot view the slide decks linked in this repository.

*** Don't want to read the slides but want to get started quick (Assuming you are on windows)? ***
#note: from here for terminal commands we will assume you are in the root of the project folder (should be here after git cloning anyways)

1)To use the code provided as an example for your own bot. Fork the repository. then in your terminal run the following commands. 
python -m venv venv #this creates a virtual environment, the next command activates it.
./venv/Scripts/Activate.ps1 #note this might be different depending on the os and terminal you are using check here for more info
pip install -r requirements.txt #This command will install all the necessary modules needed to run the bot.

2)Get your discord api key here: https://discord.com/developers/applications

Essentially go to bot -> create a bot -> copy token
![alt text](https://github.com/ColeRichardson/discord.py_Robotics_Workshop/blob/main/how%20to%20create%20bot%20pics/add%20bot%201%20of%204.jpg)
![alt text](https://github.com/ColeRichardson/discord.py_Robotics_Workshop/blob/main/how%20to%20create%20bot%20pics/get%20bot%20token%202%20of%204.PNG)

Then go to Oauth2 -> URL generator -> scopes select bot & application commands
![alt text](https://github.com/ColeRichardson/discord.py_Robotics_Workshop/blob/main/how%20to%20create%20bot%20pics/oauth%20generation%203%20of%204.PNG)

Next, set desired bot permissions by nature this will vary depending on what you want your bot to do. best practice is to avoid giving unnecssary perms.
![alt text](https://github.com/ColeRichardson/discord.py_Robotics_Workshop/blob/main/how%20to%20create%20bot%20pics/permission%20and%20url%204%20of%204.PNG)

Lastly on the bottom of the page you will see enerated URL, click the copy button and paste into your browser

Invite the bot into desired server and you are ready to go!

3)Now you should be able to run the example by simply running the script. this can be done in terminal by typing: python ./bot.py
The bot should run and you are now able to interact with it by using slash commands. 

4)Write your code and test it! Remember for your code to take affect you will need to stop the script and re run it. Also keep in mind that sometimes it take a little while newly created slash commands to sync up with discord.
