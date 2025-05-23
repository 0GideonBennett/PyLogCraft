#Script 1: Allows one to find all the Errors within a log file based on a keyword. 
#Script 2: Allow you to combine two different log files to save on time



#Variables (User Input and Storage List ) and Instrtions
print( "1 = Error-Finder" )
print( "2 = Log Combiner")
try:
    selection = int(input("Choose your Script (Enter # only) :"))
except ValueError:
    print("Please enter number 1 of 2")
    exit()

if selection == 1: 
    log =input("Enter Log name: ")
    keyword = input("Enter the Keyword you wish to detect (i.e ERROR):")
    deploy_errors = []
    #Script one funtion: Scanning Entered Log -> Saving it to a list -> Display it 
    def scan(log,keyword):
        try:
            reader = open(log, "r") 
            for line in reader:
                if keyword in line:
                    deploy_errors.append(line.strip())
            print(f"{keyword} Lines:\n" , deploy_errors)
        except FileNotFoundError:
            print(f"{log} does not exist in current dir.")
    scan(log,keyword)
elif selection == 2:

    log1 = input("Enter the first log name: ")
    log2 = input("Enter the second log name: ")
    combinedFileName = input("Enter the name of the combined file: ")
    def combine(log1, log2,combinedFileName):
        try:
            with open(log1,"r") as log1_obj:  #convert log 1 from a str to an object ( bc its tehdinally just a name and not somethign we can actually read content from) 
                log1Content = log1_obj.read() # now save the contents  of the newly created log1  object to a var
            with open(log2, "r") as log2_obj: # ^ditto
                log2Content =log2_obj.read()  #^ditto
            with open(combinedFileName,"w") as finalLog_obj: #create the a combined file obj 
                finalLog_obj.write(log1Content + "Next Log Start:\n" + log2Content)
            print(f"{combinedFileName} has been saved to your current directory!")
        except FileNotFoundError as log_obj:
            print(f"{log_obj} the log needed to make the log an object does not exsist")
    combine(log1,log2,combinedFileName)

else: 
    print("That is an invalid choice please try again")


     
#V2 Consideraiton:
# Make it so the user can say yes or no to restarting the script