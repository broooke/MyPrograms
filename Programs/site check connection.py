import requests
url = 'https://meet.google.com/zsj-ynap-wqc?pli=1&authuser=1'
timeout = 6
try:
    requests = requests.get(url,timeout=timeout)
    print("Site connected")
except:
    print("Site not connected")