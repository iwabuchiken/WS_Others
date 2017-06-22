var canvas;
var ctx;

var timeout = 1000;

var Particle;

var particle;

var clickPoint;

var mouseX;
var mouseY;

$(document).ready(function(){

//	canvas = document.querySelector('#canvas_area');
//	ctx = canvas.getContext('2d');

//	alert("ready");
	
//	alert(window.HTMLCanvasElement);

	init();
	
})

function _init_2_4() {

	canvas = document.getElementById("canvas-container");
	
	ctx = canvas.getContext('2d');
    var queue = null;
	
    //ref http://www.webopixel.net/javascript/1015.html
    window.addEventListener("resize", 
    		function() {

//    			alert("resized...");
//		        clearTimeout( queue );
//		        queue = setTimeout(function() {
//		            setCanvasSize();
//		        }, 300 );
		        
    		}//function() {
    		, false 
    );//window.addEventListener(

//    alert("clientWidth => " + document.documentElement.clientWidth);
    
    var setCanvasSize = function() {
        canvas.width = document.documentElement.clientWidth;
        canvas.height = document.documentElement.clientHeight - 300;
//        canvas.height = document.documentElement.clientHeight;
    };
    
    setCanvasSize();
    
    clickPoint = {
//    		var clickPoint = {
            x: 0,
            y: 0
    };
    
//    var Particle = function(scale, color, speed) {
    	Particle = function(scale, color, speed) {
        this.scale = scale; //大きさ
        this.color = color; //色
        this.speed = speed; //速度
        this.position = {   // 位置
            x: 0,
            y: 0
        };
    };
    
    Particle.prototype.draw = function() {
        ctx.beginPath();
        ctx.arc(this.position.x, this.position.y, this.scale, 0, 2*Math.PI, false);
        ctx.fillStyle = this.color;
        ctx.fill();
    };
    
    Particle.prototype.update = function() {
    	
    	//debug
    	console.log("updating...");
    	
        this.position.x += (clickPoint.x - this.position.x) / this.speed;
        this.position.y += (clickPoint.y - this.position.y) / this.speed;

        this.draw();
    };
    
    particle = new Particle(7, '#D0A000', 20);
//    var particle = new Particle(7, '#D0A000', 20);

    //ref C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\2_1\js\main.(5~).js
    draw();
    
//    var loop = function() {
//        requestAnimFrame(loop);
//        // 描画をクリアー
//        ctx.clearRect(0,0, ctx.canvas.width, ctx.canvas.height);
//
//        particle.update();
//    };
//    
//    loop();

    var rect = canvas.getBoundingClientRect();
    
    canvas.addEventListener('mousemove', 
		function(e) {
    	
	        mouseX = e.clientX - rect.left;
	        mouseY = e.clientY - rect.top;
//	        var mouseX = e.clientX - rect.left;
//	        var mouseY = e.clientY - rect.top;
	
	        clickPoint.x = mouseX;
	        clickPoint.y = mouseY;
	        
		    var msg = "mouseX = " + mouseX + " / "
		    		+ "mouseY = " + mouseY;
		    
	    	$('div#message_area').html(msg);

	
	    }//function(e) {
	    , false
    );//canvas.addEventListener(
    
    
    
}//_init_2_4()

function _init_2_5() {
	
	// Canvas未サポートは実行しない
    if (!window.HTMLCanvasElement) return;

    canvas = document.querySelector('#canvas-container');
    ctx = canvas.getContext('2d');
    var queue = null;

    // Canvasサイズを100%

    window.addEventListener("resize", 
    		function() {
    	
//		        clearTimeout( queue );
//		        queue = setTimeout(function() {
//		            setCanvasSize();
//		        }, 300 );
		        
    		}//function() {
    		, false 
    		
	);//window.addEventListener(

    var setCanvasSize = function() {
        canvas.width = document.documentElement.clientWidth;
        canvas.height = document.documentElement.clientHeight - 300;
//        canvas.height = document.documentElement.clientHeight;
    };
    
    setCanvasSize();


    var clickPoint = {
        x: 0,
        y: 0
    };

    var Particle = function(scale, color, speed) {
        this.scale = scale; //大きさ
        this.color = color; //色
        this.speed = speed; //速度
        this.position = {   // 位置
            x: 0,
            y: 0
        };
    };

    Particle.prototype.draw = function() {
    	
    	console.log("drawing...");
    	
        ctx.beginPath();
        ctx.arc(this.position.x, this.position.y, this.scale, 0, 2*Math.PI, false);
        ctx.fillStyle = this.color;
        ctx.fill();
    };

    Particle.prototype.update = function() {
        this.position.x += (clickPoint.x - this.position.x) / this.speed;
        this.position.y += (clickPoint.y - this.position.y) / this.speed;

        this.draw();
    };

    var particle = new Particle(7, '#D0A000', 20);

    //test
    draw(ctx, particle);
//    draw("abcde");
//    draw();
    
//    var loop = function() {
//        requestAnimFrame(loop);
//        // 描画をクリアー
//        ctx.clearRect(0,0, ctx.canvas.width, ctx.canvas.height);
//
//        particle.update();
//    };
//    loop();

    var rect = canvas.getBoundingClientRect();

    canvas.addEventListener('mousemove', function(e) {
        var mouseX = e.clientX - rect.left;
        var mouseY = e.clientY - rect.top;

        clickPoint.x = mouseX;
        clickPoint.y = mouseY;
        
	    var msg = "mouseX = " + mouseX + " / "
		+ "mouseY = " + mouseY;

	    $('div#message_area').html(msg);


    }, false);
    
}//_init_2_4()

function init() {
	
//	canvas = document.getElementById("canvas-container");
//	
//	ctx = canvas.getContext('2d');
//    var queue = null;
//	
//    //ref http://www.webopixel.net/javascript/1015.html
//    window.addEventListener("resize", 
//    		function() {
//
////    			alert("resized...");
////		        clearTimeout( queue );
////		        queue = setTimeout(function() {
////		            setCanvasSize();
////		        }, 300 );
//		        
//    		}//function() {
//    		, false 
//    );//window.addEventListener(
    
    _init_2_5();
//    _init_2_4();
    
    
//	//ref http://www.webopixel.net/javascript/1015.html
//	var rect = canvas.getBoundingClientRect();
//	
////	alert("rect => " + rect);
//	
//	console.log("rect.left => " + rect.left);
//	
//	canvas.addEventListener('click', function(e) {
//	    var mouseX = e.clientX - rect.left;
//	    var mouseY = e.clientY - rect.top;
//	    
//	    var msg = "X = " + mouseX + " / "
//	    		+ "Y = " + mouseY;
//	    
//	    $('div#message_area').html(msg);
//	    
//	    
//	}, false);
//
//	canvas.addEventListener('mousemove', function(e) {
////		console.log('moving...');
//		
//	    var mouseX = e.clientX - rect.left;
//	    var mouseY = e.clientY - rect.top;
//	    
//	    var msg = "X = " + mouseX + " / "
//	    		+ "Y = " + mouseY;
//	    
//	    $('div#message_area').html(msg);
//		
//	}, false);

//	alert(canvas);	//=> w.
	
//	canvas.addEventListener('click', function(e) {
//	    console.log('click');
//	}, false);
//	
//	canvas.addEventListener('mousemove', function(e) {
//		console.log('moving...');
//	}, false);
	
	
}

//function draw() {
//draw = function() {
//draw = function(msg) {
		//draw(ctx, particle);
draw = function(ctx, particle) {
	
//	console.log("ctx => " + ctx);

	ctx.clearRect(0,0, ctx.canvas.width, ctx.canvas.height);
	
	particle.update();

//	setTimeout(draw(ctx, particle), timeout);
	
	
//	console.log("drawing..." + " " + msg);
	
//	setTimeout(draw, timeout);
//	setTimeout(draw(), timeout);
	
}

//draw = function () {
//	
////	alert("drawing...");
//	console.log("drawing...");
//
//	particle.update();
//	
////	setTimeout(draw, timeout);
//	
//}//draw = function () {
