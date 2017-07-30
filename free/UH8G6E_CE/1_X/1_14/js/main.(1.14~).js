/*
 * regex expression
 * 
^([^\/](.|\t)+)alert

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 

C:\WORKS_2\WS\WS_Others\free\
C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\

/WS/WS_Others/free/UH8G6E_CE/
/WS/WS_Others/free/UH8G6E_CE/1_X

 */

/*
 * ref http://symfoware.blog68.fc2.com/blog-entry-1958.html
 */

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
var line_Color__Gray_180 = "rgb(180, 180, 180)";

var line_Color__Blue = "rgb(145, 190, 255)";

var numOf_Grid_Lines = 5;

var dflt_Image_URL = 'http://benfranklin.chips.jp/cake_apps/images/ifm11/2014-08-12_12-17-13_686.jpg';

var _rectangle = null;

var ratio_Final = null;

var sx = null, sy = null, sw = null, sh = null, dx = null, dy = null, dw = null, dh = null;

/***************************
	flags
 ***************************/
var flag_Canvas_Click_Start = 1;	// default ---> 1 : waiting for the first click
									//				-1 : waiting for the second click
var flag_Draw_Grid = 1;	// default ---> 1
var flag_Draw_Grid_Slanted = 1;	// default ---> 1

var flag_Draw_Grid__Slanted = 1;

var flag_Draw_Circle = 0;

/******************************************************
	funcs
******************************************************/
/***************************
@param
	(4, 5)	=> [4, 0]
	(5, 4)	=> [4, 1]
***************************/
function smaller(x, y) {

	if (x <= y) {
	//	if (x >= y) {
	
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
	//	if (aryOf_Two_Numbers[0] >= aryOf_Two_Numbers[1]) {
		
		return [aryOf_Two_Numbers[0], 0];
		
	} else {
		
		return [aryOf_Two_Numbers[1], 1];;
		
	}//if (x >= y)

}//function smaller(x, y) {

function get_ImageObj_WH_Resized(canvas, imageObj) {

	var size_Canvas = [canvas.width, canvas.height];
	
	var size_Image = [imageObj.width, imageObj.height];
	
	/***************************
		resize
	 ***************************/
	var ratio_W = size_Canvas[0] / size_Image[0] * 1.0;
	var ratio_H = size_Canvas[1] / size_Image[1] * 1.0;
	
	// calc
	ratio_Final = 0.0;
//	var ratio_Final = 0.0;

	if (ratio_W <= ratio_H) {
	
		ratio_Final = ratio_W;
	
	} else {
	
		ratio_Final = ratio_H;
	
	}//if (ratio_W >= ratio_H)
	
	var resized = [
		
		Math.floor(size_Image[0] * ratio_Final),
		
		Math.floor(size_Image[1] * ratio_Final)
		
	];
	
	/***************************
		return
	 ***************************/
	return resized;

}//get_WH_Resized(canvas, imageObj)

function get_ImageObj_WH_Resized__2(canvas, target_W, target_H) {
	
	var size_Canvas = [canvas.width, canvas.height];
	
	var size_Image = [target_W, target_H];
	//var size_Image = [imageObj.width, imageObj.height];
	
	/***************************
		resize
	 ***************************/
	var ratio_W = size_Canvas[0] / size_Image[0] * 1.0;
	var ratio_H = size_Canvas[1] / size_Image[1] * 1.0;
	
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
	
	/***************************
		return
	 ***************************/
	return resized;

}//get_WH_Resized(canvas, imageObj)

function get_Image() {
	
	var url = $('input#ipt_Image_File_URL').val();
	
	//alert("url => " + url);
	
	// set : new url
	imageObj.src = url;
	
	/***************************
		change : button color
	 ***************************/
	$('button#btn_Image_File_URL').css("background-color", "yellow");
	
	// draw
	draw();
	
}//get_Image()

function bt_Clear_All_Rects() {
	
	reacts = [];
//	reacts.pop();
	
	draw();

	/***************************
		button 'toggle' : able
	 ***************************/
	//ref http://qiita.com/pugiemonn/items/5db6fb8fd8a303406b17
	$('button#btn_Main_Toggle_Grid').prop("disabled", true);
	
	$('button#btn_Main_Toggle_Grid').css("background-color", "DarkOrange");

	/***************************
		button 'toggle' slanted : able
	 ***************************/
	//ref http://qiita.com/pugiemonn/items/5db6fb8fd8a303406b17
	$('button#btn_Main_Toggle_Grid_Slanted').prop("disabled", true);
	
	$('button#btn_Main_Toggle_Grid_Slanted').css("background-color", "DarkOrange");
	
}//bt_Clear_All_Rects()

function bt_Clear_One_Rects() {
	
	reacts.pop();
	
//	alert("reacts => " + reacts.length);
	
	draw();

	/***************************
		button 'toggle' : able
	 ***************************/
	var lenOf_Reacts = reacts.length;
	
	if (lenOf_Reacts < 1) {

		$('button#btn_Main_Toggle_Grid').prop("disabled", true);
		
		$('button#btn_Main_Toggle_Grid').css("background-color", "DarkOrange");

	}//if (lenOf_Reacts < 1) {

	/***************************
		button 'toggle' slanted : able
	 ***************************/
	var lenOf_Reacts = reacts.length;
	
	if (lenOf_Reacts < 1) {
		
		$('button#btn_Main_Toggle_Grid_Slanted').prop("disabled", true);
		
		$('button#btn_Main_Toggle_Grid_Slanted').css("background-color", "DarkOrange");
		
	}//if (lenOf_Reacts < 1) {
	
//	$('button#btn_Main_Toggle_Grid').prop("disabled", true);
	

}//bt_Clear_One_Rects()

function bt_Canvas_Zoom_In() {
	
	/***************************
		coordinates
	 ***************************/
    var start_X = $('input#ipt_Main_Range_Start_X').val();
    
    var start_Y = $('input#ipt_Main_Range_Start_Y').val();
    
    var end_X = $('input#ipt_Main_Range_End_X').val();
    
    var end_Y = $('input#ipt_Main_Range_End_Y').val();

    /***************************
		validate
	 ***************************/
	if (start_X == '' || start_Y == '') {

		alert("start X, start Y ---> not given");

		return;
		
	} else if (end_X == '' || end_Y == '') {

		alert("end X, end Y ---> not given");

		return;

	} else {

	}//if (start_X == '' || start_Y == '')
	
//    alert("4 coordinates ---> given");

    var w = end_X - start_X;
    var h = end_Y - start_Y;
    
    console.log(
    		"w = " + w
    		+ " / "
    		+ "h = " + h
    );
    
//    // update : resized
//    imageFile_WH_Resized = get_ImageObj_WH_Resized__2(canvas, w, h);
//    var resized = get_ImageObj_WH_Resized__2(canvas, w, h);
    
	/***************************
		update : others
	***************************/
    var ratio_Reverse = 1 / ratio_Final;
    
	sx = Math.floor(start_X * ratio_Reverse);
	sy = Math.floor(start_Y * ratio_Reverse);
//	sx = start_X;
//	sy = start_Y;
//	Math.floor(sx * ratio_Reverse), Math.floor(sy * ratio_Reverse), 
////	sw * 10, sh * 10, 
//	Math.floor(sw * (1 / ratio_Final)), Math.floor(sh * (1 / ratio_Final)), 
	
	sw = Math.floor(w * (1 / ratio_Final));
	sh = Math.floor(h * (1 / ratio_Final));
//	sw = w; 
//	sh = h;
//	Math.floor(sw * (1 / ratio_Final)), Math.floor(sh * (1 / ratio_Final))	
	
	dx = 0;
	dy = 0;

    // update : resized
    imageFile_WH_Resized = get_ImageObj_WH_Resized__2(canvas, w, h);

	dw = imageFile_WH_Resized[0];
	 
	dh = imageFile_WH_Resized[1];
    
	/***************************
		grid ---> remove all
	 ***************************/
	if (true) {

		reacts = [];

	}//if (true) {
	
	/***************************
		draw
	 ***************************/
	// clear canvas
	//ref https://stackoverflow.com/questions/2142535/how-to-clear-the-canvas-for-redrawing 'answered Jan 26 '10 at 20:52'
	context.clearRect(0, 0, canvas.width, canvas.height);

//	console.log("resizing...");
	
	draw();
	
	/***************************
		'toggle' button
	 ***************************/
	//ref http://qiita.com/pugiemonn/items/5db6fb8fd8a303406b17
	$('button#btn_Main_Toggle_Grid').prop("disabled", true);
	
	$('button#btn_Main_Toggle_Grid').css("background-color", "DarkOrange");

	
	
//    console.log(
//    		"canvas.w = " + canvas.width
//    		+ " / "
//    		+ "canvas.h = " + canvas.height
//    );
//    
//    console.log(
//    		"resized.w = " + resized[0]
//    		+ " / "
//    		+ "resized.h = " + resized[1]
//    );
    
    
    
    
    // zoom
//    draw_Zoomed(0, 0, 300, 300, 0, 0, 300, 300);
//    draw_Zoomed(0, 0, 100, 100, 0, 0, 300, 300);
//    draw_Zoomed(start_X, start_Y, w, h, 0, 0, resized[0], resized[1]);	//=> w.
    
}//bt_Canvas_Zoom_In()

function bt_Canvas_Clear_Zoom_In() {
	
	/***************************
		- init params
		- clear canvas
		- draw
	 ***************************/
	/***************************
		init params
	 ***************************/
	imageFile_WH_Resized = get_ImageObj_WH_Resized(canvas, imageObj);
	 
	sx = 0; sy = 0;
	
	sw = imageObj.width; sh = imageObj.height;
	
	dx = 0; dy = 0;

	dw = imageFile_WH_Resized[0];
	 
	dh = imageFile_WH_Resized[1];

	/***************************
		clear canvas
	 ***************************/
	//ref https://stackoverflow.com/questions/2142535/how-to-clear-the-canvas-for-redrawing 'answered Jan 26 '10 at 20:52'
	context.clearRect(0, 0, canvas.width, canvas.height);

	
	/***************************
		clear rects
	 ***************************/
	reacts = [];
	
	/***************************
		'toggle' button
		- disable
		- change bg color
	 ***************************/
	//ref http://qiita.com/pugiemonn/items/5db6fb8fd8a303406b17
	$('button#btn_Main_Toggle_Grid').prop("disabled", true);
	
	$('button#btn_Main_Toggle_Grid').css("background-color", "DarkOrange");

	
	/***************************
		draw
	 ***************************/
	draw();

	
}//btn_Main_Clear_Zoom_In

function bt_Canvas_Draw_Circle() {
	
	/***************************
		flag
	 ***************************/
//	alert("draw circle");
	if (flag_Draw_Circle == 0) {

		flag_Draw_Circle = 1;
		
		console.log("flag_Draw_Circle : change to => " + flag_Draw_Circle);
		
		/***************************
			change : button color
		 ***************************/
		$('button#btn_Main_Draw_Circle').css("background-color", "PaleVioletRed");

	} else {//if (flag_Draw_Grid == 1) {
		
		flag_Draw_Circle = 0;
		
		console.log("flag_Draw_Circle : change to => " + flag_Draw_Circle);

		/***************************
			change : button color
		 ***************************/
		$('button#btn_Main_Draw_Circle').css("background-color", "Gray");

	}//if (flag_Draw_Grid == 1) {

	
	
}//bt_Canvas_Draw_Circle()

function bt_Canvas_Clear_Circle() {
	
	/***************************
		call 'draw()'
	 ***************************/
	draw();
	
	console.log("draw() ---> called");
	
}//bt_Canvas_Clear_Circle()

function _draw_Grid_2__Y(rect, numOf_Grid_Lines_2) {
	
	//test
//	var tick = 20;

	var interval = $('input#ipt_Main_Grid_Interval').val();
	
	var tick = null;
	
	if (interval == '') {
		
		tick = 20;
		
	} else 	if (parseInt(interval) < 1) {

		tick = 20;

	} else {

		tick = parseInt(interval);

	}//if (parseInt(interval) < 1)

	
	var numOf_Grids_X = Math.floor(rect.endX / tick);
//	var numOf_Grids_Y = Math.floor(rect.endY / tick);
	
//	console.log("numOf_Grids_X => " + numOf_Grids_X);
//	console.log("rect.endY => " + rect.endY);
//	console.log("tick => " + tick);
	
	var alternate = 1;
	
//	for (var i = 1; i < numOf_Grids_X; i++) {
		for (var i = 1; i <= numOf_Grids_X; i++) {
//		for (var i = 1; i <= numOf_Grids_X + 1; i++) {
//		for (var i = 1; i <= numOf_Grids_X; i++) {
//		for (var i = 1; i < numOf_Grids; i++) {

		/***************************
			line coordinates
		 ***************************/
//		console.log("beginning path...");
		
		context.beginPath();
		
		context.moveTo(rect.startX, 			rect.startY + tick * i);
		context.lineTo(rect.startX + rect.endX,	rect.startY + tick * i);	//

//		console.log("moveTo = " + rect.startX + "," + (rect.startY + tick * i));
//		console.log("lineTo = " + (rect.startX + rect.endX) + "," + (rect.startY + tick * i));

		context.moveTo(rect.startX + tick * i, rect.startY);
    	context.lineTo(rect.startX + tick * i, rect.startY + rect.endY);	//

    	/***************************
			draw grids
		 ***************************/
		// color
		if (alternate == 1) {
	
//			console.log("alternate => 1 !!!!");
			
	    	context.strokeStyle = line_Color__Yellow;
	    	
	    	context.stroke();
	
	    	// color : reset
	    	context.strokeStyle = line_Color__Red;
	
	    	// update : alternate
	    	alternate = alternate * (-1);
	    	
		} else {
	
//			console.log("alternate => -1");
			
	//		context.strokeStyle = line_Color__Yellow;
	    	context.strokeStyle = line_Color__Red;
	//    	context.strokeStyle = line_Color__Gray_180;
	    	
	    	context.stroke();
	
	    	// color : reset
	    	context.strokeStyle = line_Color__Red;
	
	    	// update : alternate
	    	alternate = alternate * (-1);
	
		}//if (alternate == 1)
		
//    	context.strokeStyle = line_Color__Gray_180;
////    	context.strokeStyle = line_Color__Yellow;
//    	
//    	context.stroke();
//
//    	// color : reset
//    	context.strokeStyle = line_Color__Red;

	}//for (var i = 0; i < numOf_Grids; i++)
	
}//function _draw_Grid_2__Y(rect, numOf_Grid_Lines_2) {

function _draw_Grid_2(rect, numOf_Grid_Lines_2) {

	//test
	var interval = $('input#ipt_Main_Grid_Interval').val();
	
	var tick = null;
	
	if (interval == '') {
		
		tick = 20;
		
	} else 	if (parseInt(interval) < 1) {

		tick = 20;

	} else {

		tick = parseInt(interval);

	}//if (parseInt(interval) < 1)
	
	
//	var tick = interval;
//	var tick = 20;
	
	var numOf_Grids_Y = Math.floor(rect.endY / tick);
	
//	console.log("numOf_Grids_Y => " + numOf_Grids_Y);
//	console.log("rect.endY => " + rect.endY);
//	console.log("tick => " + tick);
	
	var tick_X = Math.floor(rect.endX / numOf_Grid_Lines);
	
	var tick_Y = Math.floor(rect.endY / numOf_Grid_Lines);

	
	var alternate = 1;
	
	for (var i = 1; i <= numOf_Grids_Y + 1; i++) {
//		for (var i = 1; i <= numOf_Grids_Y; i++) {
//		for (var i = 1; i < numOf_Grids; i++) {

		/***************************
			line coordinates
		 ***************************/
//		console.log("beginning path...");
		
		context.beginPath();
		
		context.moveTo(rect.startX, 			rect.startY + tick * i);
		context.lineTo(rect.startX + rect.endX,	rect.startY + tick * i);	//

    	/***************************
			draw grids
		 ***************************/
		// color
		if (alternate == 1) {
	
//			console.log("alternate => 1 !!!!");
			
	    	context.strokeStyle = line_Color__Yellow;
	    	
	    	context.stroke();
	
	    	// color : reset
	    	context.strokeStyle = line_Color__Red;
	
	    	// update : alternate
	    	alternate = alternate * (-1);
	    	
		} else {
	
//			console.log("alternate => -1");
			
	//		context.strokeStyle = line_Color__Yellow;
	    	context.strokeStyle = line_Color__Red;
	//    	context.strokeStyle = line_Color__Gray_180;
	    	
	    	context.stroke();
	
	    	// color : reset
	    	context.strokeStyle = line_Color__Red;
	
	    	// update : alternate
	    	alternate = alternate * (-1);
	
		}//if (alternate == 1)
		
	}//for (var i = 0; i < numOf_Grids; i++)
	
	/***************************
		grid : Y
	 ***************************/
	_draw_Grid_2__Y(rect, numOf_Grid_Lines_2);
	
}//function _draw_Grid_2(rect, numOf_Grid_Lines_2) {

function _draw_Grid(rect, numOf_Grid_Lines_2) {

	_draw_Grid_2(rect, numOf_Grid_Lines_2);
	
}//function _draw_Grid() {

function _draw_Grid__Slanted__ToLeftDown__2_LowerRight(rect, tick) {

	/***************************
		vars
	 ***************************/
	var numOf_Grids_X = Math.floor(rect.endX / tick);
	var numOf_Grids_Y = Math.floor(rect.endY / tick);

	var alternate = 1;
	
	/***************************
		main
	 ***************************/
//	for (var i = 0; i <= numOf_Grids_X + 2; i++) {
	for (var i = 0; i <= numOf_Grids_X; i++) {
	//	for (var i = 0; i < numOf_Grids_X + 1; i++) {
		
		/***************************
			line coordinates
		 ***************************/
		context.beginPath();
		
		var sX = rect.startX + tick * i;
		var sY = rect.startY + tick * (numOf_Grids_Y + 1);
		
		var eX = rect.startX + tick * (numOf_Grids_X + 1);
		var eY = rect.startY + tick * (numOf_Grids_Y - (numOf_Grids_X - i));
//		var eY = rect.startY + tick * (i + 1);
//		var eY = rect.startY + tick * i;
		
		context.moveTo(sX,	sY);
		context.lineTo(eX,	eY);	//
		
		/***************************
			draw grids
		 ***************************/
		// color
		if (alternate == 1) {
			
	//		console.log("alternate => 1 !!!!");
			
			context.strokeStyle = line_Color__Blue;
	//    	context.strokeStyle = line_Color__Yellow;
			
			context.stroke();
			
			// color : reset
			context.strokeStyle = line_Color__Red;
			
			// update : alternate
			alternate = alternate * (-1);
			
		} else {
			
	//		console.log("alternate => -1");
			
			//		context.strokeStyle = line_Color__Yellow;
	//    	context.strokeStyle = line_Color__Red;
			context.strokeStyle = line_Color__Gray_180;
			
			context.stroke();
			
			// color : reset
			context.strokeStyle = line_Color__Red;
			
			// update : alternate
			alternate = alternate * (-1);
			
		}//if (alternate == 1)
		
	}//for (var i = 0; i < numOf_Grids; i++)
	
}//function _draw_Grid__Slanted__ToLeftDown__2_LowerRight(rect, tick) {

function _draw_Grid__Slanted__ToLeftDown__1_Main(rect, tick) {

//	console.log("_draw_Grid__Slanted__ToLeftDown__1_Main(rect, tick)");
	
	
	var numOf_Grids_Y = Math.floor(rect.endY / tick);
	
	var alternate = 1;

	/***************************
		main
	 ***************************/
	
//	for (var i = 1; i < numOf_Grids_Y; i++) {
		for (var i = 1; i <= numOf_Grids_Y; i++) {

		/***************************
			line coordinates
		 ***************************/
		context.beginPath();
		
		context.moveTo(rect.startX + tick * i,	rect.startY);
		context.lineTo(rect.startX,				rect.startY + tick * i);	//

    	/***************************
			draw grids
		 ***************************/
		// color
		if (alternate == 1) {
	
//			console.log("alternate => 1 !!!!");
			
			context.strokeStyle = line_Color__Blue;
//			context.strokeStyle = line_Color__Gray_180;
//	    	context.strokeStyle = line_Color__Yellow;
	    	
	    	context.stroke();
	
	    	// color : reset
	    	context.strokeStyle = line_Color__Red;
	
	    	// update : alternate
	    	alternate = alternate * (-1);
	    	
		} else {
	
//			console.log("alternate => -1");
			
	//		context.strokeStyle = line_Color__Yellow;
//	    	context.strokeStyle = line_Color__Red;
	    	context.strokeStyle = line_Color__Gray_180;
	    	
	    	context.stroke();
	
	    	// color : reset
	    	context.strokeStyle = line_Color__Red;
	
	    	// update : alternate
	    	alternate = alternate * (-1);
	
		}//if (alternate == 1)
		
	}//for (var i = 0; i < numOf_Grids; i++)
	
}//function _draw_Grid__Slanted__ToLeftDown__1_Main(rect, tick) {

function _draw_Grid__Slanted__ToLeftDown(rect, tick) {
	
//	console.log("_draw_Grid__Slanted__ToLeftDown");
	
	
	var numOf_Grids_Y = Math.floor(rect.endY / tick);
	
	var alternate = 1;

	/***************************
		main
	 ***************************/
	_draw_Grid__Slanted__ToLeftDown__1_Main(rect, tick);

	/***************************
		lower right
	 ***************************/
	_draw_Grid__Slanted__ToLeftDown__2_LowerRight(rect, tick);
	
	
	
////	for (var i = 1; i < numOf_Grids_Y; i++) {
//		for (var i = 1; i <= numOf_Grids_Y; i++) {
//
//		/***************************
//			line coordinates
//		 ***************************/
//		context.beginPath();
//		
//		context.moveTo(rect.startX + tick * i,	rect.startY);
//		context.lineTo(rect.startX,				rect.startY + tick * i);	//
//
//    	/***************************
//			draw grids
//		 ***************************/
//		// color
//		if (alternate == 1) {
//	
////			console.log("alternate => 1 !!!!");
//			
//			context.strokeStyle = line_Color__Blue;
////			context.strokeStyle = line_Color__Gray_180;
////	    	context.strokeStyle = line_Color__Yellow;
//	    	
//	    	context.stroke();
//	
//	    	// color : reset
//	    	context.strokeStyle = line_Color__Red;
//	
//	    	// update : alternate
//	    	alternate = alternate * (-1);
//	    	
//		} else {
//	
////			console.log("alternate => -1");
//			
//	//		context.strokeStyle = line_Color__Yellow;
////	    	context.strokeStyle = line_Color__Red;
//	    	context.strokeStyle = line_Color__Gray_180;
//	    	
//	    	context.stroke();
//	
//	    	// color : reset
//	    	context.strokeStyle = line_Color__Red;
//	
//	    	// update : alternate
//	    	alternate = alternate * (-1);
//	
//		}//if (alternate == 1)
//		
//	}//for (var i = 0; i < numOf_Grids; i++)
	
}//function _draw_Grid__Slanted__ToLeftDown(rect) {

function _draw_Grid__Slanted__ToRightDown__2_UpperRight
(rect, tick, numOf_Grids_X, numOf_Grids_Y) {

	/***************************
		vars
	 ***************************/
	var alternate = 1;
	
	/***************************
		main
	 ***************************/
	for (var i = 0; i <= numOf_Grids_X + 2; i++) {
//		for (var i = 0; i <= numOf_Grids_X + 1; i++) {
//		for (var i = 0; i < numOf_Grids_X + 1; i++) {
		
		/***************************
			line coordinates
		 ***************************/
		context.beginPath();
		
		var sX = rect.startX + tick * i;
		var sY = rect.startY;
		
		var eX = rect.startX + tick * (numOf_Grids_X);
//		var eX = rect.startX + tick * (numOf_Grids_X + 1);
//		var eX = rect.startX + tick * (numOf_Grids_X + i);
//		var eX = rect.startX + tick * (i);
//		var eY = rect.startY + tick * (numOf_Grids_X + 1 - i);
		var eY = rect.startY + tick * (numOf_Grids_X - i);
		
		context.moveTo(sX,	sY);
		context.lineTo(eX,	eY);	//
		
		/***************************
			draw grids
		 ***************************/
		// color
		if (alternate == 1) {
			
	//		console.log("alternate => 1 !!!!");
			
			context.strokeStyle = line_Color__Blue;
	//    	context.strokeStyle = line_Color__Yellow;
			
			context.stroke();
			
			// color : reset
			context.strokeStyle = line_Color__Red;
			
			// update : alternate
			alternate = alternate * (-1);
			
		} else {
			
	//		console.log("alternate => -1");
			
			//		context.strokeStyle = line_Color__Yellow;
	//    	context.strokeStyle = line_Color__Red;
			context.strokeStyle = line_Color__Gray_180;
			
			context.stroke();
			
			// color : reset
			context.strokeStyle = line_Color__Red;
			
			// update : alternate
			alternate = alternate * (-1);
			
		}//if (alternate == 1)
		
	}//for (var i = 0; i < numOf_Grids; i++)
	
}//function _draw_Grid__Slanted__ToRightDown__2_UpperRight

function _draw_Grid__Slanted__ToRightDown__1_Main
(rect, tick, numOf_Grids_X, numOf_Grids_Y) {
//	function _draw_Grid__Slanted__ToRightDown__1_Main(rect, tick) {
	
//	console.log("_draw_Grid__Slanted__ToRightDown__1_Main");

	/***************************
		vars
	 ***************************/
	var alternate = 1;
	
	/***************************
		main
	 ***************************/
	//for (var i = 1; i < numOf_Grids_Y; i++) {
	for (var i = 0; i < numOf_Grids_X + 1; i++) {
	//	for (var i = 0; i < numOf_Grids_X; i++) {
	//	for (var i = 0; i <= numOf_Grids_X; i++) {
		
		/***************************
			line coordinates
		 ***************************/
		context.beginPath();
		
		var sX = rect.startX;
		var sY = rect.startY + tick * i;
	//	var eX = rect.startX + tick * (numOf_Grids_X + 1);
		
		var eX = rect.startX + tick * (numOf_Grids_X);
		var eY = rect.startY + tick * (i + numOf_Grids_X);
	//	var eY = rect.startY + tick * (i + 3 * 2);
		
		context.moveTo(sX,	sY);
		context.lineTo(eX,	eY);	//
	//	context.moveTo(rect.startX,				rect.startY + tick * i);
	//	context.lineTo(rect.startX + tick * (numOf_Grids_X + 1),	rect.startY + tick * (i + 3 * 2));	//
	//	context.lineTo(rect.startX + tick * (numOf_Grids_X + 1),	rect.startY + tick * (i + 3));	//
	//	context.lineTo(rect.startX + tick * numOf_Grids_X,	rect.startY + tick * (i + 3));	//
	//	context.lineTo(rect.startX + tick * numOf_Grids_X,	rect.startY + tick * (i + 9));	//
	//	context.lineTo(rect.startX + rect.endX,	rect.startY + tick * (i + 9));	//
	//	context.lineTo(rect.startX + rect.endX,	rect.startY + tick * (i + 3));	//
		
		/***************************
			draw grids
		 ***************************/
		// color
		if (alternate == 1) {
			
	//		console.log("alternate => 1 !!!!");
			
			context.strokeStyle = line_Color__Gray_180;
	//    	context.strokeStyle = line_Color__Yellow;
			
			context.stroke();
			
			// color : reset
			context.strokeStyle = line_Color__Red;
			
			// update : alternate
			alternate = alternate * (-1);
			
		} else {
			
	//		console.log("alternate => -1");
			
			//		context.strokeStyle = line_Color__Yellow;
	//    	context.strokeStyle = line_Color__Red;
			context.strokeStyle = line_Color__Gray_180;
			
			context.stroke();
			
			// color : reset
			context.strokeStyle = line_Color__Red;
			
			// update : alternate
			alternate = alternate * (-1);
			
		}//if (alternate == 1)
		
	}//for (var i = 0; i < numOf_Grids; i++)
	
}//function _draw_Grid__Slanted__ToRightDown__1_Main(rect, tick) {

function _draw_Grid__Slanted__ToRightDown(rect, tick) {
	
//	console.log("_draw_Grid__Slanted__ToRightDown");
	
	
	var numOf_Grids_X = Math.floor(rect.endX / tick);
	var numOf_Grids_Y = Math.floor(rect.endY / tick);
	
//	console.log("numOf_Grids_X => " + numOf_Grids_X);
//	console.log("numOf_Grids_Y => " + numOf_Grids_Y);
	
	
	var alternate = 1;
	
	/***************************
		main
	 ***************************/
	_draw_Grid__Slanted__ToRightDown__1_Main(rect, tick, numOf_Grids_X, numOf_Grids_Y);

	/***************************
		upper right
	 ***************************/
	_draw_Grid__Slanted__ToRightDown__2_UpperRight(rect, tick, numOf_Grids_X, numOf_Grids_Y);
	
////	for (var i = 1; i < numOf_Grids_Y; i++) {
//	for (var i = 0; i < numOf_Grids_X + 1; i++) {
////		for (var i = 0; i < numOf_Grids_X; i++) {
////		for (var i = 0; i <= numOf_Grids_X; i++) {
//		
//		/***************************
//			line coordinates
//		 ***************************/
//		context.beginPath();
//		
//		var sX = rect.startX;
//		var sY = rect.startY + tick * i;
////		var eX = rect.startX + tick * (numOf_Grids_X + 1);
//		
//		var eX = rect.startX + tick * (numOf_Grids_X);
//		var eY = rect.startY + tick * (i + numOf_Grids_X);
////		var eY = rect.startY + tick * (i + 3 * 2);
//		
//		context.moveTo(sX,	sY);
//		context.lineTo(eX,	eY);	//
////		context.moveTo(rect.startX,				rect.startY + tick * i);
////		context.lineTo(rect.startX + tick * (numOf_Grids_X + 1),	rect.startY + tick * (i + 3 * 2));	//
////		context.lineTo(rect.startX + tick * (numOf_Grids_X + 1),	rect.startY + tick * (i + 3));	//
////		context.lineTo(rect.startX + tick * numOf_Grids_X,	rect.startY + tick * (i + 3));	//
////		context.lineTo(rect.startX + tick * numOf_Grids_X,	rect.startY + tick * (i + 9));	//
////		context.lineTo(rect.startX + rect.endX,	rect.startY + tick * (i + 9));	//
////		context.lineTo(rect.startX + rect.endX,	rect.startY + tick * (i + 3));	//
//		
//		/***************************
//			draw grids
//		 ***************************/
//		// color
//		if (alternate == 1) {
//			
////			console.log("alternate => 1 !!!!");
//			
//			context.strokeStyle = line_Color__Gray_180;
////	    	context.strokeStyle = line_Color__Yellow;
//			
//			context.stroke();
//			
//			// color : reset
//			context.strokeStyle = line_Color__Red;
//			
//			// update : alternate
//			alternate = alternate * (-1);
//			
//		} else {
//			
////			console.log("alternate => -1");
//			
//			//		context.strokeStyle = line_Color__Yellow;
////	    	context.strokeStyle = line_Color__Red;
//			context.strokeStyle = line_Color__Gray_180;
//			
//			context.stroke();
//			
//			// color : reset
//			context.strokeStyle = line_Color__Red;
//			
//			// update : alternate
//			alternate = alternate * (-1);
//			
//		}//if (alternate == 1)
//		
//	}//for (var i = 0; i < numOf_Grids; i++)
	
}//function _draw_Grid__Slanted__ToRightDown(rect, tick) {

function _draw_Grid__Slanted(rect) {

	/***************************
		tick
	 ***************************/
	var interval = $('input#ipt_Main_Grid_Interval').val();
	
	var tick = null;
	
	if (interval == '') {
		
		tick = 20;
		
	} else 	if (parseInt(interval) < 1) {

		tick = 20;

	} else {

		tick = parseInt(interval);

	}//if (parseInt(interval) < 1)

	/***************************
		draw
	 ***************************/
	_draw_Grid__Slanted__ToLeftDown(rect, tick);
	
	_draw_Grid__Slanted__ToRightDown(rect, tick);
	
	
}//function _draw_Grid__Slanted(rect) {



function draw_Zoomed(sx, sy, sw, sh, dx, dy, dw, dh) {

	/***************************
		canvas --> clear
	 ***************************/
	//ref https://stackoverflow.com/questions/2142535/how-to-clear-the-canvas-for-redrawing 'answered Jan 26 '10 at 20:52'
	context.clearRect(0, 0, canvas.width, canvas.height);
	
	console.log("ratio_Final => " + ratio_Final);
	
	console.log("1 / ratio_Final => " + (1 / ratio_Final));
	
	/***************************
		draw
	 ***************************/
	var ratio_Reverse = 1 / ratio_Final;
	
	console.log("sx = " + sx
			+ " / "
			+ "sy = " + sy
	);
	console.log("sw = " + sw
		+ " / "
		+ "sh = " + sh
	);
	
	
	context.drawImage(imageObj, 
//				sx, sy, 
				Math.floor(sx * ratio_Reverse), Math.floor(sy * ratio_Reverse), 
//				sw * 10, sh * 10, 
				Math.floor(sw * (1 / ratio_Final)), Math.floor(sh * (1 / ratio_Final)), 
				dx, dy, dw, dh);
//	context.drawImage(imageObj, sx, sy, sw, sh, dx, dy, dw, dh);
//	context.drawImage(imageObj, 0, 0, imageFile_WH_Resized[0], imageFile_WH_Resized[1]);
	
	/***************************
		rect ---> clear all
	 ***************************/
	reacts = [];
	
	console.log("reacts --> cleared");
	
}

function draw() {
	
//	context.drawImage(imageObj, 0, 0, imageFile_WH_Resized[0], imageFile_WH_Resized[1]);	//=> w.

	context.drawImage(imageObj, sx, sy, sw, sh, dx, dy, dw, dh);
	
	console.log("drawImage() ---> using 9 params");
	
    context.lineWidth = context_Line_Width;

    //ref http://www.html5.jp/canvas/how3.html
    context.strokeStyle = line_Color__Red;
    
    reacts.forEach(
    		function(rect) {
    	
            	context.strokeRect(rect.startX, rect.startY, rect.endX, rect.endY);

            	/***************************
					grid
				 ***************************/
            	if (flag_Draw_Grid == 1) {

            		_draw_Grid(rect, numOf_Grid_Lines);

				}//if (flag_Draw_Grid == 1) {
            	
            	/***************************
					grid : slanted
				 ***************************/
            	if (flag_Draw_Grid__Slanted == 1) {

            		console.log("flag_Draw_Grid__Slanted => 1");
					
            		
            		_draw_Grid__Slanted(rect, numOf_Grid_Lines);

				}//if (flag_Draw_Grid == 1) {
				
            	
            	
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

function toggle_Grid() {
	
	if (flag_Draw_Grid == 1) {

//		console.log("flag_Draw_Grid => changing to 0");
		
		flag_Draw_Grid = 0;
		
		$('button#btn_Main_Toggle_Grid').css("background-color", "DarkOrange");
		
	} else {

//		console.log("flag_Draw_Grid => changing to 1");
		
		flag_Draw_Grid = 1;
		
		$('button#btn_Main_Toggle_Grid').css("background-color", "MediumSlateBlue");
		
	}//if (flag_Draw_Grid == 1)
	
	draw();

}//function toggle_Grid() {

function toggle_Grid_Slanted() {
	
	if (flag_Draw_Grid__Slanted == 1) {
		
		console.log("flag_Draw_Grid__Slanted => changing to 0");
		
		flag_Draw_Grid__Slanted = 0;
		
		$('button#btn_Main_Toggle_Grid_Slanted').css("background-color", "DarkOrange");
		
	} else {
		
		console.log("flag_Draw_Grid__Slanted => changing to 1");
		
		flag_Draw_Grid__Slanted = 1;
		
		$('button#btn_Main_Toggle_Grid_Slanted').css("background-color", "MediumSlateBlue");
		
	}//if (flag_Draw_Grid == 1)
	
	draw();
	
}//function toggle_Grid_Slanted() {

function _setup_Font_Size() {
	
	/***************************
		input : font size
	 ***************************/
	var input_Font_Size = $('input#ipt_Main_Font_Size').val();
	
	/***************************
		host
	 ***************************/
	var hostname = window.location.hostname;
	
	var url = "";
	
	var font_Size = '';
	
	if (hostname == "localhost") {
		
		font_Size = '25px';
		
	} else {//if (hostname == "localhost") {
		
		font_Size = '40px';
		
	}//if (hostname == "localhost") {
	
	/***************************
		set : ipt_Image_File_URL
	 ***************************/
	$('input#ipt_Image_File_URL').css("font-size", font_Size);
	
	console.log("font_Size => " + font_Size);
	
	
	
	
}//_setup_Font_Size()

function _window_OnLoad__Setup() {

//	/***************************
//		var : drawimage()
//	 ***************************/
//	sx = 0; sy = 0;
//	
//	dx = 0; dy = 0;
	
		canvas = document.getElementById('drowing');
//	var canvas = document.getElementById('drowing');
	context = canvas.getContext('2d');
//	var context = canvas.getContext('2d');
	reacts = [];
//	var reacts = [];
	
	imageFile_WH_Resized = null;
//	var imageFile_WH_Resized = null;
		
	imageObj = new Image();
//	var imageObj = new Image();
	
//	var canvas_Height_Ratio = 0.8;
	
	imageObj.onload = function() {
		
//			canvas.width = window.innerWidth / 2;
		canvas.width = window.innerWidth;
//		canvas.width = window.innerWidth;;
//		canvas.width = imageObj.width;
		canvas.height = window.innerHeight * canvas_Height_Ratio;
//	 canvas.height = window.innerHeight / 2;
//		canvas.height = imageObj.height / 2;
//		canvas.height = imageObj.height;

		size_Canvas = [canvas.width, canvas.height];
//	 var size_Canvas = [canvas.width, canvas.height];
	 
			 //test
	//		 alert("imageObj.height => " + imageObj.height);	//=> 3264
			 
		imageFile_WH_Resized = get_ImageObj_WH_Resized(canvas, imageObj);
	 
//		 sw = imageFile_WH_Resized[0];
//		 
//		 sh = imageFile_WH_Resized[1];

		 /***************************
			init : drawImage coordinates
		***************************/
		sx = 0; sy = 0;
		
		sw = imageObj.width; sh = imageObj.height;
		
		dx = 0; dy = 0;

		dw = imageFile_WH_Resized[0];
		 
		dh = imageFile_WH_Resized[1];

		draw();
			
	};
	
	/***************************
		set : image url
	 ***************************/
	var url = $('input#ipt_Image_File_URL').val();
	
	if (url == null || url == '') {


	} else {//if (url == null || url == '') {

		dflt_Image_URL = url;
	
	}//if (url == null || url == '') {
	


	
	imageObj.src = dflt_Image_URL;
//	imageObj.src = 'http://benfranklin.chips.jp/cake_apps/images/ifm11/2014-08-12_12-17-13_686.jpg';

//	console.log("imageObj.src => " + imageObj.src);
	
	
	/***************************
		rectangle
	***************************/
	_rectangle = createRect();
	
	/***************************
		setup : font size
	 ***************************/
	_setup_Font_Size();
	
}//function _window_OnLoad__Setup() {


function _setup_Grid(e) {

    if (flag_Canvas_Click_Start == 1) {

//		alert("first click");
		console.log("first click");

	    // set values
	    $('input#ipt_Main_Range_Start_X').val(e.clientX);
	    
	    $('input#ipt_Main_Range_Start_Y').val(e.clientY);
	    
//	    console.log("value set !! => Start X : " + e.clientX);

		// update
		flag_Canvas_Click_Start = flag_Canvas_Click_Start * (-1);
		
		// input boxes ---> clear
	    $('input#ipt_Main_Range_End_X').val("");
	    
	    $('input#ipt_Main_Range_End_Y').val("");
		
		
	} else {

//		alert("second click");
		console.log("SECOND click");

	    // set values
	    $('input#ipt_Main_Range_End_X').val(e.clientX);
	    
	    $('input#ipt_Main_Range_End_Y').val(e.clientY);
	    
//	    console.log("value set => End X : " + e.clientX);

		// update
		flag_Canvas_Click_Start = flag_Canvas_Click_Start * (-1);

		/***************************
			add : rectangle
		 ***************************/
		var _rectangle_Tmp = createRect();
		
		// set values
		//ref https://www.w3schools.com/jsref/jsref_parseint.asp
		_rectangle_Tmp.startX = parseInt($('input#ipt_Main_Range_Start_X').val());
		_rectangle_Tmp.startY = parseInt($('input#ipt_Main_Range_Start_Y').val());
		
		_rectangle_Tmp.endX = parseInt($('input#ipt_Main_Range_End_X').val()) - _rectangle_Tmp.startX;
		_rectangle_Tmp.endY = parseInt($('input#ipt_Main_Range_End_Y').val()) - _rectangle_Tmp.startY;

		// push
		reacts.push(_rectangle_Tmp);
		
		draw();

		/***************************
			button 'toggle' : able
		 ***************************/
		$('button#btn_Main_Toggle_Grid').prop("disabled", false);
		
		$('button#btn_Main_Toggle_Grid').css("background-color", "MediumSlateBlue");
		
		/***************************
			button 'toggle' slanted : able
		 ***************************/
		$('button#btn_Main_Toggle_Grid_Slanted').prop("disabled", false);
		
		$('button#btn_Main_Toggle_Grid_Slanted').css("background-color", "MediumSlateBlue");
		
	}//if (flag_Canvas_Click_Start == 1)

}//function _setup_Grid() {

function _draw_Circle(e) {
	
	var x = e.clientX;
	
	var y = e.clientY;
	
	console.log("x => " + x + " / " + "y => " + y);
	
	/***************************
		radius,
	 ***************************/
	var radius = $('input#ipt_Main_Circle_Radius').val();
	
	var tick = null;
	
	if (radius == '') {
		
		radius = 30;
		
	} else 	if (parseInt(radius) < 1) {

		radius = 30;

	} else {

		radius = parseInt(radius);

	}//if (parseInt(interval) < 1)


	/***************************
		draw circle
	 ***************************/
	//ref https://www.w3schools.com/tags/canvas_arc.asp
	context.beginPath();

	context.lineWidth = 4;
//	context.lineWidth = context_Line_Width;
	
//	var r = 30;
	
	context.arc(x, y, radius, 0, 2*Math.PI);
//	context.arc(x, y, r, 0, 2*Math.PI);
//	context.arc(x, y, 50, 0, 2*Math.PI);
//	context.arc(50, x, y, 0, 2*Math.PI);
//	context.arc(100,75,50,0,2*Math.PI);
	
	context.stroke();
	
	console.log("circle ==> drawn");
	
	
}//_draw_Circle()

function onMouseDown (e) {
	
	/***************************
		dispatch
	 ***************************/
	if (flag_Draw_Circle == 1) {

//		console.log("drawing circle...");
		
		_draw_Circle(e);
		
		return;

	}//if (flag_Draw_Circle == 1) {
	


	
    _rectangle.startY = e.clientY;
    _rectangle.startX = e.clientX;
//    canvas.addEventListener ("mousemove", onMouseMove, false);
    
    //test
//    console.log("selection => started !! (global function)");
    
    /***************************
		grid
	 ***************************/
    _setup_Grid(e);
    
};


function window_OnLoad() {

	_window_OnLoad__Setup();
	
    canvas.addEventListener("mousedown", onMouseDown, false);
//    canvas.addEventListener("mouseup" , onMouseUp , false);
    window.addEventListener("keyup" , onKeyUp , false);
    
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
