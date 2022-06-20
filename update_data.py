import requests;
import re;
from lxml import etree;
import json;
import get_user;
import base64;
import time;
import oss2;
import os;
while(1):
    dataa={
        "fans":0,
        "like":0,
        "video": {
                "url": "",
                "name": "",
                "date": "",
                "like": ""
            },
        "wbinf": [
                "",
                ""
            ]
        }
    try:
        ksurl=["https://www.kuaishou.com/profile/3xmrqbe6s85vf2g","旺仔小乔"];
        s=requests.session();
        hd={
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": "douyin.com; __ac_nonce=061f80e1d00fc6a1c8508; __ac_signature=_02B4Z6wo00f01"
                      "laSjpgAAIDBwkTVlMvbVUZWsooAAPRr80; ttcid=eb63097a394342348c28820bd64a17e829"
                      "; ttwid=1%7Ci9JfYkMJIeriMZQajQc-0xCe7BquqzYCelPUxpaIZxM%7C1643646494%7C54e0"
                      "c1d383cbaadfb7c1f2076c507efc9706bc190152e31ccb425c95bcb61e32; MONITOR_WEB_I"
                      "D=d31273e0-f208-4847-a585-77355a7af25f; MONITOR_DEVICE_ID=f00de692-84d8-438"
                      "f-9d41-4cd31c281d52; _tea_utm_cache_6383=undefined; douyin.com; odin_tt=59c"
                      "f48bd2b7befdafb7ba2c6dba190c6b68f1c1338d6baf4596aa39a7db04037ed6d1ed0fd4098"
                      "c9ef6ca26de35bfd81c6bf4eeca01fdcc1f2b0fd55e2071985; IS_HIDE_THEME_CHANGE=1;"
                      " THEME_STAY_TIME=299914; _tea_utm_cache_1300=undefined; pwa_guide_count=3; "
                      "home_can_add_dy_2_desktop=1; tt_scid=38czMSYH.x0EzwA7gHHp-BDwlR18LE0WTujDC2"
                      "h3eoeXoumxIaFtpPSPUd81pqDH58d3; msToken=mCJS1e7KXZ9SWMIHh8BeC-M01ZsMBPELRkvi"
                      "ilwskVCWdr1rpkTA7F8ER8-oZCYRxk-qhVmfI4BGAgunuSUplcl5FSykJEwl1Kcb4oi0moNScJ_W"
                      "jrwp4Dd9RvyNzCs=; msToken=Ua6dQyCPwWz6OJeBR9C6Z5j43_Wh0yP4nEpuUk1uFMnP3AVa_K"
                      "kE6gGexwZRNz35x0Zp4TEm1TOqWDG_UIskrMZ7HbijR-pVcDtLAxG_rLGm5f24k7GYzVg=",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }
        r=s.get("https://www.douyin.com/user/MS4wLjABAAAACdtHOv8XS_X_PTuqJ3WReO4ka7pBWg7fmzG4wjiIZVkUKFOVtbhizl9GkpdOJ-O1",headers=hd);
        r.encoding="utf-8";
        dt=r.text;
        dt = re.sub("<script[^>]*?>.*?</script>", "", dt);
        lk=re.findall("[0-9]+",re.search("已有[0-9]+个粉丝，收获了[0-9]+个喜欢",dt).group(0));
        dataa["fans"]=lk[0]
        dataa["like"]=lk[1];
        html=etree.HTML(dt);
        dynvurl="https:"+html.xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div[1]/div[2]/ul/li[4]/a/@href')[0];
        dynvwd=html.xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div[1]/div[2]/ul/li[4]/a/div/div[1]/img/@alt')[0];
        dynvlk=html.xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div[1]/div[2]/ul/li[4]/a/div/span/span/text()')[0];
        res=requests.get(dynvurl,headers=hd);
        res.encoding="utf-8";
        dynvpsttm=etree.HTML(res.text).xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div[2]/div[2]/span/text()')[1];
        dataa["video"]["url"]=dynvurl;
        dataa["video"]["name"]=dynvwd;
        dataa["video"]["date"]=dynvpsttm;
        dataa["video"]["like"]=dynvlk
        wbmsg=get_user.getinfo("7521087082");
        pp=wbmsg[1][0].split(" ");
        wkday={"Mon":"周一","Tue":"周二","Wed":"周三","Thu":"周四","Fri":"周五","Sat":"周六","Sun":"周日"}
        wbmsg[1][0]=pp[5]+"年"+pp[1]+pp[2]+wkday[pp[0]]+pp[3];
        dataa["wbinf"][0]=wbmsg[1][1];
        dataa["wbinf"][1]=wbmsg[1][0];
        with open("ajax/inf.json","w",encoding="utf-8") as f:
            json.dump(dataa,f);
        time.sleep(60);
    except Exception as e:
        print(str(e));
        continue;