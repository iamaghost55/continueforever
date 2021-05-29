import socket
import threading
import pprint

import time

# information kayidi ve kullanmak icin gerekli DEGISKENLER
SCRAPER = []            # Class halinde toplaniyor, Liste üzeri belli KURYER secilebiliyor
DÜKKANLAR = []              # Class halinde toplaniyor, Liste üzeri belli DÜKKAN secilebiliyor
total_connections = 0       # toplam baglantilar


# x = [100,2,300,4,75]
# dct = {}
#for i in x:
#    dct['lst_%s' % i] = []

# print(dct)
# {'lst_300': [], 'lst_75': [], 'lst_100': [], 'lst_2': [], 'lst_4': []}


# Kuryerci class, her KURYERCI icin yeni bir örnek
# Her örnek in socket'i ve adresi ile iliskili maddeleri var
# Atanmış bir kimlik ve müşteri tarafından seçilen bir adla birlikte
# Send KURYERCI data to DÜKKANLAR
class Kuryerci(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    # KURYERCIDEN Data alma deneyi
    # Mesaj alinamiyorsa, KURYERCI baaglantiyi kesti diye kabullen   !!!YANLIS OLABILIR!!!
    # If able to and we get data back, print it in the server and send it back to the same client

    def scrape(self):
        print("scraping...")

# Class of PRICE.py
# send PRICE data to CLIENT
class Price(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    # Attempt to get data from client
    # If unable to, assume client has disconnected and remove him from server data
    # If able to and we get data back, print it in the server and send it back to every
    # client aside from the client that has sent it
    # .decode is used to convert the byte data into a printable string
    def run(self):
        num = 0

        while self.signal:
            num += 1
            try:
                data = self.socket.recv(90)
                # print(f"New message from {self.address}: {data.decode('utf-8')}")
            except:
                print("Kuryerci " + str(self.address) + " has disconnected")
                self.signal = False
                DÜKKANLAR.remove(self)
                break
            if data.decode("utf-8") != "":
                dct[self.address[0]].append(data.decode("utf-8"))
                """if num > 0:
                    for key in dct.keys():
                        
                        if str(self.address[0]) == key[0]:
                            dct[self.address].append(data.decode("utf-8"))
                        else:
                            pass"""
                pprint.pprint(dct)
            else:
                pass

            #except:
            #    print("Kuryerci " + str(self.address) + " has disconnected")
            #    self.signal = False
            #    DÜKKANLAR.remove(self)
            #    # break

            # print(str(self.address))
            # print(len(dict))
            #for i in dct.keys():
             #   if i == self.address:
              #      dct[f"{self.address}"] = "11"            continue
            """if data != "":
                # print("PRICE ID" + str(self.id) + ": " + str(data.decode("utf-8")))

                for kuryerci in KURYERCILER:
                    if kuryerci.address == self.address:
                        kuryerci.socket.sendall(data)"""

"""class Scrape(threading.Thread):
    def __init__(self, socket, address,):
        self.address = address
        self.socket = socket
    def __str__(self):
        return str(self.id) + " " + str(self.address)

    def scraper(self):
        print("scrape...")
        print(self.address)
"""
#def scrape():
#    # und separaten thread starten

dct = {}

# Baglanti geliyor mu diye sonsuza dek bekle
def yeniBaglantilar(socket):
    num = -1
    while True:

        # gelen baglantiyi kabul et
        sock, address = socket.accept()
        # dct[address[0]] = []
        num += 1 # only because i couldnt find another local up for client.py
        # dct['Agent %s' % num + f" {str(address)}"] = []

        if bool(dct) != False:
            for key in list(dct.keys()):
                if key != address[0]:
                    dct[address[0]] = []
        else:
            dct[address[0]] = []
        #print(dct)

        global total_connections
        # print(address)

        if Price(sock, address, total_connections, "Name", True) in DÜKKANLAR:
            pass
        else:
            DÜKKANLAR.append(Price(sock, address, total_connections, "Name", True))
            DÜKKANLAR[len(DÜKKANLAR) - 1].start()
        # print("New connection | DÜKKAN")
        # DÜKKANLAR.append(Price(sock, address, total_connections, "Name", True))
        # DÜKKANLAR[len(DÜKKANLAR) - 1].start()
        # print(type(DÜKKANLAR[len(DÜKKANLAR) - 1]))

        # SCRAPER.append(Kuryerci(sock, address, total_connections, "Name", True))
        # SCRAPER[num].start()
        #SCRAPER = Scrape(sock, address)
        #print(type(SCRAPER))
        #SCRAPER.start()

        # Baglanti KURYECI den ise
        # KURYECILER Listesine "Kuryeci(sock, addressm total_connections, "Name", True)" ekle
        # SORUN: SERVER KURYERCI VE DÜKKANLARI KARISTIRMAMASI LAZIM. (Her Kuryercinin ve Dükkanin özel ismi lazim, ve bu isime göre "name" yerini degistiririz.
            # bu listeler önemli ve güzel organizasyonu gerek!!!!!!!!!!!!!!!!!!!!!
        """if address[0] != 'kuryeciadresi' and num != 0:  # böyle degistirmemiz gerek => if address[0] in KURYERCILER, cünkü kuryerciler listesi büyük olcak. Kuryerciden baglanti geldi ise, hangi kuryer olduna bak ve sonra O kuryere Göre Class ac


            # Kuryer Class'ini calistir
            KURYERCILER.append(Kuryerci(sock, address, total_connections, "Name", True))
            KURYERCILER[len(KURYERCILER) - 1].start()
            print("New connection | KURYER " + str(KURYERCILER[len(KURYERCILER) - 1]))
            total_connections += 1
            client_ip = address[0]

        # Baglanti DÜKKAN dan ise
        # DÜKKANLAR Listesine Dükkanlar(sock, address, total_connections, "Name", True) ekle
        # yukaridaki ayni sorun
        else:                                           # suanki hali sadece bir dükkan icin. Cogul gerek.
            print("New connection | DÜKKAN")
            DÜKKANLAR.append(Price(sock, address, total_connections, "Name", True))
            DÜKKANLAR[len(DÜKKANLAR) - 1].start()
            price_ip = address[0]
            #return price_ip"""
        continue

# Serveri kur ve interneti dinle (dinle <=> baglanti ara, baglanmak istiyen var mi diye bak)
def main_recv():
    # host ve port kur
    host = ""           # "" <=> her gelen IP-Adresi kabul et
    port = 7979

    # Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    # Yeni Thread kur ve "yeniBaglantilar" fonksyonunu ac
    newConnectionsThread = threading.Thread(target=yeniBaglantilar, args=(sock,))
    newConnectionsThread.start()


# main fonksoynunu ac
main_recv()


# PROGRAMDAKI ORTAYA CIKACAK OLABILEN SORUNLAR
"""

"""