## Bot to check slot availability on the Cowin portal

The script uses some of the open APIs listed on [this page](https://apisetu.gov.in/public/marketplace/api/cowin)

[Check out my implementation video](https://www.youtube.com/watch?v=Fcb8zzEton0&ab_channel=YourAverageCoder)

> #### Steps to run the script:
* Make sure you have python installed
* Install the required libraries using:
```
pip install requests datetime pyautogui
```
* Populate your **_districtId_** in the script (Use the [Get States](https://apisetu.gov.in/public/marketplace/api/cowin#/Metadata%20APIs/states) & [Get List of Districts](https://apisetu.gov.in/public/marketplace/api/cowin#/Metadata%20APIs/districts) APIs)
* Run the script using:
```
python script.py
```
