
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

import time
def main():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "8",
        "appium:deviceName": "HT7580200835",
        "appium:automationName": "UiAutomator2",
        "appium:noReset": "true",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)


    time.sleep(2)
    print("start")
    try:
        perform_click(1341, 179, driver)
        # 使用adb keyboard，输入@camglocks300
        execute_adb_command(driver, "ime enable com.android.adbkeyboard/.AdbIME")
        execute_adb_command(driver, "ime set com.android.adbkeyboard/.AdbIME")

    # 使用 ADB Keyboard 输入文本
        text = "@camglocks300"
        execute_adb_command(driver, f"am broadcast -a ADB_INPUT_TEXT --es msg '{text}'")
        
        

    # 等待输入完成
        time.sleep(2)
        
        perform_click(1297, 183, driver)
        
        time.sleep(2)
        perform_click(502, 642, driver)
        
        time.sleep(10)
        perform_click(249,1600,driver)
        
        time.sleep(10)
        # actions.w3c_actions.pointer_action.move_to_location(712, 2298)
        perform_click(712, 2298, driver)
        
        text1 = "@twins"
        execute_adb_command(driver, f"am broadcast -a ADB_INPUT_TEXT --es msg '{text1}'")
        execute_adb_command(driver, f"am broadcast -a ADB_INPUT_TEXT --es msg '{text1}'")
        execute_adb_command(driver, f"am broadcast -a ADB_INPUT_TEXT --es msg '{text1}'")
        execute_adb_command(driver, f"am broadcast -a ADB_INPUT_TEXT --es msg '{text1}'")
        execute_adb_command(driver, f"am broadcast -a ADB_INPUT_TEXT --es msg '{text1}'")
        execute_adb_command(driver, f"am broadcast -a ADB_INPUT_TEXT --es msg '{text1}'")
        execute_adb_command(driver, f"am broadcast -a ADB_INPUT_TEXT --es msg '{text1}'")
        execute_adb_command(driver, f"am broadcast -a ADB_INPUT_TEXT --es msg '{text1}'")
        
        
        
        print("el1,done")
    except Exception as e:
        print("e",e)
        
    time.sleep(20)


    driver.quit()






def perform_click(x,y,driver):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(1341, 179)
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()


def execute_adb_command(driver, command):
    driver.execute_script("mobile: shell", {'command': command})
    print(f"Executed: {command}")
if __name__ == "__main__":
    main()