from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from meet.models import MeetInfo
from meet.serializers import MeetInfoSerializer
from selenium import webdriver
from pyvirtualdisplay import Display
import time

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



@csrf_exempt
def meet_list(request):
    if request.POST:

        data = request.POST
        print("New Message Sent Requested by "+data.get("userName"))
        rMessage = data.get("message")
        mobileNo = data.get("phoneNo")
        userNameUser = data.get("userName")
        passwordUser = data.get("password")

        display = Display(visible=0, size=(800, 600))
        display.start()

        driver = webdriver.Chrome('/home/iam/Documents/Soft Linux/chromedriver')
        driver.get('http://www.meet.net.np/meet/')

        userName = driver.find_element_by_name('username')
        userName.send_keys(userNameUser)
        password = driver.find_element_by_name('password')
        password.send_keys(passwordUser)
        loginBtn = driver.find_element_by_id('loginImage')
        loginBtn.click()
        loop = True
        while (loop):
            try:
                loginBtn = driver.find_element_by_id('search_box_id')
                loop = False
            except Exception:
                print("Retrying locating element.")
                time.sleep(5)

        driver.get('http://www.meet.net.np/meet/sms/sendsms')

        englishLn = driver.find_elements_by_id("SmsLanguage1")
        englishLn[0].click();

        mobileNumber = driver.find_element_by_name("recipient")
        mobileNumber.send_keys(mobileNo)

        message = driver.find_element_by_id("message")
        message.send_keys(rMessage)

        sendButton = driver.find_element_by_name("sendbutton")
        sendButton.click()
        time.sleep(5)
        driver.quit()
        return JSONResponse(data)
    else:
        data = {}
        data['success'] = False
        data['message'] = "Requested Method Not Allowd."
        return JSONResponse(data)