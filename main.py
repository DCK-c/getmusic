import base64
from tornado import web,ioloop;
import json;
import re;
import time;
import random;
import csv;
from Crypto.Cipher import AES;
import os;
def wt(string):
    with open("dairy.log", "a", encoding="utf-8") as f:
        f.write(string+"\n");
def cbce(text,key):
    iv = b'1367753864064775';
    pad = 16 - len(text) % 16;
    text = text + chr(2) * pad;
    encryptor = AES.new(key.encode(), AES.MODE_CBC, iv);
    encryptor_str = encryptor.encrypt(text.encode());
    result_str = base64.b64encode(encryptor_str).decode();
    return result_str;
def cbcd(text,key):
    iv=b'1367753864064775';
    txt=base64.b64decode(text.encode());
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv);
    msg = cipher.decrypt(txt);
    return re.sub("\x02","",msg.decode());
class Main(web.RequestHandler):
    def get(self):
        tm=int(time.time())+1456787654;
        self.set_cookie("name",str(tm));
        self.render("point.html");
        with open("dairy.log","a",encoding="utf-8") as f:
            f.write("user from ip: "+self.request.remote_ip+" requests the MainHandler with User-Agent: "+self.request.headers["User-Agent"]+" at "+str(time.time())+"\n");
class Sou(web.RequestHandler):
    def get(self,file):
        headers = self.request.headers
        cookie = self.get_cookie("name");
        try:
            if ("python" in headers["User-Agent"] or "java" in headers["User-agent"]):
                self.write("{}");
                wt("user from ip: "+self.request.remote_ip+" get source(access denined,maybe the request is from a spider)with User-Agent: "+self.request.headers["User-Agent"]+" at "+str(time.time()))
                return;
        except KeyError:
            wt("user from ip: " + self.request.remote_ip + " get source(access denined,headers error)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.set_status(404);
            return;
        try:
            int(cookie);
        except:
            wt("user from ip: " + self.request.remote_ip + " get source(access denined,cookie-check error)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.set_status(404);
            return;
        else:
            if (abs(int(cookie) - 1456787654 - time.time()) >= 30):
                wt("user from ip: " + self.request.remote_ip + " get source(access denined,cookie-check error)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                self.set_status(404);
                return;
        blacklist = ["\./", "\.\./", "\.php", "\.py", "\.file","\.log"];
        for i in blacklist:
            if(re.search(i,file)):
                wt("user from ip: " + self.request.remote_ip + " get source(access denined,the request resource is from the blacklist)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                self.set_status(404);
                return;
        if(re.match("/",file) or ((not re.match("r/",file)))):
            wt("user from ip: " + self.request.remote_ip + " get source(access denined,the request is not a whitelistfile)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.set_status(404);
            return;
        try:
            wt("user from ip: " + self.request.remote_ip + " get source(status:200)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            with open(file,"rb") as f:
                self.write(f.read());
        except Exception as e:
            wt("user from ip: " + self.request.remote_ip + " get source(access denined,server error: " + str(
                e) + " )with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.set_status(404);
            return;
class ajax(web.RequestHandler):
    def get(self,file):
        cookie=self.get_cookie("name");
        try:
            int(cookie);
        except:
            wt("user from ip: " + self.request.remote_ip + " ajax request(access denined, cookie-check error)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.set_status(404);
            return;
        else:
            if(abs(int(cookie)-1456787654-time.time())>=30):
                wt("user from ip: " + self.request.remote_ip + " ajax request(access denined, cookie-check error)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                self.set_status(404);
                return;
        arg=self.get_argument("a");
        if(arg ==None):
            wt("user from ip: " + self.request.remote_ip + " ajax request(access denined, arg-check error)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.set_status(400);
            return;
        else:
            wt("user from ip: " + self.request.remote_ip + " ajax request(access denined, arg-check error)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            if(abs(int(arg,16)-198687890876-int(time.time())*1000)>=600000):
                self.set_status(400);
                return;
        headers=self.request.headers
        try:
            if("python" in headers["User-Agent"] or "java" in headers["User-agent"]):
                self.write("{}");
                wt("user from ip: " + self.request.remote_ip + " ajax request(access denined, maybe the request is from a spider)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                return;
            if(not re.match("http://xiaoqiao\.wzlaolv\.cn/",headers["Referer"])):#这里记得改成域名
                wt("user from ip: " + self.request.remote_ip + " ajax request(access denined, Referer error)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                self.write("{}");
                return;
        except KeyError:
            self.set_status(404);
            return;
        blacklist = ["\./", "\.\./", "\.php", "\.py", "\.file","\.log"];
        for i in blacklist:
            if (re.search(i, file)):
                wt("user from ip: " + self.request.remote_ip + " ajax request(access denined, blacklist request)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                self.set_status(404);
                return;
        if (re.match("/", file)):
            wt("user from ip: " + self.request.remote_ip + " ajax request(access denined, blacklist request)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.set_status(404);
            return;
        try:
            wt("user from ip: " + self.request.remote_ip + " ajax request(status:200)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            with open("ajax/%s.json"%file,"r",encoding="utf-8") as f:
                self.write(f.read());
        except Exception as e:
            wt("user from ip: " + self.request.remote_ip + " ajax request(access denined,server error: " + str(
                e) + " )with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.set_status(404);
            return;
class ico(web.RequestHandler):
    def get(self):
        with open("favicon.ico","rb") as f:
            self.write(f.read());
class Fans(web.RequestHandler):
    def get(self):
        token = self.get_cookie("xiaoqiao");
        tme = self.get_cookie("laolv");
        if(token!=None and tme!=None):
            try:
                tim = cbcd(tme, str(int(cbcd(token,"j*%kYI06F^ly8%fn")) - 3748921847987654345657542196328458034592345489234734895363472542354369087345623745).zfill(16))
            except Exception:
                pass;
            else:
                if (tim == "WangzaiXiaoqiao is our god, WangzaiXiaoqiao is our soul and faith--cici"):
                    self.redirect("./fans");
                    wt("user from ip: " + self.request.remote_ip + " get fans area(redirected with cookie:"+token+"||"+tme+" )with User-Agent: " +
                       self.request.headers["User-Agent"] + " at " + str(time.time()))
                    return;
        tm = int(time.time()) + 1456787654;
        wt("user from ip: " + self.request.remote_ip + " get fans area(status:200)with User-Agent: " +
           self.request.headers["User-Agent"] + " at " + str(time.time()))
        self.set_cookie("name", str(tm));
        self.render("check.html");
class Check(web.RequestHandler):
    def post(self):
        with open("post.file","r",encoding="utf-8") as f:
            fl=f.readlines();
            for i in fl:
                if(i.split("||")[0]==self.request.remote_ip):
                    self.set_status(403);
                    wt("user from ip: " + self.request.remote_ip + " login the fansarea(access denined,request very fast)with User-Agent: " +
                       self.request.headers["User-Agent"] + " at " + str(time.time()))
                    self.write("<script>alert(\"请求过于频繁，请稍后再试\");"
                               "window.location.replace(\"./tologin\")</script>");
                    return;
        with open("post.file","a",encoding="utf-8") as f:
            f.write(self.request.remote_ip+"||"+str(int(time.time()))+"\n");
        headers = self.request.headers
        cookie = self.get_cookie("name");
        try:
            if ("python" in headers["User-Agent"] or "java" in headers["User-agent"]):
                self.write("{}");
                wt("user from ip: " + self.request.remote_ip + " login the fansarea(access denined,a spider request)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                return;
            if(headers["Referer"]!="http://"+headers["Host"]+"/tologin"):
                wt("user from ip: " + self.request.remote_ip + " login the fansarea(access denined,Referer error)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                self.write("{}");
                return;
        except KeyError:
            self.set_status(404);
            wt("user from ip: " + self.request.remote_ip + " login the fansarea(access denined,request error)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            return;
        try:
            int(cookie);
        except:
            self.set_status(404);
            wt("user from ip: " + self.request.remote_ip + " login the fansarea(access denined,cookie error)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            return;
        else:
            if (abs(int(cookie) - 1456787654 - time.time()) >= 600):
                wt("user from ip: " + self.request.remote_ip + " login the fansarea(the request time too long)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                self.write("<script>alert(\"请求超时，请刷新页面重新填写表单\");"
                           "window.location.replace(\"./tologin\")</script>");
                return;
        time.sleep(random.uniform(0.7,1.5));
        birth=self.get_argument("birth");
        nm=self.get_argument("nm");
        game=self.get_argument("game");
        nam=self.get_argument("nam");
        if(birth=="20050529" and "老驴" in nm and (game=="和平精英" or game=="吃鸡") and nam=="陈晓凤"):
            self.set_status(200);
            tm=int(time.time());
            token=cbce(str(tm+3748921847987654345657542196328458034592345489234734895363472542354369087345623745),"j*%kYI06F^ly8%fn");
            tme=cbce("WangzaiXiaoqiao is our god, WangzaiXiaoqiao is our soul and faith--cici",str(tm).zfill(16))
            self.set_cookie("xiaoqiao",token);
            self.set_cookie("laolv",tme);
            self.redirect("./fans");
            wt("user from ip: " + self.request.remote_ip + " login the fansarea(status:200,set-cookie:"+token+"||"+tme+")with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            return;
        else:
            self.set_status(403);
            self.write("<script>alert(\"您的部分答案填写错误，请重新填写表单\");"
                       "window.location.replace(\"./tologin\")</script>");
            wt("user from ip: " + self.request.remote_ip + " login the fansarea(access denined,answer error)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            return;
class FansWeb(web.RequestHandler):
    def get(self):
        tm = int(time.time()) + 1456787654;
        self.set_cookie("name", str(tm));
        token=self.get_cookie("xiaoqiao");
        tme=self.get_cookie("laolv");
        if(token==None or tme==None):
            wt("user from ip: " + self.request.remote_ip + " get the fansarea(access denined,no cookie)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.redirect("./tologin");
            return;
        try:
            tim = cbcd(tme, str(int(cbcd(token,"j*%kYI06F^ly8%fn")) - 3748921847987654345657542196328458034592345489234734895363472542354369087345623745).zfill(16));
        except Exception:
            wt("user from ip: " + self.request.remote_ip + " get the fansarea(access denined,cookie error)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.redirect("./tologin")
            return;
        else:
            wt("user from ip: " + self.request.remote_ip + " get the fansarea(access denined,cookie error)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            if(tim != "WangzaiXiaoqiao is our god, WangzaiXiaoqiao is our soul and faith--cici"):
                self.redirect("./tologin");
                return;
        self.set_status(200);
        wt("user from ip: " + self.request.remote_ip + " get the fansarea(status:200 with cookie:"+token+"||"+tme+")with User-Agent: " +
           self.request.headers["User-Agent"] + " at " + str(time.time()))
        self.render("fans.html");
class Video(web.RequestHandler):
    def get(self,num):
        try:
            cookie = self.get_cookie("name");
            try:
                int(cookie);
            except:
                wt("user from ip: " + self.request.remote_ip + " get the fansvideos(access denined,cookie error)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                self.set_status(404);
                return;
            else:
                if (abs(int(cookie) - 1456787654 - time.time()) >= 30):
                    wt("user from ip: " + self.request.remote_ip + " get the fansvideos(access denined,cookie error)with User-Agent: " +
                       self.request.headers["User-Agent"] + " at " + str(time.time()))
                    self.set_status(404);
                    return;
            arg = self.get_argument("a");
            if (arg == None):
                self.set_status(400);
                wt("user from ip: " + self.request.remote_ip + " get the fansvideos(access denined,arg error)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                return;
            else:
                if (abs(int(arg, 16) - 198687890876 - int(time.time()) * 1000) >= 600000):
                    wt("user from ip: " + self.request.remote_ip + " get the fansvideos(access denined,arg error)with User-Agent: " +
                       self.request.headers["User-Agent"] + " at " + str(time.time()))
                    self.set_status(400);
                    return;
            headers = self.request.headers
            try:
                if ("python" in headers["User-Agent"] or "java" in headers["User-agent"]):
                    self.write("{}");
                    wt("user from ip: " + self.request.remote_ip + " get the fansvideos(access denined,sipder request)with User-Agent: " +
                       self.request.headers["User-Agent"] + " at " + str(time.time()))
                    return;
                if (not re.match("http://xiaoqiao\.wzlaolv\.cn/", headers["Referer"])):
                    wt("user from ip: " + self.request.remote_ip + " get the fansvideos(access denined,Referer error)with User-Agent: " +
                       self.request.headers["User-Agent"] + " at " + str(time.time()))
                    # 这里记得改成域名
                    self.write("{}");
                    return;
            except KeyError:
                wt("user from ip: " + self.request.remote_ip + " get the fansvideos(access denined,header-error)with User-Agent: " +
                   self.request.headers["User-Agent"] + " at " + str(time.time()))
                self.set_status(404);
                return;
            num=int(num);
            rtlist=[];
            ls=os.listdir("text")[:num];
            for i in ls:
                ext=os.path.splitext(i);
                if(ext[1]!=".txt"):
                    continue;
                vdo=ext[0]+".mp4";
                txt=ext[0]+".jpg";
                with open("text/"+i,"r",encoding="utf-8") as f:
                    t=f.read();
                rtlist.append({
                    "imageurl":"mode1/"+txt,
                    "videourl":"mode2/"+vdo,
                    "text":t
                })
            wt("user from ip: " + self.request.remote_ip + " get the fansvideos(status:200)with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.write(json.dumps(rtlist));
        except Exception as e:
            wt("user from ip: " + self.request.remote_ip + " get the fansvideos(access-denined,server-error:"+str(e)+")with User-Agent: " +
               self.request.headers["User-Agent"] + " at " + str(time.time()))
            self.set_status(404);
class Videosget(web.RequestHandler):
    def get(self,mode,sour):
        try:
            if(mode=='1'):
                if(os.path.splitext(sour)[1]==".jpg"):
                    self.redirect("https://qiaoweb.oss-cn-beijing.aliyuncs.com/imgs/"+sour)
                else:
                    self.set_status(403);
                    return;
            elif(mode=='2'):
                if(os.path.splitext(sour)[1]==".mp4"):
                    self.redirect("https://qiaoweb.oss-cn-beijing.aliyuncs.com/videos/"+sour)
                    return;
                else:
                    self.set_status(403);
                    return;
            else:
                self.set_status(403);
                return;
        except Exception as e:
            self.set_status(403);
            return;
app=web.Application([(r"/",Main),(r"/file/(.+)",Sou),(r"/ajax/(.+)",ajax),(r"/favicon.ico",ico),
                     (r"/tologin",Fans),(r"/answcheck",Check),(r"/fans",FansWeb),(r"/videosget/(.+)",Video),
                     (r"/mode([1-2])/(.+)",Videosget)])
app.listen(80);
ioloop.IOLoop.instance().start();