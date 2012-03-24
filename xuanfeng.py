#!/usr/bin/env python3
import hashlib
from urllib import request,parse
from http import cookiejar
import re,random,time
import threading as th
import json,os
class XF:
    """
     Login QQ
    """
    __headers ={
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.9 Safari/534.30',\
                'Referer':'http://ptlogin2.qq.com/login?u=445644667&p=11BDE88FB5BA931B10B808976DD6308D&verifycode=!ERV&aid=567008010&u1=http%3A%2F%2Flixian.qq.com%2Fmain.html&h=1&ptredirect=1&ptlang=2052&from_ui=1&dumy=&fp=loginerroralert&action=2-6-36444&mibao_css='\
    }
    __cookiepath = '/tmp/cookie'
    __downpath = '/home/maplebeats/Downloads/xuanfeng.down'
    __qq = None
    __pswd = None
    __verifycode = None
    __clientid = 21628014
    __http = {}
    __psessionid = ''
    __ptwebqq = ''
    __vfwebqq = ''
    __skey = ''
    __poll2 = None
    __get_msg_tip = None
    __rc = 0
    __send_num = 31330000
    def __init__(self):
        self.httpproess()
        self.__Login()
        pass
    def __preprocess(self,password,verifycode):
        """
            QQ密码加密部份
        """
        return hashlib.md5( (self.__md5_3((password).encode('utf-8')) + (verifycode).upper()).encode('utf-8')).hexdigest().upper()
        pass

    def __md5_3(self,str):
        """
            QQ密码md5_3部份
        """
        return hashlib.md5(hashlib.md5(hashlib.md5(str).digest()).digest()).hexdigest().upper()
        pass
    def httpproess(self):
        """
            初始化模拟进程
        """
        self.__http['cj'] = cookiejar.MozillaCookieJar(self.__cookiepath)
        self.__http['opener'] = request.build_opener(request.HTTPCookieProcessor(self.__http['cj']))
        return self.__http
        pass
    def __request(self,url,method='GET',data={},savecookie=False):
        """
            请求url
        """
        if (method).upper() == 'POST':
            data = parse.urlencode(data).encode('utf-8')
            self.__http['req'] = request.Request(url,data,self.__headers)
        else:
            self.__http['req'] = request.Request(url=url,headers=self.__headers)
        fp = self.__http['opener'].open(self.__http['req'])
        try:
            str = fp.read().decode('utf-8')
        except UnicodeDecodeError:
            str = fp.read()
        if savecookie == True:
            self.__http['cj'].save(ignore_discard=True,ignore_expires=True)
        fp.close()
        return str
        pass
    def __getcookies(self,name):
        fp = open(self.__cookiepath)
        fp.seek(130)
        for read in fp.readlines():
            str = read.split(name)
            if len(str) == 2:
                fp.close()
                return str[1].strip()
        fp.close()
        return None
        pass
    def __getverifycode(self):
        """
            @url:http://ptlogin2.qq.com/check?uin=644826377&appid=1003903&r=0.56373973749578
        """
        urlv = 'http://ptlogin2.qq.com/check?uin='+ ('%s' % self.__qq)+'&appid=1003903&r='+ ('%s' % random.Random().random())
        str = self.__request(url = urlv, savecookie=True)
        str = re.findall(r'\d|(?<=\')[a-zA-Z0-9\!]{4}',str)
        return str
        pass
    def __request_login(self):
        """
            @url:http://ptlogin2.qq.com/login
            @params:{u:644826377
                    p:73DA5C1145E0F82247F60B3A17B89E6A   verifycode:!S10   webqq_type:10
                    remember_uin:1  login2qq:1  aid:1003903  u1:http://webqq.qq.com/loginproxy.html?login2qq=1&webqq_type=10
                    h:1  ptredirect:0   ptlang:2052  from_ui:1   pttype:1  dumy:
                    fp:loginerroralert   action:1-24-62651  mibao_css:m_webqq}
        """
        urlv = 'http://ptlogin2.qq.com/login?u='+('%s' %  self.__qq) +'&' +  'p=' + ('%s' % self.__pswd) +  '&verifycode='+ ('%s' % self.__verifycode[1]) +'&remember_uin=1&aid=1003903' +  "&u1=http%3A%2F%2Flixian.qq.com%2Fmain.html" +  '&h=1&ptredirect=0&ptlang=2052&from_ui=1&pttype=1&dumy=&fp=loginerroralert'
        str = self.__request(url = urlv,savecookie=True)
        if str.find('登录成功') != -1:
            #执行二次登录
            self.__ptwebqq = self.__getcookies('ptwebqq')
            self.__skey = self.__getcookies('skey')
            self.__getlogin()
            self.__getlist()
            self.__gethttp()
            self.__creatfile()
            self.__download()
        elif str.find('不正确') != -1:
            print('你输入的帐号或者密码不正确，请重新输入。')
        else:
            print('登录失败')
        pass
    def __getlogin(self):
            urlv = 'http://lixian.qq.com/handler/lixian/do_lixian_login.php'
            str = self.__request(url =urlv,method = 'POST')
            #登陆旋风，可从str中得到用户信息

    def __getlist(self):
            """
            得到任务名与hash值
            """
            urlv = 'http://lixian.qq.com/handler/lixian/get_lixian_list.php'
            str = self.__request(urlv,'POST')
            str = json.JSONDecoder().decode(str)
            self.filename = []
            self.filehash = []
            for num in range(len(str['data'])):
                    self.filename.append(str['data'][num]['file_name'])
                    self.filehash.append(str['data'][num]['hash'])
                    print(self.filename[num])

    def __gethttp(self):
            """
            获取任务下载连接以及FTN5K值
            """
            urlv = 'http://lixian.qq.com/handler/lixian/get_http_url.php'
            self.filehttp = []
            self.filecom = []
            for num in range(len(self.filename)):
                    data = {'hash':self.filehash[num],'filename':self.filename[num],'browser':'other'}
                    str = self.__request(urlv,'POST',data)
                    self.filehttp.append(re.search(r'\"com_url\":\"(.+?)\"\,\"',str).group(1))
                    self.filecom.append(re.search(r'\"com_cookie":\"(.+?)\"\,\"',str).group(1))
           
    def __creatfile(self):
            """
            建立aria2下载文件
            """
            f = open(self.__downpath,'w')
            for num in range(len(self.filename)):
                    f.write(self.filehttp[num] + '\n  header=Cookie: FTN5K=' + self.filecom[num] +
                    '\n  continue=true\n  max-conection-per-server=5\n  split=10\n   parameterized-uri=true\n\n')
                    
    def __download(self):
            """
            调用aria2进行下载
            """
            os.system(r'aria2c -i %s' % self.__downpath)      
                    
    def __Login(self):
        """
        登录
        """
        self.__qq = input('QQ号：')
        self.__pswd = input('QQ密码：')
        self.__qq = self.__qq.strip()
        self.__pswd = self.__pswd.strip()
        self.__verifycode = self.__getverifycode()
        self.__pswd = self.__preprocess(
            self.__pswd,#密码 \
            '%s' % self.__verifycode[1]  #验证码 \
        )
        self.__request_login()
        pass

s = XF()
