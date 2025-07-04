# 🗂️ Delete Duplicates - Firefox Extension

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Firefox](https://img.shields.io/badge/Firefox-57%2B-orange.svg)](https://www.mozilla.org/firefox/)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)

Automatically detect and remove duplicate files from your Downloads folder when downloading new files in Firefox. Uses SHA-256 hash comparison for accurate duplicate detection.

## ✨ Features

- 🔍 **Automatic Detection**: Scans Downloads folder for duplicates when new files are downloaded
- 🛡️ **Safe Removal**: Only removes files with identical SHA-256 hashes and same extension
- 📁 **Smart Filtering**: Preserves the newest file, removes older duplicates
- 🔧 **Cross-Platform**: Works on Linux, macOS, and Windows
- 📊 **Detailed Logging**: Debug logs for troubleshooting

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/delete-duplicates-firefox.git
   cd delete-duplicates-firefox
   ```

2. **Install native messaging host**:
   ```bash
   # Linux/macOS
   ./scripts/install.sh
   
   # Windows
   scripts\install.bat
   ```

3. **Load extension in Firefox**:
   - Open `about:debugging`
   - Click "This Firefox" → "Load Temporary Add-on"
   - Select `extension/manifest.json`

## 📖 Documentation

- [📋 Installation Guide](docs/installation.md)
- [🔧 Troubleshooting](docs/troubleshooting.md)
- [📝 Changelog](CHANGELOG.md)

## 🛠️ Requirements

- **Firefox**: 57 or later
- **Python**: 3.6 or later
- **OS**: Linux, macOS, or Windows

## 🔧 How It Works

1. Extension monitors Firefox download events
2. When a file is downloaded, sends filename to native Python script
3. Python script calculates SHA-256 hash of the new file
4. Compares with existing files in Downloads folder
5. Removes any duplicates found (same hash + same extension)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter issues:
1. Check the [troubleshooting guide](docs/troubleshooting.md)
2. Review debug logs: `tail -f /tmp/backend_debug.log`
3. Open an issue on GitHub

## ⚠️ Disclaimer

This extension permanently deletes duplicate files. Use at your own risk and ensure you have backups of important files.