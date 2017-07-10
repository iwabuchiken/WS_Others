<!-- 

http://localhost/WS_Others/free/UH8G6E_CE/2_X/2_1/main.(2.1~).php 

C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\2_X\2_1\main.(2.1~).php

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

	<script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js">
		</script>
		
	<script type="text/javascript" src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js">
		</script>
		
	<link rel="stylesheet" type="text/css" href="<?php echo $fpath_CSS; ?>" />

	<script type="text/javascript" src="<?php echo $fpath_JS; ?>">
		</script>
		
	<script type="text/javascript" src="<?php echo "$dpath_JavaScript/three_r68.js"; ?>"></script>
	
	<script type="text/javascript" src="<?php echo "$dpath_JavaScript/TrackballControls_r68.js"; ?>"></script>
	
	<script type="text/javascript" src="<?php echo "$dpath_JavaScript/physics.js"; ?>"></script>

	<script type="text/javascript">

		window.addEventListener("load", function () {
			 
			    //仮想物理実験室オブジェクトの生成
			    PHYSICS.physLab = new PHYSICS.PhysLab({
			        //必須パラメータ
			        frameID : "canvas-frame", //額縁を表す要素のid名
			    });
			 
			    // 軸オブジェクトの準備
			    PHYSICS.physLab.objects[ 0 ] = new PHYSICS.Axis( );

// 				alert("lab starting...");
				 
			    //仮想物理実験室のスタートメソッドの実行
			    PHYSICS.physLab.startLab();

			    
			}//function () {
		);

	</script>
		
		
</head>
<body>

	<div id="canvas-frame"></div>
    
</body>
</html>
