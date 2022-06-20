var xhr= new XMLHttpRequest();
xhr.open("POST","http://127.0.0.1:800/114514",true);
var data={"000":"111"}
var fn=function(text,_)
{
    var txt=JSON.parse(text);
    $("#1").append(txt["111"]);
}

xhr.onreadystatechange=function()
{
    if(xhr.readyState==4 && xhr.status==200 || xhr.status==304)
    {
        fn.call(this,xhr.responseText);
    }
}
xhr.send(JSON.stringify(data))