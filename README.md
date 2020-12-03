# Forensics
Python3 forensics and monitoring tools

# Prefetch_v3.py
Based on https://github.com/PoorBillionaire/Windows-Prefetch-Parser

Main Features:
- Migrated entirely to Python 3
- Output format: JSON

Prefetch is one of the ways Microsoft has attempted to speed up your Windows experience. Basically, when you first run an application, Windows will store data about it in a PF file in the directory C:\Windows\Prefetch. These files’ names will be the executable’s name followed by a dash and a hash of its location – something like CHROME.EXE-CCF9F3F5.pf.

How does this help a forensic investigator? Well, the file created and file modified times of these PF files are set to the times the program was first and last run. Furthermore, multiple files with the same name could indicate that multiple versions of the program have been run, or that identical files were run from different directories on the system.
