from selenium import webdriver
import time

dri = webdriver.Chrome('software/d.exe')
# dri.fullscreen_window()
dri.get('http://my.cxxy.seu.edu.cn/')
dri.find_element_by_id('username').send_keys('238116444')
dri.find_element_by_id('password').send_keys('906100336\n')
# dri.find_element_by_xpath('//*[@id="pf144"]/div/div[2]/table/tbody/tr[4]/td[1]/a').click()
# dri.find_element_by_link_text("学工系统").click()

time.sleep(12)
xgxts = dri.find_elements_by_tag_name('a')

for xgxt in xgxts:
    if '学工系统' in xgxt.text:
        xgxt.click()
        # print(elm.text)

dri.switch_to_window(dri.window_handles[1])
time.sleep(5)
swbls = dri.find_elements_by_tag_name('a')
for swbl in swbls:
    if '事务办理' in swbl.text:
        swbl.click()
        print("OK")

time.sleep(5)
# xzdm("st_mrjkdj","每日健康情况登记","1","每日健康情况登记")"
# document.querySelector("#my_menu > div > a:nth-child(2)")
js = "document.getElementById('jsPswEdit').addEventListener('click', xzdm('st_mrjkdj','每日健康情况登记',1,'每日健康情况登记'), false);"
dri.execute_script(js)

# button = dri.find_element_by_css_selector("a.appIco.png")
# dri.execute_script("$(arguments[0]).click()",button)

time.sleep(360)
dri.quit()