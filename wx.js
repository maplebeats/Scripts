// ==UserScript==
// @name        wx
// @namespace   wx
// @description wx自动跳转
// @include     http://*support.weixin.qq.com/cgi-bin/*
// @downloadURL https://raw.githubusercontent.com/maplebeats/Scripts/master/wx.js
// @version     0.0.2
// @Author: maplebeats
// @mail: maplebeats@gmail.com
// @run-at document-end
// ==/UserScript==

var url_div = document.getElementsByClassName("url");
var url = url_div[0].innerHTML;
console.log(url);
document.getElementsByClassName("url")[0].innerHTML='<a id="target" href="'+url+'">自动跳转</a>';
var a = document.getElementById("target");
var evt = document.createEvent("MouseEvents");
evt.initEvent("click", true, true);
a.dispatchEvent(evt);
