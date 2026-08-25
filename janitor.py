#!/usr/bin/env python3
# janitor script 
# cleans up your folders because windows is messy af

import os
import shutil
import argparse
from pathlib import Path

# basic extensions to look for
cats = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".csv", ".md"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
}

def get_cat(ext):
    # just loop through and find where the extension belongs
    for c, extensions in cats.items():
        if ext.lower() in extensions:
            return c
    return "Others" # dump everything else here

def clean_it_up(target_dir, dry_run=False):
    target = Path(target_dir)
    
    if not target.exists() or not target.is_dir():
        print(f"[!] bro that's not a real folder: {target_dir}")
        return

    print(f"[*] starting scan on {target.resolve()}...")
    
    count = 0
    
    for f in target.iterdir():
        if f.is_dir():
            continue # ignore folders obviously
            
        # don't move the script itself lol
        if f.name == os.path.basename(__file__):
            continue

        c = get_cat(f.suffix)
        cat_folder = target / c
        
        # make folder if it doesnt exist
        if not dry_run and not cat_folder.exists():
            cat_folder.mkdir()
            
        dest = cat_folder / f.name
        
        # fix duplicate names (kinda hacky but works)
        n = 1
        while dest.exists():
            dest = cat_folder / f"{f.stem}_{n}{f.suffix}"
            n += 1
            
        print(f" -> moving: {f.name} => {c}/")
        
        if not dry_run:
            shutil.move(str(f), str(dest))
            
        count += 1
        
    if dry_run:
        print(f"\n[*] dry run done. would have moved {count} files.")
    else:
        print(f"\n[*] all done. cleaned up {count} files.")

if __name__ == "__main__":
    # setup args
    parser = argparse.ArgumentParser(description="auto file organizer")
    parser.add_argument("directory", nargs="?", default=".", help="folder to clean")
    parser.add_argument("--dry-run", action="store_true", help="dont actually move stuff")
    
    args = parser.parse_args()
    
    try:
        clean_it_up(args.directory, args.dry_run)
    except KeyboardInterrupt:
        print("\n[!] stopped by user.")
