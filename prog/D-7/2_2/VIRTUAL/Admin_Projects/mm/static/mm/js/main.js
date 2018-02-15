//alert("main.js");


/******************************************************
	constants
 ******************************************************/

var cname_White = "white";
var cname_Red = "red";
var cname_Yellow = "yellow";
var cname_LightBlue = "LightBlue";

var className_BT_Numbering_List = "bt_Numbering_List";

var TIME_FADE_IN = 300;
var TIME_FADE_OUT = 300;

/******************************************************
	funcs : ready
 ******************************************************/
$(document).ready(function() {
	
	//debug
	var datetime = get_Timelabel_Now();
//	var currentdate = new Date();
//	var datetime = "Last Sync: " + currentdate.getDay() + "/"+currentdate.getMonth() 
//		+ "/" + currentdate.getFullYear() + " @ " 
//		+ currentdate.getHours() + ":" 
//		+ currentdate.getMinutes() + ":" + currentdate.getSeconds();
		
	console.log("ready!" + " " + datetime);
//	console.log("ready!");
	
//    $("button").click(function(event) {
//    	
//    	//ref http://www.mysamplecode.com/2012/05/jquery-get-button-value-clicked.html
////        alert(event.target.id);
//    	var class_Name = $(this).attr('class');
////    	var tmp = $(this).attr('class');
////    	var tmp = $(this).attr('id');
////    	var tmp = $(this).prop("value");
//
////    	alert("tmp => " + tmp);
//        
//    	if (class_Name == className_BT_Numbering_List) {
//
//		} else {
//
//			console.log("Unknown class name : '" + class_Name + "'");
//
//		}//if (class_Name == )
//		
//    	
//    });
});

/******************************************************
funcs : general
******************************************************/
function show_Message(msg) {
	
	alert(msg);
	
}//function show_Message(msg) {

/*
 * https://stackoverflow.com/questions/5999209/how-to-get-the-background-color-code-of-an-element
 * answered May 14 '11 at 2:37
 */
function hexc(colorval) {
    var parts = colorval.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    delete(parts[0]);
    for (var i = 1; i <= 3; ++i) {
        parts[i] = parseInt(parts[i]).toString(16);
        if (parts[i].length == 1) parts[i] = '0' + parts[i];
    }
    color = '#' + parts.join('');
    
    return color;
}

function im_Action(_param) {
	
	/***************************
		validate : update date
	 ***************************/
	var _update;
	
	if ((_param == "11-0") ||
		(_param == "10-1")) {
//		if (_param == "11-0") {

		var tag_Date = $("input#ipt_IM_Update_Date");
		
		_update = tag_Date.val();
//		var update = tag_Date.val();
		
		if (_update == "") {

			alert("update ==> blank");

			return;
			
		} else if (_update == null) {

			alert("update ==> null");

			return;
			
		} else {
			
//			alert("_update ==> '" + _update + "'");
			
		}//if (update == "")

	}//if (_param == "11-0")
		
//	} else {//if (_param == "11-0")
//		
//		alert("_param ==> '" + _param + "'");
//		
//	}//if (_param == "11-0")
	
	
	/***************************
		operations
	 ***************************/
//	alert("!!param is => '" + _param + "'");
	
	//debug
	var td = $("td#td_Label_" + _param);
//	var tmp = $("td#td_Label_" + _param).text();
//	var tmp = $("td#td_Label_" + _param).html();
//	alert("td !! => '" + tmp + "'");
	
	//test
	var x = td.css('backgroundColor');
//	var x = $(this).css('backgroundColor');
	
	var hex = hexc(x);
	
//	alert("bg-color => '" + x + "'"
//			+ " / "
//			+ "hex => '" + hex + "'"
//	
//	);
	
	/***************************
		set : color
	 ***************************/
	var color_New = "";
	
	if (hex == "#ffffff") {

		color_New = "#ffff00";

	} else {

		color_New = "#ffffff";

	}//if (hex == "#ffffff")
	
	
	td.css("background", color_New);
//	td.css("background", cname_Yellow);
	
	/***************************
		return : if set to white
	 ***************************/
	if (color_New == "#ffffff") {
		
		return;
		
	}
	
	/*
	 * test
	 */
	$('div#index_Message_Area').html(_param);
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/im/im_actions";
//	var _url = "http://127.0.0.1:8000/im/actions";
	
	/***************************
		param
	 ***************************/
	var _data;
	
	//ref multiple conditions https://stackoverflow.com/questions/8710442/how-to-specify-multiple-conditions-in-an-if-statement-in-javascript answered Jan 3 '12 at 9:58
	if ((_param == "11-0") || 
			(_param == "10-1")) {
//		if (_param == "11-0") {

		_data = {action : _param, update : _update};

	} else {

		_data = {action : _param};

	}//if (_param == "11-0")
	
//	//debug
//	alert("data => '" + _data + "'");
	
//		_data = {action : _param};
		
	$.ajax({
		
	    url: _url,
	    type: "GET",
	    //REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
	    data: _data,
	    
	    timeout: 10000
	    
	}).done(function(data, status, xhr) {

		/***************************
			exception
		 ***************************/
		var substr = "total_data";
//		var substr = "doesn't";
		
//		alert(data);
		
	//	var res = (data.indexOf(substr) !== -1);
		
		//ref substring https://stackoverflow.com/questions/1789945/how-to-check-whether-a-string-contains-a-substring-in-javascript
//		if (data.indexOf(substr) == -1) {
		if (data.includes(substr)) {	// detected
//			if (data.indexOf(substr) !== -1) {	// detected
			
			//debug
			console.log("'doesn't' ==> detected");
			
//			alert(data);
			
			var tag = $('div#index_Area__Result');
			
			$('div#index_Area__Result')
				.css("background", cname_Red);

//			tag
//			.animate({background : "red"}, 500)
//			.animate({background : "yellow"}, 500)
//			.animate({background : "white"}, 500)
			
			;

			$('div#index_Area__Result').html(data);
			
//			//ref
//			tag
//				.animate({background : "red"}, 500)
//				.animate({background : "yellow"}, 500)
//				.animate({background : "white"}, 500)
//				
//				;
			
			//ref fadein/out https://stackoverflow.com/questions/275931/how-do-you-make-an-element-flash-in-jquery answered Feb 1 '12 at 14:19
			tag
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				
				.fadeIn(200);
			
		} else {
			
			var tag = $('div#index_Area__Result');
			
			$('div#index_Area__Result')
				.css("background", cname_LightBlue);
//			.css("background", cname_White);

			$('div#index_Area__Result').html(data);

			tag
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				
//				.fadeIn(200).fadeOut(200)
//				.fadeIn(200).fadeOut(200)
//				
//				.fadeIn(200).fadeOut(200)
//				.fadeIn(200).fadeOut(200)
				
				.fadeIn(200);

		}

		
//		$('div#index_Area__Result').html(data);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
	});

}//function im_Action(param) {

function _mm_Index_LinkTo__0() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting...";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/mm/numbering/";
	//var _url = "http://127.0.0.1:8000/im/im_actions";
	//var _url = "http://127.0.0.1:8000/im/actions";
	
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
	//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
	//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
				.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
			.css("background", cname_Red);
	});
	
}//function _mm_Index_LinkTo__0() {

function _mm_Index_LinkTo__1() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting... param is '1'";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/mm/denumbering/";
//	var _url = "http://127.0.0.1:8000/mm/numbering/";
	//var _url = "http://127.0.0.1:8000/im/im_actions";
	//var _url = "http://127.0.0.1:8000/im/actions";
	
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
		//    data: {id: id},
		//    data: {memos: memos, image_id: image_id},
		//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
		//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
		.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
		.css("background", cname_Red);
	});
	
}//function _mm_Index_LinkTo__1() {

function _mm_Index_LinkTo__2() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting... param is '1'";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/mm/build_history/";
//	var _url = "http://127.0.0.1:8000/mm/denumbering/";
	
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
		//    data: {id: id},
		//    data: {memos: memos, image_id: image_id},
		//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
		//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
		.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
		.css("background", cname_Red);
	});
	
}//_mm_Index_LinkTo__2()

function mm_Index_LinkTo(_param) {
	
//	alert("!!param is => '" + _param + "'");
	/***************************
		dispatch
	 ***************************/
	//ref https://www.w3schools.com/jsref/jsref_parseInt.asp
	var index = parseInt(_param);
	
	if (index == 0) {	//[0, "Numbering"]
		
		_mm_Index_LinkTo__0();
		
	}
	
	else if (index == 1) {	//[1, "De-numbering"]
		
		_mm_Index_LinkTo__1();
		
	} else if (index == 2) {	//[2, "Build history"]
			
		_mm_Index_LinkTo__2();
			
	} else {
		
		alert("unknown index => " + _param);
		
	}
	
	
//	/***************************
//		message
//	 ***************************/
//	var msg = "ajax starting...";
//	
//	var elem = $('div#index_Display_Area');
//	
//	elem.html(msg);
////	$('div#index_Display_Area').html(msg);
//	
//	elem.css("background", cname_Yellow);
////	elem.css("background", "yellow");
//	
//	/***************************
//		ajax
//		
//		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
//	 ***************************/
//	var _url = "http://127.0.0.1:8000/mm/numbering/";
////	var _url = "http://127.0.0.1:8000/im/im_actions";
////	var _url = "http://127.0.0.1:8000/im/actions";
//	
////	var _data = {action : _param};
//	
//	$.ajax({
//		
//		url: _url,
//		type: "GET",
//		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
////	    data: {id: id},
////	    data: {memos: memos, image_id: image_id},
////		data: _data,
//		
//		timeout: 10000
//		
//	}).done(function(data, status, xhr) {
//		
////		alert(data);
//		
//		$('div#index_Display_Area').html(data);
//		
//		$('div#index_Display_Area')
//				.css("background", cname_White);
//		
//	}).fail(function(xhr, status, error) {
//		
//		alert(xhr.status);
//		
//		var msg = "ajax returned error";
//		
//		$('div#index_Display_Area').html(msg);
//		
//		$('div#index_Display_Area')
//			.css("background", cname_Red);
//	});
	
}//function mm_Index_LinkTo(_param) {

function exec_Numbering(_param) {
	
//	alert("_param => '" + _param + "'");
	
	/***************************
		get : vars
	 ***************************/
	/***************************
		dpath
	 ***************************/
	var elem = $('input#ipt_Numbering_MainDir');
	
	//ref val https://stackoverflow.com/questions/4088467/get-the-value-in-an-input-text-box answered Apr 9 '13 at 13:28
	var _dpath = elem.val();
	
//	alert("dpath => " + dpath + "'");
	
	/***************************
		fname
	 ***************************/
	var _fname = _param;
	
//	alert("file fullpath => '" + _dpath + "\\" + _fname + "'");
	
	/***************************
		data
	 ***************************/
//	var _data = {action : _param};
	var _data = {dpath : _dpath, fname : _fname};
	
	var _url = "http://127.0.0.1:8000/mm/exec_Numbering/";

	/***************************
		background
	 ***************************/
	var elem = $('div#numbering_content_Message_Area');
	
	elem.css("background", cname_Yellow);
//	elem.css("background", "yellow");
	
	/***************************
		ajaxing
	 ***************************/
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
		data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		alert(data);
		
		$('div#numbering_content_Message_Area').html(data);
		
		$('div#numbering_content_Message_Area')
				.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);

		$('div#numbering_content_Message_Area')
				.css("background", cname_Red);

	});

}//exec_Numbering

function exec_BuildHistory(_param) {
	
//	alert("_param => '" + _param + "'");
	
	/***************************
		get : vars
	 ***************************/
	/***************************
		dpath
	 ***************************/
	var elem = $('input#ipt_Numbering_MainDir');
	
	//ref val https://stackoverflow.com/questions/4088467/get-the-value-in-an-input-text-box answered Apr 9 '13 at 13:28
	var _dpath = elem.val();
	
//	alert("dpath => " + dpath + "'");
	
	/***************************
		fname
	 ***************************/
	var _fname = _param;
	
//	alert("file fullpath => '" + _dpath + "\\" + _fname + "'");
//	
//	return;
	
	/***************************
		data
	 ***************************/
//	var _data = {action : _param};
	var _data = {dpath : _dpath, fname : _fname};
	
	var _url = "http://127.0.0.1:8000/mm/exec_BuildHistory/";
	
	/***************************
		background
	 ***************************/
	var elem = $('div#numbering_content_Message_Area');
	
	elem.css("background", cname_Yellow);
//	elem.css("background", "yellow");
	
	/***************************
		ajaxing
	 ***************************/
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
		data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		alert(data);
		
		$('div#numbering_content_Message_Area').html(data);
		
		$('div#numbering_content_Message_Area')
		.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#numbering_content_Message_Area')
		.css("background", cname_Red);
		
	});
	
}//exec_BuildHistory

function exec_DeNumbering(_param) {
	
	
	/***************************
		get : vars
	 ***************************/
	/***************************
		dpath
	 ***************************/
	var elem = $('input#ipt_DeNumbering_MainDir');
//	var elem = $('input#ipt_Numbering_MainDir');
	
	//ref val https://stackoverflow.com/questions/4088467/get-the-value-in-an-input-text-box answered Apr 9 '13 at 13:28
	var _dpath = elem.val();
	
//	alert("dpath => " + dpath + "'");
	
	/***************************
		fname
	 ***************************/
	var _fname = _param;
	
//	alert("file fullpath => '" + _dpath + "\\" + _fname + "'");
	
//	//debug
//	return;
	
	/***************************
		data
	 ***************************/
//	var _data = {action : _param};
	var _data = {dpath : _dpath, fname : _fname};
	
	var _url = "http://127.0.0.1:8000/mm/exec_DeNumbering/";
//	var _url = "http://127.0.0.1:8000/mm/exec_Numbering/";
	
	/***************************
		background
	 ***************************/
	var elem = $('div#numbering_content_Message_Area');
	
	elem.css("background", cname_Yellow);
//	elem.css("background", "yellow");
	
	/***************************
		ajaxing
	 ***************************/
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
		data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		alert(data);
		
		$('div#numbering_content_Message_Area').html(data);
		
		/***************************
			exception
		 ***************************/
		var substr = "EXCEPTION";
		
//		var res = (data.indexOf(substr) !== -1);
		
		if (data.indexOf(substr) !== -1) {
			
			alert("EXCEPTION");
			
			$('div#numbering_content_Message_Area')
				.css("background", cname_Red);
			
		} else {
			
			$('div#numbering_content_Message_Area')
				.css("background", cname_White);
		}
		
		
//		$('div#numbering_content_Message_Area')
//			.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#numbering_content_Message_Area')
		.css("background", cname_Red);
		
	});
	
}//exec_Numbering

function get_Timelabel_Now() {
	
	//ref https://stackoverflow.com/questions/10211145/getting-current-date-and-time-in-javascript
	//ref https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date
	var currentdate = new Date();
	var datetime = "Last Sync: " + currentdate.getDate() + "/"+currentdate.getMonth() + 1 
//	var datetime = "Last Sync: " + currentdate.getDay() + "/"+currentdate.getMonth() 
		+ "/" + currentdate.getFullYear() + " @ " 
		+ currentdate.getHours() + ":" 
		+ currentdate.getMinutes() + ":" + currentdate.getSeconds();

	return datetime;
	
}

function mm_Index_GO() {
	
	/***************************
		get selected
	 ***************************/
	//ref selection https://learn.jquery.com/using-jquery-core/faq/how-do-i-get-the-text-value-of-a-selected-option/
	//ref get value, not text https://stackoverflow.com/questions/13089944/jquery-get-selected-option-value-not-the-text-but-the-attribute-value Selvakumar Arumugam
	var selection = $( "#select_MM_Actions option:selected" );
//	var selection = $( "#select_MM_Actions option:selected" ).text();
	
	var text = selection.text();
	
	var value = selection.val();
	
//	alert("text => '" + text + "'" + " / " + "val = " + value);

	/***************************
		dispatch
	 ***************************/
	mm_Index_LinkTo(value);
	
}//mm_Index_GO()

/***************************
	<option value="0" class="opt_MM_Actions">Updown patterns</option>
 ***************************/
function _curr_Index_LinkTo__0() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting...";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		clear : message
	 ***************************/
	//ref clear div https://stackoverflow.com/questions/1701973/how-to-clear-all-divs-contents-inside-a-parent-div answered Nov 9 '09 at 16:05
	$('div#index_Message_Area').html('');
	
	$('div#index_Area__Result').html('');
	
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/curr/updown_patterns/";
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
	//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
	//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
				.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
			.css("background", cname_Red);
	});
	
}//function _curr_Index_LinkTo__0() {

function _curr_Index_LinkTo__1() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting...";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		clear : message
	 ***************************/
	$('div#index_Message_Area').html('');
	
	$('div#index_Area__Result').html('');

	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/curr/correlations/";
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
	//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
	//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
				.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
			.css("background", cname_Red);
	});
	
}//function _curr_Index_LinkTo__1() {

function _curr_Index_LinkTo__2() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting... param is '1'";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		clear : message
	 ***************************/
	$('div#index_Message_Area').html('');
	
	$('div#index_Area__Result').html('');

	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/mm/build_history/";
//	var _url = "http://127.0.0.1:8000/mm/denumbering/";
	
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
		//    data: {id: id},
		//    data: {memos: memos, image_id: image_id},
		//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
		//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
		.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
		.css("background", cname_Red);
	});
	
}//_curr_Index_LinkTo__2()

function curr_Index_LinkTo(_param) {
	
//	alert("!!param is => '" + _param + "'");
	/***************************
		dispatch
	 ***************************/
	//ref https://www.w3schools.com/jsref/jsref_parseInt.asp
	var index = parseInt(_param);
	
	if (index == 0) {	//[0, "Numbering"]
		
		_curr_Index_LinkTo__0();
		
	}
	
	else if (index == 1) {	//[1, "De-numbering"]
		
		_curr_Index_LinkTo__1();
		
	} else if (index == 2) {	//[2, "Build history"]
			
		_curr_Index_LinkTo__2();
			
	} else {
		
		alert("unknown index => " + _param);
		
	}
	
	
//	/***************************
//		message
//	 ***************************/
//	var msg = "ajax starting...";
//	
//	var elem = $('div#index_Display_Area');
//	
//	elem.html(msg);
////	$('div#index_Display_Area').html(msg);
//	
//	elem.css("background", cname_Yellow);
////	elem.css("background", "yellow");
//	
//	/***************************
//		ajax
//		
//		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
//	 ***************************/
//	var _url = "http://127.0.0.1:8000/mm/numbering/";
////	var _url = "http://127.0.0.1:8000/im/im_actions";
////	var _url = "http://127.0.0.1:8000/im/actions";
//	
////	var _data = {action : _param};
//	
//	$.ajax({
//		
//		url: _url,
//		type: "GET",
//		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
////	    data: {id: id},
////	    data: {memos: memos, image_id: image_id},
////		data: _data,
//		
//		timeout: 10000
//		
//	}).done(function(data, status, xhr) {
//		
////		alert(data);
//		
//		$('div#index_Display_Area').html(data);
//		
//		$('div#index_Display_Area')
//				.css("background", cname_White);
//		
//	}).fail(function(xhr, status, error) {
//		
//		alert(xhr.status);
//		
//		var msg = "ajax returned error";
//		
//		$('div#index_Display_Area').html(msg);
//		
//		$('div#index_Display_Area')
//			.css("background", cname_Red);
//	});
	
}//function mm_Index_LinkTo(_param) {

function curr_Index_GO() {
	
//	alert("curr index");
	
	var selection = $( "#select_Curr_Actions option:selected" );
//	var selection = $( "#select_MM_Actions option:selected" ).text();
	
	var text = selection.text();
	
	var value = selection.val();

//	//debug
//	alert("text => '" + text + "'" + " / " + "val = " + value);
	
	/***************************
		clear : areas
	 ***************************/
	var area_Display = $('div#index_Display_Area');
	
//	alert(area_Display);
	
//	area_Display.html() = "";
	area_Display.html('');

	// index_Message_Area
	$('div#index_Message_Area').html('');
	
	$('div#index_Area__Result').html('');
	
	
	
	/***************************
		dispatch
	 ***************************/
	curr_Index_LinkTo(value);

}

function curr_Updown_GO() {

//	alert("updown GO");

	/***************************
		message
	 ***************************/
	var msg = "ajax starting...";
	
	var elem = $('div#index_Message_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		param : body volume : up
	 ***************************/
	var tag_Vol_Up = $('input#ipt_Curr_UpdownPatterns_Range_Up');
	
	var val_Vol_Up = tag_Vol_Up.val();
	
	/***************************
		build : data
	 ***************************/
	var _data = {body_volume_up : val_Vol_Up};
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/curr/exec_updown_patterns/";
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
		data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		var tag = $('div#index_Area__Result');
//		
//		tag.html(data);
//		
//		tag
//				.css("background", cname_White);
		
		/***************************
			exception
		 ***************************/
		var substr = "ERROR";
		
		//ref substring https://stackoverflow.com/questions/1789945/how-to-check-whether-a-string-contains-a-substring-in-javascript
		if (data.includes(substr)) {	// detected
			
			//debug
			console.log("'" + substr + "'" + " ==> detected");
			
			var tag = $('div#index_Area__Result');
			
			$('div#index_Area__Result')
				.css("background", cname_Red);

			$('div#index_Area__Result')
				.css("color", cname_White);
			
			$('div#index_Area__Result').html(data);
			
			//ref fadein/out https://stackoverflow.com/questions/275931/how-do-you-make-an-element-flash-in-jquery answered Feb 1 '12 at 14:19
			tag
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
//				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
//				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				
				.fadeIn(TIME_FADE_IN);
			
		} else {
			
			var tag = $('div#index_Area__Result');
			
			$('div#index_Area__Result')
				.css("background", cname_LightBlue);
	
			$('div#index_Area__Result').html(data);
	
			tag
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
//				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
//				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				
//				.fadeIn(TIME_FADE_IN200).fadeOut(200)
//				.fadeIn(200).fadeOut(200)
//				
//				.fadeIn(200).fadeOut(200)
//				.fadeIn(200).fadeOut(200)
				
				.fadeIn(TIME_FADE_IN);
	
		}
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";

		var tag = $('div#index_Area__Result');

		tag.html(msg);
		
		tag.css("background", cname_Red);
	});
}

function curr_Correl_GO() {

	/***************************
		message
	 ***************************/
	var msg = "ajax starting... (curr_Correl_GO)";
	
	var elem = $('div#index_Message_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/curr/exec_correlations/";
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
	//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
	//	alert(data);
		
		var tag = $('div#index_Area__Result');
		
		tag.html(data);
		
		tag
				.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status + " / " + error);
//		alert(xhr.status);
		
		var msg = "ajax returned error";
	
		var tag = $('div#index_Area__Result');
	
		tag.html(msg);
		
		tag.css("background", cname_Red);
	});

}