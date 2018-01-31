//alert("main.js");


/***************************
	constants
 ***************************/
var color_Dflt_index_Display_Area = "white";


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
	
	elem.css("background", "yellow");
	
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
				.css("background", color_Dflt_index_Display_Area);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
	});
	
}//function mm_Index_LinkTo(_param) {

function exec_Numbering(_param) {
	
	alert("_param => '" + _param + "'");
	
	/***************************
		get : dpath
	 ***************************/
	var elem = $('input#ipt_Numbering_MainDir');
	
	var dpath = elem.val();
	
	alert("dpath => " + dpath + "'");
	
}//exec_Numbering
