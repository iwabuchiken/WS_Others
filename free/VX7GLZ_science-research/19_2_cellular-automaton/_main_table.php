<table border="1" id="table_main">

	<?php 

		require 'libs.php';

		//refe http://php.net/manual/ja/reserved.variables.get.php
// 		echo $_GET["ary"];
// 		echo get_class($_GET["ary"]);
// 		echo count($_GET["ary"]);
		
		$ary = $_POST["ary"];
		$lenOf_Array_Rows = $_POST["lenOf_Array_Rows"];
		$lenOf_Array_Columns = $_POST["lenOf_Array_Columns"];
		
		$block_X = $_POST["block_X"];
		$block_Y = $_POST["block_Y"];
		
		//debug
// 		echo "block_X => $block_X";
		
		$msg = "";
		
			
/*
 * @return
 * 0
 * 1
 */
		function apply_Rules($x, $y, $matrix) {
		
			$count = 0;
			$lenOf_Rows = count($matrix);
			$lenOf_Columns = count($matrix[0]);
				
			// A1 (-1, -1)
			if(  ($x - 1) >= 0   &&   ($y - 1) >= 0   &&   $matrix[ $x - 1 ][ $y - 1 ] == 1)
				$count += 1;
					
			// A2 (0, -1)
			if(  ($x - 0) >= 0   &&   ($y - 1) >= 0   &&   $matrix[ $x - 0 ][ $y - 1 ] == 1)
				$count += 1;
					
			// A3 (+1, -1)
			if(  ($x + 1) < $lenOf_Rows
					&&   ($y - 1) >= 0
					&&   $matrix[ $x + 1 ][ $y - 1 ] == 1)

				$count += 1;
							
			// A4 (+1, 0)
			if(  ($x + 1) < $lenOf_Rows
					&&   ($y - 0) >= 0
					&&   $matrix[ $x + 1 ][ $y - 0 ] == 1)

				$count += 1;
								
			// A5 (+1, +1)
			if(  ($x + 1) < $lenOf_Rows
					&&   ($y + 1) < $lenOf_Columns
					&&   $matrix[ $x + 1 ][ $y + 1 ] == 1)

				$count += 1;
									
			// A6 (0, +1)
			if(  ($x + 0) >= 0
					&&   ($y + 1) < $lenOf_Columns
					&&   $matrix[ $x + 0 ][ $y + 1 ] == 1)

				$count += 1;
										
			// A7 (-1, +1)
			if(  ($x - 1) >= 0
					&&   ($y + 1) < $lenOf_Columns
					&&   $matrix[ $x - 1 ][ $y + 1 ] == 1)

				$count += 1;
											
			// A8 (-1, 0)
			if(  ($x - 1) >= 0
					&&   ($y + 0) >= 0
					&&   $matrix[ $x - 1 ][ $y + 0 ] == 1)

				$count += 1;
												
			/******
			 * judge
			 ******/
			if ($matrix[$x][$y] == 0) {
					
				if ($count == 3) {

					return 1;	// born

				} else {

					return 0;	// remain dead
						
				}//if ($count >= 3)
					
			} else {	// live cell
					
				if ($count <= 1) {

// 					return 10;	// turns dead
					return 0;	// turns dead

				} else if ($count >= 4) {
						
// 					return 10;	// turns dead (overpopulation)
					return 0;	// turns dead (overpopulation)
						
				} else {

// 					return 11;	// remains alive
					return 1;	// remains alive
						
				}//if (conditions)

			}//if ($matrix[$x][$y] == 0)
			
		}//apply_Rules($i, $j, $matrix)

		function set_Matrix($size, $ary_tmp) {

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
				
		}//function set_Matrix($size, $ary_tmp)
		
		function set_Matrix_tmp($size, $ary_tmp) {

			for ($i = 0; $i < $size[0]; $i++) {
					
				echo "<tr>";
					
				for ($j = 0; $j < $size[1]; $j++) {
			
					$num = $ary_tmp[$i][$j] + 1;
// 					$num = $ary_tmp[$i][$j];
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
				
		}//function set_Matrix_tmp($size, $ary_tmp)
		
		function set_Matrix_tmp_2($size, $ary_tmp) {

			$matrix = array();
			
			for ($i = 0; $i < $size[0]; $i++) {
					
				$row = array();
				
// 				echo "<tr>";
					
				for ($j = 0; $j < $size[1]; $j++) {
			
					$num = apply_Rules($i, $j, $ary_tmp);
// 					$num = $ary_tmp[$i][$j]  + 3;
// 					$num = $ary_tmp[$i][$j] + 1;
					
					array_push($row, $num);
					
// 					$num = $ary_tmp[$i][$j];
					// 				$num = rand(0, 1);
			
// 					if ($num % 2 == 0) {
// 						// 				if (($i + $j) % 2 == 0) {
			
// 						echo "<td class='td_even'>";
			
// 						echo $num;
// 						// 					echo $i + $j;
			
// 						echo "</td>";
			
// 					} else {
			
// 						echo "<td class='td_odd'>";
			
// 						echo $num;
// 						// 					echo $i + $j;
			
// 						echo "</td>";
			
// 					}//if ($i * $j / 2 == 0)
						
						// 				echo "<td>";
			
						// 					echo $i + $j;
			
						// 				echo "</td>";
				}//for ($j = 0; $j < $size[1]; $j++)
			
				// push array
				array_push($matrix, $row);
			
// 				echo "</tr>";

			}//for ($i = 0; $i < $size[0]; $i++)

			// return
			return $matrix;
			
		}//function set_Matrix_tmp_2($size, $ary_tmp)
		
		function return_Html($matrix) {

			$x = count($matrix);
			$y = count($matrix[0]);
			
			for ($i = 0; $i < $x; $i++) {
					
				echo "<tr>";
					
				for ($j = 0; $j < $y; $j++) {
						
					$num = $matrix[$i][$j];
						
					if ($num % 2 == 0) {
						// 				if (($i + $j) % 2 == 0) {
							
						echo "<td class='td_even' id=\"cell_$i"."x"."$j\" onclick=\"change_Cell_Status($i,$j);\">";
// 						echo "<td class='td_even' id=\"cell_$i"."x"."$j\" onclick=\"alert($i,$j)\">";
// 						echo "<td class='td_even'>";
							
						echo $num;
						// 					echo $i + $j;
							
						echo "</td>";
							
					} else {
							
						echo "<td class='td_odd' id=\"cell_$i"."x"."$j\" onclick=\"change_Cell_Status($i,$j);\">";
// 						echo "<td class='td_odd'>";
							
						echo $num;
						// 					echo $i + $j;
							
						echo "</td>";
							
					}//if ($i * $j / 2 == 0)
			
					// 				echo "<td>";
						
					// 					echo $i + $j;
						
					// 				echo "</td>";
				}
					
					
				echo "</tr>";
					
			}//for ($i = 0; $i < $size[0]; $i++)
				
		}//function return_Html($matrix)

		$size = array(count($ary), count($ary[0]));
// 		$size = array(5, 5);
	
// 		$ary_tmp = Libs::get_InitialMatrix($size[0], $size[1]);

		$matrix = set_Matrix_tmp_2($size, $ary);

		return_Html($matrix);
		
		// return html
		
		
// 		set_Matrix_tmp($size, $ary);
// 		set_Matrix($size, $ary);
// 		set_Matrix($size, $ary_tmp);
		
// 		for ($i = 0; $i < $size[0]; $i++) {
			
// 			echo "<tr>";
			
// 			for ($j = 0; $j < $size[1]; $j++) {
				
// 				$num = $ary_tmp[$i][$j];
// // 				$num = rand(0, 1);
				
// 				if ($num % 2 == 0) {
// // 				if (($i + $j) % 2 == 0) {
				
// 					echo "<td class='td_even'>";
						
// 					echo $num;
// // 					echo $i + $j;
						
// 					echo "</td>";
				
// 				} else {
				
// 					echo "<td class='td_odd'>";
				
// 					echo $num;
// // 					echo $i + $j;
				
// 					echo "</td>";
						
// 				}//if ($i * $j / 2 == 0)
					
// // 				echo "<td>";
				
// // 					echo $i + $j;
				
// // 				echo "</td>";
// 			}
		
		
// 			echo "</tr>";
			
// 		}
	
	
	?>

</table>
