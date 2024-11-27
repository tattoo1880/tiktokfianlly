
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# ! 使用bs4
from bs4 import BeautifulSoup

import time
import re


#全局變量TARGET_LIST
TARGET_LIST = []

def switchperson():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "10",
        "appium:deviceName": "fe85f60f",
        "appium:automationName": "UiAutomator2",
        "appium:noReset": "true",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "appium:appPackage": "com.zhiliaoapp.musically",
        "appium:appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
    })
    
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    
   
        
        
    soup = BeautifulSoup(driver.page_source, 'xml')
    
    # android.widget.FrameLayout
    frame = soup.find('android.widget.FrameLayout',{'content-desc':'個人資料'})
    clickbounds = frame['bounds']
    perform_click_by_bounds(clickbounds, driver)
    
    time.sleep(3)
    
        
        
    execute_adb_command(driver, "input tap 1011 175")
    time.sleep(1)
    execute_adb_command(driver, "input tap 300 1984")
    time.sleep(3)

        
    swipe(driver, 580, 2000, 650, 1100, 350)
    time.sleep(1)
    swipe(driver, 580, 2000, 650, 1100, 350)
    time.sleep(1)
    swipe(driver, 580, 2000, 650, 1100, 350)
    time.sleep(1)
    swipe(driver, 580, 2000, 650, 1100, 350)
    time.sleep(1)
    
  
        
        
    soup = BeautifulSoup(driver.page_source, 'xml')
    
    switch_button = soup.find('android.widget.TextView', {'text': '切換帳號'})
    switch_button_bounds = switch_button['bounds']
    perform_click_by_bounds(switch_button_bounds, driver)
    
    # with open('switch.xml', 'w') as f:
    #     f.write(driver.page_source)
        
        
    # 找到所有text不为空而且不为新增帳號的TextView
    soup = BeautifulSoup(driver.page_source, 'xml')
    # textview = soup.find_all('android.widget.TextView', {'text': True})
    textview = soup.find_all('android.widget.TextView', {'text': True})
    bounds_list = []
    for text in textview:
        if text['text'] != '新增帳號':
            bounds = text['bounds']
            bounds_list.append(bounds)
    time.sleep(10)
    
    print("获取到账户bounds", bounds_list)
    
    driver.quit()
    
    return bounds_list
def main():
    list1 = switchperson()
    # list1 =  ['[231,1772][496,1827]']
    for i in list1:
        doit(i)
        
    

def mainscreen(bounds):
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "10",
        "appium:deviceName": "fe85f60f",
        "appium:automationName": "UiAutomator2",
        "appium:noReset": "true",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "appium:appPackage": "com.zhiliaoapp.musically",
        "appium:appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
    })
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    
    soup = BeautifulSoup(driver.page_source, 'xml')
    
    # android.widget.FrameLayout
    frame = soup.find('android.widget.FrameLayout',{'content-desc':'個人資料'})
    clickbounds = frame['bounds']
    perform_click_by_bounds(clickbounds, driver)
    
    time.sleep(3)
    
        
        
    execute_adb_command(driver, "input tap 1011 175")
    time.sleep(1)
    execute_adb_command(driver, "input tap 300 1984")
    time.sleep(3)

        
    swipe(driver, 580, 2000, 650, 1100, 350)
    time.sleep(1)
    swipe(driver, 580, 2000, 650, 1100, 350)
    time.sleep(1)
    swipe(driver, 580, 2000, 650, 1100, 350)
    time.sleep(1)
    swipe(driver, 580, 2000, 650, 1100, 350)
    time.sleep(1)
    
  
        
        
    soup = BeautifulSoup(driver.page_source, 'xml')
    
    switch_button = soup.find('android.widget.TextView', {'text': '切換帳號'})
    switch_button_bounds = switch_button['bounds']
    perform_click_by_bounds(switch_button_bounds, driver)
    
    time.sleep(3)
    
    # 根據bounds點擊
    perform_click_by_bounds(bounds, driver)
    
    time.sleep(10)
    print("用户切换为", bounds)
    
    driver.quit()
    
    


def doit(bound1):
    
    mainscreen(bound1)
    global TARGET_LIST
    
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "10",
        "appium:deviceName": "fe85f60f",
        "appium:automationName": "UiAutomator2",
        "appium:noReset": "true",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "appium:appPackage": "com.zhiliaoapp.musically",
        "appium:appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
    })

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    
    
    
    text = "@7jhrmbufvvuij"

    time.sleep(30)
    print("start")

    perform_click(1020, 183, driver)
    time.sleep(2)
    search_xml = driver.page_source

    # 使用bs4解析xml
    soup = BeautifulSoup(search_xml, 'xml')
    el_search = soup.find('android.widget.EditText')
    print("el_search", el_search)

    # el_search = driver.find_element(
    #     by=AppiumBy.XPATH,
    #     value='//android.widget.EditText[@class="android.widget.EditText"]'
    # )

    if el_search is not None:
        print("el_search,founded")
        try:
            # 使用adb keyboard，输入@camglocks300
            execute_adb_command(
                driver, "ime enable com.android.adbkeyboard/.AdbIME")
            execute_adb_command(
                driver, "ime set com.android.adbkeyboard/.AdbIME")

        # 使用 ADB Keyboard 输入文本
            # text = "@camglocks300"
            execute_adb_command(
                driver, f"am broadcast -a ADB_INPUT_TEXT --es msg '{text}'")

            time.sleep(2)
            perform_click(1020, 160, driver)

            time.sleep(2)
            newxml = driver.page_source
            soup = BeautifulSoup(newxml, 'xml')

            # <android.widget.Button index="0" package="com.zhiliaoapp.musically" class="android.widget.Button" text="關注" resource-id="com.zhiliaoapp.musically:id/mh3" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[794,621][1036,709]" displayed="true" />
            button = soup.find('android.widget.Button', {'text': '關注'})
            # print(button)

            
            # 不管text 前後有什麼，只要包含text就可以
            pattern = re.compile(text.split('@')[-1])

            if button is not None:
                name_confirm = soup.find('android.widget.TextView', {
                                         'text': pattern})
                print("name_confirm", name_confirm)
                if name_confirm is not None:
                    print("name_confirm,founded")
                    # bounds 屬性
                    bounds = name_confirm['bounds']
                    print("bounds", bounds)
                    perform_click_by_bounds(bounds, driver)
                    
                    time.sleep(2)
                    newnewxml = driver.page_source
                    soup = BeautifulSoup(newnewxml, 'xml')
                    # with open('newnewxml.xml', 'w') as f:
                    #     f.write(soup.prettify())
                        
                    fen_el = soup.find('android.widget.TextView', {'text': '粉絲'})
                    if fen_el is not None:
                        bounds = fen_el['bounds']
                        perform_click_by_bounds(bounds, driver)
                        print("粉絲,founded")
                        
                    time.sleep(2)
                    
                    #滑动屏幕580,1700,650,1100
                    name_lst = []
                    name_set = set()
                    for i in range(20):
                        
                        #判斷name_set的長度是否大於等於50
                        if len(name_set) >= 50:
                            break
                        
                        # with open (f'newnewxml_{i}.xml', 'w') as f:
                        #     f.write(driver.page_source)
                            
                        soup = BeautifulSoup(driver.page_source, 'xml')
                        
                        # 找到RecyclerView下的所有LinearLayout下的TextView, 並取得text屬性
                        recycleview = soup.find('androidx.recyclerview.widget.RecyclerView')
                        if recycleview is not None:
                            linearlayout = recycleview.find_all('android.widget.LinearLayout',{'index': '1'})
                            for linear in linearlayout:
                                textview = linear.find('android.widget.TextView', {'index': '1'})
                                if textview is not None:
                                    name = textview['text']
                                    name_lst.append(name)
                                    name_set.add(name)
                        # with open (f'newnewxml_{i}.xml', 'w') as f:
                        #     f.write(driver.page_source)
                        swipe(driver, 580, 2000, 650, 1100, 350)
                    print(name_set)
                    
                    # 將name_set加入全局變量TARGET_LIST
                    TARGET_LIST = list(name_set)

            if len(TARGET_LIST) >= 10:
                print("TARGET_LIST", len(TARGET_LIST))
                perform_click(820,2150,driver)
                time.sleep(4)
                video_xml = driver.page_source
                soup = BeautifulSoup(video_xml, 'xml')
                
                # with open('target_list.xml', 'w') as f:
                #     f.write(driver.page_source)
                    
                video_ele = soup.find('androidx.viewpager.widget.ViewPager')
                
                if video_ele is not None:
                    print("video_ele存在")
                
                if video_ele is not None:
                    # 找到video元素下的android.widget.TextView
                    video_text = video_ele.find('android.widget.TextView')
                    if video_text is not None:
                        print("video_text存在")
                    if video_text is not None:
                        bounds = video_text['bounds']
                        perform_click_by_bounds(bounds, driver)               
                    time.sleep(10)
                    
                    # with open('video.xml', 'w') as f:
                    #     f.write(driver.page_source)
                        
                    # ! 每5个targetlist 发一次评论
                    for j in range(0, len(TARGET_LIST), 5):
                        print("========")
                        xxxx = driver.page_source
                        time.sleep(2)
                        soupa = BeautifulSoup(xxxx, 'xml')
                            #android.widget.EditText
                        comment_el = soupa.find('android.widget.EditText')
                        if comment_el is not None:
                            bounds = comment_el['bounds']
                            perform_click_by_bounds(bounds, driver)
                        else:
                            print("comment_el不存在")
                        chunk = TARGET_LIST[j:j+5]
                            
                        
                        for i in range(len(chunk)):    
                                # soup1 = BeautifulSoup(driver.page_source, 'xml')
                                # # =====
                                # with open('comment.xml', 'w') as f:
                                #     f.write(driver.page_source)
                                
                                # time.sleep(20)
                                # =====
                                # android.widget.LinearLayout
                                # coment_el = soup1.find('android.widget.LinearLayout', {'index': '0'})
                                # comment_at = soup1.find_all('android.widget.ImageView', {'index': '0'})[-1]
                                # comment_send = soup1.find('android.widget.Button',{'content-desc': '發佈評論'})
                                # print("comment_at", comment_at['bounds'])
                                # print("comment_send", comment_send['bounds'])
                                # perform_click_by_bounds(comment_at['bounds'], driver)
                                
                                # textarget =  '@' + chunk[i]
                                perform_click(717,1330,driver)
                                textarget = chunk[i]

                                execute_adb_command(driver, f"am broadcast -a ADB_INPUT_TEXT --es msg '{textarget}'")
                                time.sleep(3)
                                
                                # with open('comment_at.xml', 'w') as f:
                                #     f.write(driver.page_source)
                                    
                                # soup2 = BeautifulSoup(driver.page_source, 'xml')
                                # target = soup2.find('android.widget.TextView', {'text': textarget})
                                
                                perform_click(100,470,driver)
                                
                                # if target is not None:
                                #     bounds = target['bounds']
                                #     perform_click_by_bounds(bounds, driver)
                                if i == 4:
                                    try:
                                        soup2 = BeautifulSoup(driver.page_source, 'xml')
                                        comment_send = soup2.find('android.widget.Button',{'content-desc': '發佈評論'})
                                        perform_click_by_bounds(comment_send['bounds'], driver)                            
                                        print("success comment")
                                    except:
                                        print("success error")
                                time.sleep(2)
                            
        except Exception as e:
                print("e", e)      
                driver.quit()
                
        finally:
            driver.quit()


def perform_click(x, y, driver):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(
        driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(1341, 179)
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()


def execute_adb_command(driver, command):
    driver.execute_script("mobile: shell", {'command': command})
    print(f"Executed: {command}")
    
# 根據bounds屬性，取得元素的中心點,點擊
def perform_click_by_bounds(bounds, driver):
    bounds = bounds.replace('[', '').replace(']', ',').split(',')
    x = (int(bounds[0]) + int(bounds[2])) / 2
    y = (int(bounds[1]) + int(bounds[3])) / 2
    perform_click(x, y, driver)


# ! 根据座标滑动屏幕
def swipe(driver, start_x, start_y, end_x, end_y, duration):
    driver.swipe(start_x, start_y, end_x, end_y, duration)

if __name__ == "__main__":
    main()
    print("TARGET_LIST", TARGET_LIST)