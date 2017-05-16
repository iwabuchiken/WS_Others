//ref global variable http://qiita.com/kenju/items/c7fad62a12cc2809b507
total = 0;	// Write this code before "testTimer" declaration code. Otherwise, "total += 1"
			//	line won't be processed.

//ref https://sites.google.com/site/jqueryjavascript/setintervaltoclearintervalno-shii-fang
testTimer;


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
	
	/***********
	 * test
	 **************/
//	var obj = $("table#table_main");
	var obj = $("table#table_main tr");
	
//	alert(table);
	//ref http://stackoverflow.com/questions/10314338/get-name-of-object-or-class-in-javascript
//	alert(obj.constructor.name);	//=> 'r'
	//ref length http://chaika.hatenablog.com/entry/2014/08/07/103459
//	alert(obj.length);	//=> '5'
//	alert(obj[0]);	//=> '[object HTMLTableRowElement]'
//	alert(obj[0].length);	//=> 'undefined'
//	alert(obj[0].text());	//=> no display
//	alert("obj[0].html() => " + obj[0].html());	//=> no window
//	alert(obj);
	//ref http://uhyohyo.net/javascript/2_8.html
//	alert(obj[0].item(0));	//=> no window
//	alert(obj[0].cells);	//=> '[object HTMLCollection]'
//	alert(obj[0].cells.length);	//=> '5'
//	alert(obj[0].cells.item(0));	//=> '[object HTMLTableCellElement]'
//	alert(obj[0].cells.item(0).html());	//=> no window
	//ref http://stackoverflow.com/questions/4253558/how-to-get-the-html-table-particullar-cell-value-using-javascript answered Nov 23 '10 at 7:34
//	alert(obj[0].cells.item(0).innerText);	//=> '0'
//	alert(obj[1].cells.item(3).innerText);	//=> '0'

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
	
//	alert("ary.length => " + ary.length);
	
//	alert(
//			ary[0] + "\n" + ary[1] + "\n"
//			
//			+ ary[2] + "\n" + ary[3] + "\n"
//			
//			+ ary[4] + "\n"
//			
////			+ ary[5] + "\n" + ary[6] + "\n"
////			+ ary[7] + "\n" + ary[8] + "\n"
//	
//	
//	);	//=> 0,1,2,3
	
	var lenOf_Array_Rows = ary.length;
	var lenOf_Array_Columns = ary[0].length;
	
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
	    		lenOf_Array_Columns : lenOf_Array_Columns
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