#!/usr/bin/env python3
"""
Asset Download Manager - Downloads and verifies required game assets.

Usage:
    python scripts/download_assets.py
"""

import os
import sys
import zipfile
from pathlib import Path

# Required asset directories
REQUIRED_ASSETS = {
    "Assets/Sounds": [
        "attack.wav", "click sfx.wav", "game bg.wav", "game bg2.wav",
        "hover.wav", "lofi bg.wav", "lose.wav", "win.wav",
    ],
    "Assets/backgrounds": [
        "combi bg.png", "cramers bg.png", "game bg.png", "main bg.png", "permu bg.png",
    ],
    "Assets/boxes": [],
    "Assets/buttons": [],
    "Assets/fonts": ["upheavtt.ttf"],
    "Assets/gametext": [
        "confirmation box.png", "yes.png", "yes hover.png", "naur.png", "no hover.png",
    ],
    "Assets/hearts": [],
    "Assets/numButtons": [],
    "Assets/rock paper scissors": ["rock.png", "paper.png", "scissors.png"],
    "Assets/rock paper scissors/Computer": ["rock.png", "paper.png", "scissors.png"],
    "Assets/slider": [],
}

DOWNLOAD_URL = "https://github.com/LosLejo/OOP-Final-Project/releases/download/assets-v1.0/assets.zip"


def check_assets():
    """Check which assets are missing."""
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
    """Print current asset status."""
    missing = check_assets()
    print("\n" + "="*60)
    print("  ASSET STATUS CHECK")
    print("="*60 + "\n")
    
    if not missing:
        print("✓ All assets present! Game is ready to play.\n")
        print("Run: python main.py (or double-click run_game.bat)")
        return True
    
    print(f"✗ Missing {len(missing)} asset(s):\n")
    for item in missing[:10]:
        print(f"  - {item}")
    if len(missing) > 10:
        print(f"\n  ... and {len(missing) - 10} more")
    return False


def create_placeholders():
    """Create asset directory structure."""
    print("\nCreating asset directories...")
    for directory in REQUIRED_ASSETS.keys():
        os.makedirs(directory, exist_ok=True)
        gitkeep = os.path.join(directory, ".gitkeep")
        Path(gitkeep).touch(exist_ok=True)
    print("✓ Directory structure created")


def download_assets():
    """Download and extract assets from GitHub."""
    print("\nDownloading assets...")
    try:
        import urllib.request
        print(f"Source: {DOWNLOAD_URL}")
        urllib.request.urlretrieve(DOWNLOAD_URL, "assets.zip")
        print("✓ Downloaded")
        
        print("Extracting...")
        with zipfile.ZipFile("assets.zip", 'r') as zip_ref:
            zip_ref.extractall(".")
        print("✓ Extracted")
        
        os.remove("assets.zip")
        print("✓ Cleaned up")
        return True
    except Exception as e:
        print(f"✗ Download failed: {e}")
        return False


def show_manual_instructions():
    """Show manual download instructions."""
    print("\n" + "="*60)
    print("  MANUAL DOWNLOAD")
    print("="*60)
    print(f"\n1. Download from: {DOWNLOAD_URL}")
    print("\n2. Extract to this directory so structure is:")
    print("   Project/")
    print("   ├── Assets/")
    print("   │   ├── Sounds/")
    print("   │   ├── backgrounds/")
    print("   │   └── ...")
    print("   └── main.py")
    print("\n3. Run again to verify: python scripts/download_assets.py")


def main():
    """Main entry point."""
    print("\n" + "="*60)
    print("  ASSET MANAGER")
    print("="*60)
    
    if print_status():
        return 0
    
    print("\n" + "="*60)
    print("  OPTIONS")
    print("="*60)
    print("\n1. Download from GitHub")
    print("2. Manual download instructions")
    print("3. Create directory structure only")
    print("4. Exit")
    
    choice = input("\nSelect (1-4): ").strip()
    
    if choice == "1":
        create_placeholders()
        if download_assets():
            print("\n✓ Success!")
            print_status()
            return 0
    elif choice == "2":
        show_manual_instructions()
        create_placeholders()
        return 0
    elif choice == "3":
        create_placeholders()
        return 0
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
