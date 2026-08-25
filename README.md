# janitor

A quick and straightforward file organizer built using Python.

If your downloads folder is a mess this script will check all the files sort them based on their file types make subfolders and automatically place everything in the right place.

## Usage

Run it in the folder:

```bash
python janitor.py
```

Run it on a specific folder:

```bash
python janitor.py "C:\Users\Name\Downloads"
```

See what changes would happen without actually moving any files (Dry Run):

```bash
python janitor.py --dry-run
```

## File Types Supported

**Images:** .jpg, .png, .gif and more.

**Videos:** .mp4, .mkv, .mov and more.

**Audio:** .mp3, .wav, .flac. More.

**Documents:** .pdf, .docx, .txt, .csv and more.

**Archives:** .zip, .rar, .7z and more.

**Executables:** .exe, .msi, .bat. More.

**Code:** .py, .js, .json, .css and more.

**Others:** Any files that do not fit into the categories.

## License

MIT
