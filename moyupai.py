from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

@retry(stop_max_attempt_number=5)
def moyupai(driver):
    try:
        # driver = get_web_driver()
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://pwl.icu/login")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='nameOrEmail']").send_keys(username)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys(password)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@class='green']").click() # 为了显示验证码，先点击一次登录
        # 登陆后
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='checkIn']").click()
        print("每日签到")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='yesterday']").click()
        print("领取昨日活跃奖励")
        time.sleep(1)
        print('moyupai签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    moyupai()
