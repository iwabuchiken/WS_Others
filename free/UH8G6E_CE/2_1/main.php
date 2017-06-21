<!-- 

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 

-->
<!doctype html>
<head>
	<meta charset="utf-8">
	<meta name="author" content="" />
	<meta name="viewport" content="width=device-width">
	
	<title>2_1</title>

	<?php 
	
		$hostname = gethostname();
		
		$dpath_JavaScript = "";
		
		if ($hostname == "iwabuchiken-PC") {
				
			$dpath_JavaScript = "/WS_Others/free/UH8G6E_CE/2_1/js";
// 			$root_JavaScript = "/WS_Others/free/UH8G6E_CE/2_1/js/main.js";
				
		} else {
				
			$dpath_JavaScript ="/WS/WS_Others/free/UH8G6E_CE/2_1/js";
		
		}//if ($hostname == "iwabuchiken-PC")
		
		// js file path
		$fname_JS = "main.js";
		
		$fpath_JS = "$dpath_JavaScript/$fname_JS";
		
		$fname_JQ_UI = "jquery-ui.js";
		
		$fpath_JQ_UI = "$dpath_JavaScript/$fname_JQ_UI";
	
	?>

	<!-- https://code.jquery.com/jquery/ -->
	<script
	  src="https://code.jquery.com/jquery-3.2.1.min.js"
	  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
	  crossorigin="anonymous"></script>

<!-- 	<script type="text/javascript" src="http://code.jquery.com/jquery-1.10.2.min.js"></script> -->
<!-- 	<script type="text/javascript" src="/cake_apps/Cake_IFM11/js/jquery-ui.js"> -->
	
	<script
	  src="https://code.jquery.com/ui/1.12.0/jquery-ui.min.js"
	  integrity="sha256-eGE6blurk5sHj+rmkfsGYeKyZx3M4bG+ZlFyA7Kns7E="
	  crossorigin="anonymous"></script>
	<!-- <script type="text/javascript" src="<?php echo $fpath_JQ_UI; ?>"></script> -->
	
	<script type="text/javascript" src="<?php echo $fpath_JS; ?>">
	</script>
	
	
</head>

<body>
yes

<br>

<button onclick="draw_Circle()">Draw circle</button>
<!-- <button onclick="alert_message()">Show message</button> -->

	<canvas id="canvas-container" width="600" height="300"></canvas>


</body>

</html>
