<!-- 

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 

-->
<?php 

	$session = "1_7";
	
	$version = "1.7~";
	
// 	$fname_JS_2 = "main.(3~).js";

?>

	<?php 
	
		$hostname = gethostname();
		
		$dpath_JavaScript = "";
		$dpath_StyleSheet = "";
		
		$dpath_ProjectRoot = "";
		
		$session_name = $session;
// 		$session_name = "3_1";
		
		$dpath_Main_PHP = "";
		
		$fname_Main_PHP = "main.($version).php";
		
		$dpath_Session_Root = "";
		
		if ($hostname == "iwabuchiken-PC") {
				
			$dpath_JavaScript = "/WS_Others/free/UH8G6E_CE/$session_name/js";

			$dpath_StyleSheet = "/WS_Others/free/UH8G6E_CE/$session_name/css";
			
			$dpath_ProjectRoot = "/WS_Others/free/UH8G6E_CE";
			
		} else {
				
			$dpath_JavaScript ="/WS/WS_Others/free/UH8G6E_CE/$session_name/js";
			
			$dpath_StyleSheet = "/WS/WS_Others/free/UH8G6E_CE/$session_name/css";
		
			$dpath_ProjectRoot = "/WS/WS_Others/free/UH8G6E_CE";
			
		}//if ($hostname == "iwabuchiken-PC")
		
		// js file path
// 		$version = "1~";
		
		$fname_JS = "main.($version).js";
		
		$fpath_JS = "$dpath_JavaScript/$fname_JS";

		// ref http://symfoware.blog68.fc2.com/blog-entry-1958.html
// 		$fpath_JS_2 = "$dpath_JavaScript/$fname_JS_2";
	
		// css file path
		$fname_CSS = "main.($version).css";
		
		$fpath_CSS = "$dpath_StyleSheet/$fname_CSS";

		// main.php
		$dpath_Main_PHP = "$dpath_ProjectRoot/$session_name/$fname_Main_PHP";

		// session root
		$dpath_Session_Root = "$dpath_ProjectRoot/$session_name";
		
	?>

