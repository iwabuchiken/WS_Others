function show_message() {
	
	
	alert("message");
	
	var div = $("div#div_main");
	
//	alert(div.html());
//	alert(div);
	
//	$("div#div_main").html("<b>yes</b>");
//	$("div#table_main").html("<b>yes</b>");
//	$("table#table_main").html("<b>yes</b>");

	var url = "http://localhost/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/_main_table.php";
	
	//ref C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	$.ajax({
		
	    url: url,
	    type: "GET",
	    //REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
	    
	    timeout: 10000
	    
	}).done(function(data, status, xhr) {
		
		alert(data);
		
		$("div#div_main").html(data);
		
	//	alert(conv_Float_to_TimeLabel(data.point));
	//	addPosition_ToList(data.point);
		
	//	_delete_position_Ajax__Done(data, status, xhr);
//		_add_KW__Genre_Changed__Done(data, status, xhr);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
	});

	
}

function update_table() {
	
	var hostname = window.location.hostname;
	
//	alert(hostname);
	
	var url;
	
	if (hostname == "benfranklin.chips.jp") {
		
		url = "/WS/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/_main_table.php";
//		url = "WS/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/_main_table.php";
//		url = "/cake_apps/Cake_NR5/keywords/add_KW__Genre_Changed";
		
	} else {
	
		url = "/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/_main_table.php";
//		url = "/Eclipse_Luna/Cake_NR5/keywords/add_KW__Genre_Changed";
//		url = "/Cake_NR5/keywords/add_KW__Genre_Changed";
	
	}

//	alert("url => '" + url + "'");
	
//	var url = "http://localhost/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/_main_table.php";
	
	//ref C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	$.ajax({
		
		url: url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		alert(data);
		
		$("div#div_main").html(data);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
	});
	
	
}

