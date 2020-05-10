# from wppbot import WppApi
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
# wpp = WppApi(60)
# while True:
# wpp.send_message('WACAO', ':)')
# messages = wpp.get_messages_chat("FIFA 🎮", 20)
# print(len(messages))
#wpp.join_group('https://chat.whatsapp.com/EbsTIzO3X6W7Svmqcx529w') 
# for message in messages:
#     print(message.text)
# chats = wpp.chat_with_unseen_messages()
# print(len(chats))
# print(chats)

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
options = Options()
options.headless = True
# firefox_capabilities['binary'] = 'driver/geckodriver'
browser = webdriver.Firefox(options=options)
browser.get("https://web.whatsapp.com/")

# chats = wpp.get_chat_names()
# print(len(chats))
# print(chats)
# wpp.join_group('https://chat.whatsapp.com/EbsTIzO3X6W7Svmqcx529w')

