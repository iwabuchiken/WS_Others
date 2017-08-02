<!-- 

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 


C:\WORKS_2\WS\WS_Others\free\
C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\

/WS/WS_Others/free/UH8G6E_CE/

-->
<?php 

	$session = "1_1";
	
	$version = "1.1~";
	
	$CE_Prefix = "1_X";
	
	$name_Project = "2R2TQN_AI";
	
	$hostname = gethostname();
	
	$dpath_JavaScript = "";
	$dpath_StyleSheet = "";
	
	$dpath_Images = "";
	
	$dpath_ProjectRoot = "";
	
	$session_name = $session;
	
	$dpath_Main_PHP = "";
	
	$fname_Main_PHP = "main.($version).php";
	
	$dpath_Session_Root = "";
	
	if ($hostname == "iwabuchiken-PC") {
			
		$dpath_ProjectRoot = "/WS_Others/free/$name_Project";
		
	} else {
			
		$dpath_ProjectRoot = "/WS/WS_Others/free/$name_Project";
		
	}//if ($hostname == "iwabuchiken-PC")

	$dpath_JavaScript = "$dpath_ProjectRoot/$CE_Prefix/$session_name/js";
	
	$dpath_StyleSheet = "$dpath_ProjectRoot/$CE_Prefix/$session_name/css";
		
	$dpath_Images = "$dpath_ProjectRoot/$CE_Prefix/$session_name/img";
	
	$fname_JS = "main.($version).js";
	
	$fpath_JS = "$dpath_JavaScript/$fname_JS";

	// css file path
	$fname_CSS = "main.($version).css";
	
	$fpath_CSS = "$dpath_StyleSheet/$fname_CSS";

	// main.php
	$dpath_Main_PHP = "$dpath_ProjectRoot/$session_name/$fname_Main_PHP";

	// session root
	$dpath_Session_Root = "$dpath_ProjectRoot/$session_name";
	
?>

