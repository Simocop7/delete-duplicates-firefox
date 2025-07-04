#!/bin/bash
# Installation script for Linux/macOS

set -e

echo "🚀 Installing Delete Duplicates Native Host..."

# Get the absolute path of the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_PATH="$SCRIPT_DIR/backend.py"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Make backend.py executable
chmod +x "$BACKEND_PATH"

# Determine the correct directory based on OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    NATIVE_HOST_DIR="$HOME/Library/Application Support/Mozilla/NativeMessagingHosts"
else
    # Linux
    NATIVE_HOST_DIR="$HOME/.mozilla/native-messaging-hosts"
fi

# Create directory if it doesn't exist
mkdir -p "$NATIVE_HOST_DIR"

# Create the native messaging host manifest
cat > "$NATIVE_HOST_DIR/com.deleteduplicates.python.json" << EOF
{
  "name": "com.deleteduplicates.python",
  "description": "Delete Duplicates Native Host",
  "path": "$BACKEND_PATH",
  "type": "stdio",
  "allowed_extensions": [
    "delete-duplicates@user"
  ]
}
EOF

echo "✅ Native host installed successfully!"
echo "📁 Configuration file: $NATIVE_HOST_DIR/com.deleteduplicates.python.json"
echo "🐍 Backend script: $BACKEND_PATH"
echo ""
echo "Next steps:"
echo "1. Open Firefox and go to about:debugging"
echo "2. Click 'This Firefox' → 'Load Temporary Add-on'"
echo "3. Select the manifest.json file from the extension folder"
echo ""
echo "📋 Test the installation:"
echo "   python3 '$BACKEND_PATH' # Should wait for input (Ctrl+C to exit)"