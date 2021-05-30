import requests
import datetime as dt
import time
import winsound
import pyautogui
import random

district_id = '240'
url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict'

# prevent machine from entering sleep mode
def preventSleep():
    pyautogui.press('volumedown')
    time.sleep(1)
    pyautogui.press('volumeup')

# returns a list of dates(starting today) to check slot availability
def getDates():
    dates = []
    for i in range(5):
        date = dt.datetime.now() + dt.timedelta(days=i)
        dates.append(date.strftime('%d-%m-%Y'))
    return dates

if __name__ == '__main__':
    dates = getDates()
    while True:
        flag = False
        for date in dates:
            try:
                queryString = '?district_id='+district_id+'&date='+date
                response = requests.get(url+queryString)
                centers = response.json()['sessions']
                for center in centers:
                    if center['vaccine']=='COVAXIN' and center['available_capacity_dose2']>0:
                        flag = True
                        print(str(center['pincode']) + ' ' + center['name'])
                        winsound.Beep(440, 1000)
                        time.sleep(1)
            except Exception as e:
                print(e)
                time.sleep(3)
        if(flag==True):
            # can add logic to notify via mail, msg etc.
            print('Found Slots at ' + str(dt.datetime.now()))
            winsound.Beep(440, 2000)
            break # or not
        preventSleep();
        time.sleep(4)
