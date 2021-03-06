# Forensics
Python3 forensics and monitoring tools

## Prefetch_v3
Based on [Windows-Prefetch-Parser](https://github.com/PoorBillionaire/Windows-Prefetch-Parser)

Main Features:
- Migrated entirely to Python 3
- Output format: JSON

Prefetch is one of the ways Microsoft has attempted to speed up your Windows experience. Basically, when you first run an application, Windows will store data about it in a PF file in the directory C:\Windows\Prefetch. These files’ names will be the executable’s name followed by a dash and a hash of its location – something like CHROME.EXE-CCF9F3F5.pf.

How does this help a forensic investigator? Well, the file created and file modified times of these PF files are set to the times the program was first and last run. Furthermore, multiple files with the same name could indicate that multiple versions of the program have been run, or that identical files were run from different directories on the system.

Usage:
* python prefetch_v3.py -f c:\windows\prefetch\NOTEPAD.EXE-032BB3D8.pf
* python prefetch_v3.py -d c:\windows\prefetch\

See [docs](https://github.com/PoorBillionaire/Windows-Prefetch-Parser)

## Digito_Verificador_v3
A la hora de hacer investigaciones sobre un vehículo en Argentina, se les solicitará una serie de datos como la patente o dominio más el "Dígito verificador". Al escuchar este término es muy probable que se pregunte cómo obtenerlo, ya que por lo general los dominios sólo muestran una cadena alfanumérica (sin dígito verificador). Aquí, una version en Python 3 para calcularlo y obtenerlo.

Basado en:
[Agip Digito Verificador](https://chrome.google.com/webstore/detail/agip-digito-verificador/mcbihanjokabdgcbickiihbcehjbefkp)


Modo de Uso:
* python digito_verificador_v3.py
