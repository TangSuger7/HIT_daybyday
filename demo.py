from selenium import webdriver
import time
import os
import sys
import getpass

for i in range(180):
    time.sleep(1)
    print(i)
# ID = input('学号:')
# key = getpass.getpass("password:");
with open('每日上报.txt','r') as f:
    ID = f.readline()
    key = f.readline()
loc = '黑龙江省哈尔滨市南岗区'

sys.path.append(os.getcwd())

driver = webdriver.Edge()
driver.minimize_window()
driver.get('https://ids.hit.edu.cn/authserver/')
driver.find_element_by_id('username').send_keys(ID)
driver.find_element_by_id('password').send_keys(key)
driver.find_element_by_class_name('auth_login_btn.primary.full_width').click()
driver.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew/edit')
driver.execute_script(f'kzl10 = "{loc}"')
driver.execute_script('document.getElementsByClassName("checkbtn")[0].click()')
driver.execute_script('document.getElementsByClassName("checkbtn")[1].click()')
driver.execute_script('document.getElementsByClassName("checkbtn")[2].click()')

driver.find_element_by_class_name('submit').click()
time.sleep(0.01)

flag = 0
try:
    driver.find_element_by_class_name('weui-toptips.bg-error.weui-toptips_visible')
except:
    flag = 1
    print('success!')
    time.sleep(3)
    driver.quit()
    os.system('explorer.exe')
    sys.exit(0)
print('error.')
time.sleep(3)
driver.quit()
sys.exit(0)
