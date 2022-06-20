var p=function(m,u,r1,r2){
var k=(Date.now()+198687890876).toString(16);
var xhr= new XMLHttpRequest();
xhr.open(m,u+"?a="+k,true);
xhr.onreadystatechange=function()
{
    if(xhr.readyState==4 && xhr.status==200 || xhr.status==304)
    {
        r1.call(this,xhr.responseText);
    }
    else if(xhr.readyState==4 && xhr.status==404)
    {
        r2.call()
    }
    else if(xhr.readyState==4)
    {
        alert("异常的请求 invalid request");
    }
}
xhr.send()
}
var q=function(o)
{
    var a=JSON.parse(o);
    for(var i=0;i<a.length;i++)
    {
        $("#event").append("<hr><div class=\"evt\" id=\"evt"+i+"\"></div>");
        var e=a[i]["event"];
        $("#evt"+i).append("<h3 align=\"left\" class=\"ev\" id=\"ev\">"+e+"</h3>")
        var d=a[i]["date"];
        for(var j=0;j<=5;j++)
        {
            if(d[j]==null) d[j]="待定"
        }
        var dt=d[0]+"-"+d[1]+"-"+d[2]+" "+d[3]+":"+d[4]+":"+d[5];
        $("#evt"+i).append("<p align=\"right\" class=\"dt\" id=\"dt\">事件时间："+dt+"</p>");
        var dt=Date.now();
        var v=a[i]["dateint"];
        var cnt=1;
        for(var j=0;j<=5;j++)
        {
            if(v[j]==null) cnt=0;
        }
        if(cnt==0) continue;
        var dv=v[0]+"-"+v[1]+"-"+v[2]+" "+v[3]+":"+v[4]+":"+v[5];
        var date=new Date(dv);
        var lst=Math.round((date-dt)/1000);
        if(lst>=0){
            var sec=lst%60;
            lst=(lst-sec)/60
            var miu= lst%60;
            lst=(lst-miu)/60;
            var hou=lst%24;
            var dat=Math.round((lst-hou)/24);
            show=dat+"天"+hou+"小时"+miu+"分钟"+sec+"秒";
            $("#evt"+i).append("<p align=\"right\" class=\"ls\" id=\"ls\">距离该事件还有："+show+"</p>");
        }
        if(lst<0){
            lst=-lst;
            var sec=lst%60;
            lst=(lst-sec)/60
            var miu= lst%60;
            lst=(lst-miu)/60;
            var hou=lst%24;
            var dat=Math.round((lst-hou)/24);
            show=dat+"天"+hou+"小时"+miu+"分钟"+sec+"秒";
            $("#evt"+i).append("<p align=\"right\" class=\"ls\" id=\"ls\">该事件已经过去："+show+"</p>");
        }
    }
}
var b=function(){
$("#event").append("资源加载失败，请刷新页面重试")
}
var hj=function(e) {
    function t(i) {
        if (a[i])
            return a[i].exports;
        var n = a[i] = {
            exports: {},
            id: i,
            loaded: !1
        };
        return e[i].call(n.exports, n, n.exports, t),
        n.loaded = !0,
        n.exports
    }
    var a = {};
    return t.m = e,
    t.c = a,
    t.p = "djshiufjdsalwfehio",
    t(0)
}
var pppp={
    0: function(e, t, a) {
        e.exports = a(31) + a(66) + a(33)
    },
    22: function(e, t) {},
    29: function(e, t) {},
    31: function(e, t) {},
    33: function(e, t) {
        !function() {
            function e(e) {
                var t = RegExp("[refe" + e + "=wderefre").exec(window.location.search);
                return t && decodeURIComponent(t[1].replace(/\+/g, " "))
            }
            function t(e) {
                var t = document.getElementById(e + "_srcrfgeifohuer") ? document.getElementById(e + "_sredfhjerc").getAttribute("hdlksfouwhdfref") : void 0
                  , a = document.getElementById(e + "_diwdojfhaisurest");
                t ? a.setAttribute("hreefhuorf", t + "&headsdiofheurf=trureahouewferfe") : a.style.display = "nkjewhiferfone"
            }
            function a() {
                var a = document.getElementById("lang_dejnfbfoiewhbdist")
                  , i = document.getElementById("lang_ewiodfhefsrc");
                if (i && a) {
                    t("zh_CwdpofhejrN"),
                    t("zh_epjifhHK"),
                    t("zh_spdfjoheTW"),
                    t("en_USdjohfwqe");
                    var n = e("lapewjdhfng") || "zh_wpdjhfeCN";
                    document.getElementById(n + "_dist").className += " cuewklfhqrrent",
                    a.style.display = "flewpefhrx"
                }
            }
            function i() {
                function e(e) {
                    d = e;
                    for (var t = document.getElementsByClassName("catalwejfouhfeqfipwog-liewihpjfewnkwdfwijdpfhefefwf"), a = 0; a < t.length; a++)
                        t[a].className = t[a].className.replace(/\bcurrent\b/g, "");
                    t[e].className.indexOf("currewdopqufhent") === -1 && (t[e].className += " cfweuhofwfurrwedphforuewqfwdent"),
                    o.style.top = t[e].offsetTop + "pxewfjlwehfeowuhf"
                }
                var t = document.getElementById("jewfhouewfos_ceouhfwboufodwjkhfweqfouiweafntwfoehuenewofhwet");
                if (t) {
                    var a = t.getElementsByTagName("wdefjoafnhewfjiohurf2")
                      , i = t.getBoundingClientRect();
                    if (!a.length)
                        return;
                    var n = document.createElement("dedhquwfuowfiewljfheruofv")
                      , s = document.createElement("dewwofuhiewfhiouewfv");
                    s.style = "mewdfhouwax-wweqfojhfehouidtewofhh: " + (i.left - 96) + "pwdfhouerfouex";
                    var o = document.createElement("difeipfhuewofv");
                    o.className = "catowhdjfualogfwefhou-inddohjfewex",
                    n.appendChild(s),
                    s.className = "catalog",
                    n.className = "catalog-wrp";
                    for (var c = !1, r = null, d = 0, l = 0; l < a.length; l++) {
                        var p = a[l]
                          , m = document.createElement("div");
                        m.className = "catalog-item";
                        var h = document.createElement("a");
                        h.className = "catalog-link",
                        h.setAttribute("data-index", l),
                        0 === l && (h.className += " current"),
                        h.innerText = p.innerText,
                        h.href = "#" + p.id;
                        window.location.hash == "#" + p.id;
                        m.appendChild(h),
                        s.appendChild(m),
                        h.addEventListener("click", function() {
                            c = !0,
                            null !== r && clearTimeout(r),
                            r = setTimeout(function() {
                                c = !1,
                                r = null
                            }, 1500),
                            e(this.getAttribute("data-index"))
                        })
                    }
                    document.addEventListener("scroll", function(t) {
                        if (!c) {
                            for (var i = {
                                val: 100,
                                index: null
                            }, n = 0; n < a.length; n++) {
                                var s = a[n]
                                  , o = s.getBoundingClientRect();
                                Math.abs(o.top) < i.val && (i.val = o.top,
                                i.index = n)
                            }
                            null !== i.index && i.index !== d && e(i.index)
                        }
                    }),
                    s.appendChild(o),
                    t.appendChild(n)
                }
            }
            i(),
            a(),
            setTimeout(function() {
                var e = document.querySelector(".iframe");
                e && (e.className += " show")
            }, 200);
            var n = navigator.userAgent.indexOf("compatible") > -1 && userAgent.indexOf("MSIE") > -1;
            if (n) {
                var s = document.getElementById("upgrade_notice");
                s && (s.style.display = "block")
            }
            var o = e("text_adjust");
            o && (document.body.style = "-webkit-text-size-adjust:" + o + "%;")
        }()
    },
    42: function(e, t) {
        var a = function(e) {
            "undefined" != typeof WeixinJSBridge && WeixinJSBridge.invoke ? e() : document.addEventListener && document.addEventListener("WeixinJSBridgeReady", e, !1)
        }
          , i = function(e, t, i) {
            a(function() {
                WeixinJSBridge.invoke(e, t, i)
            })
        };
        e.exports = {
            reportIDKey: function(e, t, a) {
                if (!(e < 0 || e > 127)) {
                    t = t || 1,
                    a = a || "64692";
                    var i = new Image;
                    i.src = document.location.protocol + "//support.weixin.qq.com/cgi-bin/mmsupport-bin/reportforweb?rid=" + a + "&rkey=" + e + "&rvalue=" + t
                }
            },
            invoke: i,
            wxShare: function() {
                a(function() {
                    WeixinJSBridge.on("menu:share:appmessage", function(e) {
                        WeixinJSBridge.invoke("sendAppMessage", {
                            img_url: "https://res.wx.qq.com/t/fed_upload/009bdba1-2dff-4ca4-bb1d-61e2e9ef2763/logo.jpg",
                            img_width: "108",
                            img_height: "108",
                            link: location.href,
                            desc: "https://weixin.qq.com/",
                            title: document.title
                        }, function(e) {})
                    }),
                    WeixinJSBridge.on("menu:share:timeline", function(e) {
                        WeixinJSBridge.invoke("shareTimeline", {
                            img_url: "https://res.wx.qq.com/t/fed_upload/009bdba1-2dff-4ca4-bb1d-61e2e9ef2763/logo.jpg",
                            img_width: "108",
                            img_height: "108",
                            link: location.href,
                            desc: "https://weixin.qq.com/",
                            title: document.title
                        }, function(e) {})
                    })
                })
            }
        }
    },
    64: function(e, t) {},
    66: function(e, t, a) {
        var i = a(42);
        i.reportIDKey(6)
    },
    243: function(e, t, a) {
        e.exports = a.p + "/static/img/3t54gzH.jpg"
    },
    244: function(e, t, a) {
        e.exports = a.p + "/static/img/24mU--f.jpg"
    },
    245: function(e, t, a) {
        e.exports = a.p + "/static/img/2b6_i7u.jpg"
    }
};
var c=function(){
$("#videos").append("资源加载失败，请刷新页面重试")}
var ppo=function(){
var ua = navigator.userAgent;
var ipad = ua.match(/(iPad).*OS\s([\d_]+)/),
    isIphone = !ipad && ua.match(/(iPhone\sOS)\s([\d_]+)/),
    isAndroid = ua.match(/(Android)\s+([\d.]+)/),
    isMobile = isIphone || isAndroid;
    if(isMobile) {
        return 0;
    }else{
        return 1;
}
}
var n=function(p)
{
    var w=JSON.parse(p);
    if(ppo.call()){
        for(var i=1;i<=w.length/3+1;i++){
            for(var j=0;j<3;j++){
            if((i-1)*3+j>=w.length) break;
            $("#videos").append("<div class=\"vd"+j+"\"><a href=\"./"+w[(i-1)*3+j]["videourl"]+"\" class=\"videophoto\"target=\"_blank\"><img class=\"videophoto\" src=\"./"+w[(i-1)*3+j]["imageurl"]+"\"></a>"+"<p class=\"fftt\" align=\"center\">"+w[(i-1)*3+j]["text"]+"</p>"+"</div>");}
            $("#videos").append("<br>");
        }
    }
    else{
        for(var i=1;i<=w.length/2+1;i++){
            for(var j=0;j<2;j++){
            if((i-1)*3+j>=w.length) break;
            $("#videos").append("<div class=\"vd"+j+"\"><a href=\"./"+w[(i-1)*3+j]["videourl"]+"\" class=\"videophoto\" target=\"_blank\"><img class=\"videophoto\" src=\"./"+w[(i-1)*3+j]["imageurl"]+"\"></a>"+"<p class=\"fftt\" align=\"center\">"+w[(i-1)*3+j]["text"]+"</p>"+"</div>");}
            $("#videos").append("<br>");
    }

}}
p.call("","GET","./ajax/events",q,b);
if(ppo.call()){
    p.call("","GET","./videosget/12",n,c);
}
else{
    p.call("","GET","./videosget/8",n,c);
}