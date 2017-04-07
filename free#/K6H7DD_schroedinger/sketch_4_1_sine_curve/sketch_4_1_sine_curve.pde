/*
  file:  C:\WORKS_2\WS\WS_Others\free#\K6H7DD_schroedinger\sketch_4_1_sine_curve\sketch_4_1_sine_curve.pde
  
  created at: 2017/04/07 15:15:29
  
  <usage>
    
*/

/**********************************
    constants
**********************************/
static final int TYPE_SERIAL      = 1;
static final int TYPE_FORMATTED    = 2;

static int STROKE    = 1;

static final int GRID_UNIT    = 100;

color yellow = color(255, 255, 0);
color yellow_dark = color(120, 120, 0);

color green = color(0, 120, 0);


static int DOT_RADIUS  = 4;  // dot in the curve

/******************************************

  variables

******************************************/
float[] yvalues;  // Using an array to store height values for the wave

int r = 4;    //=> plotting object, the radius thereof

PrintWriter output;

StackTraceElement stack;

String fname_id;
int i;  // iterator

float amplitude = 75.0;

// unit for sin(x) modulation
//float dx = TWO_PI / 200;
float dx;

/******************************************

  functions

******************************************/
void setup() {
  
  size(800, 600);

  // resizable
  //ref https://forum.processing.org/one/topic/is-there-a-way-to-resize-the-display-window-during-the-program-execution.html
  surface.setResizable(true);

  // init -->  yvalues
  yvalues = new float[width/r];

  /*
      init variables
  */
  _setup__InitVars();
  
  //// id
  //fname_id = get_time_label__Now(TYPE_SERIAL);  
  
}

void draw() {
  background(0);
  //background(255);

  /******************
    key listener
  ******************/
  _draw__KeyListener();
  
  /******************
    bg lines
  ******************/
  _draw__BgLines();
  
  // text
  _draw__ShowMessage();
  
  calcWave();
  renderWave();
  
  //// bg lines
  //_draw__BgLines();
  
  //saveFrame("images" + "/" + "frame" + "." + fname_id + "." + "####.tif");
  //saveFrame("images" + "_" + fname_id + "/" + "frame" + "." + fname_id + "." + "####.tif");

  //if(frameCount > 500) { // 20 seconds * 25 fps = 500
  ////if(frameCount > 100) { // 20 seconds * 25 fps = 500
  //  noLoop();
  //}

  
}

void calcWave() {

}

void renderWave() {

}


/***************************************
  String get_time_label__Now(int type)
  
  @original location: C:\WORKS_2\WS\WS_Processing\1#\sketch_1_1_20161227_114338\sketch_1_1_20161227_114338.pde
  @created-at: 2016/12/27 13:39:04
  @use variables:
    static final int TYPE_SERIAL      = 1;
    static final int TYPE_FORMATTED    = 2;
  @return
  TYPE_SERIAL       => serial      20161227_131300
  TYPE_FORMATTED    => formatted   2016/12/27 13:13:00
***************************************/
String get_time_label__Now(int type) {

  String label;
  
  switch(type) {
   
    case 1:
    
      label = nf(year(),4) + nf(month(),2) + nf(day(),2)
                
                + "_"
      
                + nf(hour(),2) + nf(minute(),2) + nf(second(),2);
    
      break;
    
    case 2:
    
      label = nf(year(),4) + "/" + nf(month(),2) + "/" + nf(day(),2)
                
                + " "
      
                + nf(hour(),2)  + ":" + nf(minute(),2) + ":" + nf(second(),2);
    
      break;
      
    default:
    
      label = nf(year(),4) + nf(month(),2) + nf(day(),2)
            
            + "_"
  
            + nf(hour(),2) + nf(minute(),2) + nf(second(),2);
    
      break;

  }
  
      // return
      return label;
     
}//get_time_label__Now(int type)

void _draw__BgLines() {
  
  // horizontal, center
  //fill(yellow);
  //fill(255,255,0);
  
  // thichkness
  strokeWeight(4);

  /*****************************
      prep
  *****************************/
  //int unit = height/4;
  int unit = GRID_UNIT;
  
  int ans = (width / 2) / unit;

  /*****************************
      horizontals: sub
  *****************************/
  // hori upper
  stroke(yellow_dark);
  //line(0, height/4, width, height/4);  
  //// hori lower
  //line(0, height*3/4, width, height*3/4);  

  for(i = 1; i <= ans; i++) {
   
    line(0, height/2 - unit * i, width, height/2 - unit * i);
    line(0, height/2 - unit * (-i), width, height/2 - unit * (-i));
    
    //line(width/2 - unit * (-i), 0, width/2 - unit * (-i), height);
    
  }

  /*****************************
      verticals: sub
  *****************************/
  ////debug
  //textSize(32);
  //text("ans => " + ans, 10, 30);

  // vertical left
  //line(width/2 - unit, 0, width/2 - unit, height);
  
  for(i = 1; i <= ans; i++) {
   
    line(width/2 - unit * i, 0, width/2 - unit * i, height);
    
    line(width/2 - unit * (-i), 0, width/2 - unit * (-i), height);
    
  }

  /*****************************
      mains
  *****************************/
  //ref http://labs.uechoco.com/blog/2008/02/processing_4.html
  stroke(yellow);

  // horizontal center
  line(0, height/2, width, height/2);

  // vertical center
  line(width/2, 0, width/2, height);

}//_draw__BgLines()

void _draw__ShowMessage() {

  //ref https://processing.org/reference/text_.html
  textSize(32);
  //text("word", 10, 30);
  text(width + "," + height, 10, 30);

}//_draw__ShowMessage()

void _draw__KeyListener() {

  //ref https://processing.org/reference/key.html
  if (keyPressed) {
    if (key == 'q' || key == 'Q') {
      
      exit();
      
    //} else if (key == 'a' || key == 'A') {
      
    //  diff -= diff_unit;
      
    //  // set the flag
    //  flag_diff = true;
      
    //} else if (key == 'd' || key == 'D') {
      
    //  diff += diff_unit;

    //  // set the flag
    //  flag_diff = true;

    }//if (key == 'q' || key == 'Q') {
    
  } else {
    
    //fill(255);
    
  }
  
}//_draw__KeyListener()

void _setup__InitVars() {

  // stack
  stack = new Throwable().getStackTrace()[0];  //=> 'sketch_4_1_sine_curve'

  // file io
  // file writer
  //ref https://processing.org/reference/createWriter_.html
  output = createWriter("data/positions.txt"); 

  ////output.println("dx => " + dx + " / " + "yvalues => " + yvalues.length); // Write the coordinate to the file
  //output.println(
  //            "[" + stack.getFileName() + ":" + stack.getLineNumber() + "]"
  //            + " / " + "yvalues => " + yvalues.length
  //            //+ " / " + "file => " + stack.getClassName()
  //  );
  
  //output.flush();
  output.close();

  // id
  fname_id = get_time_label__Now(TYPE_SERIAL);  

  // dx
  dx = TWO_PI / (width / 4);
  
}//_setup__InitVars(