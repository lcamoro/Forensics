#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : [Q]3rV[0]

# Modified by LCAMORO - 04/12/2020 - Migrated to Python 3 + New extraction method for Numbers/Chars.

import re

def main():
    pares = 0
    impares = 0
    letrasPatente = {"A":"14", "B":"01", "C":"00", "D":"16", "E":"05", "F":"20", "G":"19", "H":"09", "I":"24", "J":"07", "K":"21", "L":"08", "M":"04", "N":"13", "O":"25", "P":"22", "Q":"18", "R":"10", "S":"02", "T":"06", "U":"12", "V":"23", "W":"11", "X":"03", "Y":"15", "Z":"17"}
    pat = input("Nro. Dominio/Patente > ")
    patente = pat.upper()

    if re.match("[A-Z]*[0-9]*[A-Z]*?$", patente) != None:
        # LCAMORO
        nPatente = str(int(''.join(filter(str.isdigit, patente))))
        sPatente = str(''.join(filter(str.isalpha, patente)))
        
        toInt = ""
        for n in sPatente:
            toInt+= letrasPatente[n]
        
        nums = toInt + nPatente
        
        for n in range(len(nums)):
            if (n%2 == 0):
                pares += int(nums[n])
            else:
                impares += int(nums[n])

        while len(str(pares)) != 1:
            dp = 0
            for p in str(pares):
                dp += int(p)
            
            pares = dp
          
        while len(str(impares)) != 1:
            di = 0
            for i in str(impares):
                di += int(i)
            
            impares = di
       
        print ("| Patente: %s | DV: %s%s |" % (patente, pares, impares))

    else:
        print ("[*] Error, Asegurese de que el formato del dominio/patente es valido. Ejemplo: GTD125")
       
if (__name__  ==  '__main__'):
    main()