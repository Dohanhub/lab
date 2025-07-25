#!/usr/bin/env python3
"""
🔄 Replace DoganHub with DoganHub
==============================

Simple script to replace all DoganHub references with DoganHub
"""

import os
import re
from pathlib import Path

def replace_in_file(file_path, replacements):
    """Replace text in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for old_text, new_text in replacements.items():
            content = content.replace(old_text, new_text)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated: {file_path}")
            return True
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
    
    return False

def main():
    print("🔄 Replacing DoganHub with DoganHub...")
    
    # Define replacements
    replacements = {
        'DoganHub': 'DoganHub',
        'DoganHub': 'DoganHub', 
        'doganhub': 'doganhub',
        'DoganHub_COLORS': 'DOGANHUB_COLORS',
        'doganhub_branding': 'doganhub_branding',
        'doganhub-': 'doganhub-',
        '.doganhub-': '.doganhub-',
        'doganhub_': 'doganhub_',
        'apply_doganhub_branding': 'apply_doganhub_branding'
    }
    
    # Process files
    root_dir = Path("d:/DoganLab")
    updated_files = 0
    
    for file_path in root_dir.rglob("*.py"):
        if replace_in_file(file_path, replacements):
            updated_files += 1
    
    print(f"\n🎉 Replacement complete!")
    print(f"✅ Updated {updated_files} files")
    print("💙 DoganHub is now DoganHub - Omar's vision lives on!")

if __name__ == "__main__":
    main()