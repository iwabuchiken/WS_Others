<?php

// 	require_once 'cons.php';
// 	require 'cons.php';
	//ref http://webpaprika.com/935.html
	if (!class_exists('Cons')) {
		require_once 'cons.php';
	}

	class Libs {
	
		static function get_InitialMatrix($x, $y) {
			
			$ary = array();
			
			for ($i = 0; $i < $x; $i++) {
				
				$tmp = array();
				
				for ($j = 0; $j < $y; $j++) {
					
					array_push($tmp, rand(0, 1));
// 					array_push($tmp, $i * $j);
// 					$tmp.push($i * $j);
					
				}
				
				array_push($ary, $tmp);
// 				$ary.push($tmp);
				
			}
			
			return $ary;
			
		}//function get_InitialMatrix($x, $y)
	
// 		static function get_InitialMatrix__Patterns($x, $y, $pattern) {
		static function get_InitialMatrix__Patterns
		($x, $y, $pattern, $block_X, $block_Y) {
			
			$ary = array();
			
			if ($pattern == Cons::$pattern_Block_4x3) {
// 			if ($pattern == "block_4x3") {
			
				echo "(((( ".Cons::$pattern_Block_4x3." ))))))";
				
				for ($i = 0; $i < $x; $i++) {
				
					$tmp = array();
				
					for ($j = 0; $j < $y; $j++) {
							
						array_push($tmp, 0);
// 						array_push($tmp, rand(0, 1));
						// 					array_push($tmp, $i * $j);
						// 					$tmp.push($i * $j);
							
					}
				
					array_push($ary, $tmp);
					// 				$ary.push($tmp);
				
				}

				// columns
				$start_Col = count($ary) / 2 - 2;
				$end_Col = count($ary) / 2 +1;
				
				for ($j = $start_Col; $j < $end_Col; $j++) {
				
					// rows
					$start = count($ary[0]) / 2 - 2;
					$end = count($ary[0]) / 2 + 2;
					
					echo "((( start = $start / end = $end )))";
					
					for ($i = $start; $i < $end; $i++) {
					
						$ary[$j][$i] = 1;
							
					}//for ($i = 0; $i < count($ary) / 2 + 1; $i++)
								
				}//for ($j = 0; $j < $end_Col; $j++)
				
			} else if ($pattern == Cons::$pattern_Stick_4x1) {
				
				echo Cons::$pattern_Stick_4x1;
// 				echo "(((( stick_4x1 ))))))";
				
				for ($i = 0; $i < $x; $i++) {
				
					$tmp = array();
				
					for ($j = 0; $j < $y; $j++) array_push($tmp, 0);
				
					array_push($ary, $tmp);
					// 				$ary.push($tmp);
				
				}
				
				// rows
				$start = count($ary[0]) / 2 - 2;
				$end = count($ary[0]) / 2 + 2;
					
				echo "((( start = $start / end = $end )))";
					
				for ($i = $start; $i < $end; $i++) $ary[count($ary) / 2][$i] = 1;
						
// 				}//for ($i = 0; $i < count($ary) / 2 + 1; $i++)

// 				for ($i = $start; $i < $end; $i++) {
						
// 					$ary[count($ary) / 2][$i] = 1;
						
// 				}//for ($i = 0; $i < count($ary) / 2 + 1; $i++)
				
// 				}//for ($j = 0; $j < $end_Col; $j++)
				
			} else if ($pattern == Cons::$pattern_Block_XY) {
				
// 				echo "\$pattern == Cons::\$pattern_Block_XY";
				
				echo "(((( ".Cons::$pattern_Block_XY." ))))))";
				
				for ($i = 0; $i < $x; $i++) {
				
					$tmp = array();
				
					for ($j = 0; $j < $y; $j++) {
							
						array_push($tmp, 0);
						// 						array_push($tmp, rand(0, 1));
						// 					array_push($tmp, $i * $j);
						// 					$tmp.push($i * $j);
							
					}
				
					array_push($ary, $tmp);
					// 				$ary.push($tmp);
				
				}
				
				// columns
// 				$start_Col = count($ary) / 2 - 2;
// 				$end_Col = count($ary) / 2 +1;
				$start_Col = count($ary) / 2 - ($block_Y / 2);
				$end_Col = count($ary) / 2 + ($block_Y / 2);
				
				for ($j = $start_Col; $j < $end_Col; $j++) {
				
					// rows
					$start = count($ary[0]) / 2 - ($block_X / 2);
					$end = count($ary[0]) / 2 + ($block_X / 2);
// 					$start = count($ary[0]) / 2 - 2;
// 					$end = count($ary[0]) / 2 + 2;
						
					echo "((( start = $start / end = $end )))";
						
					for ($i = $start; $i < $end; $i++) {
							
						$ary[$j][$i] = 1;
							
					}//for ($i = 0; $i < count($ary) / 2 + 1; $i++)
				
				}//for ($j = 0; $j < $end_Col; $j++)
				
				
			} else if ($pattern == "block_4x3") {
				
				$ary = Libs::get_InitialMatrix($x, $y);
				
			} else { $ary = Libs::get_InitialMatrix($x, $y);
				
			}//if ($pattern == "beehive")
			
			return $ary;
			
		}//static function get_InitialMatrix__Patterns
	
	}