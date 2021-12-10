import os
import time
import sys

os.system("clear")

logo = """\033[32m

╭━━┳━┳━━┳━━╮╱╭━┳━━┳╮╱╭┳━━━╮
┃╭━┫┃┃╭╮┣╮╭┻━┫╋┃━━┫┃╱┃┃╭━━╯
┃╰╮┃┃┃┣┫┃┃┣━━┫╮╋━━┃╰━╯┃╰━━╮
╰━━┻━┻╯╰╯╰╯╱╱╰┻┻━━┻━━╮┣━━╮┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┣━━╯┃	"""
print (logo)
time.sleep(1.0)

logo1 = """\033[32m+--------------------------------------+
| This Tool Install All Basic Packages |
+--------------------------------------+
| Coded By Ranuja  | version : 1.0     |
+--------------------------------------+"""
print (logo1)


time.sleep(1.0)

def tprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

print ()

tprint('''\033[32m
[01] python
[02] nmap
[03] ruby
[04] php
[05] java
[06] macchanger''')

tprint('''\033[32m
[+] ආතල් එකට ගහපු ටූලක් හොදේ....''')

print("[+] Tool by Ranuja Sanmira")
