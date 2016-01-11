#!/usr/bin/env python2
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Import the python libraries we need to
import os 
import time
import tweepy
import sys
from random import randint
from random import randrange

argfile = str(sys.argv[1])

## Authentication Boilerplate

# Pass in these tokens using environment variables
# set them on the heroku app with: heroku config:set NAME="value"
# or pass them in with the command line: $ NAME="value" python file.py

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

heart = randrange(0,15)

if heart > 1:
    print('no heart this time')  
else:
    with open(argfile) as f:
            lines = f.readlines()
            rand_line_num = randint(0, len(lines) - 1)
            line = lines[rand_line_num]
            api.update_status(line)
            print('tweeted')