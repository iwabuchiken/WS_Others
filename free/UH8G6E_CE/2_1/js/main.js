function alert_message() {
	
	alert("message");
	
}



$(document).ready(function(){

//	alert("ready");
	
})

function draw_Circle() {

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

window.onload = function() {
    // Canvas未サポートは実行しない
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
    ctx.arc(100, 100, 20, 0, 2*Math.PI, false);
//    ctx.arc(100, 100, 20, Math.PI, 2*Math.PI, false);
    
    ctx.fillStyle = '#D0A869';
    
//    alert("filling...");
    
    ctx.fill();
};