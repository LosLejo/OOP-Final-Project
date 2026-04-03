#!/usr/bin/env python3
"""
Asset Download Manager
Downloads and verifies required game assets if they are missing.

Usage:
    python scripts/download_assets.py

This script will:
    1. Check which assets are missing
    2. Provide download instructions or automated download
    3. Extract assets to correct locations
    4. Verify asset integrity
"""

import os
import sys
import zipfile
import shutil
from pathlib import Path


# Required asset directories and example files
REQUIRED_ASSETS = {
    "Assets/Sounds": [
        "attack.wav",
        "click sfx.wav",
        "game bg.wav",
        "game bg2.wav",
        "hover.wav",
        "lofi bg.wav",
        "lose.wav",
        "win.wav",
    ],
    "Assets/backgrounds": [
        "combi bg.png",
        "cramers bg.png",
        "game bg.png",
        "main bg.png",
        "permu bg.png",
    ],
    "Assets/boxes": [],  # Directory just needs to exist
    "Assets/buttons": [],
    "Assets/fonts": ["upheavtt.ttf"],
    "Assets/gametext": [
        "confirmation box.png",
        "yes.png",
        "yes hover.png",
        "naur.png",
        "no hover.png",
    ],
    "Assets/hearts": [],
    "Assets/numButtons": [],
    "Assets/rock paper scissors": [
        "rock.png",
        "paper.png",
        "scissors.png",
    ],
    "Assets/rock paper scissors/Computer": [
        "rock.png",
        "paper.png",
        "scissors.png",
    ],
    "Assets/slider": [],
}

# Configuration - GitHub Releases URL
# See SETUP_GITHUB_RELEASES.md for how to create releases and get this URL
DOWNLOAD_URL = "https://github.com/LosLejo/OOP-Final-Project/releases/download/assets-v1.0/assets.zip"
GDRIVE_ID = "YOUR_GOOGLE_DRIVE_FILE_ID"  # Alternative: Google Drive share (optional)


def check_assets():
    """Check which assets are missing"""
    missing = []
    
    for directory, files in REQUIRED_ASSETS.items():
        if not os.path.exists(directory):
            missing.append(f"Missing directory: {directory}")
            continue
            
        for file in files:
            filepath = os.path.join(directory, file)
            if not os.path.exists(filepath):
                missing.append(f"Missing file: {filepath}")
    
    return missing


def print_status():
    """Print current asset status"""
    missing = check_assets()
    
    print("\n" + "="*60)
    print("  ASSET STATUS CHECK")
    print("="*60 + "\n")
    
    if not missing:
        print("✓ All assets present! Game is ready to play.")
        print("\nYou can now run:")
        print("  python main.py")
        return True
    else:
        print(f"✗ Missing {len(missing)} asset(s):\n")
        for item in missing[:10]:  # Show first 10
            print(f"  - {item}")
        if len(missing) > 10:
            print(f"\n  ... and {len(missing) - 10} more")
        return False


def download_from_github():
    """Download and extract assets from GitHub releases"""
    print("\nDownloading assets from GitHub...")
    print(f"URL: {DOWNLOAD_URL}")
    
    try:
        import urllib.request
        
        # Download
        print("Downloading (this may take a minute)...")
        urllib.request.urlretrieve(DOWNLOAD_URL, "assets.zip")
        print("✓ Downloaded successfully")
        
        # Extract
        print("Extracting assets...")
        with zipfile.ZipFile("assets.zip", 'r') as zip_ref:
            zip_ref.extractall(".")
        print("✓ Extracted successfully")
        
        # Cleanup
        os.remove("assets.zip")
        print("✓ Cleaned up temporary files")
        
        return True
        
    except Exception as e:
        print(f"✗ Download failed: {e}")
        return False


def download_from_gdrive():
    """Download assets from Google Drive"""
    print("\nDownloading from Google Drive...")
    print(f"File ID: {GDRIVE_ID}")
    
    if GDRIVE_ID == "YOUR_GOOGLE_DRIVE_FILE_ID":
        print("✗ Google Drive File ID not configured")
        print("   Please set GDRIVE_ID in this script")
        return False
    
    try:
        import gdown
        
        url = f"https://drive.google.com/uc?id={GDRIVE_ID}"
        print("Downloading (this may take a minute)...")
        gdown.download(url, "assets.zip", quiet=False)
        print("✓ Downloaded successfully")
        
        print("Extracting assets...")
        with zipfile.ZipFile("assets.zip", 'r') as zip_ref:
            zip_ref.extractall(".")
        print("✓ Extracted successfully")
        
        os.remove("assets.zip")
        print("✓ Cleaned up temporary files")
        
        return True
        
    except ImportError:
        print("✗ gdown module not installed")
        print("   Install with: pip install gdown")
        return False
    except Exception as e:
        print(f"✗ Download failed: {e}")
        return False


def manual_download_instructions():
    """Print manual download instructions"""
    print("\n" + "="*60)
    print("  MANUAL DOWNLOAD INSTRUCTIONS")
    print("="*60 + "\n")
    
    print("1. Download the assets archive from:")
    print(f"   GitHub: {DOWNLOAD_URL}")
    print(f"   OR Google Drive: [Link]")
    
    print("\n2. Extract the archive to this directory")
    print("   The structure should be:")
    print("   Final-Project-OOP/")
    print("   ├── Assets/")
    print("   │   ├── Sounds/")
    print("   │   ├── backgrounds/")
    print("   │   ├── fonts/")
    print("   │   └── ...")
    print("   └── main.py")
    
    print("\n3. Run this script again to verify:")
    print("   python scripts/download_assets.py")
    
    print("\n4. If assets are found, run the game:")
    print("   python main.py")


def create_placeholder_assets():
    """Create empty placeholder directories"""
    print("\nCreating asset directory structure...")
    
    for directory in REQUIRED_ASSETS.keys():
        os.makedirs(directory, exist_ok=True)
        # Create .gitkeep to preserve directory in git
        gitkeep = os.path.join(directory, ".gitkeep")
        if not os.path.exists(gitkeep):
            Path(gitkeep).touch()
    
    print("✓ Asset directories created")


def main():
    """Main entry point"""
    print("\n" + "="*60)
    print("  EDUCATIONAL GAME SUITE - ASSET MANAGER")
    print("="*60)
    
    # Check current status
    status_ok = print_status()
    
    if status_ok:
        return 0
    
    print("\n" + "="*60)
    print("  DOWNLOAD OPTIONS")
    print("="*60)
    
    print("\n1. Download from GitHub Releases (Recommended)")
    print("2. Download from Google Drive")
    print("3. Manual download instructions")
    print("4. Just create directory structure (manual download later)")
    print("5. Exit")
    
    choice = input("\nSelect option (1-5): ").strip()
    
    if choice == "1":
        # Ensure directories exist first
        create_placeholder_assets()
        if download_from_github():
            print("\n✓ Assets downloaded successfully!")
            print_status()
            return 0
    
    elif choice == "2":
        create_placeholder_assets()
        if download_from_gdrive():
            print("\n✓ Assets downloaded successfully!")
            print_status()
            return 0
    
    elif choice == "3":
        create_placeholder_assets()
        manual_download_instructions()
        return 0
    
    elif choice == "4":
        create_placeholder_assets()
        print("\n✓ Directory structure created")
        manual_download_instructions()
        return 0
    
    else:
        print("Exiting...")
        return 0
    
    print("\n✗ Unable to complete asset download")
    manual_download_instructions()
    return 1


if __name__ == "__main__":
    sys.exit(main())
