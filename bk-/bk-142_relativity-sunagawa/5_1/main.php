	<!--

http://localhost/WS_Others/bk-/bk-142_relativity-sunagawa/5_1/main.php

C:\WORKS_2\WS\WS_Others\free\
C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\

C:\WORKS_2\WS\WS_Others
C:\WORKS_2\WS\WS_Others\bk-\

/WS_Others/bk-/bk-142_relativity-sunagawa
/WS/WS_Others/bk-/bk-142_relativity-sunagawa

/WS/WS_Others/bk-
/WS/WS_Others/bk-/bk-142_relativity-sunagawa


-->
<?php

require 'setup.php';

?>

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    
    <title><?php echo $session; ?> (<?php echo $version; ?>)</title>
<!--     <title>rect select</title> -->

	<script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js">
		</script>
		
	<script type="text/javascript" src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js">
		</script>
		
	<!-- 	ref http://css.uka-p.com/basic/header.html -->
	<style type="text/css">
	
		tr.tr_Colors {
		
			height	: 40px;
		
		}
		
		td.td_Colors {
			/*
			background : yellow;
			*/
			width : 15px;
			
			color	: black;
			/*
			color	: white;
			*/
		}
	
		table#tbl_Main {
		
			border-style	: none;
			
			display			: none;
		
		}
	
	</style>
	
	<!-- ref http://www.openspc2.org/JavaScript/study/script.html	 -->
	<script type="text/javascript">

		function onLoad() {

// 			alert("loaded");
			
		}

		function btn_ShowHide_Table_1() {

			$('table#tbl_Main').toggle();
			
		}

		function btn_ShowHide_Table_2() {

			$('table#tbl_Main_2').toggle();
			
		}

		function show_Data(y, x) {

// 			alert("x => " + x
// 					+ " / "
// 					+ "y => " + y);

			//ref https://stackoverflow.com/questions/16064627/how-to-read-get-the-css-background-color-of-a-row-in-a-gridview ''
			var id = "td_" + y + "," + x;

			var td = $("td#" + id);

// 			alert("td => " + td);	//=> [object Object]
// 			alert(td.css('background-color')); //=> 'undefined'
// 			alert("bgcolor ~> " + td.css("background-color")); //=> 'undefined'
// 			alert("bgcolor ~> " + td.css("background"));

			console.log("td.css(\"background\") => " + td.css("background-color"));
// 			console.log("td.css(\"background\") => " + td.css("background"));

			var bg_color = $("td#" + id).css("background");
// 			var bg_color = $("td#" + id).css("background-color");

// 			alert("id => " + id

// 					+ " / "
// 					+ bg_color
// 			);
			
		}
		
	</script>
		
</head>

<body onload="onLoad();">
<!-- <body onload="onLoad();"> -->

<button id="btn_ShowHide_Table_1" onclick="btn_ShowHide_Table_1();">
Show/Hide
</button>
table main
<table id="tbl_Main">

	<?php 
	
		$numOf_Trs = 10;
	
		for ($j = 0; $j < $numOf_Trs; $j++) {
		
	?>


		<tr class="tr_Colors">
		
			<?php 
			
	// 			$numOf_Tds = 20;
				$numOf_Tds = 40;
			
				for ($i = 0; $i < $numOf_Tds; $i++) {
				
			?>
	
			<td class="td_Colors" style="<?php 
				
					$val_R = intval(1.0 * 255 / $numOf_Tds * $i);
					
					$val_B = 255 - intval(1.0 * 255 / $numOf_Tds * $i);
					
					$val_G = intval(1.0 * (255 + 28) / $numOf_Trs * $j);
// 					$val_G = intval(1.0 * 255 / $numOf_Trs * $j);
					
					$str_R = sprintf("%02x", $val_R);
					
					$str_B = sprintf("%02x", $val_B);
					
					$str_G = sprintf("%02x", $val_G);
					
					
					
	// 				$str_R = sprintf("%02x", dechex($val_R));
	// 				$str_R = sprintf("%02x", dechex($val_R));
					
					echo sprintf("background : #%s%s%s;", $str_R, $str_G, $str_B);
// 					echo sprintf("background : #%s00%s;", $str_R, $str_B);	//=> w.

	// 				echo sprintf("background : #%s0000;", $str_R);
	// 				echo sprintf("background : #%02x0000;", dechex($val_R));
	// 				echo sprintf("#%02x0000", dechex($val_R));
				
				?>">
			
				<?php 
				
	// 				echo "val_R = " . $val_R
	// 						. "(dechex = " . dechex($val_R)
	// 						. ")(str_R = " . $str_R . ")";
					
				?>
			
			</td>
	
			<?php 
			
				}//for ($i = 0; $i < 50; $i++)
			
			?>	
		</tr>

	<?php 

		}
	
	?>
	
</table>
    
<br>

<button id="btn_ShowHide_Table_2" onclick="btn_ShowHide_Table_2();">
Show/Hide
</button>
table main 2
<table id="tbl_Main_2">

	<?php 
	
		$numOf_Trs = 10;
		
		$tickOf_Trs = (255 + 28) / $numOf_Trs;
// 		$tickOf_Trs = 255 / $numOf_Trs;
	
		for ($j = 0; $j < $numOf_Trs; $j++) {
		
	?>


		<tr class="tr_Colors">
		
			<?php 
			
	// 			$numOf_Tds = 20;
				$numOf_Tds = 40;
			
				$h = intval($tickOf_Trs * $j);
// 				$h = $tickOf_Trs * $j;
				
				$tickOf_Tds = (255 - $h) / $numOf_Tds;
// 				$tickOf_Tds = (255 - $h) / $numOf_Tds;
// 				$tickOf_Tds = (255 - $tickOf_Trs * $j) / $numOf_Tds;
				
				for ($i = 0; $i < $numOf_Tds; $i++) {
				
			?>
	
			<td class="td_Colors"
				id="td_<?php echo "$j,$i"; ?>"
				onclick="show_Data(<?php echo $j . ',' . $i;?>);" 
				style="<?php 
				
					$val_R = intval(1.0 * $tickOf_Tds * $i + $h);
// 					$val_R = intval(1.0 * $tickOf_Tds * $i);
					
					$val_B = 255 - $tickOf_Tds;
// 					$val_B = 255 - $val_R;
					
					$val_G = intval(1.0 * ($h * 1.003));
// 					$val_G = intval(1.0 * $h);
// 					$val_G = intval(1.0 * $tickOf_Trs * $j);
// 					$val_G = intval(1.0 * 255 / $numOf_Trs * $j);
					
					$str_R = sprintf("%02x", $val_R);
					
					$str_B = sprintf("%02x", $val_B);
					
					$str_G = sprintf("%02x", $val_G);
					
					$str_Total = sprintf("background : #%s%s%s;", $str_R, $str_G, $str_B);
					
					echo $str_Total;
// 					echo sprintf("background : #%s%s%s;", $str_R, $str_G, $str_B);
				
				?>">
				
				<?php 
				
// 					echo $val_R . "(str_R = $str_R / total = $str_Total)";
// 					echo $h;
				?>
			
			</td>
	
			<?php 
			
				}//for ($i = 0; $i < 50; $i++)
			
			?>	
		</tr>

	<?php 

		}
	
	?>
	
</table>
    
<!-- <table id="tbl_Main"> -->

<!-- 	<tr class="tr_Colors"> -->
	
		<?php 
		
// // 			$numOf_Tds = 20;
// 			$numOf_Tds = 40;
		
// 			for ($i = 0; $i < $numOf_Tds; $i++) {
			
// 		?>

		<td class="td_Colors" style="<?php 
			
// 				$val_R = intval(1.0 * 255 / $numOf_Tds * $i);
				
// 				$val_B = 255 - intval(1.0 * 255 / $numOf_Tds * $i);
				
// 				$str_R = sprintf("%02x", $val_R);
				
// 				$str_B = sprintf("%02x", $val_B);
				
// // 				$str_R = sprintf("%02x", dechex($val_R));
// // 				$str_R = sprintf("%02x", dechex($val_R));
				
// 				echo sprintf("background : #%s00%s;", $str_R, $str_B);
// // 				echo sprintf("background : #%s0000;", $str_R);
// // 				echo sprintf("background : #%02x0000;", dechex($val_R));
// // 				echo sprintf("#%02x0000", dechex($val_R));
			
			?>">
		
			<?php 
			
// // 				echo "val_R = " . $val_R
// // 						. "(dechex = " . dechex($val_R)
// // 						. ")(str_R = " . $str_R . ")";
				
// 			?>
		
<!-- 		</td> -->

		<?php 
		
// 			}//for ($i = 0; $i < 50; $i++)
		
		?>	
<!-- 	</tr> -->

<!-- </table> -->
    
</body>
</html>
