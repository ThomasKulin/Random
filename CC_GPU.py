import requests
import datetime
import time
import os
import threading

# name, api call
links_3060ti = [["GIGABYTE RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=188703"],
         ["EVGA RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185988"],
         ["EVGA RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185987"],
         ["ZOTAC RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185752"],
         ["ZOTAC RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185751"],
         ["GIGABYTE RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185408"],
         ["GIGABYTE RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185407"],
         ["GIGABYTE RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185405"],
         ["ASUS RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185168"],
         ["MSI GeForce RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185087"],
         ["MSI RTX 3060 Ti ", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185086"],
         ["ASUS RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184760"],
         ["ASUS RTX 3060 Ti", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184759"],
         ["ASUS RTX 3060 Ti ", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184431"],
         ]

links_3070 = [["Gigabyte RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184167"],
         ["Gigabyte RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183101"],
         ["MSI RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183210"],
         ["Gigabyte RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183099"],
         ["EVGA RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183500"],
         ["ASUS RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183636"],
         ["Gigabyte RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184167"],
         ["ASUS RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183637"],
         ["MSI RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183208"],
         ["ASUS RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183637"],
         ["Gigabyte RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184168"],
         ["EVGA RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183498"],
         ["ASUS RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183638"],
         ["ZOTAC RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183561"],
         ["MSI RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183209"],
         ["EVGA RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183499"],
         ["ASUS RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184743"],
         ["Gigabyte RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183100"],
         ["ZOTAC RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183560"],
         ["ZOTAC RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185675"],
         ]

links_3080 = [["ASUS RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181842"],
         ["MSI RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181348"],
         ["ASUS RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181415"],
         ["MSI RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181347"],
         ["Gigabyte RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181354"],
         ["EVGA RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181375"],
         ["Gigabyte RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181353"],
         ["zotac RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181420"],
         ["Gigabyte RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=182754"],
         ["Gigabyte RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=182755"],
         ["evga RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181797"],
         ["Gigabyte RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183098"],
         ["asus RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=186309"],
         ["zotac RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183510"],
         ["gigabyte RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184166"],
         ["zotac RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184837"],
         ["msi RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185084"],
         ["gigabyte RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=186345"],
         ]

links_3090 = [["MSI RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=185085"],
         ["GIGABYTE RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184164"],
         ["ASUS RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181413"],
         ["GIGABYTE RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=188242"],
         ["GIGABYTE RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=188241"],
         ["GIGABYTE RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=187349"],
         ["ASUS RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=186355"],
         ["ASUS RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=186308"],
         ["GIGABYTE RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184165"],
         ["Gigabyte RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=182755"],
         ["GIGABYTE RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=183096"],
         ["EVGA RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181854"],
         ["EVGA RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181853"],
         ["ASUS RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181841"],
         ["ZOTAC RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181419"],
         ["GIGABYTE RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181352"],
         ["GIGABYTE RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181351"],
         ["MSI  RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181350"],
         ["MSI RTX 3090", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181349"],
         ]



def func_3070():
    func(links_3070)

def func_3080():
    func(links_3080)

def func(links):
    while True:
        for i in range(len(links)):
            DateTime = datetime.datetime.now().strftime("%Y_%m_%d %H_%M").replace('.', '-')
            try:
                response = requests.get(links[i][1]).content.decode("utf-8")
            except:
                print("connection failed")
            if response != '{"loc":"All Locations","avail":0,"avail2":"NO AVAILABLE","loc2":"ONLINE"}' and response != '{"loc":"ONLINE","avail":0}':
                print(DateTime + '\t' + links[i][
                    0] + '\t' + response + '\nhttps://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=' +
                      links[i][1][-6:])
                os.system("KillingInTheName.mp3")

        time.sleep(1)

thread_3070 = threading.Thread(target=func_3070)
thread_3070.start()
thread_3080 = threading.Thread(target=func_3080)
thread_3080.start()