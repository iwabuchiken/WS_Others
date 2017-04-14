/*
  file:  C:\WORKS_2\WS\WS_Others\free#\K6H7DD_schroedinger\sketch_6_1_sine_curve\sketch_6_1_sine_curve.pde
  
  created at: 2017/04/11 17:41:30
  
  <usage>
    
*/

import java.io.FileWriter;

/**********************************
    constants
**********************************/
static final int TYPE_SERIAL      = 1;
static final int TYPE_FORMATTED    = 2;

static int STROKE    = 1;

static final int GRID_UNIT    = 100;

color white = color(255, 255, 255);

color yellow = color(255, 255, 0);
color yellow_dark = color(10, 120, 0);
color yellow_lower = color(120,120,0);

color green = color(0, 120, 0);
color green_light = color(0, 255, 0);

//color purple_light = color(100,0,100);
color purple_light = color(200,0,200);

color red_light = color(255, 140, 140);

static int DOT_RADIUS  = 4;  // dot in the curve

static final int delay_chattering = 200;
//static final int delay_pause      = 300;
static final int delay_pause      = 30;

final int stop_number      = 125;

/******************************************

  variables

******************************************/
float[] yvalues;  // Using an array to store height values for the wave
float[] yvalues_2;
float[] yvalues_3;
float[] yvalues_aggre;    // sin + cos
float[] yvalues_aggre_2;  // sin + cos + aggre


int r = 4;    //=> plotting object, the radius thereof

PrintWriter output;

//ref https://forum.processing.org/two/discussion/561/easiest-way-to-append-to-a-file-in-processing
FileWriter out;

StackTraceElement stack;

String fname_id;
int i;  // iterator

float amplitude = 75.0;

// unit for sin(x) modulation
//float dx = TWO_PI / 200;
float dx;

// dx denominator
//int dx_denomi = 8;
int dx_denomi = 10;
int denomi_addition = 1;

int turning_point = 30;

// draw cycle count
int cnt_draw = 0;

//test
//ref http://stackoverflow.com/questions/41710079/imports-in-processing answered Jan 23 at 1:46
Button bt = new Button();

/*
  phase-related
*/
float phase_2 = TWO_PI / 8;

/*
  others
*/
int frame_number = 1;


/******************************************

  functions

******************************************/
void setup() {
  
  size(800, 600);

  // resizable
  //ref https://forum.processing.org/one/topic/is-there-a-way-to-resize-the-display-window-during-the-program-execution.html
  surface.setResizable(true);

  // init -->  yvalues
  yvalues        = new float[width/r];
  yvalues_2    = new float[width/r];
  yvalues_3    = new float[width/r];
  yvalues_aggre  = new float[width/r];
  yvalues_aggre_2  = new float[width/r];

  /*
      init variables
  */
  _setup__InitVars();
  
  //// id
  //fname_id = get_time_label__Now(TYPE_SERIAL);  

  /*
      wave-related
  */
  //calcWave();
  //renderWave();

  /*
    test
  */
  //Button bt = new Button();


}//setup()

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

  /*
      delay
  */
  
  delay(100);

  /**********************
    change phase values
  **********************/
  phase_2 -= 0.1;
  
  if (phase_2 < -5) phase_2 = 5;

  ///**********************
  //  save image
  //**********************/
  saveFrame("images" + "_" + fname_id + "/" + "frame" + "." + fname_id + "." + "####.tif");

  ///**********************
  //  stop
  //**********************/
  //cnt_draw ++;
  
  ////if (cnt_draw > (turning_point * 2 + 2)) {
  //  if (cnt_draw > (turning_point * 4 + 2)) {
   
  //  noLoop();
    
  //}

  /**********************
    increment ---> frame numberq
  **********************/
  frame_number ++;


  /**********************
    save frame
  **********************/
  //saveFrame("images" + "_" + fname_id + "/" + "frame" + "." + fname_id + "." + "####.tif");
  
  /**********************
    stop
  **********************/
  if (frame_number > (stop_number)) {
   
    noLoop();
    
  }
  
  /**********************
    pause
  **********************/
  delay(delay_pause);
  
}//void draw() {

void calcWave() {

  /**********************
      update denominator
  **********************/
  dx = TWO_PI / (width / dx_denomi);
  
  /**********************
      calculate
  **********************/
  float x = 0.0;
  
  // calc --> yvalues
  for (int i = 0; i < yvalues.length; i++) {

    yvalues[i] = sin(x)*amplitude;
    
    //yvalues_cos[i] = cos(x)*amplitude;
    //yvalues_cos[i] = cos(x + phase_2)*amplitude;
    yvalues_2[i] = sin(x + phase_2)*amplitude;
    
    yvalues_3[i] = sin(x * phase_2)*amplitude;

    //yvalues_aggre[i] = yvalues[i] + yvalues_2[i];
    yvalues_aggre[i] = yvalues[i] + yvalues_2[i] + yvalues_3[i];
    
    //yvalues_aggre_2[i] = yvalues[i] + yvalues_2[i] + yvalues_aggre[i];

    x+=dx;

  }

  ///**********************
  //    update: denomi
  //**********************/
  //// change denominator
  ////if(dx_denomi > 20) {
  //  if(dx_denomi > turning_point) {

  //  denomi_addition = -1;
    
  ////} else if (dx_denomi < -20) {
  //  } else if (dx_denomi < -turning_point) {
    
  //  denomi_addition = 1;
    
  //}

  //dx_denomi += denomi_addition;
  
  //if(dx_denomi == 0) dx_denomi += denomi_addition;
    

  
      
  // validate
  //if(dx_denomi == 0) dx_denomi = -1;


  ///*
  //  debug: yvalues ---> write to a file
  //*/
  //try{
    
  //  //File fout = new File("data" + "/log" + get_time_label__Now(TYPE_SERIAL) + ".txt");
  //  File fout = new File("C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/sketch_4_1_sine_curve/data"
  //                + "/log." + get_time_label__Now(TYPE_SERIAL) + ".txt");
    
  //  if(fout.exists()) {
      
  //    //out = new FileWriter("data" + "/log" + get_time_label__Now(TYPE_SERIAL) + ".txt", true);
  //    out = new FileWriter(fout, true);
      
  //  } else {
      
  //    System.out.println("file doesn't exist");
      
  //    //out = new FileWriter("data" + "/log" + get_time_label__Now(TYPE_SERIAL) + ".txt");
      
  //    fout.createNewFile();
      
  //    out = new FileWriter(fout);
      
  //  }
    
  //  //out = new FileWriter("data" + "/log" + get_time_label__Now(TYPE_SERIAL) + ".txt", true);

  //  for (int i = 0; i < yvalues.length; i++) {

  //    out.write(i + "\t" + yvalues[i] + "\n");
  
  //  }//for (int i = 0; i < yvalues.length; i++)

  //  out.flush();
    
  //  out.close();

  //}
  //catch(IOException e) {

  //  e.printStackTrace();
    
  //}//try{
  

  
}//void calcWave()

void renderWave() {

  noStroke();
  fill(255);
  
  // A simple way to draw the wave with an ellipse at each location
  for (int x = 0; x < yvalues.length; x++) {

    /******************
      sine
    ******************/    
    fill(255);
    
    //ellipse(x*xspacing, height/2+yvalues[x], 16, 16);
    //ellipse(x*xspacing, height/2+yvalues[x], DOT_RADIUS, DOT_RADIUS);
    ellipse(x * r, height/2+yvalues[x], r, r);
    
    /******************
      cos
    ******************/
    fill(purple_light);
    
    ////ellipse(x*xspacing, height/2+yvalues[x], 16, 16);
    ////ellipse(x*xspacing, height/2+yvalues[x], DOT_RADIUS, DOT_RADIUS);
    ellipse(x * r, height/2 + yvalues_2[x], r, r);
    
    /******************
      yvalues_3
    ******************/
    fill(red_light);
    
    ////ellipse(x*xspacing, height/2+yvalues[x], 16, 16);
    ////ellipse(x*xspacing, height/2+yvalues[x], DOT_RADIUS, DOT_RADIUS);
    ellipse(x * r, height/2 + yvalues_3[x], r, r);
    
    /******************
      aggregate
    ******************/
    //fill(green);
    fill(green_light);
    
    //ellipse(x * r, height/2+yvalues_aggre[x], r, r);
    ellipse(x * r, height/2+yvalues_aggre[x], r + 3, r + 3);

    ///******************
    //  aggregate
    //******************/
    //fill(green_light);
    
    //ellipse(x * r, height/2+yvalues_aggre_2[x], r, r);

  }

  
}//void renderWave() {


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
  //stroke(yellow_dark);
  
  //fill(yellow_dark);
  
  //stroke(white);
  
  //stroke(yellow_dark);

  stroke(yellow_lower);
  
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

  fill(white);
  
  //ref https://processing.org/reference/text_.html
  textSize(32);
  //text("word", 10, 30);
  text(width + "," + height, 10, 30);
  
  ///*******************
  //    dx denominator
  //*******************/
  //text("dx denomi => " + dx_denomi, 10, 60);

  /*******************
      curves 
  *******************/
  //fill(255,255,255);
  fill(white);
  text("sine", 10, 90);

  fill(purple_light);
  //fill(red_light);
  //text("cosine", 10, 120);
  text("sin_2 (+ " + phase_2 + ")", 10, 120);

  fill(red_light);
  //text("cosine", 10, 120);
  text("sin_3 (* " + phase_2 + ")", 10, 150);

  fill(green_light);
  //fill(green);
  //fill(yellow);
  text("aggregate", 10, 180);

  /******************
    frame number
  ******************/
  fill(white);
  //fill(yellow);
  text("frame = " + frame_number, width - 250, 50);
  

  //fill(green_light);
  ////fill(yellow);
  //text("aggregate_2", 10, 150);

  // reset filling
  //fill(yellow);

  ////test
  ////text(bt.number, 10, 150);
  //text(Button.number, 10, 180);

}//_draw__ShowMessage()

void _draw__KeyListener() {

  //ref https://processing.org/reference/key.html
  if (keyPressed) {
    if (key == 'q' || key == 'Q') {
      
      exit();
      
    } else if (key == 'a' || key == 'A') {

      // decrement
      phase_2 -= 0.1;
      
      // delay
      delay(delay_chattering);
      
      //diff -= diff_unit;
      
      //// set the flag
      //flag_diff = true;
      
    } else if (key == 'd' || key == 'D') {
      
      // decrement
      phase_2 += 0.1;

      // delay
      delay(delay_chattering);

      //diff += diff_unit;

      //// set the flag
      //flag_diff = true;

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
  //fname_id = get_time_label__Now(TYPE_SERIAL);  
  fname_id = Utils.get_time_label__Now(TYPE_SERIAL);

  // dx
  //dx = TWO_PI / (width / 4);
  //dx = TWO_PI / (width / 8);
  dx = TWO_PI / (width / dx_denomi);
  
  //debug
  stack = new Throwable().getStackTrace()[0];
  
  System.out.println("[" + stack.getLineNumber() + "]" + " " + "dx => " + dx);
  
  
}//_setup__InitVars(