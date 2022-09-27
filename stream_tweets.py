import twitter
import json
import os

consumer_key = os.environ['twitter_api_key']
consumer_secret = os.environ['twitter_api_key_secret']
access_token = os.environ['twitter_access_token']
access_token_secret = os.environ['twitter_access_token_secret']

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

def main(directory, filename, filterby, languages):
    with open(directory+'/'+filename+'.txt', 'a') as f:
        for line in api.GetStreamFilter(track=filterby, languages=languages):
            json_file = json.dumps(line)
            f.write(json_file)
            f.write('\n')
   
filter_text = [':)']
language_choice = ['en']

user_dir = 'C:/Users/jrilk/OneDrive/LHL/txt_files'

txt_file1= 'positiveJR'

main(user_dir, txt_file1, filter_text, language_choice)
