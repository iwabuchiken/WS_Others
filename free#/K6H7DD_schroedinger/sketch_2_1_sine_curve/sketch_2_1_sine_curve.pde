/*
  file:  C:\WORKS_2\WS\WS_Others\free#\K6H7DD_schroedinger\sketch_2_1_sine_curve\sketch_2_1_sine_curve.pde
  
  created at: 2017/04/05 14:56:22
  
  <usage>
    
*/

/**********************************
    constants
**********************************/
static final int TYPE_SERIAL      = 1;
static final int TYPE_FORMATTED    = 2;

static int STROKE    = 1;

static final String  fname_trunk  = "2_1";  
static final String  fname_ext  = ".png";

/******************************************

  variables

******************************************/
int xspacing = 16;   // How far apart should each horizontal location be spaced
int w;              // Width of entire wave

float theta = 0.0;  // Start angle at 0
float amplitude = 75.0;  // Height of wave
float period = 500.0;  // How many pixels before the wave repeats
float dx;  // Value for incrementing X, a function of period and xspacing
float[] yvalues;  // Using an array to store height values for the wave


String fname_id;

/******************************************

  functions

******************************************/
void setup() {
  size(640, 360);
  w = width+16;
  dx = (TWO_PI / period) * xspacing;
  yvalues = new float[w/xspacing];
  
  
  // id
  fname_id = get_time_label__Now(TYPE_SERIAL);  
  
}

void draw() {
  background(0);
  calcWave();
  renderWave();
  
  //saveFrame("images" + "/" + "frame" + "." + fname_id + "." + "####.tif");
  saveFrame("images" + "_" + fname_id + "/" + "frame" + "." + fname_id + "." + "####.tif");

  if(frameCount > 500) { // 20 seconds * 25 fps = 500
  //if(frameCount > 100) { // 20 seconds * 25 fps = 500
    noLoop();
  }

  
}

void calcWave() {
  // Increment theta (try different values for 'angular velocity' here
  theta += 0.02;

  // For every x value, calculate a y value with sine function
  float x = theta;
  for (int i = 0; i < yvalues.length; i++) {
    yvalues[i] = sin(x)*amplitude;
    x+=dx;
  }
}

void renderWave() {
  noStroke();
  fill(255);
  // A simple way to draw the wave with an ellipse at each location
  for (int x = 0; x < yvalues.length; x++) {
    ellipse(x*xspacing, height/2+yvalues[x], 16, 16);
  }
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