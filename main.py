print "let's get started"
spy_name = raw_input("Enter your name here.")
# '+' denotes the process of concatination.
spy_salutation = raw_input("What should we call you (Mr. or Ms.)?")
spy_name = spy_salutation + " " + spy_name
# parsing take place in above command, reading right to left.
# considering the priority of operators from right to left.
print "Identification Started......"
# Need Time interval for the above code
print "User Identified."
print "welcome\t" + spy_name

