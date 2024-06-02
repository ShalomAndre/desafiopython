import requests

request= requests.get("https://www.youtube.com/@shalomandre7615")

print(request.status_code)