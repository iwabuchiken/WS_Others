//var canvas;
//var ctx;



var unit = 100,
    canvas, context, canvas2, context2,
    height, width, xAxis, yAxis,
    draw
//    , timeout = 10
    , timeout = 20
    ;

var interval = 500;

$(document).ready(function(){

//	canvas = document.querySelector('#canvas_area');
//	ctx = canvas.getContext('2d');

	alert("ready");

	init();
	
})

//ref http://jsfiddle.net/umaar/fWSUk/
function init() {
    
    canvas = document.getElementById("sineCanvas");
    
    canvas.width = 800;
    canvas.height = 300;
    
    context = canvas.getContext("2d");
    context.font = '18px sans-serif';
    context.strokeStyle = '#000';
    context.lineJoin = 'round';
    
    height = canvas.height;
    width = canvas.width;
    
    xAxis = Math.floor(height/2);
    yAxis = Math.floor(width/4);
    
//    alert("init => done");
    
    //ref http://www.html5.jp/canvas/ref/method/save.html
    context.save();
    draw();
    
}//function init() {

draw = function () {
	
	/***************************
		unit
	 ***************************/
	//ref random https://syncer.jp/javascript-reverse-reference/create-random-number
//	unit = 80 + Math.floor( Math.random() * 50 );	//=> works.
//	unit = 100 + Math.floor( Math.random() * 20 ) + 5;
	
//	alert("draw => starting...");
	
    // Clear the canvas
    context.clearRect(0, 0, width, height);

    // Draw the axes in their own path
    context.beginPath();
    drawAxes();
    context.stroke();
	
    // Set styles for animated graphics
    context.save();

    context.strokeStyle = '#00f';
    context.fillStyle = '#fff';
    context.lineWidth = 2;

    // Draw the sine curve at time draw.t, as well as the circle.
    context.beginPath();
    
    drawSine(draw.t);
    
//    context.strokeStyle = '#ff0';
    context.strokeStyle = '#f00';
    context.stroke();
    context.strokeStyle = '#00f';
    
    drawCircle();
    
    context.stroke();

//     Draw the arrow at time t in its own path.
    drawArrow(draw.t);

    // Restore original styles
    context.restore();
    
    // Draw the xAxis PI tick and the time
    context.fillText("Ï�", xAxis + 59+3*unit, 18+xAxis);
    context.fillText("t = "+Math.floor(Math.abs(draw.seconds)), 10, 20);
    
    // Update the time and draw again
    draw.seconds = draw.seconds - .007;
    draw.t = draw.seconds*Math.PI;
    
    setTimeout(draw, timeout);
//    setTimeout(draw, 35);
    
//    //debug
    //ref https://stackoverflow.com/questions/5113374/javascript-check-if-variable-exists-is-defined-initialized 'answered Feb 6 '09 at 4:56'
//    alert((typeof variable !== 'undefined') ? draw.t : "draw.t => undefiend");
    $('#message_area').html(draw.t);

};//draw = function () {

draw.seconds = 0;
draw.t = 0;


function drawAxes() {
    
    // Draw X and Y axes
    context.moveTo(0, xAxis);
    context.lineTo(width, xAxis);
    context.moveTo(yAxis, 0);
    context.lineTo(yAxis, height);
    
    // Draw X axis tick at PI
    context.moveTo(yAxis+Math.PI*unit, xAxis+5);
    context.lineTo(yAxis+Math.PI*unit, xAxis-5);

    //test
    // Draw support lines
    //ref https://www.w3schools.com/tags/canvas_moveto.asp
    context.moveTo(0, xAxis -unit);
    context.lineTo(width, xAxis -unit);
    
    context.moveTo(0, xAxis + unit);
    context.lineTo(width, xAxis + unit);
    
//    context.moveTo(0, xAxis);
//    context.lineTo(width, xAxis + 10);
//    context.lineTo(width, xAxis);
    
}

function drawSine(t) {

	//ref https://stackoverflow.com/questions/11895807/why-cant-i-draw-two-lines-of-varying-colors-in-my-html5-canvas 'answered Aug 10 '12 at 5:20'
	/***************************
		begin path
	 ***************************/
	context.beginPath();
	
    // Set the initial x and y, starting at 0,0 and translating to the origin on
    // the canvas.
    var x = t;
    var y = Math.sin(x);
    context.moveTo(yAxis, unit*y+xAxis);
    
    /***************************
		line color : prep
	 ***************************/
//    var tmp_StrokeStyle = context.strokeStyle;
//    var tmp_FillStyle = context.fillStyle;
//    var tmp_LineWidth = context.lineWidth;

//    context.strokeStyle = '#f00';
//    context.fillStyle = '#fff';
//    context.lineWidth = 2;
    
    /***************************
		draw line
	 ***************************/
    // Loop to draw segments
    for (i = yAxis; i <= width; i += 10) {
        x = t+(-yAxis+i)/unit;
        y = Math.sin(x);
        
        context.lineTo(i, unit*y+xAxis);
        
    }
    
    /***************************
		line color : restore
	 ***************************/
//	context.strokeStyle = '#00f';
//	context.fillStyle = tmp_FillStyle;
//	context.lineWidth = tmp_LineWidth;
	
}

function drawCircle() {
	
	/***************************
		begin path
	 ***************************/
	context.beginPath();
	
    context.moveTo(yAxis+unit, xAxis);
    context.arc(yAxis, xAxis, unit, 0, 2*Math.PI, false);
}

function drawArrow(t) {
    
    // Cache position of arrow on the circle
    var x = yAxis+unit*Math.cos(t);
    var y = xAxis+unit*Math.sin(t);
    
    // Draw the arrow line
    context.beginPath();
    context.moveTo(yAxis, xAxis);
    context.lineTo(x, y);
    
    //test
    context.strokeStyle = '#0f0';
    context.stroke();
    context.strokeStyle = '#00f';

    
//    context.stroke();
    
    // Draw the arrow bead
    context.beginPath();
    context.arc(x, y, 5, 0, 2*Math.PI, false);
    context.fill();
    context.stroke();
    
    // Draw dashed line to yAxis
    context.beginPath();
    var direction = (Math.cos(t) < 0) ? 1 : -1;
    var start = (direction==-1) ? -5 : 0;
    for (var i = x;  direction*i < direction*yAxis-5; i = i+direction*10) {
        context.moveTo(i+direction*5, y);
        context.lineTo(i+direction*10, y);
    }
    
    //test
    context.strokeStyle = '#f0f';
    context.stroke();
    context.strokeStyle = '#00f';

    
//    context.stroke();
    
    // Draw yAxis bead
    context.beginPath();
    context.arc(yAxis, y, 5, 0, 2*Math.PI, false);
    context.fill();
    context.stroke();
}
