<!-- 
http://localhost/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/ 
-->

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>three.js sample</title>
</head>

<?php 

	/*
	 * from : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\Lib\utils\utils.php
	 * at : 2017/05/09 17:52:02
	 */
// 	function
// 	get_HostName() {
			
// 		$pieces = parse_url(Router::url('/', true));
			
// 		return $pieces['host'];
			
// 	}//public function get_HostName()

	//ref http://php.net/manual/ja/reserved.variables.server.php
	$hostname = $_SERVER['SERVER_NAME'];
// 	$hostname = gethostname();
	
// 	echo "hostname => $hostname";
	
	if ($hostname == "localhost") {
	
		$script_src = "/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/three.min.js";
	
	} else {
	
		$script_src = "/WS/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/three.min.js";
	
	}
	
// 	$script_src = "";
	
	

?>

<body>

	<!-- ref https://html5experts.jp/yomotsu/5225/ -->
	<!-- <script src="three.min.js"></script> -->
	<script src=<?php echo $script_src; ?>></script>
<!-- 	<script src="/WS_Others/free/VX7GLZ_science-research/13_threejs/13_1/three.js/js/three.min.js"></script> -->
	
	<script>
	
		var main = function () {
		  // ここにあなたのコードを書いていきます
		  //alert("loaded");
		  
		  var scene = new THREE.Scene();
		  
		  var width  = 600;
		  var height = 400;
		  var fov    = 60;
		  var aspect = width / height;
		  var near   = 1;
		  var far    = 1000;
		  var camera = new THREE.PerspectiveCamera( fov, aspect, near, far );
		  camera.position.set( 0, 0, 50 );
		  
		  var renderer = new THREE.WebGLRenderer();
		  renderer.setSize( width, height );
		  document.body.appendChild( renderer.domElement );
		  
		  var directionalLight = new THREE.DirectionalLight( 0xffffff );
		  directionalLight.position.set( 0, 0.7, 0.7 );
		  scene.add( directionalLight );
		  
		  //var geometry = new THREE.CubeGeometry( 30, 30, 30 );
		  var geometry = new THREE.CubeGeometry( 30, 10, 30 );
		  var material = new THREE.MeshPhongMaterial( { color: 0xff0000 } );
		  var mesh = new THREE.Mesh( geometry, material );
		  scene.add( mesh );
		  
		  //renderer.render( scene, camera );
		  
		   ( function renderLoop () {
			    requestAnimationFrame( renderLoop );
			    mesh.rotation.set(
			      //0,
			      mesh.rotation.x + .01,
			      //0,
			      mesh.rotation.y + .01,
			      mesh.rotation.z + .01
			    );
			    renderer.render( scene, camera );
			  } )();
		  
		  
		};
		 
		window.addEventListener( 'DOMContentLoaded', main, false );
		
	</script>

</body>
</html>