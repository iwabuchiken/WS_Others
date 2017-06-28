<!-- 

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 

-->
<?php 

	require_once 'setup.php';

// 	$session = "4_1";
// 	$version = "1~";

?>

<!doctype html>
<head>
	<meta charset="utf-8">
	<meta name="author" content="" />
	<meta name="viewport" content="width=device-width">
	
	<title><?php echo $session; ?> (<?php echo $version; ?>)</title>


	<!-- https://code.jquery.com/jquery/ -->
	<script
	  src="https://code.jquery.com/jquery-3.2.1.min.js"
	  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
	  crossorigin="anonymous"></script>

	
	<script
	  src="https://code.jquery.com/ui/1.12.0/jquery-ui.min.js"
	  integrity="sha256-eGE6blurk5sHj+rmkfsGYeKyZx3M4bG+ZlFyA7Kns7E="
	  crossorigin="anonymous"></script>

	<?php 
	
// 		$hostname = gethostname();
		
// 		$dpath_JavaScript = "";
// 		$dpath_StyleSheet = "";
		
// 		$dpath_ProjectRoot = "";
		
// 		$session_name = $session;
// // 		$session_name = "3_1";
		
// 		if ($hostname == "iwabuchiken-PC") {
				
// 			$dpath_JavaScript = "/WS_Others/free/UH8G6E_CE/$session_name/js";

// 			$dpath_StyleSheet = "/WS_Others/free/UH8G6E_CE/$session_name/css";
			
// 			$dpath_ProjectRoot = "/WS_Others/free/UH8G6E_CE";
				
// 		} else {
				
// 			$dpath_JavaScript ="/WS/WS_Others/free/UH8G6E_CE/$session_name/js";
			
// 			$dpath_StyleSheet = "/WS/WS_Others/free/UH8G6E_CE/$session_name/css";
		
// 			$dpath_ProjectRoot = "/WS/WS_Others/free/UH8G6E_CE";
			
// 		}//if ($hostname == "iwabuchiken-PC")
		
// 		// js file path
// // 		$version = "1~";
		
// 		$fname_JS = "main.($version).js";
		
// 		$fpath_JS = "$dpath_JavaScript/$fname_JS";
	
// 		// css file path
// 		$fname_CSS = "main.($version).css";
		
// 		$fpath_CSS = "$dpath_StyleSheet/$fname_CSS";
	
		
	?>

	<script type="text/javascript" src="<?php echo $fpath_JS; ?>">
		</script>
		
	<link rel="stylesheet" type="text/css" href="<?php echo $fpath_CSS; ?>" />
	
</head>


<body>

<div id="div_canvas-container" style="width: 800px; height: 300px;">

    <canvas id="canvas-container" width="100%" height="100%"></canvas>
    
</div>
<br>
	
yes

<br>

<div id="message_area">


</div>

<br>
<button onclick="stop_Count();" id="stop">Stop</button>
<!-- ref disabled http://qiita.com/pugiemonn/items/5db6fb8fd8a303406b17 -->
<button onclick="start_Count();" id="start" disabled="true">Start</button>

<hr>
<a
	href="<?php echo $dpath_ProjectRoot; ?>"
	target="_blank"
	>
	project root
</a>

</body>

</html>
