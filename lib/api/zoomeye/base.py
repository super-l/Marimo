__author__ = 'luhaoliang'

import requests
import getpass


class Zoomeye:
    def __init__(self,username=None,password=None):
        self.username = username
        self.password = password
        self.token = ''
        self.zoomeye_login_api = "https://api.zoomeye.org/user/login"
        self.zoomeye_dork_api = "https://api.zoomeye.org/{}/search"

    def autologin(self):
        try:
            self.username = 'xxx'
            self.password = 'xxx'
        except:
            pass
        if bool(self.username and self.password):
            if self.get_token():
                return
        self.manual_login()



    def get_token(self):
        data = '{{"username": "{}", "password": "{}"}}'.format(self.username,self.password)
        res = requests.post(self.zoomeye_login_api,data=data)
        if res and res.status_code == 200 and 'access_token' in res.json():
            self.token = res.json().get('access_token')
            return self.token
        return False

    def set_token(self,token):
        self.token = token.strip()


    def manual_login(self):
        msg = "Please input your your Zoomeye Email and password"
        print msg

        self.username = raw_input('Zoomeye Username(Email): ')
        self.password = getpass.getpass(prompt='ZoomEye Password: ')
        if not self.get_token():
            msg = 'Invalid ZoomEye username or password.'
            print msg



    def dork_search(self,dork,page=0,resource='web',facet=['ip']):
        result = []
        if isinstance(facet,(tuple,list)):
            facet = ','.join(facet)

        zoomeye_api = self.zoomeye_dork_api.format(resource)
        headers = {'Authorization': 'JWT %s' % self.token}
        params = {'query': dork, 'page': page + 1, 'facet': facet}
        res = requests.get(zoomeye_api, params=params, headers=headers)
        if res and res.status_code == 200 and 'matches' in res.json():
            matches = res.json().get('matches')
            result = matches

        return result

    def resource_info(self):
        data = None
        zoomeye_api = "https://api.zoomeye.org/resources-info"
        headers = {'Authorization': 'JWT %s' % self.token}
        res = requests.get(zoomeye_api,headers=headers)
        if res and res.status_code == 200 and 'plan' in res.json():
            data = res.json()
        return data


def show_site_ip(data):
    if data:
        for i in data:
            print(i.get('site'), i.get('ip'))


def show_ip_port(data):
    if data:
        for i in data:
            print(i.get('ip'), i.get('portinfo').get('port'))






