<!-- 

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 

C:\WORKS_2\WS\WS_Others\free\
C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\

/WS/WS_Others/free/UH8G6E_CE/

-->
<?php 

	require 'setup.php';
// 	require_once 'setup.php';

?>

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    
    <title><?php echo $session; ?> (<?php echo $version; ?>)</title>
<!--     <title>rect select</title> -->

	<link rel="stylesheet" type="text/css" href="<?php echo $fpath_CSS; ?>" />

	<script type="text/javascript" src="<?php echo $fpath_JS; ?>">
		</script>
		
</head>
<body>
	
	<div id="div_message">
		
		<?php 
		
// 			echo "\$fpath_CSS : " . $fpath_CSS;
			
// 			echo "<br>"; 
			
// 			echo "\$fpath_JS_2" . $fpath_JS_2;
		
		?>
	
	</div><!-- <div id="div_message"> -->
	
    <div class="main">
<!--         <canvas id="drowing" class="drowing" width="300px" height="300px"></canvas> -->
<!--         <canvas id="drowing" class="drowing" width="50%" height="0"></canvas> -->
        <canvas id="drowing" class="drowing" width="0" height="0"></canvas>
    </div>
    <div>
        <div>zキーで最新の矩形を削除</div>
    </div>
</body>
</html>