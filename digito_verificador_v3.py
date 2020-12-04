#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : LCAMORO - - 04/12/2020

lcamoro = """
                           ------   LCAMORO   ------
,                                                                               
,                                                                 .@@,          
,                                                               @@@%            
,             @@                                            #@@@,               
,              *@@@@                                     @@@@                   
,                  @@@@                               @@@@                      
,                     @@@@,                       #@@@&                         
,                         @@@@                 @@@@                             
,                            *@@@@          @@@@                                
,                                *@@@@   @@@@                                   
,                                     @@@@&                                     
,                                  @@@(   @@@@@                                 
,                               @@@,          @@@@                              
,                            @@@#                ,@@@%                          
,                         @@@@@%              @@     @@@@@                      
,                       @@@   @@&    @@@@      @@@&  @@@@@@                     
,                     @@@      @@@@@@@           @@@@@    @@@                   
,                   @@@       @@@@@%            @@@@@@      @@@                 
,                 @@@     @@@@@   @@@          @@    @@@      @@@               
,                @@@                                  @@@      @@@              
,               @@                                              @@              
,              @@                                       @@@     @@@             
,             @@@                                     %@@/      @@#             
,             @@        @@                          @@@@        @@              
,             @@         @@@*                  @#@@@@@@&       @@ @@@@@         
,             @@@          .@@@@           @@@@@@@    @@@    @@@      @@@       
,              @@@              @@@@@@@@@@@@    @@@    &@@ ,@@@@        @@@     
,           #@@@ @@@                      @@@    @@      @@@(  ,@@@      #@@    
,         /@@@     @@@@#                   @@    .@@   @@@@@@&    @@@      @@%  
,        @@@         @@@@@@@@(             @@@    @@@@     @@@@@   @@@      @@@ 
,      *@@         @@@       @@@@@@@@@@@@@@@@@/    @@*     @@@ @@@              
,     @@@         @@@        @@            @@@     @@@     @@@   @@#            
,    @@@         @@         @@*            .@@     .@@     @@@    @@@           
,   &@@        .@@         @@@              @@     (@@     @@*                  
,              .@          @@               @@@    %@@    &@@                   
,                                            @@@          @@                    
,                                             @@@       %@@                     
,                                              (@@@  *@@@@                      
,                                                 &@@@                          
"""
print(lcamoro)

import re

def reducir(numero):
    numero = str(numero)
    val = 0

    for x in numero:
        val += int(x)

    if (val > 9):
        return reducir(val)
    else:
        return val

def digito_verificador(codigo):
    # De IZQ a DER, sumar todos los caracteres ubicados en las posiciones impares.
    impares = sum([int(c) for i,c in enumerate(codigo) if not i%2])
    
    # De IZQ a DER, sumar todos los caracteres que están ubicados en las posiciones pares.
    pares = sum([int(c) for i,c in enumerate(codigo) if i%2])
    
    # 'Reducir' un numeros a un solo digito
    part1 = str(reducir(impares))
    part2 = str(reducir(pares))
    
    # Concatenar resultados
    digito = part1 + part2
    
    return digito


def main():
    pares = 0
    impares = 0
    letrasPatente = {"A":"14", "B":"01", "C":"00", "D":"16", "E":"05", "F":"20", "G":"19", "H":"09", "I":"24", "J":"07", "K":"21", "L":"08", "M":"04", "N":"13", "O":"25", "P":"22", "Q":"18", "R":"10", "S":"02", "T":"06", "U":"12", "V":"23", "W":"11", "X":"03", "Y":"15", "Z":"17"}
    pat = input("Nro. Dominio/Patente > ")
    patente = pat.upper().replace(" ", "")

    # Patentes formato: ABC123
    if re.match("[A-Z]*[0-9]*$", patente) != None:
        #Extraigo solo numeros
        nPatente = str(int(''.join(filter(str.isdigit, patente))))
        #Extraigo solo texto/string
        sPatente = str(''.join(filter(str.isalpha, patente)))

        toNum = ""
        for n in sPatente:
            toNum+= letrasPatente[n]
        
        nums = toNum + nPatente

    # Patentes formato: BA321CD
    elif re.match("[A-Z]*[0-9]*[A-Z]*$", patente) != None:
        # Extraigo string parte 1
        fPatente = patente[0:2]
        # Extraigo solo numeros
        nPatente = str(int(''.join(filter(str.isdigit, patente))))
        # Extraigo string parte 2
        lPatente = patente[5:]
        
        ftoNum = ""
        ltoNum = ""
        
        for f in fPatente:
            ftoNum+= letrasPatente[f]
        
        for l in lPatente:
            ltoNum+= letrasPatente[l]
        
        nums = ftoNum + nPatente + ltoNum
    else:
        print ("El formato del dominio/patente deber ser valido. Ejemplo: ABC123 o BA321CD")
    
    # Obtengo DV
    print(digito_verificador(nums))

    
if (__name__  ==  '__main__'):
    main()