var canvas;
var ctx;


$(document).ready(function(){

	canvas = document.querySelector('#canvas-container');
	ctx = canvas.getContext('2d');
//	var canvas = document.querySelector('#canvas-container');
//	var ctx = canvas.getContext('2d');

	alert("ready");

	
})

var count = 0;
var countup = function(){
	console.log(count++);
} 

//	setInterval(countup, 1000);
var id = setInterval(function(){
		countup();
		
	    ctx.beginPath();
	    
	    ctx.arc(100 + (count - 1) * 20 , 100, 30, 0, 2*Math.PI, false);
	    ctx.fillStyle = '#FFFFFF';
//	    ctx.fillStyle = '#FF0000';
	    ctx.fill();
	    
	    ctx.beginPath();
	    
	    ctx.arc(100 + count * 20 , 100, 20, 0, 2*Math.PI, false);
	    ctx.fillStyle = '#FF00FF';
	    ctx.fill();

		
//		if(count > 5){　
		if(count > 50) {
			clearInterval(id);　//idをclearIntervalで指定している
		}
	}//function()
	, 
	1000
);
