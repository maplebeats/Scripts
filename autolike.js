// ==UserScript==
// @name        QQ空间自动点赞
// @namespace   qzone auto like
// @description QQ空间自动点赞
// @include     http://user.qzone.qq.com*
// @version     1.0
// @grant       none
// @Author      maplebeats
// @mail        maplebeats@gmail.com
// ==/UserScript==
//
//

function refresh()
{
    console.log("auto:refresh");
    jQuery("#feed_friend_refresh").click();
}

function getlikeobj()
{
    like = jQuery("[data-clicklog='like'][class='item qz_like_btn_v3']")[0];
    return like;
}

function autolike()
{
    console.log("auto:like");
    obj = getlikeobj();
    obj.click();
}

function main()
{
    var inter = setInterval(function(){
        autolike();
        refresh();
    },3000);
}
main();
