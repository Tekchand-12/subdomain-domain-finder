import requests,threading,sys,time,termcolor,warnings

domain=set()
warnings.filterwarnings('ignore')
storage=set()
if sys.argv < 1:
        print "Usage: python subdomain.py url list"
        sys.exit(1)
else:                                                                                                                         with open(str(sys.argv[2]),'rb') as fp:                                                                                       for i in fp.readlines():
                        storage.add(str(i).replace("\n",''))
        def handler(msfhandler):                                                                                                      data=str(sys.argv[1])                                                                                                 if data.startswith("https"):                                                                                                  https=data.split(data[7:8])
                        https[0]="https://"
                        https.insert(1,msfhandler+".")
                        handler.maker="".join(https)
                else:
                        http=data.split(data[6:7])
                        http[0]="http://"
                        http.insert(1,msfhandler+".")
                        handler.maker="".join(http)
                try:
                        requests.get(handler.maker,allow_redirects=True,verify=False)
                        sys.stdout.write("\r"+str(termcolor.colored("[+] subdomain found -> %s\n" % (handler.maker),"y
ellow",attrs=['reverse'])))
                        domain.add(handler.maker)
                        sys.stdout.flush()
                except:
                        sys.stdout.write("\r"+termcolor.colored("[*]Processing -> %s" % (handler.maker),"cyan",attrs=[
'bold']))
                        sys.stdout.flush()
if __name__ == "__main__":
        for j in storage:
                remote=threading.Thread(target=handler,args=(j,))
                remote.start()
                remote.join()
with open("domains.txt","a+") as mp:
        for t in domain:
            mp.writelines(t+"\n")
~
