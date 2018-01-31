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

function im_Action(_param) {
	
	alert("!!param is => '" + _param + "'");
	
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
	
	var _data = {action : _param};
		
	$.ajax({
		
	    url: _url,
	    type: "GET",
	    //REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
	    data: _data,
	    
	    timeout: 10000
	    
	}).done(function(data, status, xhr) {
		
		alert(data);
		
		$('div#index_Area__Result').html(data);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
	});

}//function im_Action(param) {

function mm_Index_LinkTo(_param) {
	
//	alert("!!param is => '" + _param + "'");
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting...";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
//	$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
//	elem.css("background", "yellow");
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/mm/numbering/";
//	var _url = "http://127.0.0.1:8000/im/im_actions";
//	var _url = "http://127.0.0.1:8000/im/actions";
	
//	var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
//		data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		alert(data);
		
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
	
	alert("file fullpath => '" + _dpath + "\\" + _fname + "'");
	
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