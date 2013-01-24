// ==UserScript==
// @name        baidu
// @namespace   baidu
// @description 抢第一个和自动签到
// @include     http://tieba.baidu.com/f?kw=*
// @include     http://tieba.baidu.com/f?*&kw=*
// @version     0.1
// @Author:     maplebeats
// ==/UserScript==

var JQueryDiv = document.createElement("div");
JQueryDiv.setAttribute("onclick", "return $;");
$ = JQueryDiv.onclick();

var bar_name=unsafeWindow.PageData.forum.name; 
var tbs=unsafeWindow.PageData.tbs;
var is_like=unsafeWindow.PageData.user.is_like;
var is_sign=unsafeWindow.PageData.is_sign_in;
var data = {ie:"=utf-8", kw:bar_name, tbs:tbs };

function sign(){
   if(is_like&&!is_sign){
      $.post("http://tieba.baidu.com/sign/add", data, function callback(Ajax_data){
         if(!Ajax_data.error){
            is_sign=1;
            location.reload();
         }
      },"json");
   }
    return false;
}
var scount = 1;
function srequest(){
    console.log(scount++);
    if(!sign()){
        setTimeout(srequest, 100);
    }
}
var d = new Date();
var t = ((23-d.getHours())*60 + (60-d.getMinutes()))*60*1000 + (1000-d.getMilliseconds());
console.log(t);
if(d.getHours() != 0){
    var s = setTimeout(srequest, t);
    is_sign = 0; //假定没签到。。
}else{
    srequest();
}
window.addEventListener('load', sign, false);
