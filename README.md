# Educational Game Suite

An interactive collection of educational games built with Python and Pygame. Includes rock-paper-scissors battle scenarios, mathematical puzzles (combinations, permutations, Cramer's rule), and graph visualizations.

**Features:**
- 🎮 Multiple interactive games (5+ games available)
- 🎨 GUI-based gameplay with Pygame
- 📚 Educational content for math and logic
- 🔊 Sound effects and immersive audio
- 🎯 Cross-platform support (Windows, macOS, Linux)

## System Requirements

- **Python:** 3.8 or higher (tested with 3.12.1)
- **OS:** Windows, macOS, or Linux with a graphical display
- **Memory:** ~500 MB minimum
- **Display:** 1280x720 resolution or higher

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Final-Project-OOP.git
cd Final-Project-OOP
```

### 2. Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Assets

The game assets (images, sounds, fonts) are not included in the repository to keep it lightweight. Download from **GitHub Releases**:

**Automatic Download** (Recommended):
```bash
python scripts/download_assets.py
```

Then select option **1** to download from GitHub Releases. The script will:
- ✅ Check if assets already exist
- ✅ Download from releases automatically
- ✅ Extract to correct folders
- ✅ Verify everything is in place

**Manual Download:**
1. Go to [GitHub Releases](https://github.com/TODO_UPDATE_WITH_YOUR_REPO/releases)
2. Download the latest `assets.zip` (e.g., `assets-v1.0`)
3. Extract to your project root directory
4. Verify `Assets/` folder now contains: `Sounds/`, `backgrounds/`, `fonts/`, etc.

See [SETUP_GITHUB_RELEASES.md](SETUP_GITHUB_RELEASES.md) for how to create releases and [ASSETS.md](ASSETS.md) for detailed asset information.

### 5. Run the Game

```bash
python main.py
```

A menu will appear letting you select which game to play:
- **1. Rock-Paper-Scissors Battle** - Strategic hand game with AI
- **2. Combination Puzzle** - Math puzzle using combinatorics
- **3. Cramer's Rule Solver** - Linear algebra challenge
- **4. Permutation Challenge** - Permutation-based puzzle
- **5. Graph Visualization** - Interactive graph exploration

## Project Structure

```
Final-Project-OOP/
├── main.py                      # Main entry point
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── ASSETS.md                    # Asset documentation
├── .gitignore                   # Git ignore rules
├── .dockerignore                # Docker ignore rules
├── Dockerfile                   # Docker container setup
├── docker-compose.yml           # Docker Compose configuration
├── Assets/                      # Game modules and resources
│   ├── __init__.py
│   ├── Game.py                  # Rock-Paper-Scissors game
│   ├── Combination.py           # Combination puzzle
│   ├── Cramers.py              # Cramer's rule solver
│   ├── Permutation.py          # Permutation challenge
│   ├── Graph.py                # Graph visualization
│   ├── menuBox.py              # Menu system
│   ├── buttonGame.py           # Button controls
│   ├── backButton.py           # Back button handler
│   ├── Sound.py                # Sound management
│   ├── healthBar.py            # Health bar UI
│   ├── slider.py               # Slider UI component
│   ├── Sounds/                 # Audio files (excluded from repo)
│   ├── backgrounds/            # Background images (excluded from repo)
│   ├── buttons/                # Button images (excluded from repo)
│   ├── fonts/                  # Font files (excluded from repo)
│   ├── gametext/               # Game text images (excluded from repo)
│   └── ...                     # Other asset folders
└── scripts/                    # Utility scripts
    └── download_assets.py      # Asset download script (coming soon)
```

## Installation Troubleshooting

### "ModuleNotFoundError: No module named 'pygame'"
Make sure you've activated your virtual environment and run `pip install -r requirements.txt`

### "FileNotFoundError: Assets not found"
Download the assets file using the method described in Step 4 above.

### Port/Display Issues on Headless Servers
This is a GUI application and requires a display. Use:
- **SSH X11 Forwarding:** `ssh -X user@host`
- **Docker with display forwarding** (see Docker section below)
- **Run natively on a machine with a display**

## Docker Setup (Optional)

### Run with Docker on Any OS

**Option 1: Using Docker Compose (Recommended)**

On **Windows/macOS** (with Docker Desktop):
```bash
docker-compose up
```

On **Linux** (requires X11 display setup):
```bash
docker-compose up
```

**Option 2: Manual Docker Build**

```bash
# Build the image
docker build -t educational-games .

# Run with display on Windows
docker run -e DISPLAY=host.docker.internal:0 educational-games

# Run with display on Linux
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix educational-games

# Run with display on macOS
docker run -e DISPLAY=docker.for.mac.host.internal:0 educational-games
```

## Development

### Running from Source

1. Activate virtual environment
2. Install requirements
3. Download assets
4. Run: `python main.py`

### Code Style

This project uses standard Python conventions. Please follow PEP 8 where possible.

### Adding New Games

To add a new game:
1. Create a new module in `Assets/game_name.py`
2. Implement a `runGameName(title, surface)` function
3. Update `main.py` to include the new game in the menu
4. Test thoroughly with assets

## Dependencies

- **pygame** - Game development library
- **numpy** - Numerical computing
- **pillow** - Image processing
- **PyTMX** - Tiled map format support

See `requirements.txt` for versions.

## Deployment

### To GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files (respecting .gitignore)
git add .

# Commit
git commit -m "Initial commit: Educational game suite"

# Add remote and push
git remote add origin https://github.com/yourusername/Final-Project-OOP.git
git push -u origin main
```

### To Cloud Services

**Heroku** (Requires web framework, not suitable for GUI)
**AWS/Azure** (Use Docker container)
**GitHub Releases** (Upload assets separately)

## Performance Tips

- Use the Docker container for consistent experience across devices
- Ensure you have 1280x720 or higher display resolution
- Close other applications for smoother gameplay
- Update graphics drivers for better performance

## Known Issues

- GUI may not work on remote/headless servers without X11 forwarding
- Sound may not work on some Linux distributions without ALSA/PulseAudio setup
- PyTMX dependency may require additional setup on some systems

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions:
1. Check [ASSETS.md](ASSETS.md) for asset-related problems
2. Review troubleshooting section above
3. Check GitHub issues

## Credits

Built as an educational project in Python with Pygame.

---

**Last Updated:** April 2026
**Python Version:** 3.8+
**Pygame Version:** 2.5.2+
