//////ref C:\WORKS_2\WS\Eclipse_Luna\Cake_NR5\app\webroot\js\main.js
//$(document).ready(function(){
//	
//	alert("ready");
//	
//});

////test
//alert("ready!!");


//ref global variable http://qiita.com/kenju/items/c7fad62a12cc2809b507
total = 0;	// Write this code before "testTimer" declaration code. Otherwise, "total += 1"
			//	line won't be processed.

////test
//alert("js");

//ref https://sites.google.com/site/jqueryjavascript/setintervaltoclearintervalno-shii-fang
//testTimer;
testTimer = null;

////test
//alert("js");


//		var testTimer;
	
function startTimer(){

//	alert("start timer");

	$("div#div_message").text("Starting...");
	
	testTimer = setInterval(update_table , 1000);
	
}

function stopTimer(){
	
	clearInterval(testTimer);

	$("div#div_message").text("Stopped.");

}





//// ref global variable http://qiita.com/kenju/items/c7fad62a12cc2809b507
//total = 0;

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

/*
 * @return
 * true		any element in the ary is 1 then ---> return true
 */
function validate_AllDead(ary) {
	
	var x = ary.length;
	var y = ary[0].length;
	
//	var judge = false;
	
	for (var i = 0; i < x; i++) {
		
		for (var j = 0; j < y; j++) {
			
			if (ary[i][j] == 1) return true;
			
		}
	}
	
	// return --> default
	return false;
	
}//validate_AllDead(ary)

function update_table() {
	
	//test
//	alert("update");
	
	/***********
	 * test
	 **************/
//	var obj = $("table#table_main");
	var obj = $("table#table_main tr");
	
	var ary = [];
	
	for (var i = 0; i < obj.length; i++) {
		
		var ary_tmp = [];
		
		var row = obj[i];
		
		var len_cells = row.cells.length;
		
		for (var j = 0; j < len_cells; j++) {
	
			//ref push https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array
			ary_tmp.push(row.cells.item(j).innerText);
//			ary.push(row.cells.item(j).innerText);
			
		}
		
		ary.push(ary_tmp);
		
	}
	
	var lenOf_Array_Rows = ary.length;
	var lenOf_Array_Columns = ary[0].length;
	
	var block_X = $("input#init_X").val();
	var block_Y = $("input#init_Y").val();

	var valueOf_Default_Init_X = 4;
	var valueOf_Default_Init_Y = 3;
	
	if (block_X == "") {
		
		$("input#init_X").val(valueOf_Default_Init_X);
		
		block_X = valueOf_Default_Init_X;
		
	}
		
	if (block_Y == "") {
		
		$("input#init_Y").val(valueOf_Default_Init_Y);
		
		block_Y = valueOf_Default_Init_Y;
		
	}
	
	/*
	 * validate: all dead?
	 */
	var res = validate_AllDead(ary);
	
	if (res == false) {
		
//		alert("all dead");
//		alert("all dead ==> stopping the timer");
		
		// stop
//		stopTimer();
		clearInterval(testTimer);
		
		$("div#div_message").text("Stopped. (All dead)");
//		$("div#div_message_2").text("All dead.");
		
		return;
		
	}
	
	var hostname = window.location.hostname;
	
	var url;
	
	if (hostname == "benfranklin.chips.jp") {
		
		url = "/WS/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/_main_table.php";
		
	} else {
	
		url = "/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/_main_table.php";
	
	}

	//ref C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	$.ajax({
		
		url: url,
		type: "POST",
//		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	    data: {
	    		ary: ary, 
	    		lenOf_Array_Rows : lenOf_Array_Rows, 
	    		lenOf_Array_Columns : lenOf_Array_Columns,
	    		block_X : block_X,
	    		block_Y : block_Y
	    },
//	    data: {ary: ary},
//	    data: {ary: ary_tmp},
//	    data: {memos: memos, image_id: image_id},
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
		
//		alert("ajax ==> done");
		
		total += 1;
		
		//ref remove http://www.buildinsider.net/web/jqueryref/007
//		$("div#div_main").removeAttribute('id').prepend(data);
		//ref prepend http://api.jquery.com/prepend/
//		$("div#div_main").prepend(data);
		$("div#div_main").html(data);
		
//		alert("div_main => updated");
		
		// set message ---> count
//		total += 1;
		
//		alert("total => incremeted");
		
		$("div#div_message_2").text("(" + total + ")");
		
//		alert("total => updated");
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
	});
	
	
}

//ref http://stackoverflow.com/questions/7652342/how-to-print-the-following-multi-dimensional-array-in-java-script answered Oct 4 '11 at 18:40
function console_test() {
	
	console.log("missed the particulars of the loops, fixed");
	
}

function change_Cell_Status(x, y) {
	
//	alert("changing cell status for => " + x + " / " + y);
	
	var td = $("td#cell_" + x + "x" + y);
	
//	var status = td.val();	//=> blank
	//ref html() http://stackoverflow.com/questions/376081/how-to-get-a-table-cell-value-using-jquery "answered Dec 17 '08 at 21:39"
	var status = td.html();	//=> '1', '0'
	
//	alert("status => " + status + " / " + "status + 1 => " + (status + 1));
//	alert("status => " + status + " / " + "status + 1 => " + (parseInt(status) + 1));
	
	var status_new = parseInt(status) == 1 ? 0 : 1;
	
	// change cell status
	// ref parseInt https://www.w3schools.com/jsref/jsref_parseint.asp
	td.html(status_new);
//	td.html(parseInt(status) == 1 ? "0" : "1");
	
	// cell attribute
	td.attr("class", status_new == 1 ? "td_odd" : "td_even");
//	td.attr("class", parseInt(status) == 1 ? "td_even" : "td_odd");
	
//	//debug
//	alert("td => " + (td == null ? "null" : td));
//	
//	alert("status => " + (status == null ? "null" : (status == "" ? "blank" : status)));
	
	
	
	
//	alert("td => " + td);
	
//	alert("cell " + x + "/" + y + " => status is " + status);
	
	
}//function change_Cell_Status(x, y) {


////ref C:\WORKS_2\WS\Eclipse_Luna\Cake_NR5\app\webroot\js\main.js
// NOTICE : this main.js file needs to be included AFTER jquery is included.
// 	=> otherwise, the browser console says :
		//Uncaught ReferenceError: $ is not defined
		//at main.js:294
		//(anonymous) @ main.js:294
		// ref http://stackoverflow.com/questions/6085964/document-ready-not-working "answered May 22 '11 at 4:14"	
$(document).ready(function(){
	
//	alert("document -> ready");
	
	$('#select_initial').change(function(){
		
//		alert("changed");
		
    	//REF http://stackoverflow.com/questions/10659097/jquery-get-selected-option-from-dropdown answered May 18 '12 at 20:14
    	var id = $('#select_initial').find(":selected").val();
    	
    	var hostname = window.location.hostname;
    	
    	var url = "";
    	
    	if (hostname == "localhost") {

    		url = "http://localhost/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/main.php?select_initial=" + id;
    			
		} else {
			
			url = "http://benfranklin.chips.jp/WS/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/main.php?select_initial=" + id;

		}

    	// init_X, init_Y
    	var block_X = $("input#init_X").val();
    	var block_Y = $("input#init_Y").val();
//    	var block_X = $("input#input_X").text();
    	
//    	alert("block_X => '" + block_X + "'");
    	
    	var valueOf_Default_Init_X = 4;
    	var valueOf_Default_Init_Y = 3;
    	
    	if (block_X == "") {
    		
    		$("input#init_X").val(valueOf_Default_Init_X);
    		
    		block_X = valueOf_Default_Init_X;
    		
    	}
    		
    	if (block_Y == "") {
    		
    		$("input#init_Y").val(valueOf_Default_Init_Y);
    		
    		block_Y = valueOf_Default_Init_Y;
    		
    	}

//    	alert("onchange => block_X " + block_X + " / " + "block_Y " + block_Y);
    	
    	// update url
    	url = url + "&" + "block_X=" + block_X
    			+ "&" + "block_Y=" + block_Y;
    	
//    	alert("url => '" + url + "'");
    	
    	//REF https://developer.mozilla.org/en-US/docs/Web/API/window.location "Basic Example"
    	location.assign(url);

	});//$('#genre').change(function(){
	
	
});//$(document).ready(function(){
