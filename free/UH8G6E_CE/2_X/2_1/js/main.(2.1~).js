/*
 * regex expression
 * 
^([^\/](.|\t)+)alert

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 

C:\WORKS_2\WS\WS_Others\free\
C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\

/WS/WS_Others/free/UH8G6E_CE/


 */

/*
 * ref http://symfoware.blog68.fc2.com/blog-entry-1958.html
 */

//alert("js starting...");

function window_OnLoad() {
	
	alert("loaded");
	
	window.addEventListener("load", function () {
		 
		    //仮想物理実験室オブジェクトの生成
		    PHYSICS.physLab = new PHYSICS.PhysLab({
		        //必須パラメータ
		        frameID : "canvas-frame", //額縁を表す要素のid名
		    });
		 
		    // 軸オブジェクトの準備
		    PHYSICS.physLab.objects[ 0 ] = new PHYSICS.Axis( );
	
	//			alert("lab starting...");
			
		    //ref view-source:http://www.natural-science.or.jp/physics.js/physics.js_r14/example/ball.html
	    	////////////////////////////////////////////////////////////////////
			// 床オブジェクトの準備
			////////////////////////////////////////////////////////////////////
			PHYSICS.physLab.floor = new PHYSICS.Floor({
				dynamic : false,        //運動の有無
				draggable: false,       //マウスドラックの有無
				allowDrag : false,      //マウスドラックの可否
				collision: true,        //衝突判定の有無
				position: {x:0, y:0, z:0},
				boundingBox : {
					visible : false,     //バウンディングボックスの可視化
					color : 0xFF0000,   //バウンディングボックスの色
				},
				width : 20,                //横幅
				height :20,                //縦幅
				material : {
					type : "Phong",      //材質の種類
					receiveShadow : true,  //影の描画
					specular:0x080808,
					shininess:100
				}
		 	})
			//床オブジェクトを登場
			PHYSICS.physLab.objects.push( PHYSICS.physLab.floor );
		    
		    
		    //仮想物理実験室のスタートメソッドの実行
		    PHYSICS.physLab.startLab();
	
		    
		}//function () {
	);

	
}//window_OnLoad();

window.onload = function() {
	
	window_OnLoad();
    
};
