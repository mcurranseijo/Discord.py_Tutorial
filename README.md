# Discord.py_Tutorial
Tutorial for setting up a discord.py bot on host sapling

### Using the Template

* If you don't have discord.py installed go to [this url](https://pypi.org/project/discord.py/) for instructions on that
* In the bot.py file replace the bot token with your own if you need help [this tutorial is helpful](https://www.writebots.com/discord-bot-token/)
* Duplicate the example cogs file for each cog you want to make and modify it as needed

##### Other Info
This a barebones template with some basic info to get you started, the example cog should have enough info to get you started on using commands and embeds

##### What is a cog?
A cog is a way to sort your commands into categories and clean up your code, they can also be loaded, reloaded and unloaded without having to restart your server which makes modifying easier


### Setting up your Server

* Once you have a server the first step is to log in, depending on when you signed up that will either be [panel.factat.bike](https://panel.fatcat.bike/) or [https://panel.hostsapling.net/auth/login](https://panel.hostsapling.net/auth/login). 
* Once your logged in navigate to the file manager tab.
* Upload your files either as a zip or individually, you can then unzip your files by clicking the three dots. If uploading individually make sure you put your cogs in a cogs folder.
* Create a file called requirements.txt in that file add a line that says: discord.py
* You should be good to go, navigate to the panel and click start, the first time it will install the needed libraries once it finishes you'll want to press start again and your bot should now be up and running
