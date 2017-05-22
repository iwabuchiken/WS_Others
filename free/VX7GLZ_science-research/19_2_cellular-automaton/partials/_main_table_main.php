<?php 

	require_once './libs.php';
// 	require_once '../libs.php';	//=> n.w.

	function show_table($select_initial, $block_X, $block_Y) {
		
// 		echo "show_table";
		
		echo "<table border=\"1\" id=\"table_main\">";
		
		$size = array(Cons::$valueOf_Initial_WorldSize_X, Cons::$valueOf_Initial_WorldSize_Y);
// 		$size = array(30,30);
		// 				$size = array(15, 15);
		// 				$size = array(8, 8);
		// 				$size = array(5, 5);
		
		if (isset($select_initial)) {
		
			$matrix = Libs::get_InitialMatrix__Patterns(
					$size[0], $size[1], $select_initial,
					$block_X, $block_Y);
			// 										$size[0], $size[1], $select_initial);
				
		} else {//if (isset($select_initial))
				
			$matrix = Libs::get_InitialMatrix($size[0], $size[1]);
				
		}
		
		for ($i = 0; $i < $size[0]; $i++) {
				
			echo "<tr>";
				
			for ($j = 0; $j < $size[1]; $j++) {
		
				if ($matrix[$i][$j] == 0) {
					// 						if ($i * $j % 2 == 0) {
		
					echo "<td class='td_even' id='cell_$i"."x"."$j' onclick='alert(\"$i,$j\");'>";
// 					echo "<td class='td_even'>";
						
					echo $matrix[$i][$j];
						
					echo "</td>";
		
				} else {
		
					echo "<td class='td_odd' id='cell_$i"."x"."$j'>";
// 					echo "<td class='td_odd'>";
		
					echo $matrix[$i][$j];
		
					echo "</td>";
						
				}//if ($i * $j / 2 == 0)
		
			}
		
			echo "</tr>";
				
		}//for ($i = 0; $i < $size[0]; $i++) {
	
		echo "</table>";
		
	}//function show_table() {


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
			
			?>
		
<!-- 		</table> -->

<!-- 	</div> -->
	
<!-- </body> -->
