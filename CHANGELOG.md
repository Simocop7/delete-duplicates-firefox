# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-XX

### Added
- Initial release
- Automatic duplicate detection and removal
- SHA-256 hash-based comparison
- Cross-platform support (Linux, macOS, Windows)
- Firefox extension with native messaging
- Debug logging
- Installation scripts
- Comprehensive documentation

### Features
- Monitors Firefox download events
- Compares files by SHA-256 hash and extension
- Removes older duplicates, keeps newest file
- Works with Downloads folder
- Detailed logging for troubleshooting

### Supported Platforms
- Firefox 57+
- Python 3.6+
- Linux, macOS, Windows