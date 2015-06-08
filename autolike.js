// ==UserScript==
// @name        QQ空间自动点赞
// @namespace   qzone auto like
// @description QQ空间自动点赞
// @include     http://user.qzone.qq.com*
// @version     1.1
// @grant       none
// @Author      maplebeats
// @mail        maplebeats@gmail.com
// @TODO        1.逻辑优化 2.图形选择窗 3.自动翻页点赞
// ==/UserScript==

function refresh()
{
    console.log("auto:refresh");
    jQuery("#feed_friend_refresh").click();
}

function getlikeobj()
{
    var like = jQuery("[data-clicklog='like'][class='item qz_like_btn_v3']");
    return like;
}

function getiframelikeobj()
{
    var like = jQuery("iframe").contents().find("[data-clicklog='like'][class='item qz_like_btn_v3']");
    return like;
}

function autolike(obj)
{
    console.log("auto:like");
    var len = obj.length;
    var i = 0;
    for(i;i<len;i++){
        obj[i].click();
    }
}

function inter()
{
    if(localStorage.fresh && localStorage.auto){
        ;
    }
    localStorage.fresh=3000;
    localStorage.auto=30000;
    table+='<div id="autolike" class="position:absolute">'+
        '<table>'+
            
        '</table>'+
        '</div>';
    $("body").append(table);
}
function main()
{
    var inter = setInterval(function(){
        var obj = getlikeobj();
        if(obj.length == 0){
            obj = getiframelikeobj();
        }
        autolike(obj);
    },3000);
    var inter = setInterval(function(){
        refresh();
    },30000);
}
main();
