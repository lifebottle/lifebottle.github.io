# xdelta3

## Windows
Use xDelta GUI.  Alternatively, try the [python-xdelta3ui](https://github.com/pnvnd/python-xdelta3ui) (beta).

### Applying xDelta3 Patch (Windows)
1. Get xdeltaUI from https://www.romhacking.net/utilities/598/
1. Open xdeltaUI.exe
1. Select original ISO file
1. Select patch file .xdelta
1. Browse to a location to save the patched ISO file
1. Enjoy!

![alt text](xdelta_patch.png "xdeltaUI patching instructions.")

### Creating xDelta3 Patch (Windows)
1. Get xdeltaUI from https://www.romhacking.net/utilities/598/
1. Open xDeltaUI.exe
1. Click on `Create Patch` tab  
![alt text](xdelta_01.png "Create xdeltaUI patch step 1.")
1. Original File: Browse to a clean ISO
1. Modified File: Browse to a patched ISO
1. Patch Destination: Browse to a location to save the patch  
![alt text](xdelta_02.png "Create xdeltaUI patch step 2.")
1. Click `Patch` and wait about 1 minute.  
![alt text](xdelta_03.png "Create xdeltaUI patch step 3.")
1. If patch takes longer than 5 minutes, the patched ISO might be *too different* from the original, resulting in large patch size.
1. Upload patch somewhere and share it!

## Linux
Use the command line to download `xdelta3`.
```bash
sudo apt install xdelta3
```

### Applying xDelta3 Patch (Linux)

[![Alt text](https://img.youtube.com/vi/bODynsUS8cg/0.jpg)](https://www.youtube.com/watch?v=bODynsUS8cg)

```bash
xdelta3 -d -s original.iso patch.xdelta patched.iso
```

The `-d` is to decompress, `-s` is the source.

### Creating xDelta3 Patch (Linux)

[![Alt text](https://img.youtube.com/vi/SD7f5UPbQTU/0.jpg)](https://www.youtube.com/watch?v=SD7f5UPbQTU)

```bash
xdelta3 -e -s original.iso patched.iso patch.xdelta
```
The `-e` is to compress, `-s` is the source.

## Mac
Use the command line to download xdelta3.

## Android
Use online patching service.

## iOS
Use online patching service.