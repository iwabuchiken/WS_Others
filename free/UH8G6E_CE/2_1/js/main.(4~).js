var canvas;
var ctx;

var interval = 500;

$(document).ready(function(){

	canvas = document.querySelector('#canvas_area');
//	canvas = document.querySelector('#canvas-container');
	ctx = canvas.getContext('2d');
//	var canvas = document.querySelector('#canvas-container');
//	var ctx = canvas.getContext('2d');

	alert("ready");

	
})

var count = 0;

var color_string = "";

var timer = setInterval(function(){
	
//	  ctx.fillStyle="#ffffff";//消去時の色
	  ctx.fillStyle="#fff";//消去時の色
	  ctx.clearRect(0,0,300,300);//消す
//	  ctx.fillStyle="#ff0000";//塗りつぶし色を赤に
	  
//	  ctx.fillStyle="#f00";//塗りつぶし色を赤に
//	  ctx.fillStyle="#ff00" + count;//塗りつぶし色を赤に
	  
	  //ref https://stackoverflow.com/questions/57803/how-to-convert-decimal-to-hex-in-javascript
	  
	  var element = Math.floor(count * 5 % 256.0).toString(16);
//	  var element = Math.floor(count * 10 / 256.0).toString(16);
//	  var element = count.toString(16);
	  
	  $('#message_area').html(element);
	  
	  if (element.length == 1) {
		  
		  element = "0" + element;
		  
	  }
	  
	  color_string = "#ff00" + element;
//	  color_string = "#ff00" + count.toString(16);
	  
//	  $('#message_area').html(color_string + "(len = " + color_string.length + ")");
	  
	  ctx.fillStyle= color_string;
//	  ctx.fillStyle="#ff00" + count.toString(16);//塗りつぶし色を赤に
	  
	  ctx.fillRect(30+count,30+count,30,30);
	  count++;
	  if(count>200){
	    clearInterval(timer);
	  }
	},
	100
);



function stop_Count() {
	
//	alert("stopping...");
	
	clearInterval(timer);

	/***************************
		disable
	 ***************************/
	//ref http://qiita.com/pugiemonn/items/5db6fb8fd8a303406b17
	$('button#stop').prop("disabled", true);
	$('button#start').prop("disabled", false);
	
}//function stop_Count()

function start_Count() {
	
//	alert("starting...");

//	id = setInterval(function(){
//		countup();
//		
//	    ctx.beginPath();
//	    
//	    ctx.arc(100 + (count - 1) * 20 , 100, 30, 0, 2*Math.PI, false);
//	    ctx.fillStyle = '#FFFFFF';
////	    ctx.fillStyle = '#FF0000';
//	    ctx.fill();
//	    
//	    ctx.beginPath();
//	    
//	    ctx.arc(100 + count * 20 , 100, 20, 0, 2*Math.PI, false);
//	    ctx.fillStyle = '#FF00FF';
//	    ctx.fill();
//
//		
////		if(count > 5){　
//		if(count > 50) {
//			clearInterval(id);　//idをclearIntervalで指定している
//		}
//	}//function()
//	, 
//	1000
//);

	timer = setInterval(function(){
//		setInterval(function(){
//			countup();
			
		  ctx.fillStyle="#fff";//消去時の色
		  ctx.clearRect(0,0,300,300);//消す
		  ctx.fillStyle="#f00";//塗りつぶし色を赤に
		  ctx.fillRect(30+count,30+count,30,30);
		  count++;
		  if(count>200){
		    clearInterval(timer);
		  }
		},
		100
	);
	
	/***************************
		disable
	 ***************************/
	//ref http://qiita.com/pugiemonn/items/5db6fb8fd8a303406b17
	$('button#stop').prop("disabled", false);
	$('button#start').prop("disabled", true);

}//function start_Count()


