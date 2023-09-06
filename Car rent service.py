print("________Lawo Cab Service________")
#Vehicals Data

car01=["Mazda Mini",3,"Non AC"]
car02=["Mini Cooper",3,"Non AC"]
car03=["Toyota Corolla",4,"Non AC"]
car04=["BMW R6",4,"AC"]
car05=["Lancer Evolution 10",4,"AC"]

car=[car01,car02,car03,car04,car05]

van01=["Mazda",6,"Non AC"]
van02=["Toyota",8,"Non AC"]
van03=["Mitsubishi",6,"Non AC"]
van04=["Toyota",8,"AC"]
van05=["Hiace",8,"AC"]

van=[van01,van02,van03,van04,van05]

weel01=["Bajaj",3]
weel02=["TVS",3]
weel03=["Bajaj",3]

weel=[weel01,weel02,weel03]

truck01=["TATA",7]
truck02=["Mahindra",7]
truck03=["Bajaj",7]
truck04=["TATA",12]
truck05=["Mahindra",12]

truck=[truck01,truck02,truck03,truck04,truck05]

lorry01=["TATA",2500]
lorry02=["Mahindra",2500]
lorry03=["Bajaj",2500]
lorry04=["TATA",3500]
lorry05=["Mazda",3500]

lorry=[lorry01,lorry02,lorry03,lorry04,lorry05]

i=0
x=1
a=0
hire=[]
            

while(True):
    #menu
    print("\n(1) Vehicle Details \n(2) Hire Vehical \n(3) Add Vehical \n(4) Delete Vehical \n(5) Exit ")
    path=int(input("Choose path : "))

    #Vehical details
    if(1==path):
        print("""
    o  car : Maximum number of passengers - 3 and 4 | AC/Non AC
    o  van : Maximum number of passengers - 6 and 8 | AC/ Non AC
    o  3wheeler : Maximum number of passengers - 3
    o  truck : Size – 7 ft and 12 ft
    o  lorry : Max load and size - 2500kg and 3500kg""")

    #vehical hire
    elif(2==path):
        category=input("\nChoose Category for hire : ")

        #car
        if("car" == category):
            #check cars availabel
            if(len(car)<=0):
                print("Not Availabel")
                break

            #get details
            pesenger=int(input("Select pasenger (3/4) : "))
            AC=input("Select AC type (AC / Non AC) :")

            #filter cars
            print("")
            while(i<len(car)):
                if(pesenger==car[i][1] and AC==car[i][2]):
                    print(x,". ",car[i][0])
                    hire.append(car[i])
                    x=x+1
                i=i+1
                
            chooseVehical=int(input("\nChoose Car : "))
            chooseVehical=chooseVehical-1

            #hired car
            if(chooseVehical<=len(hire)):
               print("\nYou hired ",hire[chooseVehical][0])
               print("___________________________________________________")
               
               #delete car details in the array
               while(a<len(car)):
                   if(hire[chooseVehical]==car[a]):
                       car.remove(car[a])
                   a=a+1
            else:
                print("\nYour choice is not valid")
                print("___________________________________________________")

        #van
        elif("van" == category):
            #check van available
            if(len(van)<=0):
                print("Not Availabel")
                break
            
            #get details
            pesenger=int(input("Select pasenger (6/8) : "))
            AC=input("Select AC type (AC / Non AC) :")

            #filter vans
            print("")
            while(i<len(van)):
                if(pesenger==van[i][1] and AC==van[i][2]):
                    print(x,". ",van[i][0])
                    hire.append(van[i])
                    x=x+1
                i=i+1

            
            chooseVehical=int(input("\nChoose Van : "))
            chooseVehical=chooseVehical-1
            
            #hired van
            if(chooseVehical<=len(hire)):
               print("\nYou hired ",hire[chooseVehical][0])
               print("___________________________________________________")
               
               #delete van details in the array
               while(a<len(van)):
                   if(hire[chooseVehical]==van[a]):
                       van.remove(van[a])
                   a=a+1
            else:
                print("\nYour choice is not valid")
                print("___________________________________________________")

        #3wheeler
        elif("3wheeler" == category):
            #check 3wheeler available
            if(len(weel)<=0):
                print("Not Availabel")
                break

            #filter 3weelers
            print("")
            while(i<len(weel)):
                print(x,". ",weel[i][0])
                x=x+1
                i=i+1

            chooseVehical=int(input("\nChoose 3Wheeler : "))
            chooseVehical=chooseVehical-1

            #hired 3wheeler
            if(chooseVehical<=len(weel)):
               print("\nYou hired ",weel[chooseVehical][0])
               print("___________________________________________________")
               
               #delete 3wheeler details in the array
               weel.remove(weel[chooseVehical])

            else:
                print("\nYour choice is not valid")
                print("___________________________________________________")

        #truck
        elif("truck" == category):
            #check truck available
            if(len(truck)<=0):
                print("Not Availabel")
                break

            #get details
            size=int(input("Select truck size (7ft/12ft) : "))

            #filter truck
            print("")
            while(i<len(truck)):
                if(size==truck[i][1]):
                    print(x,". ",truck[i][0])
                    hire.append(truck[i])
                    x=x+1
                i=i+1

            chooseVehical=int(input("\nChoose truck : "))
            chooseVehical=chooseVehical-1

            #hired truck
            if(chooseVehical<=len(hire)):
               print("\nYou hired ",hire[chooseVehical][0])
               print("___________________________________________________")

               #delete truck details in the array
               while(a<len(truck)):
                   if(hire[chooseVehical]==truck[a]):
                       truck.remove(truck[a])
                   a=a+1
            else:
                print("\nYour choice is not valid")
                print("___________________________________________________")

        #lorry
        elif("lorry" == category):
            #check lorry available
            if(len(lorry)<=0):
                print("Not Availabel")
                break

            #get details
            load=int(input("Select lorry load (2500kg/3500kg) : "))
            
            #filter lorry
            print("")
            while(i<len(lorry)):
                if(load==lorry[i][1]):
                    print(x,". ",lorry[i][0])
                    hire.append(lorry[i])
                    x=x+1
                i=i+1

            chooseVehical=int(input("\nChoose lorry : "))
            chooseVehical=chooseVehical-1

            #hired lorry
            if(chooseVehical<=len(hire)):
               print("\nYou hired ",hire[chooseVehical][0])
               print("___________________________________________________")

               #delete lorry details in the array
               while(a<len(lorry)):
                   if(hire[chooseVehical]==lorry[a]):
                       lorry.remove(lorry[a])
                   a=a+1
               
            else:
                print("\nYour choice is not valid")
                print("___________________________________________________")

    #Add vehicals
    elif(3==path):
        category=input("\nChoose Category for Addition : ")

        if("car" == category):
            name=input("Input vehical name : ")
            pasen=int(input("Input passenger (3/4) : "))
            ac=input("AC type (AC/Non AC) : ")

            newcar=[name,pasen,ac]
            car.append(newcar)

        elif("van" == category):
            name=input("Input vehical name : ")
            pasen=int(input("Input passenger (6/8) : "))
            ac=input("AC type (AC/Non AC) : ")

            newvan=[name,pasen,ac]
            van.append(newvan)

        elif("3wheeler" == category):
            name=input("Input vehical name : ")
            passengers=3

            newweel=[name,passengers]
            weel.append(newweel)

        elif("truck" == category):
            name=input("Input vehical name : ")
            size=int(input("Input truck size (7ft/12ft) : "))

            newtruck=[name,size]
            truck.append(newtruck)

        elif("lorry" == category):
            name=input("Input vehical name : ")
            load=int(input("Input lorry load (2500kg/3500kg) : "))

            newlorry=[name,load]
            lorry.append(newlorry)

    #delete vehicals
    elif(4==path):
        category=input("\nChoose Category for Delete : ")

        if("car" == category):
            while(i<len(car)):
                print(x,". ",car[i][0])
                x=x+1
                i=i+1

            chooseVehical=int(input("\nChoose car : "))
            chooseVehical=chooseVehical-1
            car.remove(car[chooseVehical])

        elif("van" == category):
            while(i<len(van)):
                print(x,". ",van[i][0])
                x=x+1
                i=i+1

            chooseVehical=int(input("\nChoose van : "))
            chooseVehical=chooseVehical-1
            van.remove(van[chooseVehical])

        elif("3wheeler" == category):
            while(i<len(weel)):
                print(x,". ",weel[i][0])
                x=x+1
                i=i+1

            chooseVehical=int(input("\nChoose 3wheeler : "))
            chooseVehical=chooseVehical-1
            weel.remove(weel[chooseVehical])

        elif("truck" == category):
            while(i<len(truck)):
                print(x,". ",truck[i][0])
                x=x+1
                i=i+1

            chooseVehical=int(input("\nChoose truck : "))
            chooseVehical=chooseVehical-1
            truck.remove(truck[chooseVehical])

        elif("lorry" == category):
            while(i<len(lorry)):
                print(x,". ",lorry[i][0])
                x=x+1
                i=i+1

            chooseVehical=int(input("\nChoose lorry : "))
            chooseVehical=chooseVehical-1
            lorry.remove(lorry[chooseVehical])

    #Finish program
    elif(5==path):
        break

