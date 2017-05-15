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

	<!-- ref https://techacademy.jp/magazine/5537 -->
	<script>

// 		var id = self.setInterval(update_table, 1000);
//       var count = 0;
//       var countup = function(){
//         console.log(count++);
//       } 

//       setInterval(countup, 1000);
//       var id = setInterval(countup, 1000);
//       var id = self.setInterval(countup, 1000);
//       var id = self.setInterval("countup", 1000);
      
    </script>

	<!-- ref http://stackoverflow.com/questions/3138756/calling-a-function-every-60-seconds answered Jun 29 '10 at 7:44 -->
	<script>
	
// 		var interval = self.setInterval(update_table(), 1000);
// 		var int=self.setInterval(update_table(), 1000);
// 		var int=self.setInterval(update_table(), 60000);
		
	</script>

	<input type="button" value="abc" id="btn_update" onclick="update_table();">
	
	<?php echo "<br>"; echo "<br>";
	
	?>
	
	<!-- ref http://stackoverflow.com/questions/3138756/calling-a-function-every-60-seconds answered Jun 29 '10 at 7:44 -->
	<!-- Stop Button -->
	<a href="#" onclick="alert('stop'); window.clearInterval(id);return false;">Stop</a>
	<!-- <a href="#" onclick="window.clearInterval(id);return false;">Stop</a> -->
	<!-- <a href="#" onclick="window.clearInterval(id);return false;">Stop</a> -->
	<!-- <a href="#" onclick="window.clearInterval(countup);return false;">Stop</a> -->
	<?php echo "<br>"; echo "<br>";
	
	?>

	<div id="div_main">
	
		<table border="1" id="table_main">
		
			<?php 
			
// 				$size = [5, 5];
				$size = array(5, 5);
			
				for ($i = 0; $i < $size[0]; $i++) {
					
					echo "<tr>";
					
					for ($j = 0; $j < $size[1]; $j++) {
						
						if ($i * $j % 2 == 0) {
						
							echo "<td class='td_even'>";
							
							echo $i * $j;
							
							echo "</td>";
						
						} else {
						
							echo "<td class='td_odd'>";
								
							echo $i * $j;
								
							echo "</td>";
							
						}//if ($i * $j / 2 == 0)
						
						
						
// 						echo "<td>";
						
// 							echo $i * $j;
						
// 						echo "</td>";
					}
				
				
					echo "</tr>";
					
				}
			
			
			?>
		
		</table>

	</div>
	
</body>
