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
  
  def _get_header(self):
    return {"Authorization": self._token}


if __name__ == "__main__":
  tt = TouchTunes("TOKEN_HERE")
  print(json.dumps(tt.get_self_info(), indent=4))
