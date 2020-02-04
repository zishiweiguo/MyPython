import time
from bs4 import BeautifulSoup
from selenium import webdriver
from utils import auth

chrome_path = '/Users/xuchao/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)  # driver = webdriver.PhantomJS()

jd_login = 'https://passport.jd.com/new/login.aspx'
bean_url = "https://bean.jd.com/myJingBean/list"

def login_jd():
    # 登陆京东(Chrome、PhantomJS or FireFox)
    driver.get(jd_login)

    # 窗口最大化
    driver.maximize_window()

    # QQ授权登录
    driver.find_element_by_xpath('//*[@id="kbCoagent"]/ul/li[1]/a').click()
    auth.qq(driver)
    time.sleep(3)

# 获取店铺
def get_shops():
    driver.get(bean_url)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    bean_shop_list = soup.find_all('a', class_='s-btn')
    shops = []
    for shop_url in bean_shop_list:
        shops.append(shop_url['href'])
    return shops

# 店铺签到
def sign_shop(shop_url):

    try:
        driver.get(shop_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # 获取店铺 id
        shop_id = soup.find(id='shop_id')['value']
        # 拼接签到地址
        sign_url = 'https://mall.jd.com/shopSign-{}.html'.format(shop_id)
        driver.get(sign_url)
        print('签到地址：{}, 签到成功'.format(sign_url))
        return 0
    except Exception as error:
        print('签到地址：{}, 签到失败'.format(sign_url))
        print(error)
        return -1


if __name__ == '__main__':

    count = 0
    login_jd()
    shops = get_shops()
    if len(shops) == 0:
        print('全部店铺已签到')
    else:
        for shop in shops:
            result = sign_shop(shop)
            if result == 0:
                count += 1
            else:
                count -= 1
        print('成功签到 {} 个店铺'.format(count))

    driver.quit()
