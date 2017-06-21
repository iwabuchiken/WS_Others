//$(document).ready(function(){
//
//	alert("ready");
//
//	loop();
//	
//})


//var can = document.getElementById("canvas");
//var ctx = can.getContext("2d");
//
//var count = 0;//アニメーションカウンター
//var timer = setInterval(function(){
//  ctx.fillStyle="#fff";//消去時の色
//  ctx.clearRect(0,0,300,300);//消す
//  ctx.fillStyle="#f00";//塗りつぶし色を赤に
//  ctx.fillRect(30+count,30+count,30,30);
//  count++;
//  if(count>200){
//    clearInterval(timer);
//  }
//},100);

 var count = 0;
  var countup = function(){
    console.log(count++);
  } 
  setInterval(countup, 1000);
