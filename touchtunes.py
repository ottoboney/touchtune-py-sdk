import requests
import json

class TouchTunes():
  ## For now have to get token manually
  def __init__(self, bearer):
    self._token = 'Bearer ' + bearer
    self._url = 'https://api.mytouchtunes.com/v2'

  def get_self_info(self):
    PATH = '/users/self'
    headers = self._get_header()
    res = requests.get(self._url + PATH, headers = headers)
    return res.json()

  def get_locations(self, latitude, longitude, radius=1600, limit=5):
    PATH = '/locations'
    headers = self._get_header()
    params = { 'latitude': latitude, 'longitude': longitude,
               'user_latitude': latitude, 'user_longitude': longitude,
               'radius': radius, 'limit': limit}
    res = requests.get(self._url + PATH, params = params, headers = headers)
    return res.json()
    
  def play_song(self, location_id, device_id, song_id, play_next=0):
    PATH = "/locations/%s/devices/%s/queues/jukebox" % (location_id, device_id)
    headers = self._get_header()
    body = { "play_next": play_next,
             "song_id": song_id }
    res = requests.post(self._url + PATH, data=body, headers=headers)
    return res.json()
  
  def get_token(self, user, password):
    PATH = '/access_token'
    headers = { "User-Agent": "TouchTunes-iOS-3.19.6" }
    body = { "grant_type": "password",
             "username": user,
             "password": password,
             "oauth_consumer_key": None,
             "token": None }
    res = requests.post(self._url + PATH, json=body)
    return res.json()

  def _get_header(self):
    return {"Authorization": self._token,
            "User-Agent": "TouchTunes-iOS-3.19.6"}


if __name__ == "__main__":
  tt = TouchTunes("TOKEN")
  print(json.dumps(tt.play_song("", "", "")))
  print(json.dumps(tt.get_locations("", ""), indent=4))
  print(json.dumps(tt.get_self_info(), indent=4))
