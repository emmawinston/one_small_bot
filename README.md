# One Small Step for Bot, One Giant Leap for Botkind

A bot to tweet random lines from a text file that will actually work on Heroku and not continually crash. 
Based on [Mary Dickson's tutorial](http://marydickson.com/build-a-twitter-bot-with-python/) but altered to remove sleep time and add a random number generator so it'll work with Heroku's scheduler without tweeting too frequently.

I'd ultimately like this to work through the list sequentially like [@everyword](http://twitter.com/everyword), but can't get this working in Heroku due to their ephemeral file storage. If anyone has any suggestions on (preferably free) alternatives, please get in touch! I'm looking at Openshift but am a bit overwhelmed by it at present.