<!-- 
http://localhost/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/ 

FileZilla
C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\13_threejs\13_1\
/WS/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1

-->

<!DOCTYPE html>
<html>

<head>

	<meta charset="UTF-8">
	
	<!-- ref C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\13_threejs\13_1\sample (1)\index.html -->
	<!-- 	ref http://www.tagindex.com/html5/page/meta_viewport.html -->
	<meta name="viewport" content="minimum-scale=0.5">
<!-- 	<meta name="viewport" content="width=180, minimum-scale=0.5"> -->
<!-- 	<meta name="viewport" content="width=480"> -->
<!-- 	<meta name="viewport" content="width=device-width"> -->
	
	<title>VX7GLZ 13#1.2</title>
	
</head>

<?php 

	/*
	 * from : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\Lib\utils\utils.php
	 * at : 2017/05/09 17:52:02
	 */

	//ref http://php.net/manual/ja/reserved.variables.server.php
	$hostname = $_SERVER['SERVER_NAME'];
	
	//ref http://stackoverflow.com/questions/4117555/simplest-way-to-detect-a-mobile-device
	$useragent=$_SERVER['HTTP_USER_AGENT'];
	
	$fname_js_main = "main.js";
	$proj_root_local = "/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js";
	
	$font_size = "";
	$font_size_Local = "5";
	$font_size_Remote = "10";
	
// 	echo "hostname = $hostname";
// 	echo "<br>";
	
// 	echo "useragent = $useragent";
// 		// 	Mozilla/5.0 (Windows NT 6.1; Win64; x64)
// 	echo "<br>";

	//ref http://php.net/manual/ja/function.preg-match.php
	//ref http://stackoverflow.com/questions/4117555/simplest-way-to-detect-a-mobile-device answered Nov 7 '10 at 12:01
	$subject = $useragent;
	$pattern = '/iPhone/';
// 	$pattern = '/\(iphone/';
// 	$pattern = '/(iphone/';
	$res = preg_match($pattern, $subject, $matches, PREG_OFFSET_CAPTURE, 3);
	
// 	echo "subject='$useragent' | pattern='$pattern' | res = $res";
	
	
	if ($hostname == "localhost") {
	
		$script_src = "$proj_root_local/js/three.min.js";
// 		$script_src = "/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/three.min.js";
// 		$script_src_main = "/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/$fname_js_main";
		$script_src_main = "$proj_root_local/js/$fname_js_main";
		
		$page_root = $proj_root_local;
// 		$page_root = "/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js";

		$font_size = $font_size_Local;
	
	} else {
	
		$script_src = "/WS/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/three.min.js";
		$script_src_main = "/WS/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/$fname_js_main";
// 		$script_src_main = "/WS/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/main.js";
	
		$page_root = "/WS/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js";
		
		// set font size ---> use : user agent
		if ($res == 1) {
		
			$font_size = $font_size_Remote;
		
		} else {
		
			$font_size = $font_size_Local;
			
		}//if ($res == 1)
		
		
// 		$font_size = $font_size_Remote;
		
	}

?>

<body>

	<a href="
		
			<?php echo $page_root?>
		
		">
<!-- 		ref https://www.w3schools.com/tags/tag_font.asp -->
			<font size="<?php echo $font_size; ?>">Back</font>
	</a>
	
<!-- 	<a href=" -->
		<?php //echo $page_root?>
<!-- 		">Back</a> -->
	
	<hr>

	<!-- ref https://html5experts.jp/yomotsu/5225/ -->
	<script src=<?php echo $script_src; ?>></script>
	<script src=<?php echo $script_src_main; ?>></script>
	
</body>
</html>