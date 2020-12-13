# Robot Seipp

Personal discord bot.

## Developer Setup

Create a personal testing server on discord to run your bot on.  Then go to the discord developer portal in your web browser.  Go to the applications tab and create a new application.  Inside the application, create a bot in the bot tab.  Set its permissions to administrator.  Go to the OAuth2 tab.  Generate a URL with the bot scope and administrator privilleges.  Copy the URL in a new tab, and add the bot to your test server.  Now the bot should be added to your server.  You can bring it to life by running the deployment script.  Make changes to the code and run the deployment script to test the bot.  Don't forget to run the teardown script, or else both versions of your bot will act together!


Before running Robot Seipp, you must install discord.py, a python library that serves as an API wrapper for the discord API. 

	pip3 install discord.py

Before running the scripts to deploy and teardown the bot, make sure you have the proper permissions set up for them.
	chmod 700 ./deploy
	chmod 700 ./teardown	

You can run the bot by running the deploy script, and kill it with the teardown script
	./deploy
	./teardown
