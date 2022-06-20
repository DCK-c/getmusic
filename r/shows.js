
var fn=function(a,_)
{
    var b=JSON.parse(a);
    for(var i=0;i<b.length;i++)
    {
        $("#xiaoqiao").append("<p align=\"center\" class=\"imptmsg\">"+b[i]+"</p><hr>");
    }
}
var fq=function()
{
     $("#xiaoqiao").append("资源请求失败，请刷新页面重试");
}
var w=function(o,_)
{
    var a=JSON.parse(o);
    for(i=0;i<a["videourl"].length;i++)
    {
        if(i%2==0) ind="r";
        else ind="w"
        $("#xiaoqiao2").append("<a href=\""+a["videourl"][i]+"\" target=\"_blank\" class=\"sv"+ind+"\">"+a["text"][i]+"</a><br>");
    }
}
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
xhr.send(JSON.stringify(data))
}
var e=function()
{
    $("#xiaoqiao2").append("资源请求失败，请刷新页面重试");
}
var t=function(o,_)
{
    var d=JSON.parse(o);
    $("#data").append("<div class=\"dyinfo\"><h3 style=color:#0000ff><p>抖音账号：<a href=\"https://www.douyin.com/user/MS4wLjABAAAACdtHOv8XS_X_PTuqJ3WReO4ka7pBWg7fmzG4wjiIZVkUKFOVtbhizl9GkpdOJ-O1\" target=\"_blank\">旺仔小乔</a></p></h3><p>抖音现在有"+d["fans"]+"个粉丝</p><p>已经收获了"+d["like"]+"个赞</p></div>");
    $("#data").append("<hr>");
    $("#data").append("<div class=\"dynv\"><h3 style=color:#0000ff> 抖音最新视频信息</h3><p> 抖音最新视频：<a href=\""+d["video"]["url"]+"\" target=\"_blank\">"+d["video"]["name"]+"</a>于"+d["video"]["date"]+"发出</p><p> 现在视频已经收获了"+d["video"]["like"]+"个赞</p></div>");
    $("#data").append("<hr>");
    $("#data").append("<div class=\"wbmsg\"><h3 style=color:#0000ff>微博账号:<a href=\"https://weibo.com/u/7521087082\" target=\"_blank\">旺仔小乔会吃饭</a>,\n所在地：安徽 合肥</h3><p><a href=\""+d["wbinf"][0]+"\" target=\"_blank\">最新微博</a>发送于"+d["wbinf"][1]+"</p></div>")
}
var j=function(q,_)
{
    var a=JSON.parse(q);
    for(var i=0;i<a["text"].length;i++)
    {
        $("#importants").append("<a href=\""+a["link"][i]+"\" target=\"_blank\">"+a["text"][i]+"</a><br>");
    }
}
var c=function(){$("#data").append("<div>资源请求失败，请刷新页面重试</div>")}
var b=function(){$("#importants").append("资源请求失败，请刷新页面重试")}
var tp=function(m,_)
{
    var a=JSON.parse(m);
    for(var i=0;i<a["text"].length;i++)
    {
        $("#slc").append("<a href=\""+a["links"][i]+"\" target=\"_blank\">"+a["text"][i]+"</a><br>")
    }
}
var jk=function(){$("#slc").append("资源请求失败，请刷新页面重试")};
p.call("","GET","./ajax/shows",fn,fq);
p.call("","GET","./ajax/videos",w,e);
p.call("","GET","./ajax/inf",t,c);
p.call("","GET","./ajax/impt",j,b);
p.call("","GET","./ajax/slc",tp,jk);
