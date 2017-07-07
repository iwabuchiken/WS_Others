/*
 * regex expression
 * 
^([^\/](.|\t)+)alert

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 

C:\WORKS_2\WS\WS_Others\free\
C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\

/WS/WS_Others/free/UH8G6E_CE/


 */

/*
 * ref http://symfoware.blog68.fc2.com/blog-entry-1958.html
 */

//alert("js starting...");

/***************************
	@param
		(4, 5)	=> [4, 0]
		(5, 4)	=> [4, 1]
 ***************************/
function smaller(x, y) {
	
	if (x <= y) {
//		if (x >= y) {

		return [x, 0];

	} else {

		return [y, 1];;

	}//if (x >= y)
	
}//function smaller(x, y) {

/***************************
	@param
		[4, 5]	=> [4, 0]
		[5, 4]	=> [4, 1]
 ***************************/
function smaller_InArray(aryOf_Two_Numbers) {
	
	/***************************
		validate
	 ***************************/
	if (aryOf_Two_Numbers.length < 1) {

		//alert("smaller_InArray : array size less than 1");
		
		return null;

	}//if (aryOf_Two_Numbers.length) {

	/***************************
		operations
	 ***************************/
	if (aryOf_Two_Numbers[0] <= aryOf_Two_Numbers[1]) {
//		if (aryOf_Two_Numbers[0] >= aryOf_Two_Numbers[1]) {
		
		return [aryOf_Two_Numbers[0], 0];
		
	} else {
		
		return [aryOf_Two_Numbers[1], 1];;
		
	}//if (x >= y)
	
}//function smaller(x, y) {

function get_ImageObj_WH_Resized(canvas, imageObj) {

	var size_Canvas = [canvas.width, canvas.height];
	
	var size_Image = [imageObj.width, imageObj.height];
	
//	alert("size_Canvas => " + size_Canvas);

//	var res_Smaller = smaller_InArray(size_Canvas);
//	
//	alert("size_Canvas => " + size_Canvas
//			
//			+ " / "
//			+ "res_Smaller => " + res_Smaller
//	);
	
	/***************************
		resize
	 ***************************/
	var ratio_W = size_Canvas[0] / size_Image[0] * 1.0;
	var ratio_H = size_Canvas[1] / size_Image[1] * 1.0;
	
//	alert("ratio W => " + ratio_W
//	
//			+ " / "
//			+ "ratio H => " + ratio_H
//	);

	// calc
	var ratio_Final = 0.0;
	
	if (ratio_W <= ratio_H) {

		ratio_Final = ratio_W;

	} else {

		ratio_Final = ratio_H;

	}//if (ratio_W >= ratio_H)

	var resized = [
		
		Math.floor(size_Image[0] * ratio_Final),
		
		Math.floor(size_Image[1] * ratio_Final)
		
	];
	
//	//debug
//	alert("orig => " + size_Image
//	
//			+ " / "
//			+ "resized => " + resized
//			
//			+ " / "
//			+ "canvas => " + size_Canvas
//			
//	);
	
	/***************************
		return
	 ***************************/
	return resized;
//	return null;
	
//	var ratio = 0.0;
//	
//	var str_Ratio = "";
//	
//	var w_Resized = 0.0;
//	
//	var h_Resized = 0.0;
//	
//	if (res_Smaller[1] == 0) {	// smaller ==> width
//
//		alert("res_Smaller[1] => 0");
//		
//		ratio = size_Canvas[0] / size_Image[0] * 1.0
//		
//		str_Ratio = size_Canvas[0]  + " / " + size_Image[0];
//
//		// resize
//		w_Resized = size_Canvas[0];
//		
//		h_Resized = ratio * size_Image[1];
//		
//	} else {	// smaller ==> height
//
//		alert("res_Smaller[1] => 1");
//		
//		ratio = size_Canvas[1] / size_Image[1] * 1.0
//
//		str_Ratio = size_Canvas[1]  + " / " + size_Image[1];
//
//		// resize
//		w_Resized = ratio * size_Image[0];
//		
//		h_Resized = size_Canvas[1];
//
//	}//if (res_Smaller[1] == 0)
//	
////	alert("ratio => " + ratio + "(" + "str_Ratio = " + str_Ratio + ")");
////	
//	alert("orig => " + size_Image
//			+ " / " + "resize => " + [w_Resized, h_Resized]
//			+ " / " + "canvas => " + size_Canvas
//			
//	);
//	
//	// 
//
//	// return
//	return [Math.floor(w_Resized), Math.floor(h_Resized)];
////	return [w_Resized, h_Resized];
	
}//get_WH_Resized(canvas, imageObj)

function get_Image() {
	
	var url = $('input#ipt_Image_File_URL').val();
	
//	alert("url => " + url);
	
	// set : new url
	imageObj.src = url;

	/***************************
		change : button color
	 ***************************/
	$('button#btn_Image_File_URL').css("background-color", "yellow");
	
	// draw
	draw();
	
}//get_Image()

var canvas = null;
var context = null;
var reacts = null;
var imageFile_WH_Resized = null;
var imageObj = null;
//var canvas_Height_Ratio = 1.0;
//var canvas_Height_Ratio = 2.0;
var canvas_Height_Ratio = 0.8;
var size_Canvas = null;

var context_Line_Width = 1;
//var context_Line_Width = 2;

var line_Color__Red = "rgb(255, 0, 0)";
var line_Color__Yellow = "rgb(255, 255, 0)";

var numOf_Grid_Lines = 5;

var dflt_Image_URL = 'http://benfranklin.chips.jp/cake_apps/images/ifm11/2014-08-12_12-17-13_686.jpg';

var _rectangle = null;

/***************************
	flags
 ***************************/
var flag_Canvas_Click_Start = 1;	// default ---> 1 : waiting for the first click
									//				-1 : waiting for the second click

/******************************************************
	funcs
******************************************************/
function bt_Clear_All_Rects() {
	
	reacts = [];
//	reacts.pop();
	
	draw();
	
}//bt_Clear_All_Rects()

function bt_Clear_One_Rects() {
	
	reacts.pop();
	
	draw();
	
}//bt_Clear_One_Rects()

function draw() {
	
//	context.drawImage(imageObj, 0, 0, 100, 100);
	context.drawImage(imageObj, 0, 0, imageFile_WH_Resized[0], imageFile_WH_Resized[1]);
	
    context.lineWidth = context_Line_Width;
//    context.lineWidth = 5;
    //ref http://www.html5.jp/canvas/how3.html
    context.strokeStyle = line_Color__Red;
//    context.strokeStyle = "rgb(255, 0, 0)";
    
    reacts.forEach(
    		function(rect) {
    	
            	context.strokeRect(rect.startX, rect.startY, rect.endX, rect.endY);
            
            	//test
            	var tick_X = Math.floor(rect.endX / numOf_Grid_Lines);
            	
            	var tick_Y = Math.floor(rect.endY / numOf_Grid_Lines);
            	
//            	alert("tick X => " + tick_X 
//            			+ " / "
//            			+ "tick Y => " + tick_Y
//            	);
            	
            	context.beginPath();
            	
            	for (var int = 1; int < numOf_Grid_Lines; int++) {
//            		for (var int = 1; int < 4; int++) {
					
            		context.moveTo(rect.startX + tick_X * int, rect.startY);
                	context.lineTo(rect.startX + tick_X * int, rect.startY + rect.endY);	//
                	
                	context.moveTo(rect.startX, rect.startY + tick_Y * int);
                	context.lineTo(rect.startX + rect.endX, rect.startY + tick_Y * int);	//
                	
				}
            	
//            	context.moveTo(rect.startX + tick_X, rect.startY);
//            	context.lineTo(rect.startX + tick_X, rect.startY + rect.endY);	// 
            	
//            	context.moveTo(rect.startX, rect.startY);
//            	context.lineTo(100, 100);
//            	context.lineTo(rect.endX, rect.endY);	// n.w.
//            	context.lineTo(rect.startX + rect.endX, rect.startY + rect.endY);	// 
            	
            	
//            	context.closePath();
            	
            	// color
            	context.strokeStyle = line_Color__Yellow;
            	
            	context.stroke();

            	// color : reset
            	context.strokeStyle = line_Color__Red;

        	}//reacts.forEach(function(rect) {
    		
    );//reacts.forEach(

	/***************************
		change : button color
	 ***************************/
	$('button#btn_Image_File_URL').css("background-color", "LightCyan");

};//function draw() {

function createRect() {
    return { startY:0, startX:0, endY:0, endX:0 };
};


function _window_OnLoad__Setup() {

    canvas = document.getElementById('drowing');
//  var canvas = document.getElementById('drowing');
  context = canvas.getContext('2d');
//  var context = canvas.getContext('2d');
  reacts = [];
//  var reacts = [];
  
  imageFile_WH_Resized = null;
//  var imageFile_WH_Resized = null;
  	
  imageObj = new Image();
//  var imageObj = new Image();
  
//  var canvas_Height_Ratio = 0.8;
  
  imageObj.onload = function() {
  	
//      canvas.width = window.innerWidth / 2;
      canvas.width = window.innerWidth;
//    canvas.width = window.innerWidth;;
//    canvas.width = imageObj.width;
   canvas.height = window.innerHeight * canvas_Height_Ratio;
//   canvas.height = window.innerHeight / 2;
//    canvas.height = imageObj.height / 2;
//    canvas.height = imageObj.height;

   size_Canvas = [canvas.width, canvas.height];
//   var size_Canvas = [canvas.width, canvas.height];
   
	     //test
	//     alert("imageObj.height => " + imageObj.height);	//=> 3264
	     
	     imageFile_WH_Resized = get_ImageObj_WH_Resized(canvas, imageObj);
   
      draw();
      
  };
	
  imageObj.src = dflt_Image_URL;
//  imageObj.src = 'http://benfranklin.chips.jp/cake_apps/images/ifm11/2014-08-12_12-17-13_686.jpg';

  /***************************
	rectangle
 ***************************/
  _rectangle = createRect();
  
}//function _window_OnLoad__Setup() {

function onMouseMove (e) {
    draw();
    _rectangle.endY = e.layerY - _rectangle.startY;
    _rectangle.endX = e.layerX - _rectangle.startX;
    
    context.lineWidth = context_Line_Width;
//    context.lineWidth = 5;
    
    context.strokeStyle = "rgb(255, 0, 0)";
    context.strokeRect (_rectangle.startX, _rectangle.startY, _rectangle.endX, _rectangle.endY);
};


function onMouseDown (e) {
    _rectangle.startY = e.clientY;
    _rectangle.startX = e.clientX;
    canvas.addEventListener ("mousemove", onMouseMove, false);
    
    //test
    console.log("selection => started !! (global function)");
    
//    // set values
//    $('input#ipt_Main_Range_Start_X').val(e.clientX);
////    $('input#ipt_Main_Range_Start_X').text(e.clientX);
//    
//    console.log("value set !! => Start X : " + e.clientX);
    
//    alert("selection => started !!");
//    alert("selection => started");
    if (flag_Canvas_Click_Start == 1) {

//		alert("first click");
		console.log("first click");

	    // set values
	    $('input#ipt_Main_Range_Start_X').val(e.clientX);
	    
	    $('input#ipt_Main_Range_Start_Y').val(e.clientY);
	    
	    console.log("value set !! => Start X : " + e.clientX);

		// update
		flag_Canvas_Click_Start = flag_Canvas_Click_Start * (-1);

	} else {

//		alert("second click");
		console.log("second click");

	    // set values
	    $('input#ipt_Main_Range_End_X').val(e.clientX);
	    
	    $('input#ipt_Main_Range_End_Y').val(e.clientY);
	    
	    console.log("value set !! => End X : " + e.clientX);

		// update
		flag_Canvas_Click_Start = flag_Canvas_Click_Start * (-1);

	}//if (flag_Canvas_Click_Start == 1)
	
    
};


function window_OnLoad() {

	_window_OnLoad__Setup();
	
    canvas.addEventListener("mousedown", onMouseDown, false);
    canvas.addEventListener("mouseup" , onMouseUp , false);
    window.addEventListener("keyup" , onKeyUp , false);
    
    // 矩形オブジェクト
//    var _rectangle = createRect();
    
//    function createRect() {
//        return { startY:0, startX:0, endY:0, endX:0 };
//    };
    
//    function onMouseDown (e) {
//        _rectangle.startY = e.clientY;
//        _rectangle.startX = e.clientX;
//        canvas.addEventListener ("mousemove", onMouseMove, false);
//        
//        //test
//        console.log("selection => started !!");
//        
//        // set values
//        
//        
////        alert("selection => started !!");
////        alert("selection => started");
////        if (flag_Canvas_Click_Start == 1) {
////
////			alert("first click");
////			
////			// update
////			flag_Canvas_Click_Start = flag_Canvas_Click_Start * (-1);
////
////		} else {
////
////			alert("second click");
////
////			// update
////			flag_Canvas_Click_Start = flag_Canvas_Click_Start * (-1);
////
////		}//if (flag_Canvas_Click_Start == 1)
//		
//        
//    };
    
//    function onMouseMove (e) {
//        draw();
//        _rectangle.endY = e.layerY - _rectangle.startY;
//        _rectangle.endX = e.layerX - _rectangle.startX;
//        
//        context.lineWidth = context_Line_Width;
////        context.lineWidth = 5;
//        
//        context.strokeStyle = "rgb(255, 0, 0)";
//        context.strokeRect (_rectangle.startX, _rectangle.startY, _rectangle.endX, _rectangle.endY);
//    };
    function onMouseUp (e) {
    	
        reacts.push(_rectangle);
        
//        //debug
//        alert("rectangle => " + _rectangle);
        
        draw();
        
        _rectangle = createRect();
        
        canvas.removeEventListener ("mousemove", onMouseMove, false);

        //test
        console.log("selection => ended");
//        alert("selection => ended");

    };
    
    function onKeyUp (e) {
        switch(e.key) {
            case 'z':
                reacts.pop();
                break;
            default:
                return;
        };
        draw();
    };

}//window_OnLoad

window.onload = function() {
	
	window_OnLoad();
    
};
