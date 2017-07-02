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


    
<script type="text/javascript">
// window.onload = function() {
//     var canvas = document.getElementById('drowing');
//     var context = canvas.getContext('2d');
//     var reacts = [];
    
//     var imageObj = new Image();
//     imageObj.onload = function() {

//         //ref https://stackoverflow.com/questions/1664785/resize-html5-canvas-to-fit-window 'answered Jun 20 '10 at 6:43'
//         canvas.width = window.innerWidth / 2;
// //         canvas.width = window.innerWidth;;
// //         canvas.width = imageObj.width;
//         canvas.height = window.innerHeight / 2;
// //         canvas.height = imageObj.height / 2;
// //         canvas.height = imageObj.height;
        
//         draw();
        
//     };
//     imageObj.src = 'http://benfranklin.chips.jp/cake_apps/images/ifm11/2014-08-12_12-17-13_686.jpg';
// //     imageObj.src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Hannibal_Poenaru_-_Nasty_cat_%21_%28by-sa%29.jpg/270px-Hannibal_Poenaru_-_Nasty_cat_%21_%28by-sa%29.jpg';
// //     imageObj.src = 'sample2_image.jpg';
    
//     canvas.addEventListener("mousedown", onMouseDown, false);
//     canvas.addEventListener("mouseup" , onMouseUp , false);
//     window.addEventListener("keyup" , onKeyUp , false);
    
//     // 矩形オブジェクト
//     var _rectangle = createRect();
    
//     function createRect() {
//         return { startY:0, startX:0, endY:0, endX:0 };
//     };
    
//     function onMouseDown (e) {
//         _rectangle.startY = e.clientY;
//         _rectangle.startX = e.clientX;
//         canvas.addEventListener ("mousemove", onMouseMove, false);
//     };
//     function onMouseMove (e) {
//         draw();
//         _rectangle.endY = e.layerY - _rectangle.startY;
//         _rectangle.endX = e.layerX - _rectangle.startX;
//         context.lineWidth = 5;
//         context.strokeStyle = "rgb(255, 0, 0)";
//         context.strokeRect (_rectangle.startX, _rectangle.startY, _rectangle.endX, _rectangle.endY);
//     };
//     function onMouseUp (e) {
//         reacts.push(_rectangle);
//         draw();
//         _rectangle = createRect();
//         canvas.removeEventListener ("mousemove", onMouseMove, false);
//     };
    
//     function draw() {
//         context.drawImage(imageObj, 0, 0);
//         context.lineWidth = 5;
//         context.strokeStyle = "rgb(255, 0, 0)";
//         reacts.forEach(function(rect) {
//             context.strokeRect(rect.startX, rect.startY, rect.endX, rect.endY);
//         });
//     };
    
//     function onKeyUp (e) {
//         switch(e.key) {
//             case 'z':
//                 reacts.pop();
//                 break;
//             default:
//                 return;
//         };
//         draw();
//     };
    
// };

</script>
    
</head>
<body>
	
	<div id="div_message">
		
		<?php 
		
			echo "\$fpath_CSS : " . $fpath_CSS;
			
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
