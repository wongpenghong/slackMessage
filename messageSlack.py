import requests
import json

# Get Credentials Config
with open("config.json", "r") as read_file:
    CONFIG = json.load(read_file)['config']


# slack access bot token
data = {
    # Token ID
    'token': CONFIG['tokenSlack'],
    # Channel ID
    'channel': CONFIG['channel'],    # User ID. 
    # show sender as user or tester api
    'as_user': True,
    # text that you want to send
    'text': CONFIG['text']
}

# Hit the url with POST method
requests.post(url='https://slack.com/api/chat.postMessage',
              data=data)
