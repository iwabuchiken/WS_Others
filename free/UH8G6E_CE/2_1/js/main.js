$(document).ready(function(){

	alert("ready");

	loop();
	
})


var canvas = document.querySelector('#canvas-container');
var ctx = canvas.getContext('2d');

var speed = 2;    //移動速度
var x = 0;      //X軸の位置

// ループ処理
function loop() {
	
	alert("looping...");
	
    requestAnimFrame(loop);
    
    alert("requestAnimFrame => called");
    
    ctx.clearRect(0,0, ctx.canvas.width, ctx.canvas.height);
    // ループ毎にxを加算
    x += speed;
    // 丸を描画
    drawCircle(x, 100, 20, '#0000FF');
    
    if (x > 600) x = 0;
}


function drawCircle(x, y, scale, color) {
    ctx.beginPath();
    ctx.arc(x, y, scale, 0, 2*Math.PI, false);
    ctx.fillStyle = color;
    ctx.fill();
}

window.requestAnimFrame = (function(){
	
	alert("requestAnimFrame => starting...");
	
    return  window.requestAnimationFrame   ||
        window.webkitRequestAnimationFrame ||
        window.mozRequestAnimationFrame    ||
        window.oRequestAnimationFrame      ||
        window.msRequestAnimationFrame     ||
        function(callback){
            window.setTimeout(callback, 120 / 60);
        };
})();

//loop();

//$(document).ready(function(){
//
//	alert("ready");
//	
//})
