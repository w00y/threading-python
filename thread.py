import requests
import sys
import os
from multiprocessing import Pool

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'





count= 0
file_ip_found="jenkins_vulnurable_manage"
file_ip=sys.argv[1]
file = open(file_ip, 'rt')
urls = file.read().split('\n')
global total
total = sum(1 for line in open(file_ip))


def baner(ip,resultat,count):

    try:
        num_lines = sum(1 for line in open(file_ip_found))
    except:
        num_lines =  0
    print ("[ TOTAL ] : [ "+str(total)+" ]", end='',flush=True)
    print ("          [ TEST NUMBER ] : [ "+str(count) +" ]", end='',flush=True)
    print ("          [ Found ] : [ "+str(num_lines) +" ]")
    print ("")

    print ("  IP : [ "+bcolors.OKBLUE+ip+bcolors.BOLD +bcolors.ENDC+" ]", end='',flush=True)
    print (resultat, end='',flush=True)





















def news(url):
	global count
	count = count + 1
	#url="http://52.199.204.129:8080/
	try:

		resp=requests.get(url, timeout=5)
		if resp.status_code==200:
			if 'manage' in resp.text:
				resultat = bcolors.BOLD +bcolors.OKGREEN+"  Ok"+bcolors.BOLD +bcolors.ENDC+ '\n'
				save(url)
		os.system('clear')
		baner(url,resultat,count)
	except:
		os.system('clear')
		resultat = bcolors.BOLD +bcolors.FAIL+"  OFF"+bcolors.BOLD +bcolors.ENDC+ '\n'
		baner(url,resultat,count)






def save(api):
    with open(file_ip_found, 'a') as f:
        f.write(api + '\n')




def multi():
    p = Pool(processes=4)
    result = p.map(news, urls)




multi()
