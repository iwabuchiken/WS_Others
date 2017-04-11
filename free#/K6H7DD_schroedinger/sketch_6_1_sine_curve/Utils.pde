static class Utils {
  
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
  //String get_time_label__Now(int type) {
    static String get_time_label__Now(int type) {

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

  
  
}//Utils