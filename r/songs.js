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
var f1=function(a,_)
{
    var a = JSON.parse(a);
    for(var i=0;i<a["name"].length;i++)
    {
        $("#songsbody").append("<a href=\""+a["audio"][i]+"\" target=\"blank\" class=\""+(i%2==0?"l11":"r11")+"\">"+a["name"][i]+"</a>");
        if(i%2==1){
        $("#songsbody").append("<br>");
        }
    }
}
var f2=function()
{
    $("#songsbody").append("资源请求失败，请刷新页面重试")
}
p.call("","GET","./ajax/songs",f1,f2);
