<!-- 

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 

C:\WORKS_2\WS\WS_Others\free\
/WS/WS_Others/free/UH8G6E_CE/

-->
<?php 

	require 'setup.php';
// 	require_once 'setup.php';

// 	$session = "4_1";
// 	$version = "1~";

?>

<!DOCTYPE html>
<html lang="ja">
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

	<script type="text/javascript" src="<?php echo $fpath_JS_2; ?>">
		</script>
		
	<link rel="stylesheet" type="text/css" href="<?php echo $fpath_CSS; ?>" />

<!--     <meta charset="UTF-8"> -->
<!--     <title>rect select</title> -->
    
    
</head>
<body>
    <div class="main">
        <canvas id="drowing" class="drowing" width="0" height="0"></canvas>
    </div>
    <div>
        <div>zキーで最新の矩形を削除</div>
    </div>
</body>
</html>
