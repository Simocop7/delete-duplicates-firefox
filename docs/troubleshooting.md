# 🔧 Troubleshooting

## Common Issues

### "Initial connection test failed"

**Symptoms**: Console shows connection test failure
**Causes**: 
- Native host not installed correctly
- Python not found
- Incorrect file paths
- Permission issues

**Solutions**:
```bash
# Check if Python is available
python3 --version

# Test native host manually
python3 /path/to/backend.py

# Check configuration file
cat ~/.mozilla/native-messaging-hosts/com.deleteduplicates.python.json

# Verify file permissions
ls -la /path/to/backend.py
chmod +x /path/to/backend.py
```

### "Native messaging host not found"

**Symptoms**: Error about missing native messaging host
**Causes**: 
- Configuration file in wrong location
- Incorrect JSON syntax
- Wrong file paths

**Solutions**:
```bash
# Verify configuration file location
# Linux: ~/.mozilla/native-messaging-hosts/
# macOS: ~/Library/Application Support/Mozilla/NativeMessagingHosts/
# Windows: %APPDATA%\Mozilla\NativeMessagingHosts\

# Validate JSON syntax
python3 -m json.tool ~/.mozilla/native-messaging-hosts/com.deleteduplicates.python.json

# Check file exists
ls -la /path/to/backend.py
```

### Duplicates not being removed

**Symptoms**: Files download but duplicates remain
**Causes**: 
- Extension not active
- Files have different extensions
- Permission issues
- Native host not responding

**Solutions**:
```bash
# Check debug logs
tail -f /tmp/backend_debug.log

# Test duplicate detection manually
cd ~/Downloads
echo "test content" > test1.txt
echo "test content" > test2.txt
# Download a file and check if test2.txt is removed

# Verify extension is loaded
# Go to about:debugging and check "Delete Duplicates" is listed
```

### Python script not starting

**Symptoms**: No logs generated, no response
**Causes**: 
- Python not in PATH
- Script not executable
- Syntax errors in script

**Solutions**:
```bash
# Check Python installation
which python3
python3 --version

# Test script syntax
python3 -m py_compile /path/to/backend.py

# Check script permissions
chmod +x /path/to/backend.py

# Test script directly
python3 /path/to/backend.py
```

## Debug Mode

Enable detailed logging by modifying `backend.py`:

```python
logging.basicConfig(
    level=logging.DEBUG,  # Change to DEBUG for more detail
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/tmp/backend_debug.log'),
        logging.StreamHandler()  # Also log to console
    ]
)
```

## Platform-Specific Issues

### Linux
- SELinux may block native messaging
- AppArmor restrictions
- Snap Firefox has limited native messaging support

### macOS
- Gatekeeper may block unsigned scripts
- SIP (System Integrity Protection) restrictions
- Notarization requirements for distribution

### Windows
- Windows Defender may flag the script
- UAC permissions required for registry changes
- Path length limitations

## Log Analysis

Common log patterns:

```bash
# Successful operation
=== BACKEND STARTED ===
Message length: 25
Received message: {"fileName": "document.pdf"}
Looking for duplicates of document.pdf in /home/user/Downloads
Removed duplicate: /home/user/Downloads/document-old.pdf
Total duplicates removed: 1

# Connection test
=== BACKEND STARTED ===
Message length: 34
Received message: {"fileName": "test-connection.txt"}
Sent response: {"status": "success", "message": "Connection successful"}

# Error conditions
File /home/user/Downloads/missing.pdf does not exist
Error calculating hash for /path/to/file: Permission denied
Error removing /path/to/duplicate: Permission denied
```

## Getting Help

1. **Check logs**: `tail -f /tmp/backend_debug.log`
2. **Test manually**: Run backend.py directly
3. **Validate configuration**: Check JSON syntax and file paths
4. **Restart Firefox**: After configuration changes
5. **Create issue**: Include logs and system info

## Clean Installation

If all else fails, try a clean installation:

```bash
# Remove existing configuration
rm ~/.mozilla/native-messaging-hosts/com.deleteduplicates.python.json

# Remove logs
rm /tmp/backend_debug.log

# Re-run installation
cd /path/to/delete-duplicates-firefox/native-host
./install.sh

# Restart Firefox
# Reload extension
```