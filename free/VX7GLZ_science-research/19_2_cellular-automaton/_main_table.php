<table border="1" id="table_main">

	<?php 

// 		foreach ($_SERVER as $elem) {
		
// 			echo $elem;
// 			echo "<br>"; echo "<br>";
			
			
			
// 		}//foreach ($_SERVER as $elem)
		
// 		echo $_SERVER['SERVER_ADDR'];
		//ref http://qiita.com/tsujimomo/items/c293d15e34646a826266
// 		echo $_SERVER["REQUEST_URI"];
// 		echo "<br>"; echo "<br>";
		
// 		echo dirname($_SERVER["REQUEST_URI"]);
// 		echo "<br>"; echo "<br>";
		
		
	
// 		$size = [5, 5];
		$size = array(5, 5);
	
		for ($i = 0; $i < $size[0]; $i++) {
			
			echo "<tr>";
			
			for ($j = 0; $j < $size[1]; $j++) {
				
				$num = rand(0, 1);
				
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
