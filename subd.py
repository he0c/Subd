#Subd.py
import socket
from colorama import init, Fore, Back, Style
init()
subdomains = ["www", "www1", "www2", "www3", "indumil", "edu", "educacion", "education", "dep", "eu", "pr", "uk", "arg", "us", "centro", "ayuda", "help", "center", "db", "sql", "database", "alcalde", "presidencia", "policia", "staff", "admin", "ayudante", "moderador", "helper", "moderator", "administrator", "administrador", "ovh", "ovh0", "ovh1", "ovh2", "ovh3", "ovh4", "ovh5", "gov", "gob", "dashboard", "idm", "anycast", "app", "embed", "panel", "autoconfig", "mc", "play", "builder", "time", "salud", "health", "home", "inicio", "img", "imagen", "nasa", "mil", "army", "milicia", "docs", "drive", "ipv3", "api", "mail", "main", "main", "book", "ftp", "smtp", "localhost", "pop", "ns1", "cpanel", "ns2", "imap", "dev", "forum", "mysql", "old", "support", "mobil", "mx", "lists", "list", "cp", "email", "phone", "ip", "demo", "portal", "dns1", "dns", "server", "game", "shell", "cloud", "my", "chat", "site", "sites", "proxy", "ads", "backup", "file", "files", "store", "tienda", "ftp1","ftp2", "ftp3", "service", "login", "moodle", "phpmyadmin", "control", "payment", "dev", "dev1", "dev2", "community", "facebook", "game", "games", "tool", "tools", "mailhost", "host2", "host", "hosts", "host1", "network", "port", "proxy", "student", "students", "assets", "wordpress", "ipfixe", "user", "users", "market", "marketplace", "dbadmin", "php"]
print("")
print(Fore.LIGHTRED_EX + """
   _____       _         _               
  / ____|     | |       | |              
 | (___  _   _| |__   __| |  _ __  _   _ 
  \___ \| | | | '_ \ / _` | | '_ \| | | |
  ____) | |_| | |_) | (_| |_| |_) | |_| |
 |_____/ \__,_|_.__/ \__,_(_) .__/ \__, |
                            | |     __/ |
                            |_|    |___/ 
                            
                            beta version by Heoc
""")
print(Fore.LIGHTYELLOW_EX + "")
print("Subd.py in process, enter the target (Only domain for example: example.com): ")
print(Fore.LIGHTCYAN_EX + "")
link = e=input("-=> ")
print("")
for heocsbd in subdomains:
    try:
        hosts = str(heocsbd) + "." + str(link)
        heocip = socket.gethostbyname(str(hosts))
        print(Fore.GREEN + ">> " + str(heocsbd) + "." + str(link) + " | " + str(heocip))
    except:
        pass