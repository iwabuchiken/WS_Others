var canvas = document.querySelector('#canvas-container');
var ctx = canvas.getContext('2d');

var speed = 2;    //移動速度
var x = 0;      //X軸の位置


function alert_message() {
	
	alert("message");
	
}

//ref http://www.webopixel.net/javascript/1001.html
/*
 * @param color	=> e.g. '#D0A869'
 * @param scale	=> radius
 * 
 */
function drawCircle(x, y, scale, color) {
	
//	alert("drawing...");

    ctx.beginPath();
    ctx.arc(x, y, scale, 0, 2*Math.PI, false);
    ctx.fillStyle = color;
    ctx.fill();
}

//ループ処理
function loop() {
	
    requestAnimFrame(loop);
    
    ctx.clearRect(0,0, ctx.canvas.width, ctx.canvas.height);
    // ループ毎にxを加算
    x += speed;
    // 円を描画
    drawCircle(x, 100, 20, '#D0A869');
    
    if (x > 600) x = 0;
    
}

//$(document).ready(function(){
//
////	alert("ready");
//	
//})

function draw_Circle() {

	var x = 200;
	var y = 200;
	var scale = 50;
	var color = '#0000FF';
	
	drawCircle(x, y, scale, color);
	
	return;
	
//	alert("drawing a circle...");
	
    if (!window.HTMLCanvasElement) {
    	
    	alert("canvas ---> not supported");
    	
    	return;
    }
    var canvas = document.querySelector('#canvas-container');
    var ctx = canvas.getContext('2d');
 
    // 円の描画
    ctx.beginPath();
    
    //ref http://www.html5.jp/canvas/ref/method/arc.html
    // arc(x, y, radius, startAngle, endAngle, anticlockwise)
//    ctx.arc(100, 100, 20, 0, 2*Math.PI, false);
    
    //ref https://syncer.jp/javascript-reverse-reference/create-random-number
    var x = Math.floor( Math.random() * 200 ) + 100;
    var y = Math.floor( Math.random() * 200 ) + 100;
    
    var angle_Start = Math.random() * Math.PI * 2;
    var angle_End = Math.random() * Math.PI * 2;
    
    var tmp;
    
    if (angle_Start > angle_End) {
    	
    	tmp = angle_Start;
    	
    	angle_Start = angle_End;
    	
    	angle_End = tmp;
    	
    }
    
    alert("angle_Start => " + angle_Start
    		+ " / "
    		+ "angle_End => " + angle_End
	);
    
    ctx.arc(x, y, 20, angle_Start, angle_End, false);
//    ctx.arc(x, y, 20, Math.PI, 2*Math.PI, false);
    
    ctx.fillStyle = '#D0A869';
    
//    alert("filling...");
    
    ctx.fill();

}

//window.onload = function() {
//    // Canvas未サポートは実行しない
//    if (!window.HTMLCanvasElement) {
//    	
//    	alert("canvas ---> not supported");
//    	
//    	return;
//    }
//    var canvas = document.querySelector('#canvas-container');
//    var ctx = canvas.getContext('2d');
// 
//    // 円の描画
//    ctx.beginPath();
//    
//    //ref http://www.html5.jp/canvas/ref/method/arc.html
//    // arc(x, y, radius, startAngle, endAngle, anticlockwise)
//    ctx.arc(100, 100, 20, 0, 2*Math.PI, false);
////    ctx.arc(100, 100, 20, Math.PI, 2*Math.PI, false);
//    
//    ctx.fillStyle = '#D0A869';
//    
////    alert("filling...");
//    
//    ctx.fill();
//};

//ref http://www.webopixel.net/javascript/1001.html
window.requestAnimFrame = (function(){
    return  window.requestAnimationFrame   ||
        window.webkitRequestAnimationFrame ||
        window.mozRequestAnimationFrame    ||
        window.oRequestAnimationFrame      ||
        window.msRequestAnimationFrame     ||
        function(callback){
            window.setTimeout(callback, 1000 / 60);
        };
})();

loop();
