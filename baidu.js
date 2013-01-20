// ==UserScript==
// @name        Auto sign in for TieBa in BaiDu
// @namespace   haha
// @include     http://tieba.baidu.com/f?kw=*
// @include     http://tieba.baidu.com/f?*&kw=*
// ==/UserScript==
var bar_name=unsafeWindow.PageData.forum.name;
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
				var pos_x="-336px";
				var pos_y=$('.sign_btn2').css("background-position").split(" ")[1];
				var inner_span="<span class='sign_keep_span'>连续签到<span id='sign_btn_keep' class='sign_btn_keep'>"+Ajax_data.data.uinfo.cont_sign_num+"</span>天</span>";
				$('.sign_btn2').css("background-position",pos_x+" "+pos_y);
				$('.sign_btn2').append(inner_span);
			}
		},"json");
        return true;
	}
    return false;
}
function request(){
    if(!sign()){
        setTimeout(sign, 100);
    }
}
var d = new Date();
var t = (24-d.getHours())*24*60*1000 + (60-d.getMinutes())*60*1000 + 1000-d.getMilliseconds()
setTimeout(sign, t);

//事件型
window.addEventListener('load',sign,false);
