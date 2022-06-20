#https://open.weibo.com/wiki/2/comments/show
import requests;
import json;
import time;
def getinfo(uid):
    url="https://weibo.com/ajax/profile/info?uid=%s"%uid;
    headers = {"cookie":
                "SUB=_2AkMVZKL8dcPxrAVYkPkVxG7hbI1H-jymscsKAn7uJhMyAxgP7moJqSVutBF-XJKSwy_Y47YejqTMCluxlkKl9Lrv; "
                "SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WW.cGW7oq33fhFy-EZ7pm4I5JpVF02Re05pehn7ehzp;"
        ,
               "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
    res=requests.get(url,headers=headers);
    #print(res.text)
    data=json.loads(res.text);
    fans=data["data"]["user"]["followers_count"];
    name=data["data"]["user"]["screen_name"];
    all=data["data"]["user"]["location"];
    url="https://weibo.com/ajax/statuses/mymblog?uid=%s&page=1&feature=0"%uid;
    res=requests.get(url,headers=headers);
    data=json.loads(res.text);
    new=data["data"]["list"][0];
    crt=new["created_at"];
    url="https://weibo.com/%s/%s"%(uid,new["mblogid"]);
    return [[name,fans,all],[crt,url]];
def getc(user_id):
    headers={"cookie":
                 "SUB=_2AkMVZKL8dcPxrAVYkPkVxG7hbI1H-jymscsKAn7uJhMyAxgP7moJqSVutBF-XJKSwy_Y47YejqTMCluxlkKl9Lrv; "
                 "SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WW.cGW7oq33fhFy-EZ7pm4I5JpVF02Re05pehn7ehzp;"
                      ,
             "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
    since_id=""
    ids = [];
    while(1):
        url="https://weibo.com/ajax/statuses/mymblog?uid=%s&feature=0&since_id=%s"%(user_id,since_id);
        res=requests.get(url,headers=headers);
        data=json.loads(res.text);
        for i in data["data"]["list"]:
            ids.append([i["idstr"],i["mblogid"],i["text"],i["text_raw"]]);
        if(data["data"]["since_id"]==""):
            break;
        else:
            since_id=data["data"]["since_id"];
    allcmt={}
    for i in ids:
        mid=0;
        comments = [];
        while(1):
            url="https://weibo.com/ajax/statuses/buildComments?" \
                "is_reload=1&id=%s&is_show_bulletin=3&is_mix=0&count=200&uid=%s&max_id=%d"%(i[0],user_id,mid);
            res=requests.get(url,headers=headers);
            data=json.loads(res.text);
            for j in data["data"]:
                apd=[[j["user"]["name"],j["user"]["idstr"],j["created_at"],j["text_raw"]]]
                for k in j["comments"]:
                    apd.append([k["user"]["name"],k["user"]["idstr"],k["created_at"],k["text_raw"]])
                comments.append(apd)
            if(data["max_id"]!=0):
                mid=data["max_id"];
            else:
                break;
            if(data["data"]==[]):
                break;
        allcmt[i[0]]=comments;
    return [ids,allcmt];