import urllib,re,requests,sys,random
from lib.core.data import paths


file = paths.DICT_PATH + '/lfi'
lfis = [line.strip() for line in open(file, 'r')]
flag = " LFI "
def scan(url):
    lfiurl = url.rsplit('=', 1)[0]

    if lfiurl[-1] != "=":
        lfiurl += "="

    for lfi in lfis:
        target = lfiurl+lfi.replace("n", "")
        try:
            check = requests.get(target).content
            if re.findall('root:',check):
                return [1,1,flag]
            else:
                return [1,0,flag]

        except:
            return [1,0,flag]

