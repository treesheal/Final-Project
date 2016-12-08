
#need to make it so it returns the whole file, not just the line, into a list.
#creating function to read file, split it at the end of a line, and close file
def f():
    try:
        fin = open('CustomerList.txt')
        contents = fin.read()
        lines = contents.split('\n')
        fin.close()
        return lines
    except:
        print'An error occured while opening file'

#setting file to list
z = f()
data = list(z)
print data

#creating color class
class color:
   BLUE = '\033[34m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

menu_choice = 0

#creating def for selection 1
def choice_one(data):
    try:
        y = 'Y'
        n = 'N'
        id = raw_input('Please Enter User ID: ')
        for item in data:
            userid, first, last, street, city, state, code, phone = item.split(',')

            if id == userid:
                print 'Customer ID: ' + userid
                print 'Customer Name: ' + first, last
                print 'Address: ' + street, city, state, code
                print 'Phone Number: ' + phone
                confirm = raw_input('Confirm (Y/N)')
                if confirm == y:
                    quit()
                elif confirm == n:
                    quit()
                break
    except:
        print 'Customer could not be found. Goodbye.'

#creating def for selection 2
def choice_two(data):
    #get first name
    fn = raw_input("Please enter first name: ")
    first_name = fn.title()
    while len(first_name) < 1 or not str.isalpha(first_name):
        first_name = raw_input(color.BOLD + color.RED + "First name is required, please re-enter." + color.END)
    #get their last name
    ln = raw_input("Please enter last name: ")
    last_name = ln.title()
    while len(ln) < 1 or not str.isalpha(ln):
        ln = raw_input(color.BOLD + color.RED + "Last name is required, please re-enter." + color.END)
    #get street address
    street = raw_input('Please enter street address:  ')
    st = street.title()
    while len(street) < 1:
        street = raw_input('Invalid entry. Please re-enter:  ')
    #get city
    city = raw_input('Please enter city:  ')
    c = city.title()
    while city < 1:
        city = raw_input('Invalid entry. Please re-enter:  ')
    #get state abbreviation
    state = (raw_input('Please enter state abbreviation:  '))
    s = state.upper()
    while len(state) < 1 and len(state) > 2:
        state = raw_input('Invalid. Enter state abbreviation  ')
    #get zip code
    zc = raw_input('Plese enter zip code:  ')
    while len(zc) <5 and len(zc) > 5:
        zc = raw_input('Invalid entry. Enter a 5 digit zip code:  ')
    #get phone number
    ph = raw_input('Please enter phone number; digits only:  ')
    while len(ph) < 10 or len(ph)> 10:
        ph = raw_input('Please enter a vilid 10 digit number:  ')
    #create user id
    newid = (data[-2:-1][0]).split(',')
    new = str(newid[:1]).strip("[']")
    l = list(new)
    l[-4:] = ""
    customer = "".join(l)
    n = int(customer) + 1
    cph = str(n) + (ph[-4:])
    info = cph+ first_name+ last_name+ st + c + s + zc, ph
    info = list(''.join(info))
    customer_info = list(info)
    customer_info = ''.join(customer_info)
    print customer_info


    #creating user output
    print 'Customer Information: '
    print (first_name), last_name
    print st
    print c + ', ' + s + ', ' + zc
    print ph
    print color.BLUE + 'You have been added to our system. Your customer ID is: ' + cph + color.END
    return (customer_info)

#creating def for selection 3
def choice_three():
    print color.BLUE + "Welcome! Please create a new User to use this kiosk." + color.END + "\n"

#creating selection screen function for when user inputs an invalid option
def menu_2():
    menu_choice = 0
    while menu_choice >= 0:
        print "==========================="
        print "  1. " + color.RED + "Existing User" + color.END
        print "  2. " + color.RED + "Add new User" + color.END
        print "  3. " + color.RED + "Continue as Guest" + color.END
        print "==========================="
        choice =raw_input(color.BOLD + color.RED + 'Choose from the available options:   ' + color.END + '\n')
        if choice.strip() not in ['1', '2', '3']:       #testing for good values as strings
            print(color.BOLD + color.RED + 'Invalid selection, re-enter' + color.END)
            menu_choice = 0         #reset to invalid value
        else:
            menu_choice = int(choice)       #if its good convert to int
        if menu_choice == 1:
            choice_one(data)
            quit()
        elif menu_choice == 2:
            info = [(choice_two(data))]
            customer = ''.join(data + info)
            with open('CustomerList.txt', 'wb') as fin:
                for line in customer:
                    fin.write(line)
                    fin.write("\n")
            fin.close()
            quit()
        elif menu_choice == 3:
            choice_three()
            quit()

#creating initial main selection screen
while menu_choice >= 0:
    print ("\n" + color.BOLD+ 'Self Service Customer Kiosk' + color.END + "\n")
    print color.BLUE + "==========================="
    print "  1. " + color.END + "Existing User" + color.BLUE
    print "  2. " + color.END + "Add new User" + color.BLUE
    print "  3. " + color.END+ "Continue as Guest" + color.BLUE
    print "===========================" + color.END
    choice =raw_input('Please choose from the above options:   ' + '\n')
    if choice.strip() not in ['1', '2', '3']:       #testing for good values as strings
        print color.BOLD + color.RED + 'Invalid selection, re-enter:  ' + color.END
        menu_2()
    else:
        menu_choice = int(choice)       #if its good convert to int
    if menu_choice == 1:
        choice_one(data)
        menu_choice = -1
    elif menu_choice == 2:
        info = [(choice_two(data))]
        customer = ''.join(data + info)
        with open('CustomerList.txt', 'wb') as fin:
            for line in customer:
                fin.write(line)
                fin.write("\n")
            fin.close()
            quit()
        menu_choice = -1
    elif menu_choice == 3:
        choice_three()
        menu_choice = -1

