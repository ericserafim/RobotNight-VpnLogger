from pywinauto.application import Application
import pyperclip
import time
import pyautogui
import config

def rsa_stuff():        
        app = Application().start(cmd_line=config.RSA_PATH)
        rsa = app.QWidget
        rsa.wait('ready')
        rsa.click_input()   

        time.sleep(1) 
        pyautogui.typewrite(config.RSA_PIN)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('space')
        token = pyperclip.paste()
        print(f'RSA Token = {token}')
        app.kill()
        return token

def vpn_stuff():                
        rsa_token = rsa_stuff()        
        app = Application().start(cmd_line=config.GLOBAL_PROTECT_PATH)
        time.sleep(1)                
        pyautogui.click(config.ASSETS_DIR + 'connect.png')

        #First Login        
        if wait_for_image_on_screen('sign.png') == False:
          print("Failed to login on VPN using UserName and Password")
          return

        pyautogui.typewrite(config.VPN_USERNAME)
        pyautogui.press('tab')
        pyautogui.typewrite(config.VPN_PASSWORD)         
        pyautogui.press('enter')

        #Second Login with RSA Token
        if wait_for_image_on_screen('sign.png'):
           pyautogui.typewrite(config.VPN_USERNAME) 
           pyautogui.press('tab')     
           pyautogui.typewrite(rsa_token)
           pyautogui.press('enter')
        
        isConnected(1)

def wait_for_image_on_screen(imagePath):
        print(f"Searching for image {imagePath}...")
        image = None
        for i in range(0, config.TIMEOUT):
           image = pyautogui.locateOnScreen(config.ASSETS_DIR + imagePath, confidence=0.8, grayscale=True)                      
           if image != None: return True
           time.sleep(1)

        return False

def isConnected(step):                
        if wait_for_image_on_screen('connected.png') == False: 
           #print(f'"Failed to connect on VPN. {step == 1 if "Trying to use RSA Token" else ""}"') 
           print("Failed to connect on VPN.") 
           return False           
        else:
           print("Connected")
           return True

vpn_stuff()