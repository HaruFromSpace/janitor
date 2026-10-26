# janitor

A quick and straightforward file organizer built using Python.

If your Downloads folder is a mess, janitor sorts every file into a subfolder by type (Images, Videos, Documents and so on). It only moves files in the top level of the folder and leaves existing subfolders alone. If a file with the same name is already there, the new one gets a number added instead of overwriting it.

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

**Images:** .jpg, .png, .gif, .webp and others

**Videos:** .mp4, .mkv, .mov, .webm and others

**Audio:** .mp3, .wav, .flac, .m4a

**Documents:** .pdf, .docx, .txt, .csv and others

**Archives:** .zip, .rar, .7z, .tar, .gz

**Executables:** .exe, .msi, .bat

**Code:** .py, .js, .html, .css, .json

**Others:** anything that doesn't fit the groups above

## License

MIT
