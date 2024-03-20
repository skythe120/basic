#command examples 1d20, 4d6, 1d6+3, 2d6+3<5
import random
x = 'hi'
breakme = []


def checkmate(x):
    ErrorHandler = ' '
    dgood = ' '
    lt = ' ' 
    gt = ' ' 
    pl = ' ' 
    mn = ' ' 
    if('d' not in x):
        print("Dice not found! Example: 3d6")
        ErrorHandler = True
    elif('+' in x and '-' in x):
        print("Can't have + and - in same roll! eg 3d6+3")
        ErrorHandler = True
    elif('<' in x and '>' in x):
        print("Can't have < and > in same roll! eg 3d6>4")
        ErrorHandler = True
    else:
        if('d' in x):
            try:
                breakdicenumber = x.split("d")
                NumberOfDice = int(breakdicenumber[0])
                x = breakdicenumber[1]
                dgood = True
            except:
                print("----Error in syntax---")
                print("Example Syntax 3d6")   
                ErrorHandler = True
        if('<' in x):
            try:
                lt = True
                gt = False
                breakgtltnumber = x.split("<")
                Numbergtlt = int(breakgtltnumber[1])
                x = breakgtltnumber[0]
            except:
                print("----Error in syntax---")
                print("Example Syntax 3d6<4")
                ErrorHandler = True
        elif('>' in x):
            try:
                lt = False
                gt = True
                breakgtltnumber = x.split(">")
                Numbergtlt = int(breakgtltnumber[1])
                x = breakgtltnumber[0]
            except:
                print("----Error in syntax---")
                print("Example Syntax 3d6<>")
                ErrorHandler = True
        if('+' in x):
            try:
                pl = True
                mn = False
                breakplmn = x.split("+")
                Numberplmn = int(breakplmn[1])
                x = breakplmn[0]
                
            except:
         
                print("----Error in syntax---")
                print("Example Syntax 3d6+4")
                ErrorHandler = True
        elif('-' in x):
            try:
                pl = False
                mn = True
                breakplmn = x.split("-")
                Numberplmn = int(breakplmn[1])
                x = breakplmn[0]
            except:
         
                print("----Error in syntax---")
                print("Example Syntax 3d6-4")
                ErrorHandler = True
        try:
            x = int(x)
        except:
            Errorhandler = True
                
    
    if(ErrorHandler == True):
        print("Error Handler Triggered")
    else:
        i = 0
        total = []      
        while(i < NumberOfDice):
            y = x + 1
            dice = random.randrange(1, y)
            total.append(dice)
            i = i + 1
        
        if(gt == True or lt == True):
            gtltfilter = []
            if(gt == True):
                for i in total:
                    if(i > Numbergtlt):
                        gtltfilter.append(i)
                total = gtltfilter
                if len(gtltfilter) > 0:
                    print(f"Rolled: {gtltfilter}")
            elif(lt == True):
                for i in total:
                    if(i < Numbergtlt):
                        gtltfilter.append(i)
                total = gtltfilter
                if len(gtltfilter) > 0:
                    print(f"Rolled: {gtltfilter}")
                
        
        if(gt == True and not total or lt == True and not total):
            print("0")
        
        elif(pl == True or mn == True):
            dcounter = 0
            grandtotal = 0
            tlen = len(total)
            if(pl == True):
                while(dcounter < tlen):
                    grandtotal = grandtotal + total[dcounter]
                    dcounter = dcounter + 1
                grandtotal = grandtotal + Numberplmn
                print(grandtotal)
            elif(mn == True):
                while(dcounter < tlen):
                    grandtotal = grandtotal + total[dcounter]
                    dcounter = dcounter + 1
                grandtotal = grandtotal - Numberplmn
                print(grandtotal)
        else:
            dcounter = 0
            grandtotal = 0
            tlen = len(total) 
            while(dcounter < tlen):
                    grandtotal = grandtotal + total[dcounter]
                    dcounter = dcounter + 1
            print(f"Grand Total: {grandtotal}")
                
  
    
while True:
    x = input("Roll Commmand: ")
    checkmate(x)
    
