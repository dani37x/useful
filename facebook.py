# get token from facebook
# script would take your name and posts from facebook

import facebook
import json

token = 'EAAQVixZBldbkBAGw9pmQLLpZAIzu7RYBnZBZCvFrbrZBZArECVKsq2J3Acykhgl8TwHsrNStHHlM6VvQTZCBQmovRwDBofHnS8y0iu3sIRbKZAPs051G8p9EAH8v5fj2EYEDXNHhqWzWUv5d45yJBZCM7ayZAvsLuvFdEdAr0EYoHstQ1wMDZCA5blOz5LsnasOwHFmXOkeN2mktgZDZD'

def get_own_posts(token):
  graph = facebook.GraphAPI(access_token=token, version="3.1")

  list_of_data = []
  who = graph.request('me')
  posts = graph.request('me?fields=posts')
  posts = posts['posts']['data']

  for post in posts:
    data = {}
    data['author'] = who['name']

    for key, value in post.items():

      if key == 'message':
        # print(value)
        data['message'] = value

      if key == 'created_time':
        # print(value)
        data['created_time'] = value
        
    list_of_data.append(data)
    
  return list_of_data


print(get_own_posts(token=token))
