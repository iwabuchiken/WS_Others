/*
 * ref http://symfoware.blog68.fc2.com/blog-entry-1958.html
 */

//alert("js starting...");

/***************************
	@param
		(4, 5)	=> [4, 0]
		(5, 4)	=> [4, 1]
 ***************************/
function smaller(x, y) {
	
	if (x <= y) {
//		if (x >= y) {

		return [x, 0];

	} else {

		return [y, 1];;

	}//if (x >= y)
	
}//function smaller(x, y) {

/***************************
	@param
		[4, 5]	=> [4, 0]
		[5, 4]	=> [4, 1]
 ***************************/
function smaller_InArray(aryOf_Two_Numbers) {
	
	/***************************
		validate
	 ***************************/
	if (aryOf_Two_Numbers.length < 1) {

		alert("smaller_InArray : array size less than 1");
		
		return null;

	}//if (aryOf_Two_Numbers.length) {

	/***************************
		operations
	 ***************************/
	if (aryOf_Two_Numbers[0] <= aryOf_Two_Numbers[1]) {
//		if (aryOf_Two_Numbers[0] >= aryOf_Two_Numbers[1]) {
		
		return [aryOf_Two_Numbers[0], 0];
		
	} else {
		
		return [aryOf_Two_Numbers[1], 1];;
		
	}//if (x >= y)
	
}//function smaller(x, y) {

function window_OnLoad() {

	//debug
	alert("starting...");
	
    var canvas = document.getElementById('drowing');
    var context = canvas.getContext('2d');
    var reacts = [];
    
    var imageObj = new Image();
    
    imageObj.onload = function() {
    	
//        canvas.width = window.innerWidth / 2;
        canvas.width = window.innerWidth;
//      canvas.width = window.innerWidth;;
//      canvas.width = imageObj.width;
     canvas.height = window.innerHeight / 2;
//      canvas.height = imageObj.height / 2;
//      canvas.height = imageObj.height;

     
     //test
     var size_Window = [window.innerWidth, window.innerHeight];
     
     alert("size_Window => " + size_Window);
     
     var labelsFor_Size_Window = ["width", "height"];
     
     var res = smaller_InArray(size_Window);
     
     alert("smaller_InArray => done");
     
     alert(res);
     
     // validate
     if (res == null) {

		alert("smaller_InArray => returned null; quitting...");

		return;
		
	}//if (res == null) {
	
//     var res = smaller(window.innerWidth, window.innerHeight);
     
     alert("window size : smaller => "
    		 + res[0]
//    		 + " / "
    		 + "("
    		 + labelsFor_Size_Window[res[1]]
//    		 + (res[1] == 0 ? "width" : "height")
    		 + ")"
    		 
//    		 + " / "
//    		 + "larger is => "
//    		 + (res[1] == 0 ? "height" : "width")
//    		 + "("
//    		 + (res[1] == 0 ? "width" : "height")
//    		 + ")"
     );
     
     
    	
//        canvas.width = imageObj.width;
//        canvas.height = imageObj.height;
    	
        draw();
    };
    imageObj.src = 'http://benfranklin.chips.jp/cake_apps/images/ifm11/2014-08-12_12-17-13_686.jpg';
//     imageObj.src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Hannibal_Poenaru_-_Nasty_cat_%21_%28by-sa%29.jpg/270px-Hannibal_Poenaru_-_Nasty_cat_%21_%28by-sa%29.jpg';
//     imageObj.src = 'sample2_image.jpg';
    
    canvas.addEventListener("mousedown", onMouseDown, false);
    canvas.addEventListener("mouseup" , onMouseUp , false);
    window.addEventListener("keyup" , onKeyUp , false);
    
    // 矩形オブジェクト
    var _rectangle = createRect();
    
    function createRect() {
        return { startY:0, startX:0, endY:0, endX:0 };
    };
    
    function onMouseDown (e) {
        _rectangle.startY = e.clientY;
        _rectangle.startX = e.clientX;
        canvas.addEventListener ("mousemove", onMouseMove, false);
    };
    function onMouseMove (e) {
        draw();
        _rectangle.endY = e.layerY - _rectangle.startY;
        _rectangle.endX = e.layerX - _rectangle.startX;
        context.lineWidth = 5;
        context.strokeStyle = "rgb(255, 0, 0)";
        context.strokeRect (_rectangle.startX, _rectangle.startY, _rectangle.endX, _rectangle.endY);
    };
    function onMouseUp (e) {
        reacts.push(_rectangle);
        draw();
        _rectangle = createRect();
        canvas.removeEventListener ("mousemove", onMouseMove, false);
    };
    
    function draw() {
    	
//    	alert(
//    			"canvas : width => " + canvas.width
//    			+ " / "
//    			+ "height => " + canvas.height
//    			
//    			+ " || "
//    			
//    			+ "window : width => " + window.innerWidth
//    			+ " / "
//    			+ "window : height => " + window.innerHeight
//    			
//    			
////    			"image file : width => " + imageObj.width
////    			+ " / "
////    			+ "height => " + imageObj.height
//		);
    	
    	// ref http://www.html5.jp/canvas/how6.html '画像をトリミングしてみましょう'
    	context.drawImage(imageObj, 0, 0, canvas.width, canvas.height);
//        context.drawImage(imageObj, 0, 0, this.width, this.height);
//        context.drawImage(imageObj, 0, 0);
        
        context.lineWidth = 5;
        context.strokeStyle = "rgb(255, 0, 0)";
        
        reacts.forEach(function(rect) {
        	
            context.strokeRect(rect.startX, rect.startY, rect.endX, rect.endY);
            
        });
        
    };
    
    function onKeyUp (e) {
        switch(e.key) {
            case 'z':
                reacts.pop();
                break;
            default:
                return;
        };
        draw();
    };

}//window_OnLoad

window.onload = function() {
	
	window_OnLoad();
    
};
