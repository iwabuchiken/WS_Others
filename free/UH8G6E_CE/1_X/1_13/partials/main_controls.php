<div id="div_Main_Contorls_Buttons">

	<button id="btn_Main_Clear_All_Rects" onclick="bt_Clear_All_Rects();" class="btn_Main_Controls">
		C-All</button>
	
	<button id="btn_Main_Clear_One_Rects" onclick="bt_Clear_One_Rects();" class="btn_Main_Controls">
		C-One</button>
	
	<button id="btn_Main_Toggle_Grid" onclick="toggle_Grid();" class="btn_Main_Controls" disabled>
<!-- 		Toggle Grid -->
	
		<img alt="zoom in" src="<?php echo "$dpath_Images/toggle.png"?>">
		
	</button>
	
	<button id="btn_Main_Toggle_Grid_Slanted" onclick="toggle_Grid_Slanted();" class="btn_Main_Controls" disabled>
<!-- 		Toggle Grid -->
	
		<img alt="zoom in" src="<?php echo "$dpath_Images/toggle_slanted.png"?>">
		
	</button>
	
	<button id="btn_Main_Zoom_In" onclick="bt_Canvas_Zoom_In();" class="btn_Main_Controls">
		<img alt="zoom in" src="<?php echo "$dpath_Images/zoom_in.png"?>">
<!-- 	Zoom In -->
	</button>

	<button id="btn_Main_Clear_Zoom_In" onclick="bt_Canvas_Clear_Zoom_In();" class="btn_Main_Controls">
		C-Zoom
	</button>

</div>

<!-- <br> -->

<table>

	<tr>
	
		<td>
			<span class="spn_Lbl_Main_Range">
			
				Start X
				
			</span>
		</td>
		
		<td>
			<input 
			type="text" 
			id="ipt_Main_Range_Start_X"
			
			class="ipt_Main_Range"
			>
		</td>

		<td>
			<span class="spn_Lbl_Main_Range">
		
				End X
			
			</span>
			
		</td>
		
		<td>
			<input 
			type="text" 
			id="ipt_Main_Range_End_X"
			class="ipt_Main_Range"
			>
		</td>
		
	</tr>
	
	<tr>

		<td>
			<span class="spn_Lbl_Main_Range">
		
				Start Y
			
			</span>
			
		</td>
		
		<td>
			<input 
			type="text" 
			id="ipt_Main_Range_Start_Y"
			class="ipt_Main_Range"
				>
		</td>
		
	
		<td>
			<span class="spn_Lbl_Main_Range">
		
				End Y
			
			</span>
			
		</td>
		
		<td>
			<input 
			type="text" 
			id="ipt_Main_Range_End_Y"
			class="ipt_Main_Range"
				>
		</td>
		
	</tr>

	<tr>
	
		<td>
			Grid interval
		</td>
	
		<td>

			<input 
			type="text" 
			id="ipt_Main_Grid_Interval"
			class="ipt_Main_Range"
				>
		
		</td>
	</tr>
	
</table>
