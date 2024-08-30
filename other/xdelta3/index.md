# xdelta3

## Windows
Use xDelta GUI.  Alternatively, try the [python-xdelta3ui](https://github.com/pnvnd/python-xdelta3ui) (beta).

### Applying xDelta3 Patch (Windows)

[![Alt text](https://img.youtube.com/vi/Kx5pPlKWjQE/0.jpg)](https://www.youtube.com/watch?v=Kx5pPlKWjQE)

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

```bash
xdelta3 -d -s original.iso patch.xdelta patched.iso
```

The `-d` is to decompress, `-s` is the source.

### Creating xDelta3 Patch (Linux)

```bash
xdelta3 -e -s original.iso patched.iso patch.xdelta
```
The `-e` is to compress, `-s` is the source.

## Mac
Use the command line to download xdelta3.  Alternatively, try the [python-xdelta3ui](https://github.com/pnvnd/python-xdelta3ui) (beta) script.

### Creating and Applying xDelta3 Patch (Mac)

```zsh
brew install xdelta
git clone https://github.com/pnvnd/python-xdelta3ui.git
python3 xdelta3ui.py
```

![](https://raw.githubusercontent.com/pnvnd/python-xdelta3ui/main/xdelta3ui_03.png)

## Android
Use [UniPatcher](https://github.com/btimofeev/UniPatcher/releases) on Android to patch.

1. Install UniPatcher from the Play Store, download the required file and prefered `xdelta` file
2. Start UniPatcher, tap the Patch file box and select the `xdelta` file
3. Tap the "Rom" file box and select the file you want to patch
4. Tap the "Output" file box and just tap save on the name it gives you (it should be `<Your_File> [patched].iso` by default)
5. Tap the red save icon at the bottom right. A "Patching complete" message should popup if it worked
6. Now use the patched file

## iOS
Use online patching service.
