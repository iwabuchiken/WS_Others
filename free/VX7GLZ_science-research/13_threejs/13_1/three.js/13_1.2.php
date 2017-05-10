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
<title>VX7GLZ 13#1.2</title>
</head>

<?php 

	/*
	 * from : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\Lib\utils\utils.php
	 * at : 2017/05/09 17:52:02
	 */

	//ref http://php.net/manual/ja/reserved.variables.server.php
	$hostname = $_SERVER['SERVER_NAME'];
	
	if ($hostname == "localhost") {
	
		$script_src = "/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/three.min.js";
		$script_src_main = "/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/main.js";
		
		$page_root = "/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js";
	
	} else {
	
		$script_src = "/WS/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/three.min.js";
		$script_src_main = "/WS/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/main.js";
	
		$page_root = "/WS/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js";
		
	}

?>

<body>

	<a href="<?php echo $page_root?>">Back</a>
	
	<hr>

	<!-- ref https://html5experts.jp/yomotsu/5225/ -->
	<script src=<?php echo $script_src; ?>></script>
	<script src=<?php echo $script_src_main; ?>></script>
	
</body>
</html>