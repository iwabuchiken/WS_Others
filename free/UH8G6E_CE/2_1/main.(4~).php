<!-- 

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 

-->
<!doctype html>
<head>
	<meta charset="utf-8">
	<meta name="author" content="" />
	<meta name="viewport" content="width=device-width">
	
	<title>3</title>


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
	
		$hostname = gethostname();
		
		$dpath_JavaScript = "";
		$dpath_StyleSheet = "";
		
		if ($hostname == "iwabuchiken-PC") {
				
			$dpath_JavaScript = "/WS_Others/free/UH8G6E_CE/2_1/js";

			$dpath_StyleSheet = "/WS_Others/free/UH8G6E_CE/2_1/css";
				
		} else {
				
			$dpath_JavaScript ="/WS/WS_Others/free/UH8G6E_CE/2_1/js";
			
			$dpath_StyleSheet = "/WS/WS_Others/free/UH8G6E_CE/2_1/css";
		
		}//if ($hostname == "iwabuchiken-PC")
		
		// js file path
		$fname_JS = "main.(4~).js";
		
		$fpath_JS = "$dpath_JavaScript/$fname_JS";
	
		// css file path
		$fname_CSS = "main.(4~).css";
		
		$fpath_CSS = "$dpath_StyleSheet/$fname_CSS";
	
		
	?>

	<script type="text/javascript" src="<?php echo $fpath_JS; ?>">
		</script>
		
	<link rel="stylesheet" type="text/css" href="<?php echo $fpath_CSS; ?>" />
	
</head>


<body>

    <canvas id="canvas_area" style="width: 800px; height: 300px;" width="800" height="300"></canvas>
<!--     <canvas id="canvas" style="width: 800px; height: 300px;" width="800" height="300"></canvas> -->

<br>
	
yes

<button onclick="stop_Count();" id="stop">Stop</button>
<!-- ref disabled http://qiita.com/pugiemonn/items/5db6fb8fd8a303406b17 -->
<button onclick="start_Count();" id="start" disabled="true">Start</button>

</body>

</html>
