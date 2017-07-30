

<div id="div_Main_Contorls_Buttons">
<table>
	<tr>
		<td>
		
			<button id="btn_Main_Clear_All_Rects" onclick="bt_Clear_All_Rects();" class="btn_Main_Controls">
				C-All</button>
			
			<button id="btn_Main_Clear_One_Rects" onclick="bt_Clear_One_Rects();" class="btn_Main_Controls">
				C-One</button>
		</td>
	</tr>
	<tr>	
		<td>	
			<button id="btn_Main_Toggle_Grid" onclick="toggle_Grid();" class="btn_Main_Controls" disabled>
		<!-- 		Toggle Grid -->
			
				<img alt="zoom in" src="<?php echo "$dpath_Images/toggle.png"?>">
				
			</button>
			
			<button id="btn_Main_Toggle_Grid_Slanted" onclick="toggle_Grid_Slanted();" class="btn_Main_Controls" disabled>
		<!-- 		Toggle Grid -->
			
				<img alt="zoom in" src="<?php echo "$dpath_Images/toggle_slanted.png"?>">
				
			</button>
			
		</td>
	<tr>
		<td>
			<button id="btn_Main_Zoom_In" onclick="bt_Canvas_Zoom_In();" class="btn_Main_Controls">
				<img alt="zoom in" src="<?php echo "$dpath_Images/zoom_in.png"?>">
		<!-- 	Zoom In -->
			</button>
		
			<button id="btn_Main_Clear_Zoom_In" onclick="bt_Canvas_Clear_Zoom_In();" class="btn_Main_Controls">
				C-Zoom
			</button>
		</td>
	</tr>
	
	<tr>
		<td>

			<button 
					id="btn_Main_Draw_Circle" 
					onclick="bt_Canvas_Draw_Circle();" 
					class="btn_Main_Controls">
				<img alt="draw circle" src="<?php echo "$dpath_Images/switch-draw-circle.png"?>">
			</button>
		
<!-- 		</td> -->
	
<!-- 		<td> -->

			<button 
					id="btn_Main_Clear_Circle" 
					onclick="bt_Canvas_Clear_Circle();" 
					class="btn_Main_Controls"
					
					>
					
				<img alt="clear circle" src="<?php echo "$dpath_Images/switch-draw-circle_clear-all.png"?>">
				
			</button>
		
		</td>
	
	</tr>
	
</table>

</div>