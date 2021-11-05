from util import *

username = sys.argv[1]
password = sys.argv[2]

def Sliding_Captcha(driver):
    # 获取验证图片
    slide_img = driver.find_element_by_xpath("//*[@id='captcha-verify-image']")
    backgroud_img = driver.find_element_by_xpath("//*[@class='captcha_verify_img_slide react-draggable sc-VigVT ggNWOG']")
    slide_url = slide_img.get_attribute("src")
    backgroud_url = backgroud_img.get_attribute("src")
    
    track = Track()
    result = track.get_track(slide_url, backgroud_url)

    verify_div = driver.find_element(By.XPATH, '''//div[@class="sc-kkGfuU bujTgx"]''')

    # 按下鼠标左键
    ActionChains(driver).click_and_hold(verify_div).perform()
    time.sleep(0.5)
    # 遍历轨迹进行滑动
    for t in result:
        time.sleep(0.01)
        ActionChains(driver).move_by_offset(xoffset=t, yoffset=0).perform()
    # 释放鼠标
    ActionChains(driver).release(on_element=verify_div).perform()
    time.sleep(10)

def juejin():
        flag = True
        while flag:
            try:
                driver = get_web_driver()
                driver.maximize_window()
                driver.get("https://juejin.cn/")
                driver.find_element_by_xpath("//*[@class='login-button']").click()  # 点击"登录"按钮
                driver.find_element_by_xpath("//*[@class='clickable']").click()  # 点击"其他登录方式"
                driver.find_element_by_xpath("//*[@name='loginPhoneOrEmail']").send_keys(username)
                driver.find_element_by_xpath("//*[@name='loginPassword']").send_keys(password)
                driver.find_element_by_xpath("//*[@class='btn']").click()  # 点击"登录"按钮
                time.sleep(5)

                # 验证码处理的正确率不高
                Sliding_Captcha(driver)  # 验证码处理 如果验证失败怎么办

                # 登陆后进入每日签到页面
                juejin_url = 'https://juejin.cn'
                driver.get(juejin_url)
                pagesource = driver.page_source

                time.sleep(5)
                if "的头像" in pagesource:
                    flag = False
                    driver.get('https://juejin.cn/user/center/signin')
                    if driver.find_elements_by_xpath("//*[@class='signedin btn']") != []:
                        # driver.find_element_by_xpath("//*[@class='signin btn']").click()
                        driver.find_element_by_xpath("//*[@class='signedin btn']").click()
                        time.sleep(10)
                        print("JueJin签到成功")
                else:
                    print("验证码未正确识别，签到失败！")
            except:
                raise
            finally:
                driver.quit()


if __name__ == '__main__':
    juejin()
