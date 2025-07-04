# 📋 Installation Guide

## Prerequisites

- **Firefox**: Version 57 or later
- **Python**: Version 3.6 or later
- **Operating System**: Linux, macOS, or Windows

## Step-by-Step Installation

### 1. Download the Extension

```bash
git clone https://github.com/yourusername/delete-duplicates-firefox.git
cd delete-duplicates-firefox
```

### 2. Install Native Messaging Host

Choose your operating system:

#### Linux/macOS
```bash
cd native-host
chmod +x install.sh
./install.sh
```

#### Windows
```batch
cd native-host
install.bat
```

### 3. Load Extension in Firefox

1. Open Firefox
2. Navigate to `about:debugging`
3. Click "**This Firefox**"
4. Click "**Load Temporary Add-on**"
5. Navigate to the `extension/` folder
6. Select `manifest.json`

### 4. Verify Installation

1. In the `about:debugging` page, find "Delete Duplicates"
2. Click "**Inspect**"
3. Check the console for:
   ```
   === INITIAL CONNECTION TEST SUCCESS ===
   ```

## Manual Installation

If the automated scripts don't work, follow the manual steps:

### Linux
```bash
# Create native messaging directory
mkdir -p ~/.mozilla/native-messaging-hosts

# Create configuration file
cat > ~/.mozilla/native-messaging-hosts/com.deleteduplicates.python.json << 'EOF'
{
  "name": "com.deleteduplicates.python",
  "description": "Delete Duplicates Native Host",
  "path": "/full/path/to/backend.py",
  "type": "stdio",
  "allowed_extensions": ["delete-duplicates@user"]
}
EOF

# Make script executable
chmod +x /full/path/to/backend.py
```

### macOS
```bash
# Create native messaging directory
mkdir -p ~/Library/Application\ Support/Mozilla/NativeMessagingHosts

# Create configuration file
cat > ~/Library/Application\ Support/Mozilla/NativeMessagingHosts/com.deleteduplicates.python.json << 'EOF'
{
  "name": "com.deleteduplicates.python",
  "description": "Delete Duplicates Native Host",
  "path": "/full/path/to/backend.py",
  "type": "stdio",
  "allowed_extensions": ["delete-duplicates@user"]
}
EOF

# Make script executable
chmod +x /full/path/to/backend.py
```

### Windows
1. Create folder: `%APPDATA%\Mozilla\NativeMessagingHosts`
2. Create file: `com.deleteduplicates.python.json` with content:
```json
{
  "name": "com.deleteduplicates.python",
  "description": "Delete Duplicates Native Host",
  "path": "C:\\full\\path\\to\\backend.py",
  "type": "stdio",
  "allowed_extensions": ["delete-duplicates@user"]
}
```

## Testing

### Test Native Host
```bash
# Should wait for input (Ctrl+C to exit)
python3 /path/to/backend.py

# Test with sample input
echo '{"fileName": "test-connection.txt"}' | python3 /path/to/backend.py
```

### Test Extension
1. Create test files in Downloads:
   ```bash
   cd ~/Downloads
   echo "test content" > test1.txt
   echo "test content" > test2.txt  # This should be removed
   ```
2. Download any file with Firefox
3. Check if duplicate was removed

## Troubleshooting

See [troubleshooting.md](troubleshooting.md) for common issues and solutions.