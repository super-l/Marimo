__author__ = 'luhaoliang'

import urlparse
import re
import datetime
import time
from common import download



def link_crawler(seed_url,delay=5,max_url=100,user_agent='Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',link_regex=None):

    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    throtle = Throttle(delay)
    url_num = 0
    while crawl_queue:
        url = crawl_queue.pop()
        throtle.wait(url)
        html = download(url,user_agent)
        for link in get_links(html):
            if re.match(link_regex,link):
                link = urlparse.urljoin(seed_url,link)
                if link not in seen:
                    url_num += 1
                    seen.add(link)
                    crawl_queue.append(link)
                if url_num == max_url:
                    return crawl_queue






def get_links(html):
    webpage_regex =re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_regex.findall(html)



class Throttle:
    def __init__(self,delay):
        self.delay = delay
        self.domains = {}

    def wait(self,url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is  not None:
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.datetime.now()


# print link_crawler(seed_url="http://ccst.jlu.edu.cn",link_regex='.*',max_url=20)