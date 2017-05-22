<!-- 

C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\19_2_cellular-automaton\main.php
C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\19_2_cellular-automaton
C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research

/WS/WS_Others/free/VX7GLZ_science-research
/WS/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton
http://benfranklin.chips.jp/WS/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/
http://benfranklin.chips.jp/WS/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/main.php

http://localhost/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/
http://localhost/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton/main.php

 -->

<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<!-- ref C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\13_threejs\13_1\sample (1)\index.html -->
<!-- 	<meta name="viewport" content="width=device-width"> -->

<!-- <meta name="viewport" content="minimum-scale=0.1"> -->
<!-- <meta name="viewport" content="minimum-scale=0.5"> -->

<?php 

// 	require_once 'libs.php';	
// 	require_once 'cons.php';	
// 	require 'libs.php';	
// 	require 'cons.php';	
// 	require_once 'cons.php';	
// 	require_once 'libs.php';	
	if (!class_exists('Cons')) {
		require_once 'cons.php';
	}
	if (!class_exists('Libs')) {
		require_once 'libs.php';
	}

	require_once 'partials/_main_table_main.php';
	

	$dpath = dirname($_SERVER["REQUEST_URI"]);
	
	$fname_css = "main.css";
	
	$fpath_css = $dpath."/".$fname_css;
	
	$fname_js = "main.js";
	$fpath_js = $dpath."/".$fname_js;
	
	$fname_jquery = "jquery-3.2.1.min.js";
	$fpath_jquery = $dpath."/".$fname_jquery;
	

?>

<!-- ref http://www.htmq.com/csskihon/004.shtml -->
<link rel="stylesheet" type="text/css" href='<?php echo $fpath_css;?>'>

<script type="text/javascript" src='<?php echo $fpath_jquery;?>'></script>

<script type="text/javascript" src='<?php echo $fpath_js;?>'></script>


<title>automaton</title>



</head>
<body>

	<!-- ref https://techacademy.jp/magazine/5537 -->
	<script>

	<!-- ref http://stackoverflow.com/questions/3138756/calling-a-function-every-60-seconds answered Jun 29 '10 at 7:44 -->
	<script>
	
	</script>

	<input type="button" value="update_table" id="btn_update" onclick="update_table();">
	<input type="button" value="abc" id="btn_update" onclick="startTimer();">
	
	&nbsp;&nbsp;&nbsp;
	
	<?php //echo "<br>"; echo "<br>";
	
	?>
	
	<!-- ref http://stackoverflow.com/questions/3138756/calling-a-function-every-60-seconds answered Jun 29 '10 at 7:44 -->
	<!-- Stop Button -->
	<a href="#" onclick="stopTimer();">Stop</a><!-- works -->

	&nbsp;&nbsp;&nbsp;
	
	<?php 
	
		
	
		$select_list = array(
			
				array("basic", "basic"),
				array("block_4x3", "block_4x3"),
				array(Cons::$pattern_Stick_4x1, Cons::$pattern_Stick_4x1),
				array(Cons::$pattern_Block_XY, Cons::$pattern_Block_XY),
		);
	
	?>

<!-- 	get select_itnial value -->
	<?php 
	
		@$select_initial = $_GET['select_initial'];
		
// 		echo "\$select_initial => ".$select_initial;
	
	?>
	
	
	<select name="select_initial" id="select_initial">
	
		<?php 
		
			foreach ($select_list as $select) {
				
				if (isset($select_initial) && $select_initial == $select[0]) {
					
					echo "select_initial == select (".$select_initial." / ".$select.")";
					echo "<br>";
					
					//ref http://www.tagindex.com/html_tag/form/select.html
					echo "<option value=\"".$select[1]."\" selected>".$select[0]."(selected)</option>";
				
				} else {
				
					echo "select_initial != select (".$select_initial." / ".$select.")";
					echo "<br>";
					
					echo "<option value=\"".$select[1]."\">".$select[0]."</option>";
					
				}//if (isset($select_initial) && $select_initial == $select)
				
			}//foreach ($select_list as $select)
			
		?>
	
	</select>
	
<!-- 	X, Y -->
	<?php 
	
		@$block_X = $_GET["block_X"];
		@$block_Y = $_GET["block_Y"];
	
	?>
	&nbsp;&nbsp;&nbsp;
	<label>X</label>
	<input type="text" name="lname" id="init_X" size="2" 
			value="<?php echo isset($block_X) ? $block_X : ""?>"
		>
	
	<label>Y</label>
	<input type="text" name="lname" id="init_Y" size="2"
			value="<?php echo isset($block_Y) ? $block_Y : ""?>"
		>

	<?php 

		// set : block_X
		if (isset($block_X)) {
			
		} else if ($block_X == "") {
		
			$block_X = Cons::$valueOf_Default_Block_X;
		
		} else {
		
			$block_X = Cons::$valueOf_Default_Block_X;
			
		}//if (isset($block_X))

		// set : block_Y
		if (isset($block_Y))  ;
		else if ($block_X == "") $block_X = Cons::$valueOf_Default_Block_X;
		else $block_X = Cons::$valueOf_Default_Block_X;
			
		
	
	
	?>
	
	<?php 
		
// 		echo "<br>"; echo "<br>";
		echo "<br>";
	
	?>

	<div id="div_message">message 1</div>
	<div id="div_message_2">message 2</div>
	

	
	<hr>
	
	<div id="div_main">
	
		<?php 
		
			show_table($select_initial, $block_X, $block_Y);
		
		?>
	
	
<!-- 		<table border="1" id="table_main"> -->
		
			<?php 
			
// 				$size = array(30,30);
// // 				$size = array(15, 15);
// // 				$size = array(8, 8);
// // 				$size = array(5, 5);
				
// 				if (isset($select_initial)) {
				
// 					$matrix = Libs::get_InitialMatrix__Patterns(
// 										$size[0], $size[1], $select_initial,
// 										$block_X, $block_Y);
// // 										$size[0], $size[1], $select_initial);
					
// 				} else {//if (isset($select_initial))
					
// 					$matrix = Libs::get_InitialMatrix($size[0], $size[1]);
					
// 				}
				
// 				for ($i = 0; $i < $size[0]; $i++) {
					
// 					echo "<tr>";
					
// 					for ($j = 0; $j < $size[1]; $j++) {
						
// 						if ($matrix[$i][$j] == 0) {
// // 						if ($i * $j % 2 == 0) {
						
// 							echo "<td class='td_even'>";
							
// 							echo $matrix[$i][$j];
							
// 							echo "</td>";
						
// 						} else {
						
// 							echo "<td class='td_odd'>";
								
// 							echo $matrix[$i][$j];
								
// 							echo "</td>";
							
// 						}//if ($i * $j / 2 == 0)
						
// 					}
				
// 					echo "</tr>";
					
// 				}
			
// 			?>
		
<!-- 		</table> -->

	</div>
	
</body>
