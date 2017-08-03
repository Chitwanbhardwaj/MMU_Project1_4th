import time
print "****SPY SEE****"
spy_name = raw_input("Enter your assigned name here.")
# '+' denotes the process of concatination.
spy_salutation = raw_input("What should we call you (Mr. or Ms.)?")
# Needs to modify the above code..
if len(spy_name) > 0 and len(spy_salutation) > 0 :
    print 'Input Taken'
    spy_name = spy_salutation + " " + spy_name
# parsing take place in above command, reading right to left.
# considering the priority of operators from right to left.
    print "Identification Started......"
    start = time.time()
    time.sleep(3)
    done = time.time()
# Need Time interval for the above code
    print "User Identified."
    print "welcome\t" + spy_name
    print "Alright\t" + spy_name + "\nBefore proceeding, Lets talk little more about you."
else:
    print 'Authentication failed'
