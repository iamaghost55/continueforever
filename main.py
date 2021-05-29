# PRICE.PY
import time
import random
import multiprocessing
from selenium import webdriver
from selenium_stealth import stealth

from datetime import date
today = date.today().strftime("%d%m%Y")

import socket
import threading

# _________SOCKET____________________________________________________________________________________________________________
HEADER = 64
PORT = 7676
HOST_NAME = socket.gethostname()

#SERVER = "127.0.0.1"
#SERVER = '127.0.0.1'
SERVER = socket.gethostbyname(HOST_NAME)
FORMAT = 'utf-8'
DISCONNECTED = "!DISCONNECTED"
ADDR = (SERVER,PORT)

# connect to server.py
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        print("trying to connect")
        client.connect(ADDR)
        break
    except:
        print("no connection to host")
        continue
# _________________________________________________________________________________________________________________________

# time scales for waiting
lang = random.uniform(3000,6001) # 30-60min
kurz = random.uniform(0.8,2)
kurzmittel = random.uniform(3,10)
mittel = random.uniform(300,600)
kurzmitbisschenlang = [kurz, kurz, kurz, kurz, kurz, kurz, kurz, kurz, kurz, kurz, kurz, kurz, kurzmittel, kurzmittel]#, mittel]
kurzmitmehrlang = [kurz, random.uniform(2,3), random.uniform(2,4), random.uniform(3,5)]

# SELENIUM ________________________________________________________________________________________________________________________________________________________-
agentur_code = "DE5902553"
Agent_ID = "DE5902553"
Passwort = "Isik4543"

url = "https://www.sunexpress.com/reservation/ibe/login?locale=tr"
path = "C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe"

UA = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",]
PROXY_LIST = ["34.200.144.37:8080", '80.248.15.86:8080']
# ____________________________________________________________________________________________________________________________________________________________________________________

PNR_PREISVERGLEICH_LIST = []
PNR_PREISVERGLEICH_DICT = {}
PNR = dict()

vorübergehende_test_liste = ["ali", "kaya", 15062021,15000,"22072021",12082021,2120,"dus","esb"]

PNR_LISTE = []
PNR_LISTE_VERGLEICH = []

#print(int(PNR_LISTE[0][4][2:4]))
#print(PNR_LISTE[0][7].upper())
#print(PNR_LISTE[0][8].upper())

class BackgroundTasks(threading.Thread):
    def run(self,*args,**kwargs):
        while True:
            print('Background listening')
            #toaster.show_toast("Information", "Überprüfe Inbox...", icon_path=None, duration=10, threaded=True)

            encodedmessage = client.recv(64)
            if encodedmessage:
                print("message received from server")
                # encodedmessage = client.recv(64)
                message = encodedmessage.decode(FORMAT)
                # print(message)
                # preis_list_constructor(message)
                PNR_LISTE.append(message.split())
                #toaster.show_toast("preisveränderung", "PNR Preis hat sich verändert", icon_path=None, duration=10, threaded=True,)# callback_on_click=tabelle)
            else:
                print("nothing received")
                time.sleep(12)
            """try:
                print("checking for messages")

                encodedmessage = client.recv(64)
                message = encodedmessage.decode(FORMAT)
                print(message)
                toaster.show_toast("preisveränderung", "PNR Preis hat sich verändert", icon_path=None, duration=10, threaded=True, callback_on_click=tabelle)
            except:
                print("nothing received")
            time.sleep(60)
            """

thread = BackgroundTasks()
thread.start()

def compare_sort():
    pass
def check_frist():
    pass

num = -1
while True:
    print(f"{num}: loop started")

    # if not first time looping -> wait long
    if num > 0:
        print(f"{num}: sleeping long")
        time.sleep(random.choice(lang))
        pass

    # if we scraped the whole PNR list, start PNR list looping from the beginning by making num -1
    if len(PNR_LISTE) == num:
        print(f"Pnr list completed: {len(PNR_LISTE)} - {num}")
        num = -1
        pass

    # check flight, scrape data, send to server.py
    def buchungssuche():
        global num
        print(f"{num}: logging in")
        driver.get(url)
        # cookie
        time.sleep(random.choice(kurzmitbisschenlang))  # wait
        driver.find_element_by_id("onetrust-accept-btn-handler").click()

        # LOGIN
        time.sleep(random.choice(kurzmitbisschenlang))  # wait
        driver.find_element_by_name("agencyCode").send_keys(agentur_code)
        time.sleep(random.choice(kurzmitbisschenlang))  # wait
        driver.find_element_by_name("agencyId").send_keys(Agent_ID)
        time.sleep(random.choice(kurzmitbisschenlang))  # wait
        driver.find_element_by_name("password").send_keys(Passwort)
        time.sleep(random.choice(kurzmitbisschenlang))  # wait
        driver.find_element_by_xpath('//button[@type="button"]').click()

        numnum = 0
        while True: # einstellen wieviele ich bei einem loop scrapen soll, max 3?
            # einstellen, dass wenn num > len(PNR_LISTE) -> num zurücksetzen
            num += 1
            numnum += 1
            print(f"{num}: staring PNR loop")
            # delete element if option time is reached
            if PNR_LISTE[num][2] == today:  # noch optimieren
                print(f"{num}: optionsfrist abgelaufen")
                PNR_LISTE[num].pop(2)
                pass

            def eingabe():
                    print(f"{num}: choosing flight")
                    time.sleep(random.choice(kurzmitbisschenlang))  # wait
                    time.sleep(random.choice(kurzmitbisschenlang))  # wait
                    driver.find_element_by_id("aiRESOrigin0_chosen").click()
                    time.sleep(random.choice(kurzmitbisschenlang))  # wait
                    kalkis_liste = driver.find_elements_by_xpath("//li[@class='active-result']")
                    time.sleep(random.choice(kurzmitbisschenlang))  # wait
                    for kalkis in kalkis_liste:
                        # print(kalkis.text)
                        if kalkis.text[-4:-1] == PNR_LISTE[num][7].upper():
                            print(kalkis.text + "1111111")
                            time.sleep(random.choice(kurzmitbisschenlang))
                            kalkis.click()
                            break
                    time.sleep(random.choice(kurzmitbisschenlang))  # wait
                    driver.find_element_by_id("aiRESDestination0_chosen").click()
                    time.sleep(random.choice(kurzmitbisschenlang))  # wait
                    varis_liste = driver.find_elements_by_xpath("//div[@id='aiRESDestination0_chosen']//div[@class='chosen-drop']//li[@class='active-result']")
                    time.sleep(random.choice(kurzmitbisschenlang))
                    for varis in varis_liste:
                        # print(varis.text)
                        if varis.text[-4:-1] == PNR_LISTE[num][8].upper():
                            print(varis.text)
                            time.sleep(random.choice(kurzmitbisschenlang))
                            varis.click()
                            break
                    # driver.find_element_by_id("aiRESDestination0_chosen").send_keys(PNR_LISTE[num][8])
                    time.sleep(random.choice(kurzmitbisschenlang))  # wait
                    driver.find_element_by_xpath(f"//*[@id='search-form']/div[4]//input[@placeholder='gg/aa/yyyy']").send_keys(PNR_LISTE[num][4])
                    # driver.find_element_by_id("search-date-outward")
                    # year = driver.find_element_by_xpath(f"//div[@id='ui-datepicker-div']//div[@class='ui-datepicker-title']//select[@class='ui-datepicker-year']//option[@value={PNR_LISTE[0][4][4:8]}")
                    # for year in year_list:
                    #   if year.text == PNR_LISTE[num][4]:
                    #      year.click()
                    #     break
                    # driver.find_element_by_id("search-date-outward").send_keys(PNR_LISTE[num][4])

                    # month = driver.find_element_by_xpath(f"//div[@id='ui-datepicker-div']//div[@class='ui-datepicker-title']//select[@class='ui-datepicker-month']//option[@value={int(PNR_LISTE[0][4][2:4])}")
                    time.sleep(random.choice(kurzmitmehrlang))  # wait
                    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[1]").click()
                    time.sleep(random.choice(kurzmitbisschenlang))
                    # day = driver.find_elements_by_xpath(f"//*[@id='ui-datepicker-div']/table//tbody//tr")
                    # days = driver.find_elements_by_xpath("//*[@id='ui-datepicker-div']//table//tbody//tr//td")
                    # for day in days:
                    #   print(day.text)
                    #  if day.text == PNR_LISTE[num][4][0:2]:
                    #     day.click()
                    #    time.sleep(random.choice(kurzmitbisschenlang))
                    #   break

                    # driver.find_element_by_id("proceed").click()
                    driver.find_element_by_xpath(
                        "/html/body/div[4]/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[1]").click()
                    time.sleep(random.choice(kurzmitbisschenlang))  # wait
                    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[1]/form/div[3]/div[1]/div/div/div/div[8]/div/input").click()
                    print("done")
            eingabe()
            def scrapee():
                time.sleep(random.choice(kurzmitbisschenlang))
                clock = driver.find_element_by_xpath("//*[@id='search']/div[2]/div[1]/div[3]/div[1]/div/table/tbody/tr[1]/td[1]/div[1]")
                print(f"{num}: comparing times -> {PNR_LISTE[num][6]}:{clock.text[0:2] + clock.text[3:5]}")

                # ICH GLAUBE DER VERÄNDERT DEN PREIS EGAL OB GEICH ODER NICHT. ALSO KRIEGT CLIENT.PY EIN TOAST NOTIFICATION OBGLEICH VERÄNDERUNG ODER NCIHT
                # IF STATEMENTS MÜSSEN NOCH EINGE BAUT WERDEN. IF PREIS TEURER SCHICK DAS; IF NOT SCHICK DAS
                if PNR_LISTE[num][6] == clock.text[0:2] + clock.text[3:5]:
                    time.sleep(random.choice(kurzmitbisschenlang))
                    new_price = driver.find_element_by_xpath("//*[@id='search']/div[2]/div[1]/div[3]/div[1]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/div/span/span[1]/strong")
                    print(f"the new price is {new_price.text}")
                    # new_price_str = new_price.text[0:1] + new_price.text[3:4]
                    new_price_str = new_price.text[-10:-7] + new_price.text[-6:-4]
                    PNR_LISTE_VERGLEICH = PNR_LISTE
                    PNR_LISTE_VERGLEICH[num][3] = new_price_str
                    print(PNR_LISTE_VERGLEICH)
                    notification = " ".join(PNR_LISTE_VERGLEICH[num])
                    # print(notification)
                    # send new PNR to server.py
                    def sendmessage(msg):
                        print(notification)
                        notification_encoded = msg.encode(FORMAT)
                        client.send(notification_encoded)
                        print("notification sent to client.py")
                    sendmessage(notification)
                    # [['Fatih', 'Senguel', '22222222', '10000', '21042021', '89665675', '2215', 'ada', 'ams']]
                    pass
            scrapee()
            if numnum == 4:
                break
            elif len(PNR_LISTE) == num:
                break

    # if we received a message -> set selenium options and call buchungssuche()
    # neue ip erst nach einigen malen noch machen
    if len(PNR_LISTE) != 0:
        print(f"{num}: setting new options. New PNR: {PNR_LISTE}")
        options = webdriver.ChromeOptions()
        prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_encoded_extension("useAutomationExtension", False)
        options.add_experimental_option('useAutomationExtension', False)

        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options, executable_path=path)

        stealth(driver,
                user_agent=random.choice(UA),
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True, )
        options.add_argument("--proxy-server=%s" % random.choice(PROXY_LIST))
        buchungssuche()
    else:
        print("waiting...")
        time.sleep(random.uniform(5,20))
        #time.sleep(random.uniform(300,400))
        continue

# p1 = multiprocessing(target=compare_sort())