import requests
import datetime
import time
import os

# name, api call
links = [["Gigabyte RTX 3070", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=184167"],
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
         ["ASUS RTX 3080", "https://www.canadacomputers.com/product_info.php?ajaxstock=true&itemid=181842"],
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

flag = [0 for p in range(len(links))]

while True:
    for i in range(len(links)):
        DateTime = datetime.datetime.now().strftime("%Y_%m_%d %H_%M").replace('.', '-')
        try:
            response = requests.get(links[i][1]).content.decode("utf-8")
        except:
            print("connection failed")
        if flag[i] == 0 and response != '{"loc":"All Locations","avail":0,"avail2":"NO AVAILABLE","loc2":"ONLINE"}' and response != '{"loc":"ONLINE","avail":0}':
            flag[i] = 1
            print(DateTime+'\t'+links[i][0]+'\t'+response+'\nhttps://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id='+links[i][1][-6:])
            os.system("KillingInTheName.mp3")

    time.sleep(1)