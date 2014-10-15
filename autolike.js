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

function autolike()
{
    console.log("auto:like");
    var obj = getlikeobj();
    var len = obj.length;
    var i = 0;
    for(i;i<len;i++){
        obj[i].click();
    }
}

function main()
{
    var inter = setInterval(function(){
        autolike();
    },3000);
    var inter = setInterval(function(){
        refresh();
    },30000);
}
main();
