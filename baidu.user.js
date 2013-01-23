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

var bar_name=unsafeWindow.PageData.forum.name; //BUG 签到C++贴吧的时候post数据为C
var tbs=unsafeWindow.PageData.tbs;
var is_like=unsafeWindow.PageData.user.is_like;
var is_sign=unsafeWindow.PageData.is_sign_in;

function sign(){
	if(is_like&&!is_sign){
		//发送
		$.post("http://tieba.baidu.com/sign/add","ie=utf-8&kw="+bar_name+"&tbs="+tbs,function callback(Ajax_data){
			if(!Ajax_data.error){
				//成功
				is_sign=1;
                location.reload();
			}
		},"json");
        return true;
	}
    return false;
}
function srequest(){
    if(!sign()){
        setTimeout(srequest, 100);
    }
}
var d = new Date();
var t = (60-d.getMinutes())*60*1000 + (1000-d.getMilliseconds());
if(t>0 && d.getHours>0){
    var s = setTimeout(srequest, t);
}else{
    srequest();
}

//事件型
window.addEventListener('load', sign, false);
