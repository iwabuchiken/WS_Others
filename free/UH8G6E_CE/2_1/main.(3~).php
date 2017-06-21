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
		
		if ($hostname == "iwabuchiken-PC") {
				
			$dpath_JavaScript = "/WS_Others/free/UH8G6E_CE/2_1/js";
// 			$root_JavaScript = "/WS_Others/free/UH8G6E_CE/2_1/js/main.js";
				
		} else {
				
			$dpath_JavaScript ="/WS/WS_Others/free/UH8G6E_CE/2_1/js";
		
		}//if ($hostname == "iwabuchiken-PC")
		
		// js file path
		$fname_JS = "main.(3~).js";
		
		$fpath_JS = "$dpath_JavaScript/$fname_JS";
	
		
	?>

	<script type="text/javascript" src="<?php echo $fpath_JS; ?>">
		</script>
		
</head>


<body>

    <canvas id="canvas-container" style="width: 800px; height: 300px;" width="800" height="300"></canvas>

	
yes

</body>

</html>
