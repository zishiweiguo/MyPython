import time
from urllib.parse import parse_qs

import time
import requests
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# 额外抽取的授权模块
# from utils import auth


class QMM(object):
    """借助券妈妈平台褥京东京豆"""

    def __init__(self, sleep=3, months=None, days=None):
        self.timeout, self.months, self.days = sleep, None, None
        # 爬取规则
        if months:
            month_interval = months.split('-')
            start_month, end_month = int(month_interval[0]), int(month_interval[-1])
            self.months = list(map(lambda m: '{}月'.format(m), range(start_month, end_month + 1)))
        if days:
            day_interval = days.split('-')
            start_day, end_day = int(day_interval[0]), int(day_interval[-1])
            self.days = list(map(lambda d: '{}日'.format(d), range(start_day, end_day + 1)))
        # 手机店铺(用作提醒输出，可复制链接到手机端领取)
        self.m_shop = []
        # 统计京豆总数
        self.jing_dou = 0

    def _crawl_url(self):
        """ 抓取京豆更新页, 获得店铺京豆领取地址"""

        # 日期更新页
        qmm_collect = 'http://www.quanmama.com/zhidemai/2459063.html'
        bs = BeautifulSoup(requests.get(qmm_collect).text, 'html.parser')
        for link in bs.tbody.find_all('a'):
            text = link.text
            if self.months:
                if not list(filter(lambda m: m in text, self.months)): continue
            if self.days:
                if not list(filter(lambda d: d in text, self.days)): continue

            qmm_detail = link.get('href')

            # 店铺领取页
            resp = requests.get(qmm_detail)
            bs = BeautifulSoup(resp.text, 'html.parser')
            for body in bs.find_all('tbody'):
                for mall in body.find_all('a'):
                    url = self._parse_url(mall.get('href'))
                    if 'shop.m.jd.com' in url:
                        self.m_shop.append(url)
                    else:
                        yield url

    @staticmethod
    def _parse_url(url):
        """提取URL中的url参数"""

        mall_url = parse_qs(url).get('url')
        return mall_url.pop() if mall_url else url

    def start(self):
        """ 登录京东，领取店铺羊毛"""

        malls = set(self._crawl_url())
        print('共有 %d 个可褥羊毛PC端店铺页面' % len(malls))

        m_malls = self.m_shop
        print('共有 %d 个可褥羊毛手机端店铺页面' % len(m_malls))
        for m_mall in m_malls:
            print(m_mall)

        if malls:
            # 登陆京东(Chrome、PhantomJS or FireFox)
            driver = webdriver.Chrome()  # driver = webdriver.PhantomJS()
            jd_login = 'https://passport.jd.com/new/login.aspx'
            driver.get(jd_login)

            # 窗口最大化
            driver.maximize_window()

            # # QQ授权登录
            # driver.find_element_by_xpath('//*[@id="kbCoagent"]/ul/li[1]/a').click()
            # auth.qq(driver)
            # time.sleep(self.timeout)
            # 账号密码登录

            time.sleep(3)
            s1 = r'//div/div[@class="login-tab login-tab-r"]/a'
            userlogin = driver.find_element_by_xpath(s1)
            userlogin.click()
            # time.sleep(5)
            username = driver.find_element_by_id("loginname")
            username.send_keys("")
            userpswd = driver.find_element_by_id("nloginpwd")
            userpswd.send_keys("password")
            # time.sleep(5)
            driver.find_element_by_id("loginsubmit").click()
            time.sleep(3)
            while True:
                try:
                    getPic()
                except:
                    print("登陆成功----")
                    break
            time.sleep(5)

            # 开始褥羊毛
            for i, detail in enumerate(malls):
                driver.get(detail)
                print('%d.店铺: %s' % (i + 1, detail), end='')
                try:
                    # 查找"领取"按钮
                    btn = WebDriverWait(driver, self.timeout).until(
                        lambda d: d.find_element_by_css_selector("[class='J_drawGift d-btn']"))
                except TimeoutException:
                    # 失败大多数情况下是无羊毛可褥(券妈妈平台只是简单汇总但不一定就有羊毛)
                    print(' 领取失败, TimeoutException ')
                else:
                    try:
                        # 输出羊毛战绩
                        items = WebDriverWait(driver, self.timeout).until(
                            lambda d: d.find_elements_by_css_selector("[class='d-item']"))
                        for item in items:
                            item_type = item.find_element_by_css_selector("[class='d-type']").text
                            item_num = item.find_element_by_css_selector("[class='d-num']").text
                            if item_type == '京豆': self.jing_dou += item_num
                            print(' {}{} '.format(item_type, item_num), end='')
                    except:
                        # 此处异常不太重要, 忽略
                        pass
                    finally:
                        btn.click()
                        print(' 领取成功')

            # 以下附加功能可选
            self._print_jing_dou()
            self._un_subscribe(driver)
            self._finance_sign(driver)

    def _print_jing_dou(self):
        print('O(∩_∩)O哈哈~, 共褥到了{}个京豆，相当于RMB{}元', self.jing_dou, self.jing_dou / 100)

    def _un_subscribe(self, driver):
        """批量取消店铺关注"""

        # 进入关注店铺
        subscribe_shop = 'https://t.jd.com/vender/followVenderList.action'
        driver.get(subscribe_shop)

        try:
            # 批量操作
            batch_btn = WebDriverWait(driver, self.timeout).until(
                lambda d: d.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[2]/div[2]/div/a'))
            batch_btn.click()
            # 全选店铺
            all_btn = WebDriverWait(driver, self.timeout).until(
                lambda d: d.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[2]/div[2]/div/div/span[1]'))
            all_btn.click()
            # 取消关注
            cancel_btn = WebDriverWait(driver, self.timeout).until(
                lambda d: d.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[2]/div[2]/div/div/span[2]'))
            cancel_btn.click()
            # 弹框确认
            confirm_btn = WebDriverWait(driver, self.timeout).until(
                lambda d: d.find_element_by_xpath("/html/body/div[7]/div[3]/a[1]"))
        except TimeoutException:
            print(' 批量取关店铺失败, TimeoutException ')
        else:
            confirm_btn.click()
            print(' 已批量取消关注店铺')

    def _finance_sign(self, driver):
        """京东金融签到领钢镚"""

        # 进入京东金融
        jr_login = 'https://jr.jd.com/'
        driver.get(jr_login)

        try:
            # 点击签到按钮
            sign_btn = WebDriverWait(driver, self.timeout).until(
                lambda d: d.find_element_by_xpath('//*[@id="primeWrap"]/div[1]/div[3]/div[1]/a'))
        except TimeoutException:
            print(' 京东金融签到失败, TimeoutException ')
        else:
            sign_btn.click()
            print(' 京东金融签到成功')

    def getPic(brower):
        # 用于找到登录图片的大图
        s2 = r'//div/div[@class="JDJRV-bigimg"]/img'
        # 用来找到登录图片的小滑块
        s3 = r'//div/div[@class="JDJRV-smallimg"]/img'
        bigimg = brower.find_element_by_xpath(s2).get_attribute("src")
        smallimg = brower.find_element_by_xpath(s3).get_attribute("src")
        # print(smallimg + '\n')
        # print(bigimg)
        # 背景大图命名
        backimg = "backimg.png"
        # 滑块命名
        slideimg = "slideimg.png"
        # 下载背景大图保存到本地
        request.urlretrieve(bigimg, backimg)
        # 下载滑块保存到本地
        request.urlretrieve(smallimg, slideimg)
        # 获取图片并灰度化
        block = cv2.imread(slideimg, 0)
        template = cv2.imread(backimg, 0)
        # 二值化后的图片名称
        blockName = "block.jpg"
        templateName = "template.jpg"
        # 将二值化后的图片进行保存
        cv2.imwrite(blockName, block)
        cv2.imwrite(templateName, template)
        block = cv2.imread(blockName)
        block = cv2.cvtColor(block, cv2.COLOR_RGB2GRAY)
        block = abs(255 - block)
        cv2.imwrite(blockName, block)
        block = cv2.imread(blockName)
        template = cv2.imread(templateName)
        # 获取偏移量
        result = cv2.matchTemplate(block, template,
                                   cv2.TM_CCOEFF_NORMED)  # 查找block在template中的位置，返回result是一个矩阵，是每个点的匹配结果
        x, y = np.unravel_index(result.argmax(), result.shape)
        # print("x方向的偏移", int(y * 0.4 + 18), 'x:', x, 'y:', y)
        # 获取滑块
        element = brower.find_element_by_xpath(s3)
        ActionChains(brower).click_and_hold(on_element=element).perform()
        ActionChains(brower).move_to_element_with_offset(to_element=element, xoffset=y, yoffset=0).perform()
        ActionChains(brower).release(on_element=element).perform()
        time.sleep(3)


if __name__ == '__main__':
    qmm = QMM(sleep=3, months='7-8', days='16-31')
    qmm.start()
