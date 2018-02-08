//alert("main.js");


/******************************************************
	constants
 ******************************************************/

var cname_White = "white";
var cname_Red = "red";
var cname_Yellow = "yellow";

var className_BT_Numbering_List = "bt_Numbering_List";


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
	
	if (_param == "11-0") {

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
	
	if (_param == "11-0") {

		_data = {action : _param, update : _update};

	} else {

		_data = {action : _param};

	}//if (_param == "11-0")
	
	
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
		
//		alert(data);
		
		$('div#index_Area__Result').html(data);
		
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


