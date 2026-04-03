# GitHub Releases Setup Guide for Assets

This guide explains how to upload your game assets to GitHub Releases so users can download them automatically.

## Step 1: Prepare the Assets File

On your local machine, create `assets.zip` with all asset folders:

### Windows (PowerShell):
```powershell
# Navigate to project root
cd c:\Carlos\Coding\Final Project OOP

# Create zip with all assets
$compress = @{
  Path = "Assets/Sounds", "Assets/backgrounds", "Assets/boxes", "Assets/buttons", "Assets/fonts", "Assets/gametext", "Assets/hearts", "Assets/numButtons", "Assets/rock paper scissors", "Assets/slider"
  CompressionLevel = "Optimal"
  DestinationPath = "assets.zip"
}
Compress-Archive @compress
```

### macOS/Linux:
```bash
cd ~/Final-Project-OOP
zip -r assets.zip Assets/Sounds Assets/backgrounds Assets/boxes Assets/buttons Assets/fonts Assets/gametext Assets/hearts Assets/numButtons "Assets/rock paper scissors" Assets/slider
```

**Result:** An `assets.zip` file (~100-150 MB) in your project root

## Step 2: Create GitHub Release

### Via GitHub Web UI (Easiest):

1. Go to your repository: `https://github.com/LosLejo/OOP-Final-Project`
2. Click **Releases** (on the right side)
3. Click **Create a new release**
4. Fill in the form:
   - **Tag name:** `assets-v1.0` (or `v1.0-assets`)
   - **Release title:** `Game Assets Package v1.0`
   - **Description:**
     ```
     Complete asset package including:
     - Sound effects and background music
     - Game graphics and backgrounds
     - UI elements and fonts
     - Rock-paper-scissors game sprites
     
     Extract to project root. See ASSETS.md for details.
     ```
5. **Attach files:** Click "Attach binaries" and upload `assets.zip`
6. Click **Publish release**

### Via GitHub CLI (Faster):

```bash
# Install GitHub CLI from: https://cli.github.com/

# Login once
gh auth login

# Create release with assets attached
gh release create assets-v1.0 assets.zip --title "Game Assets Package v1.0" --notes "Complete asset package for the educational games"
```

## Step 3: Get the Download URL

After creating the release:

1. Go to **Releases** page: `https://github.com/LosLejo/OOP-Final-Project/releases`
2. Find your release (e.g., `assets-v1.0`)
3. Right-click on `assets.zip` → **Copy link address**
4. URL will look like: 
   ```
   https://github.com/LosLejo/OOP-Final-Project/releases/download/assets-v1.0/assets.zip
   ```

## Step 4: Update Your Project

Open `scripts/download_assets.py` and update:

```python
DOWNLOAD_URL = "https://github.com/LosLejo/OOP-Final-Project/releases/download/assets-v1.0/assets.zip"
```

## Step 5: Commit and Push

```bash
git add scripts/download_assets.py
git commit -m "Update asset download URL for GitHub Releases"
git push
```

## Step 6: Test the Download Script

```bash
# This will now download from your GitHub Release
python scripts/download_assets.py
```

Select option **1** (Download from GitHub Releases) and it should download automatically!

## Updating Assets Later

When you update assets (add new graphics, sounds, etc.):

1. **Create new `assets.zip`** with updated files
2. **Create new release** with tag like `assets-v1.1`
3. **Upload `assets.zip`** to new release
4. **Update `DOWNLOAD_URL`** in `scripts/download_assets.py`
5. **Commit and push** changes
6. Users can now download the latest assets!

### Example Release Tags:
- `assets-v1.0` - Initial release
- `assets-v1.1` - Bug fixes to graphics
- `assets-v2.0` - Major update with new content

## Advantages of GitHub Releases

✅ **Free hosting** - Part of your GitHub repo  
✅ **Reliable** - GitHub CDN  
✅ **Versioning** - Keep old versions if needed  
✅ **Easy updates** - Just create new releases  
✅ **Automatic download** - Your script handles it  
✅ **No external dependencies** - No Google Drive, AWS, etc.

## Release Naming Conventions

**Recommended pattern:**
```
Tag: assets-v{VERSION}
Title: Game Assets Package v{VERSION}
```

Examples:
- `assets-v1.0` - First release
- `assets-v1.1` - Patch (bug fixes)
- `assets-v2.0` - Major release (new features)

## Bandwidth & Limits

GitHub Releases are:
- **Unlimited downloads** - No bandwidth limits
- **Reliable** - ~100 MB file size is fine
- **CDN backed** - Fast downloads worldwide

## Troubleshooting

### "Release not found" error
- Double-check URL is exactly correct
- Verify tag name matches: `https://github.com/USERNAME/REPO/releases/download/TAG_NAME/assets.zip`
- Make sure file is still attached to release

### Release creates but asset upload fails
- Asset may be too large (unlikely, GitHub supports multi-GB)
- Try uploading again or split into multiple .zip files

### Users get "corrupt zip" error
- Verify your `assets.zip` extracts locally first
- If yes, re-upload to new release with new tag

## Sharing Your Project

Now users can do:

```bash
git clone https://github.com/LosLejo/OOP-Final-Project.git
cd OOP-Final-Project
python -m venv venv
venv\Scripts\activate  # or: source venv/bin/activate
pip install -r requirements.txt
python scripts/download_assets.py    # Download from your GitHub Release!
python main.py
```

No manual download needed - completely automated!

---

**Need help?**
1. Check GitHub Releases API docs: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
2. Verify your release URL matches the pattern above
3. Test locally with `python scripts/download_assets.py`
