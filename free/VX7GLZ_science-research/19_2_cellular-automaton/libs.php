<?php

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
	
	}