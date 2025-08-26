import time 

def vacuum_cleaning(dirt,vacuum):
    while (dirt[0] == True) or (dirt[1] == True):
        if vacuum[0] == True:
            print("Vacuum Cleaner is in room A \n")
            time.sleep(3)
            
            if dirt[0] == True:
                print("Dirt found in room A \n")
                time.sleep(3)
                
                print("Cleaning dirt in room A \n")
                time.sleep(3)  
                
                print("Cleaning Complete...\n\nNow moving to room B \n")
                time.sleep(3)  
                
                dirt[0] = False
                vacuum[0] = False 
                vacuum[1] = True
            else:
                print("No dirt found in room A \n")
                time.sleep(3)
                
                print("Moving to room B \n")
                time.sleep(3)
                
                vacuum[0] = False 
                vacuum[1] = True
                
        else:
            print("Vacuum Cleaner is in room B \n")
            time.sleep(3)
            
            if dirt[1] == True:
                print("Dirt found in room B \n")
                time.sleep(3)
                
                print("Cleaning dirt in room B \n")
                time.sleep(3)
                
                print("Cleaning Complete...\n\nNow moving to room A \n")
                time.sleep(3)
                
                dirt[1] = False
                vacuum[0] = True 
                vacuum[1] = False
            else:
                print("No dirt found in room B \n")
                time.sleep(3)
                
                print("Moving to room A \n")
                time.sleep(3)
                
                vacuum[0] = True 
                vacuum[1] = False
                
    print("The rooms are clean :) \n\n")
    
def main():
    dirt_list = [ False , True ]
    vaccum_position = [ True , False ]
    vacuum_cleaning(dirt_list , vaccum_position)

main() 