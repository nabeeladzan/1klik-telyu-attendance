from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
import json
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from jadwal import schedule

f = open('config.json', 'r')
config = json.load(f)
browser = config['browser']
username = config['username']
password = config['password']
jenis_tempat_tinggal = config['asrama']
tempat_tinggal = config['kos']
subjenis_tempat_tinggal = config['rumahOrtu']
kota = config['kota']

today = datetime.datetime.today().weekday()
path = "./drivers/"+ browser +".exe"
driver = webdriver.Edge(executable_path=path)
actions = ActionChains(driver)
driver.get("https://checkin.telkomuniversity.ac.id/home")

site = driver.find_element_by_tag_name("body")

def inputMataKuliah(matkul, jamMulai, jamSelesai):
    driver.find_element_by_name("tipePerkuliahan").click()
    driver.find_element_by_name("mataKuliah").send_keys(matkul)
    driver.find_element_by_name("timeStart").click()
    if jamMulai > 12:
        start = jamMulai - 12
        driver.find_element_by_xpath("/html/body/time-picker/div/div/div[1]/div[2]/div[2]").click()
    else:
        start = jamMulai
    driver.find_element_by_id("timepicker-item-id-" + str(start)).click()
    driver.find_element_by_xpath("/html/body/time-picker/div/div/div[3]/button[2]").click()
    driver.find_element_by_name("timeEnd").click()
    if jamSelesai > 12:
        end = jamSelesai - 12
        driver.find_element_by_xpath("/html/body/time-picker/div/div/div[1]/div[2]/div[2]").click()
    else:
        end = jamSelesai
    driver.find_element_by_id("timepicker-item-id-" + str(end)).click()
    driver.find_element_by_xpath("/html/body/time-picker/div/div/div[3]/button[2]").click()
    driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-ui-modal/div/div/div/div[2]/div/form/div/div[5]/div/div/button[2]").click()


while True:
        try:
            username_form = driver.find_element_by_name("username")
            password_form = driver.find_element_by_name("password")
            break
        except:
            sleep(1)
for i in username:
    username_form.send_keys(i)
username_form = driver.find_element_by_name("username")
for i in password:
    password_form.send_keys(i)

submit_login = driver.find_element_by_xpath("/html/body/app-root/app-auth/app-login/div/div/div[2]/div/form/button")
submit_login.click()
while True:
        try:
            open_menubar = driver.find_element_by_class_name("mobile-menu")
            break
        except:
            sleep(1)
open_menubar.click()
sleep(2)
while True:
        try:
            presensi = driver.find_element_by_link_text("Presensi Harian")
            break
        except:
            sleep(1)

presensi.click()
sleep(3)
if today == 1 or today == 6:
    driver.find_element_by_id("isWeekday2").click()
else:
    driver.find_element_by_id("isWeekday1").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-card/div/div/wizard/div/wizard-step[1]/form/app-card[3]/div/div[2]/div/div[1]/div/button").click()
    for i in schedule[today]:
        inputMataKuliah(i[0], i[1], i[2])
    driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-ui-modal/div/div/div/div[2]/div/form/div/div[5]/div/div/button[1]").click()
sleep(2)
selanjutnya = driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-card/div/div/wizard/div/wizard-step[1]/form/div/div/div")
selanjutnya.click()
sleep(1)
jenis_tempat_tinggal_sel = driver.find_element_by_name("tempatTinggal").click()
if jenis_tempat_tinggal is True:
    driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-card/div/div/wizard/div/wizard-step[2]/app-card/div/div[2]/form/div/div/div/ng-select/select-dropdown/div/div[2]/ul/li[1]/span").click()
else:
    driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-card/div/div/wizard/div/wizard-step[2]/app-card/div/div[2]/form/div/div/div/ng-select/select-dropdown/div/div[2]/ul/li[2]/span").click()


tempat_tinggal_sel = driver.find_element_by_name("houseType").click()
if tempat_tinggal is True:
    driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-card/div/div/wizard/div/wizard-step[2]/app-card/div/div[2]/form/div/div[2]/div/ng-select/select-dropdown/div/div[2]/ul/li[1]/span").click()
else:
    driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-card/div/div/wizard/div/wizard-step[2]/app-card/div/div[2]/form/div/div[2]/div/ng-select/select-dropdown/div/div[2]/ul/li[2]/span").click()


subjenis_tempat_tinggal_sel = driver.find_element_by_name("famhouseDestination").click()
if subjenis_tempat_tinggal is True:
    driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-card/div/div/wizard/div/wizard-step[2]/app-card/div/div[2]/form/div/div[3]/div/ng-select/select-dropdown/div/div[2]/ul/li[1]/span").click()
else:
    driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-card/div/div/wizard/div/wizard-step[2]/app-card/div/div[2]/form/div/div[3]/div/ng-select/select-dropdown/div/div[2]/ul/li[2]/span").click()

driver.find_element_by_name("famhouseCity").send_keys(kota)
driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-card/div/div/wizard/div/wizard-step[2]/div/div/div/button[2]").click()
driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-card/div/div/wizard/div/wizard-step[3]/app-card/div/div/form/div/div/div/div/div[1]/input").click()
driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div/div/app-presence/app-card/div/div/wizard/div/wizard-step[3]/div/div/div/button[2]").click()
sleep(5)
driver.close()