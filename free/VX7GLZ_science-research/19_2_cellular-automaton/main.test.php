<!-- 

C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\19_2_cellular-automaton\main.php
C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\19_2_cellular-automaton
C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research

/WS/WS_Others/free/VX7GLZ_science-research/19_2_cellular-automaton

 -->

<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<!-- ref C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\13_threejs\13_1\sample (1)\index.html -->
<!-- 	<meta name="viewport" content="width=device-width"> -->

<meta name="viewport" content="minimum-scale=0.5">

<?php 

	$dpath = dirname($_SERVER["REQUEST_URI"]);
	
	$fname_css = "main.css";
	
	$fpath_css = $dpath."/".$fname_css;
	
	$fname_js = "main.js";
	$fpath_js = $dpath."/".$fname_js;
	
	$fname_jquery = "jquery-3.2.1.min.js";
	$fpath_jquery = $dpath."/".$fname_jquery;
	

?>

<!-- ref http://www.htmq.com/csskihon/004.shtml -->
<link rel="stylesheet" type="text/css" href='<?php echo $fpath_css;?>'>

<script type="text/javascript" src='<?php echo $fpath_js;?>'></script>

<script type="text/javascript" src='<?php echo $fpath_jquery;?>'></script>


<title>automaton</title>


</head>
<body>

	<input type="button" value="abc" id="btn_update" onclick="update_table();">
	

	<div id="div_main">
	
		<table border="1" id="table_main">

			<?php 
						
				$size = array(5, 5);
// 				$size = [5, 5];
							
			?>
		
		</table>
	
	
	</div>	
</body>
