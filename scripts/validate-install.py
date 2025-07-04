#!/usr/bin/env python3
"""
Validation script to check if Delete Duplicates is installed correctly
"""

import os
import sys
import json
import platform
from pathlib import Path

def check_python():
    """Check Python version"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print("❌ Python 3.6+ required, found", f"{version.major}.{version.minor}")
        return False
    print("✅ Python", f"{version.major}.{version.minor}.{version.micro}")
    return True

def check_native_host_config():
    """Check native messaging host configuration"""
    system = platform.system()
    
    if system == "Linux":
        config_path = Path.home() / ".mozilla" / "native-messaging-hosts" / "com.deleteduplicates.python.json"
    elif system == "Darwin":
        config_path = Path.home() / "Library" / "Application Support" / "Mozilla" / "NativeMessagingHosts" / "com.deleteduplicates.python.json"
    elif system == "Windows":
        config_path = Path(os.getenv("APPDATA")) / "Mozilla" / "NativeMessagingHosts" / "com.deleteduplicates.python.json"
    else:
        print("❌ Unsupported operating system:", system)
        return False
    
    if not config_path.exists():
        print("❌ Native host configuration not found:", config_path)
        return False
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        required_fields = ["name", "description", "path", "type", "allowed_extensions"]
        for field in required_fields:
            if field not in config:
                print(f"❌ Missing required field '{field}' in configuration")
                return False
        
        # Check if backend script exists
        backend_path = Path(config["path"])
        if not backend_path.exists():
            print("❌ Backend script not found:", backend_path)
            return False
        
        # Check if script is executable (Unix-like systems)
        if system in ["Linux", "Darwin"]:
            if not os.access(backend_path, os.X_OK):
                print("❌ Backend script not executable:", backend_path)
                return False
        
        print("✅ Native host configuration:", config_path)
        print("✅ Backend script:", backend_path)
        return True
        
    except json.JSONDecodeError as e:
        print("❌ Invalid JSON in configuration:", e)
        return False
    except Exception as e:
        print("❌ Error reading configuration:", e)
        return False

def check_downloads_folder():
    """Check if Downloads folder exists and is writable"""
    downloads_path = Path.home() / "Downloads"
    
    if not downloads_path.exists():
        print("❌ Downloads folder not found:", downloads_path)
        return False
    
    if not downloads_path.is_dir():
        print("❌ Downloads path is not a directory:", downloads_path)
        return False
    
    # Test write permissions
    try:
        test_file = downloads_path / ".delete-duplicates-test"
        test_file.write_text("test")
        test_file.unlink()
        print("✅ Downloads folder accessible:", downloads_path)
        return True
    except Exception as e:
        print("❌ Cannot write to Downloads folder:", e)
        return False

def main():
    """Main validation function"""
    print("🔍 Validating Delete Duplicates installation...\n")
    
    checks = [
        ("Python version", check_python),
        ("Native host configuration", check_native_host_config),
        ("Downloads folder", check_downloads_folder),
    ]
    
    all_passed = True
    for name, check_func in checks:
        print(f"Checking {name}...")
        if not check_func():
            all_passed = False
        print()
    
    if all_passed:
        print("🎉 All checks passed! Installation appears to be correct.")
        print("\nNext steps:")
        print("1. Open Firefox and go to about:debugging")
        print("2. Load the extension by selecting extension/manifest.json")
        print("3. Check the console for 'INITIAL CONNECTION TEST SUCCESS'")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()