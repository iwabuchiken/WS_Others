var canvas;
var ctx;


$(document).ready(function(){

//	canvas = document.querySelector('#canvas_area');
//	ctx = canvas.getContext('2d');

//	alert("ready");
	
	alert(window.HTMLCanvasElement);

	init();
	
})

function init() {
	
	canvas = document.getElementById("canvas-container");
	
	//ref http://www.webopixel.net/javascript/1015.html
	var rect = canvas.getBoundingClientRect();
	
//	alert("rect => " + rect);
	
	console.log("rect.left => " + rect.left);
	
	canvas.addEventListener('click', function(e) {
	    var mouseX = e.clientX - rect.left;
	    var mouseY = e.clientY - rect.top;
	    
	    var msg = "X = " + mouseX + " / "
	    		+ "Y = " + mouseY;
	    
	    $('div#message_area').html(msg);
	    
	    
	}, false);

	canvas.addEventListener('mousemove', function(e) {
//		console.log('moving...');
		
	    var mouseX = e.clientX - rect.left;
	    var mouseY = e.clientY - rect.top;
	    
	    var msg = "X = " + mouseX + " / "
	    		+ "Y = " + mouseY;
	    
	    $('div#message_area').html(msg);
		
	}, false);

//	alert(canvas);	//=> w.
	
//	canvas.addEventListener('click', function(e) {
//	    console.log('click');
//	}, false);
//	
//	canvas.addEventListener('mousemove', function(e) {
//		console.log('moving...');
//	}, false);
	
	
}