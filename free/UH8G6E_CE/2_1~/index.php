<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<!-- ref C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\13_threejs\13_1\sample (1)\index.html -->
<!-- 	<meta name="viewport" content="width=device-width"> -->

<meta name="viewport" content="minimum-scale=0.5">

<title>UH8G6E_CE 2_1</title>


</head>
<body>

<?php

//ref http://php.net/manual/ja/reserved.variables.server.php
$hostname = $_SERVER['SERVER_NAME'];

//ref http://stackoverflow.com/questions/4117555/simplest-way-to-detect-a-mobile-device
$useragent=$_SERVER['HTTP_USER_AGENT'];

$font_size = "";
$font_size_Local = "4";
$font_size_Remote = "10";

$subject = $useragent;
$pattern = '/iPhone/';
// 	$pattern = '/\(iphone/';
// 	$pattern = '/(iphone/';
$res = preg_match($pattern, $subject, $matches, PREG_OFFSET_CAPTURE, 3);

// set font size ---> use : user agent
if ($res == 1) {

	$font_size = $font_size_Remote;

} else {

	$font_size = $font_size_Local;
		
}//if ($res == 1)


?>

<?php
	//http://phpspot.net/php/pg%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%83%AA%E3%82%B9%E3%83%88%E3%82%92%E5%8F%96%E5%BE%97.html
	
// 	if ($dir = opendir("data/")) {
	if ($dir = opendir(".")) {
		
// 		$count = 0;
		
		$file_names = array();
		
		while (($file = readdir($dir)) !== false) {
			
// 			$count += 1;
			
			if ($file != "." && $file != "..") {
				
				array_push($file_names, $file);
				
// 				$count += 1;
				
// // 				echo "count=".$count;
// // 				$items = array($_SERVER['SERVER_NAME'], $_SERVER['PHP_SELF']);
// 				$items = array($_SERVER['PHP_SELF']);
				
// 				$link = join($items);
				
// // 				echo $count."."."<a href='".$link."'>"."$file"."</a>"."\n";
// 				echo $count."."."<a href='".$file."'>"."$file"."</a>"."\n";
				
// 				echo "<br/>";
			}
		}
		closedir($dir);

		// Sort names
		sort($file_names);
		
		// Show file names
		$count = 1;
		
		foreach ($file_names as $name) {
			
			echo $count.". "."<a href='".$name."'>"
				
				."<font size=\"$font_size\">"
				."$name"
				."</font>"
				."</a>"."\n";
			echo "<br/>";
// 			echo "<br/>";
			
			$count += 1;
		}
		
	}//if ($dir = opendir("."))
	
	//echo "<br/>";
	//echo "Done";
	//echo `whoami`;
	
?>

</body>
