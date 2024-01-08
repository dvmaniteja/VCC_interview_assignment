import requests
import time
import urllib3
import ssl, socket
urllib3.disable_warnings()
 
class NetworkQualityTesting():
    def __init__(self,url,timeout=10,verify=False) -> None:
        self.url = url
        self.ip = self.url.split('/')[2]
        self.verify = verify
        self.timeout = timeout
    def latency(self):
        try:
            t1 = time.perf_counter()
            r = requests.get(self.url,timeout=self.timeout,verify=self.verify)
            t2 = time.perf_counter()
            tim = t2-t1
            return '{:.6f}s for the roundtrip'.format(tim)
        except requests.exceptions.ConnectTimeout:
            return("unable to connect to the host {}".format(self.ip))
        except requests.exceptions.SSLError as e:
            return('Unable to verify certificate')
 
    def rtt(self):
        try:
            t1 = time.time()
            r = requests.get(self.url,timeout=self.timeout,verify=self.verify)
            t2 = time.time()
            tim = str(t2-t1)
            return tim
        except requests.exceptions.ConnectTimeout:
            return("unable to connect to the host {}".format(self.ip))
        except requests.exceptions.SSLError as e:
            return('Unable to verify certificate')
    def cert_info(self):
        try:
            ctx = ssl.create_default_context()
            with ctx.wrap_socket(socket.socket(), server_hostname=self.ip) as s:
                s.connect((self.ip, 443))
                cert = s.getpeercert()
            subject = dict(x[0] for x in cert['subject'])
            issued_to = subject['commonName']
            issuer = dict(x[0] for x in cert['issuer'])
            issued_by = issuer['commonName']
            return issued_to,issued_by
        except ssl.SSLCertVerificationError as e:
            return(e.reason, e.verify_message)
            return("unable to verify the certificate")      
 
 
obj = NetworkQualityTesting(url="https://www.google.com/")
print(obj.latency())
print(obj.rtt())
print(obj.cert_info())