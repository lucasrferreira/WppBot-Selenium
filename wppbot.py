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
from datetime import datetime
from wpp_message import message
import time
from urllib import request

class WppApi:
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    options = Options()
    # options.headless = True #Add after implement QRCode and run in docker
    # firefox_capabilities['binary'] = 'driver/geckodriver'
    browser = webdriver.Firefox(options=options)
    timeout = 10

    def __init__(self, wait):
        self.browser.get("https://web.whatsapp.com/")

        self.browser.save_screenshot('QRCODE.png')
        WebDriverWait(self.browser, wait).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._1FTCC')))
        

    # seleciona um chat
    def get_chat(self, chat_name):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(chat_name+Keys.ENTER)
        time.sleep(5)

    def join_group(self, invite_link):
        self.browser.get(invite_link)
        try:
            Alert(self.browser).accept()
        except:
            print("No alert Found")
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#action-button')))
        join_chat = self.browser.find_element_by_css_selector("#action-button")
        join_chat.click()
       

    def send_message(self, name, msg):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        # we will send the name to the input key box
        search.send_keys(name+Keys.ENTER)
        try:
            send_msg = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")))
            msgs = msg.split("\n")
            for msg in msgs:
                send_msg.send_keys(msg)
                send_msg.send_keys(Keys.SHIFT+Keys.ENTER)
            send_msg.send_keys(Keys.ENTER)
            return True
        except TimeoutException:
            raise TimeoutError(
                "Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException:
            return False
        except Exception:
            return False

    def refresh(self):
        try:
            self.browser.refresh()
            Alert(self.browser).accept()
        except Exception as e:
            print(e)
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._2zCfw')))

    def check_exists_by_class(self, driver, class_name):
        try:
            driver.find_element_by_css_selector('.'+class_name)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_xpath(self, driver, xpath):
        try:
            driver.find_element_by_xpath('//'+xpath)
        except NoSuchElementException:
            return False
        return True
    
    def check_exists_by_tag(self, driver, tag):
        try:
            driver.find_element_by_tag_name(tag)
        except NoSuchElementException:
            return False
        return True

    def get_and_save_image(self, src, chat_name):
        main_window = self.browser.current_window_handle
        self.browser.execute_script('''window.open("%s", "_blank");'''%(src))
        self.browser.switch_to_window(self.browser.window_handles[1])

        actionChains = ActionChains(self.browser)
        element =  self.browser.find_element_by_tag_name('img')
        actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        # self.browser.get(src)
        print('DONE')
        # request.urlretrieve(src, "media/images/img.png")

    # retorna lista com ultimas menssagens
    def get_messages_chat(self, chat_name, wait):
        self.get_chat(chat_name)
        messages = []
        divs = self.browser.find_elements_by_class_name('message-in')

        # print(len(divs))
        for div in divs:

            if self.check_exists_by_tag(div, 'img'):
                print('achou img')
                img = div.find_element_by_tag_name('img')
                src = img.get_attribute('src')
                print(src)
                # self.get_and_save_image(src, chat_name)

            if self.check_exists_by_class(div, 'copyable-text'):
                info = div.find_element_by_class_name('copyable-text')
                infoMsg = info.get_attribute('data-pre-plain-text')
                infoMsg = infoMsg.replace('[', '')
                infoMsg = infoMsg.replace(',', '')
                infoMsg = infoMsg.replace(']', '')
                vtMsg = infoMsg.split()
                msg = message(vtMsg[1], vtMsg[0], vtMsg[2], info.text)
                messages.append(msg)
                # print(msg.text)
        return messages

    def chat_with_unseen_messages(self):
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._1FTCC')))
        time.sleep(5)

        chat_names= []
        div_side = self.browser.find_element_by_id('pane-side')
        size = self.browser.execute_script('return arguments[0].scrollHeight', div_side)
        ini = 0
        while ini + size/10 < size - size/10:
            chats = self.browser.find_elements_by_css_selector('.X7YrQ')
            for chat in chats:
                if self.check_exists_by_class(chat, 'P6z4j'):
                    neme = chat.find_element_by_css_selector('._3H4MS')
                    unseen = chat.find_element_by_css_selector('.P6z4j')
                    chat_tuple = (neme.text, unseen.text)
                    if chat_tuple not in chat_names:
                        chat_names.append(chat_tuple)
            self.browser.execute_script('arguments[0].scrollTop += arguments[0].scrollHeight/10', div_side)
            ini = self.browser.execute_script('return arguments[0].scrollTop', div_side)
            time.sleep(1)
        return chat_names

    def get_chat_names(self):
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._1FTCC')))
        time.sleep(5)

        chat_names= []
        div_side = self.browser.find_element_by_id('pane-side')
        size = self.browser.execute_script('return arguments[0].scrollHeight', div_side)
        ini = 0
        while ini + size/10 < size - size/10:
            chats = self.browser.find_elements_by_css_selector('._2wP_Y')
            for chat in chats:
                neme = chat.find_element_by_css_selector('._1wjpf _3NFp9 _3FXB1')
                chat_name = neme.text
                if chat_name not in chat_names:
                    chat_names.append(chat_name)
            self.browser.execute_script('arguments[0].scrollTop += arguments[0].scrollHeight/10', div_side)
            ini = self.browser.execute_script('return arguments[0].scrollTop', div_side)
        self.browser.minimize_window()
        return chat_names