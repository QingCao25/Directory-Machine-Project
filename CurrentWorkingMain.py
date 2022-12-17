from tkinter import *
import tkinter as tk
import os

############################################################
#   Helpful OS Line Commands
#   rmdir - removes dirs
#   makedir - creates dirs
#   chdir - chooses dirs
############################################################

def main():
# Get Directory Information
    Customer_Name = str(input("Enter Customer Name: "))
    Part_ID = str(input("Enter Part Number: "))
    Machines = (input("Enter a Space separated list of Machines: ")).split(" ")

# Initialize key var
    Parent_Dir = "N:/" + Customer_Name + "/" + Part_ID + "/" + Part_ID + ", A"
    REV = "A"

# Check if Setup var is an int

    while True:
        try:
            Setup = int(input("Enter # of Setups?: "))
        except ValueError:
            print("Please Enter a valid number")
            continue
        else:
            break


# Make the Parent Dir with Rev and then go into that directory
    os.chdir("N:/" + Customer_Name)
    os.makedirs(Part_ID + "/" + Part_ID + ", A")
    os.chdir(Parent_Dir)

# Create Dovetail Folder and machine code abrv then go into parent dir
    Create_DoveTail_Dir(Parent_Dir)

    for i in range(1,Setup + 1):
# Create Setup Directories
        Setup_Dir = "S0" + str(i) 
        os.makedirs(Setup_Dir)
        for Machine in Machines: # Cycle Through all machines listed

            os.chdir(Parent_Dir + "/" + Setup_Dir)
            Create_Machine_Dir(Machine, Customer_Name, Parent_Dir, Setup_Dir, Part_ID, REV, i )
            os.chdir(Parent_Dir + "/" + Setup_Dir)
# If loop iteration is at last machine, go to Parent Dir
            if Machine == Machines[len(Machines) - 1]:
                    os.chdir(Parent_Dir)

def Write_Abreviations():
    TextFile = open("MACHINE ABREVIATIONS.txt", "w")
    TextFile.write("\
    MACHINE CODES: \n\
    OKV - OKUMA VERTICAL \n\
    OKH - OKUMA HORIZONTAL \n\
    MORI - MORI HORIZONTAL \n\
    MAZ - MAZAK 3/4 \n\
    MAZ5 - MAZAK 5-AXIS \n\
    MAK - MAKINO \n\
    MX - MX330 \n\
    MAM - MAM72-35V \n\
    HAAS - HAAS \n\
    VX - VX1000")
    TextFile.close()

def Write_File_Format():
    Textfile = open("File Format Instructions.txt", "w")
    Textfile.write("\
    FILE FORMAT: \n\
    \n\
    PART NUMBER (FROM PRINT) \n\
    CUSTOMER REVISION (FROM PRINT) \n\
    SETUP CODE \n\
    ADDITIONAL CLARIFIER (OPTIONAL) \n\
    MACHINE (SEE CODES LISTED BELOW) \n\
    \n\
    EXAMPLE: \n\
    715-101136-214_D_S01AA_MAZ5 \n\
    715-101136-214_D_F01AA_FXT-OP1_MAZ5 - (HERE FXT-OP1 IS ADDED TO CLARIFY WHICH S## THE FIXTURE IS FOR) \n\
    \n\
    SETUP CODE IS A 5 DIGIT CODE: \n\
    DIGIT-1 = TYPE (S = SETUP, F = FIXTURE, D = DOVETAIL) \n\
    DIGITS 2&3 = SEQUENCE OF OPERATION 01 THRU 99 \n\
    DIGITS 4&5 = INTERNAL REVISION CONTROL STARTING AA THRU ZZ \n\
    \n\
    EXAMPLES: 	S01AA = SETUP ONE INITIAL RELEASE \n\
            S02AF = SETUP TWO 6TH REVISION \n\
            F01AA = FIXTURE OP1 INITIAL RELEASE \n\
    \n\
    ADDITIONAL MODIFIERS SHOULD BE LIMITED IN SIZE AND ONLY TO DISTINGUISH FROM BASIC FORMAT \n\
    EXAMPLES: 	TEMP \n\
            FXT-OP1 \n\
            SET1 \n\
            SUB \n\
")
    Textfile.close()

def Write_WorkBook(Part_ID, REV, Setup_Num, Machine):
    File = open(Part_ID + "_" + REV + "_S0" + str(Setup_Num) + "_" + Machine + "_WORKBOOK.xlsx", "w")
    File.close()

def Create_Machine_Dir(Machine, Customer_Name, Parent_Dir, Setup_Dir, Part_ID, REV, i ):

# Create Machine Dir
    os.mkdir(Machine)
    os.chdir("N:/" + Customer_Name + "/" + Part_ID + "/" + Part_ID + ", A" + "/"  + "S0" + str(i) + "/" + Machine)
    os.mkdir("DOWN REV")
    os.makedirs("NC_FILES/"+ Part_ID + "_" + REV + "_S0" + str(i) + "_"+ Machine +"_VERICUT")
    Write_File_Format()
    Write_WorkBook(Part_ID, REV, i, Machine)

def Create_DoveTail_Dir(Parent_Dir):
    if (input(str("Does this part require a dovetail setup? (y/n): ")) == "y"):
        os.mkdir("D01")
        os.chdir("D01")
        os.mkdir("VX")
        os.mkdir("HAAS")
        os.mkdir("MAZ")
        Write_Abreviations()
        os.chdir(Parent_Dir)

main()
#back()