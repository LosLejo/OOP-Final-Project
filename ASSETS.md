# Assets Documentation

This document explains the game assets structure and how to set them up.

## Why Assets Are Excluded from Repository

The asset files (images, sounds, fonts) **are not included in the GitHub repository** because:

- 🎯 **Large file size** - Audio and image files can total 100+ MB
- 📦 **Lightweight repository** - Easier to clone and download
- ⚡ **Faster CI/CD** - Better for automated testing and deployment
- 💾 **Separate distribution** - Easier to update or replace assets independently

## Asset Directory Structure

All assets must be placed in the `Assets/` directory with the following structure:

```
Assets/
├── Sounds/                           # Audio files for the game
│   ├── attack.wav
│   ├── click sfx.wav
│   ├── game bg.wav
│   ├── game bg2.wav
│   ├── hover.wav
│   ├── lofi bg.wav
│   ├── lose.wav
│   └── win.wav
│
├── backgrounds/                      # Background images
│   ├── combi bg.png
│   ├── cramers bg.png
│   ├── game bg.png
│   ├── main bg.png
│   └── permu bg.png
│
├── boxes/                            # UI box elements
│   └── [box graphics]
│
├── buttons/                          # Button graphics
│   └── [button images]
│
├── fonts/                            # Game fonts
│   ├── upheavtt.ttf
│   └── [other font files]
│
├── gametext/                         # Game UI text images
│   ├── confirmation box.png
│   ├── yes.png
│   ├── yes hover.png
│   ├── naur.png (no button)
│   ├── no hover.png
│   ├── vs.png
│   ├── user.png
│   ├── computer.png
│   ├── challenger.png
│   ├── win.png
│   ├── lose.png
│   └── [other UI elements]
│
├── hearts/                           # Health/heart graphics
│   └── [heart icons]
│
├── numButtons/                       # Number button graphics
│   └── [number button images]
│
├── rock paper scissors/              # Rock-paper-scissors game graphics
│   ├── rock.png
│   ├── paper.png
│   ├── scissors.png
│   ├── arrow.png
│   ├── rockh.png (hover state)
│   ├── paperh.png (hover state)
│   ├── scissorh.png (hover state)
│   └── Computer/
│       ├── rock.png
│       ├── paper.png
│       ├── scissors.png
│       ├── arrow.png
│       ├── rockh.png
│       ├── paperh.png
│       └── scissorh.png
│
└── slider/                           # Slider UI component graphics
    └── [slider images]
```

## Getting the Assets

### Option 1: Automatic Download (Recommended)

```bash
python scripts/download_assets.py
```

Select option **1** to download from GitHub Releases. The script will automatically:
- Check which assets are missing
- Download from GitHub Releases
- Extract to the correct directories
- Verify everything is installed

### Option 2: GitHub Releases (Manual)

1. Go to [GitHub Releases](https://github.com/LosLejo/OOP-Final-Project/releases)
2. Download the latest `assets.zip` (e.g., `assets-v1.0`)
3. Extract to your project root directory
4. Verify `Assets/` folder contains the required subdirectories (see structure above)

**Setup Instructions:** See [SETUP_GITHUB_RELEASES.md](SETUP_GITHUB_RELEASES.md) for how to create releases.

### Option 3: Manual File Upload (Alternative)

If GitHub Releases isn't available:
1. Contact the project maintainer for download link
2. Extract to project root
3. Run: `python scripts/download_assets.py` (select option 4 to verify)

## Asset File Specifications

### Audio Files (.wav)

| File | Size (Est.) | Duration | Purpose |
|------|-------------|----------|---------|
| `attack.wav` | 50-200 KB | ~1 sec | Attack sound effect |
| `click sfx.wav` | 30-100 KB | ~0.5 sec | Button click sound |
| `game bg.wav` | 500 KB - 2 MB | ~30+ sec | Background music (game) |
| `game bg2.wav` | 500 KB - 2 MB | ~30+ sec | Alternative background music |
| `hover.wav` | 30-100 KB | ~0.5 sec | Hover sound effect |
| `lofi bg.wav` | 500 KB - 2 MB | ~30+ sec | Lo-fi background music |
| `lose.wav` | 100-300 KB | ~1-2 sec | Loss sound effect |
| `win.wav` | 100-300 KB | ~1-2 sec | Win sound effect |

### Image Files (.png)

All images are PNG format with transparency (RGBA):

- **Backgrounds:** 1280x720 (will be scaled as needed)
- **Buttons/UI:** Variable sizes, typically 100-400px
- **Game graphics:** Variable sizes depending on use

Total estimated size: 20-50 MB for all assets

### Font Files (.ttf)

- `upheavtt.ttf` - Main game font

## Verifying Assets are Installed

Run the game and check:

```bash
python main.py
```

If assets are missing, you'll see errors like:
```
FileNotFoundError: Assets\backgrounds\game bg.png
```

### Quick Verification Script

```python
import os
import sys

REQUIRED_ASSETS = [
    "Assets/Sounds/attack.wav",
    "Assets/backgrounds/game bg.png",
    "Assets/fonts/upheavtt.ttf",
    "Assets/gametext/confirmation box.png",
    # ... add all required files
]

missing = []
for asset in REQUIRED_ASSETS:
    if not os.path.exists(asset):
        missing.append(asset)

if missing:
    print(f"Missing {len(missing)} assets:")
    for asset in missing:
        print(f"  - {asset}")
    sys.exit(1)
else:
    print("✓ All assets present!")
```

## Asset Licensing & Attribution

- **Source:** Created for educational project OOP final assignment
- **Usage:** Educational purposes only
- **Modifications:** Feel free to customize or replace assets for your fork

## Updating Assets

To update or replace assets:

1. **Keep the same filenames** - Code references specific file names
2. **Maintain aspect ratios** - UI assumes certain image dimensions
3. **Test thoroughly** - Run all games after updating assets
4. **Update this document** - If adding new assets

## Troubleshooting

### "FileNotFoundError: Cannot find asset files"

**Solution:**
```bash
# Verify directory structure
ls -la Assets/

# If empty, download assets using one of the methods above
```

### Assets load but look wrong/distorted

**Possible causes:**
- Image dimensions changed
- Aspect ratio not maintained
- File corruption during download

**Solution:**
- Verify image dimensions match originals
- Re-download assets from source

### Audio doesn't play

**Possible causes:**
- Audio files not in `.wav` format
- File corruption
- Audio system not initialized

**Solution:**
- Convert audio to WAV format: `ffmpeg -i file.mp3 file.wav`
- Reinstall audio drivers
- Try different audio system settings

### Game runs but no assets load

1. Verify `Assets/` directory exists in project root
2. Check file names match exactly (case-sensitive on Linux/macOS)
3. Verify file permissions (should be readable)
4. Check console for specific error messages

## Contributing Asset Improvements

To contribute improved or additional assets:

1. Create a fork
2. Add new assets to `Assets/` directory
3. Test with the game
4. Submit pull request with description of changes
5. Include any licensing information for new assets

## Asset Backup

**Important:** Keep a backup of your assets outside the repository!

```bash
# Create backup
tar -czf assets-backup.tar.gz Assets/

# Or on Windows
Compress-Archive -Path Assets -DestinationPath assets-backup.zip
```

---

**Last Updated:** April 2026
**Expected Total Asset Size:** ~100 MB
**Required:** Yes (game will not run without assets)
