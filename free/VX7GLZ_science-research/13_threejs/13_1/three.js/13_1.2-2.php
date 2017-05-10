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

	require 'libs.php';	//=> C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\13_threejs\13_1\three.js\libs.php
		// 	$page_root
		// 	$font_size
		// 	$script_src

?>

<body>

	<a href="
		
			<?php echo $page_root?>
		
		">
		<!-- 		ref https://www.w3schools.com/tags/tag_font.asp -->
			<font size="<?php echo $font_size; ?>">Back</font>
	</a>
	
	<hr>

	<!-- ref https://html5experts.jp/yomotsu/5225/ -->
	<script src=<?php echo $script_src; ?>></script>
	
	<script src=<?php echo $page_root."/js/13_1.2-2.js"; ?>></script>

	<div id="container"></div>
	
</body>

</html>