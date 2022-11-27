# Apache3

## Create Patched ISO
1. Download Apache3 Preview from https://www.psx-place.com/threads/apache.19171/
   
1. Open `Apache3.exe` and do NOT download update.  Close dialog on top-right.  
![alt text](apache3_01.png "Step 1 - Close dialog.")

1. Close the dialog for StarBurn  
![alt text](apache3_02.png "Step 2 - Click OK.")

1. If you get stuck at the Apache3 splash screen, press Enter to close hidden dialog behind it (ATL+TAB to see it)  
![alt text](apache3_03.png "Step 3 - It's not frozen, press Enter.")

1. Open the ISO you want to modify  
![alt text](apache3_04.png "Step 4 - Open ISO file.")

1. Select a copy of the original ISO, as you'll need the original and the modified ISO to make the xDelta patch.  
![alt text](apache3_05.png "Step 5 - Select ISO to modify.")

1. Once it loads, right-click on the file you need to swap out, and select "Replace Selected File".  
![alt text](apache3_06.png "Step 6 - Right-click file to swap.")

1. Replace `DAT.TBL`, `DAT.BIN`, `SLPS_258.42`, etc. or whatever file you need to swap out as needed.  
![alt text](apache3_07.png "Step 7 - Replace Selected File.")

1. Uncheck `Update TOC` and check `Ignore File Size Differences` and Replace File.  
![alt text](apache3_08.png "Step 8 - Apache3 might crash if you don't.")

1. Replacing large files such as `DAT.BIN` may take long since it's a large file.  
![alt text](apache3_09.png "Step 9 - Wait for it to complete.")

1. Once you replace all the required files, close Apache3 Preview.  

1. Make an [xDelta3](other/xdelta3/index) patch and share!