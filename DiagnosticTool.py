# Calvin Zug
# ctzug@wm.edu
# 7/10/2020
# Project 2: Fever Diagnostic Tool
# 
# This is a basic medical diagnostic tool which will ask questions about symptoms of a user.
# Based off the user's responses the program will show the user's syptoms as well as a possible
# diagnosis. The user will then be asked if they would like to run the program again, and the 
# program will continue until the user answers no.
# 

#Create intial variable
run_again = "y"
diagnosis_type = 0
diagnosis =  ""
symptoms = "\nSymptoms\n"

#Funtion made to streamline selecting the proper diagnosis
def possible_diagnosis():
    if diagnosis_type == 1:
        print("Diagnosis\n*Possibilities include pneumonia or infection of airways\n") 
    elif diagnosis_type == 2:
        print("Diagnosis\n*Possibilities include meningitis\n") 
    elif diagnosis_type == 3:
        print("Diagnosis\n*Possibilities include viral infection\n") 
    elif diagnosis_type == 4:
        print("Diagnosis\n*Possibilities include digestive tract infection\n") 
    elif diagnosis_type == 5:
        print("Diagnosis\n*Possibilities include throat infection\n") 
    elif diagnosis_type == 6:
        print("Diagnosis\n*Possibilities include kidney infection\n") 
    elif diagnosis_type == 7:
        print("Diagnosis\n*Possibilities include urinary tract infection\n") 
    else: 
        print("Diagnosis\n*Insufficient information to list possibilities\n")

#   Main while loop that runs at least once, will end once the user does not want to input another set of symptoms
while run_again.lower() == "y":
    print("\nFever Diagnostic Tool\n---------------------")
    print("\nPlease note that this program performs no true diagnostic activity.")  
    print("No decisions should be made based upon the tool's")
    print("analysis.  If you have a fever, you should contact your doctor.\n")
    fever = input("Do you have a fever (y,n): ")
    print(fever)

    #Checking for a fever
    if fever.lower() == "y":
        symptoms += ("*Fever\n")
        
        #Checking for coughing
        coughing = input("Are you coughing (y,n): ")
        print(coughing)
        if coughing.lower() == "y":
            symptoms += ("*Coughing\n")

            #Checking if short of breath or wheezing or coughing up phlegm
            wheezing = input("Are you short of breath or wheezing or coughing up phlegm? (y,n): ")
            print(wheezing)
            if wheezing.lower() == "y":
                symptoms += ("*Short of breath or wheezing or coughing up phlegm\n")
                diagnosis_type = 1
                        
            #Checking for a headache
            elif wheezing.lower() == "n":
                headache = input("Do you have a headache (y,n): ")
                print(headache)            
                if headache.lower() == "y":
                    symptoms += ("*Headache\n")
                    diagnosis_type = 3
                            
                #Checking for sore throat
                elif headache.lower() == "n": 
                    sore_throat = input("Do you have a sore throat (y,n): ")
                    print(sore_throat)            
                    if sore_throat.lower() =="y":
                        symptoms += ("*Sore throat\n")
                        diagnosis_type = 5
                                                
                    #Checking for a back pain just above the waist with chills and fever
                    elif sore_throat.lower() =="n":
                        back_pain = input("Do you have back pain just above the waist with chills and fever (y,n): ")
                        print(back_pain)
                        if back_pain.lower() =="y":
                            symptoms += ("*Back pain just above the waist with chills and fever\n")
                            diagnosis_type = 6
                        
                        #Checking for pain or frequency urinating
                        elif back_pain.lower() =="n":
                            urinating = input("Do you have pain urinating or are urinating more often (y,n): ")
                            print(urinating)            
                            if urinating.lower() =="y":
                                symptoms += ("*Pain urinating or are urinating more often\n")
                                diagnosis_type = 7

#Elses used in case letter other than "y" or "n" is typed
                            else:
                                diagnosis_type = 0
                        else:
                            diagnosis_type = 0
                    else:
                        diagnosis_type = 0
                else:
                    diagnosis_type = 0
        
        #Checking for headache
        elif coughing.lower() == "n":
            headache = input("Do you have a headache (y,n): ")
            print(headache)            
            if headache.lower() == "y":
                symptoms += ("*Headache\n")

                #Checking for pain when bending head forward, nausea or vomiting, bright light hurting eyes, drowsiness, or confusion
                misc = input("Are you experiencing pain when bending head forward, nausea or vomiting, bright light hurting eyes, drowsiness, or confusion (y,n): ")
                print(misc) 
                if misc.lower() =="y":
                    symptoms += ("*Pain when bending head forward, nausea or vomiting, bright light hurting eyes, drowsiness, or confusion\n")
                    diagnosis_type = 2 
                else:
                    diagnosis_type = 0
            
            #Checking for vomiting and diarrhea
            if headache.lower() == "n" or misc.lower() =="n":
                vomit = input("Are you vomiting or have had diarrhea (y,n): ")
                print(vomit)            
                if vomit.lower() =="y":
                    symptoms += ("*Vomiting and diarrhea\n")
                    diagnosis_type = 4
# Elses used in case letter other than "y" or "n" is typed
                else:
                    diagnosis_type = 0
            else:
                diagnosis_type = 0
        else:
            diagnosis_type = 0
            
    else:
        symptoms += ("*None\n")
        diagnosis_type = 0

# Prints out the users syptoms, gives a possible diagnosis, resets the variable, 
# and asks the user if they would like to run the program again
    print(symptoms)
    possible_diagnosis()
    symptoms = "\nSymptoms\n"
    run_again = input("Would you like to input another set of symptoms?: ")
    print(run_again)




