import requests
import win10toast
import datetime

try:
    data = requests.get("http://corona-rest-api.herokuapp.com/Api/russia")
except:
    print("Check your Internet connection")
    data = None

if data is not None:
    getData = data.json()
    covid_Russia = getData["Success"]
    title = """ Covid-19 Russia / {}""".format(datetime.date.today())
    message=""" In Russia covid-19 total cases is : {} , deaths : {} , recovered : {} , today-case is : {}""".format(covid_Russia["cases"],
    covid_Russia["deaths"],covid_Russia["recovered"],covid_Russia["todayCases"])

    toaster = win10toast.ToastNotifier()
    
    toaster.show_toast(title, message,duration=10, icon_path="covid-19.ico")