import hashlib;
import os
import pinyin
from lxml import etree;
import requests;
import json;
import re;
import time;
import random;
from Crypto.Cipher import AES;
from binascii import hexlify;
import base64;
def a(a=16):
    key="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    ls="";
    for i in range(a):
        ls+=random.choice(key);
    return ls;
def b(text,key):
    iv = b'0102030405060708';
    pad = 16 - len(text) % 16;
    text = text + chr(2) * pad;
    encryptor = AES.new(key.encode(), AES.MODE_CBC, iv);
    encryptor_str = encryptor.encrypt(text.encode());
    result_str = base64.b64encode(encryptor_str).decode();
    return result_str;
def c(text,pub_key):
    #f
    modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3' \
              'ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557' \
              'c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e8' \
              '2047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    text = text[::-1];
    result = pow(int(hexlify(text.encode()),16),int(pub_key,16),int(modulus,16));#第一个函数是把字符串改为16进制
    return format(result,'x').zfill(131)#相当于是把结果的数字改成16进制的字符串
def d(d,e="010001",g="0CoJUm6Qyw8W8jud"):
    d=json.dumps(d);
    i=a(16);
    enctext=b(b(d,g),i);
    encseckey=c(i,e);
    return {"params":enctext,"encSecKey":encseckey};
def get_data(url,data):
    res=requests.post(url,data=d(data));
    return res.text;
keyword=["旺仔小乔"];
while(1):
    lt=pinyin.get(keyword[0][0])[0];
    if(lt==keyword[0][0] and (90<ord(lt)<97 or ord(lt)<65 or ord(lt)>122)):
        lt="null"
    cnt=1;
    for i in range(1,6):
        url="https://www.kugou.com/yy/singer/index/%d-%s-1.html"%(i,lt);
        res=requests.get(url);
        if(re.search(keyword[0],res.text)):
            html=etree.HTML(res.text);
            s1=html.xpath('//*[@id="list_head"]/li/strong/a/text()');

            for j in range(len(s1)):
                if(s1[j]==keyword[0]):
                    url=html.xpath('//*[@id="list_head"]/li[%d]/a/@href'%(j+1));
                    cnt=0;
                    break;
            if(cnt==0):
                break;
            s2=html.xpath('//*[@id="list1"]/ul');
            for j in range(len(s2)):
                if(keyword[0] in html.xpath('//*[@id="list1"]/ul[%d]/li/a/text()'%(j+1))):
                    cnt=0;
                    li=html.xpath('//*[@id="list1"]/ul[%d]/li/a/text()'%(j+1))
                    for k in range(len(li)):
                        if(keyword[0]==li[k]):
                            url=html.xpath('//*[@id="list1"]/ul[%d]/li[%d]/a/@href'%(j+1,k+1));
                            break;
                    break;
            if(cnt==0):
                break;
    url=url[0];
    res=requests.get(url);
    html=etree.HTML(res.text);
    data=json.loads(re.search("\[\{.+\}\]",html.xpath('/html/head/script[2]/text()')[0]).group(0));
    name=[i.split("|")[0] for i in html.xpath('//*[@id="song_container"]/li/a/input/@value')]
    ids=[];
    audio=[];
    for i in data:
        audio.append("https://www.kugou.com/song/#hash="+str(i["hash"])+"&album_id="+str(i["album_id"]));
        ids.append([i["hash"],i["album_id"],i["album_audio_id"]])
    for i in range(len(ids)):
        if("+" in name[i] or "吉他弹唱" in name[i]):
            ids[i] = [];
            name[i] = "";
            audio[i] = "";
            continue;
        url="https://wwwapi.kugou.com/yy/index.php?" \
            "r=play/getdata&" \
            "hash=%s&" \
            "dfid=3eyJFz1T7jaE4O78Mx1UBxM9&appid=1014&" \
            "mid=49bb73f7c479ebe382bc8396ce40cbae&" \
            "platid=4&" \
            "album_id=%s&" \
            "album_audio_id=%s&" \
            "_=1654589371138"%(ids[i][0],ids[i][1],ids[i][2]);
        res=json.loads(requests.get(url).text);
        if(res["data"]["timelength"]<=120000):
            ids[i]=[];
            name[i]="";
            audio[i]="";
    nm=[];
    aud=[];
    for i in range(len(name)):
        if(name[i]!=""):
            nm.append(name[i]+"（来自酷狗音乐）");
            aud.append(audio[i]);
    res = requests.get("https://music.163.com/artist?id=32980337");
    html = etree.HTML(res.text);
    songname = html.xpath('//*[@id="song-list-pre-cache"]/ul/li/a/text()');
    songurl = ["https://music.163.com/#"+i for i in html.xpath('//*[@id="song-list-pre-cache"]/ul/li/a/@href')];

    ind=-1;
    for i in songurl:
        ind+=1;
        if("伴奏" in songname[ind]):
            songname[ind] = "";
            songurl[ind] = "";
            continue;
        else:
            for p in nm:
                if(songname[ind].split("（")[0] in p):
                    songname[ind] = "";
                    songurl[ind] = "";
                    continue;
        songid=i.split("=")[1];
        url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
        data = {"csrf_token": "", "encodeType": "aac", "ids": "[%s]" % songid, "level": "standard"};
        while (1):
            try:
                dt = json.loads(get_data(url, data))["data"];
            except json.decoder.JSONDecodeError:
                time.sleep(random.uniform(1.2, 2));
            else:
                break;
        if(not dt[0]["url"] or dt[0]["size"]<=1.5*1024*1024):
            songname[ind]="";
            songurl[ind]="";
    nam=[];
    audo=[];
    for i in range(len(songname)):
        if(songname[i]):
            nam.append(songname[i]+"（来自网易云音乐）");
            audo.append(songurl[i]);
    name=nm+nam;
    audio=aud+audo;
    with open("ajax/songs.json","w",encoding="utf-8") as f:
        json.dump({"name":name,"audio":audio},f);
    time.sleep(3600*24*14);


