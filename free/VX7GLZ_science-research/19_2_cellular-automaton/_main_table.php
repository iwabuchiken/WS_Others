<table border="1" id="table_main">

	<?php 

		require 'libs.php';
		
// 		$ary_tmp = Libs::get_InitialMatrix(5, 5);
		
// 		foreach ($ary_tmp as $entry) {
		
// 			foreach ($entry as $cell) {
			
// 				echo $cell;
				
// 				echo "<br>";
				
				
				
// 			}//foreach ($entry as $cell)
			
// 			;
			
// 		}//foreach ($ary_tmp as $entry)
		
		
	
// 		$size = [5, 5];
		$size = array(5, 5);
	
		$ary_tmp = Libs::get_InitialMatrix($size[0], $size[1]);

		for ($i = 0; $i < $size[0]; $i++) {
			
			echo "<tr>";
			
			for ($j = 0; $j < $size[1]; $j++) {
				
				$num = $ary_tmp[$i][$j];
// 				$num = rand(0, 1);
				
				if ($num % 2 == 0) {
// 				if (($i + $j) % 2 == 0) {
				
					echo "<td class='td_even'>";
						
					echo $num;
// 					echo $i + $j;
						
					echo "</td>";
				
				} else {
				
					echo "<td class='td_odd'>";
				
					echo $num;
// 					echo $i + $j;
				
					echo "</td>";
						
				}//if ($i * $j / 2 == 0)
					
// 				echo "<td>";
				
// 					echo $i + $j;
				
// 				echo "</td>";
			}
		
		
			echo "</tr>";
			
		}
	
	
	?>

</table>
