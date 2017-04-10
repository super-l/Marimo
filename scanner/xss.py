
import re,requests
from lib.core.data import paths

file = paths.DICT_PATH + '/xsses'
xsses = [line.strip() for line in open(file, 'r')]


def scan(url):
    vul = []


    for xss in xsses:
        try:
            source = requests.get(url + xss.replace("\n", "")).content
            if re.findall(str("<OY1Py"), source) or re.findall(str("<LOY2PyTRurb1c"), source):
                if url not in vul:
                    print("XSS Found ---> %s" % url)
                    vul.append(url)


        except:
            pass
    return [0,0,0]

