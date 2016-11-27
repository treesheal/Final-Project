#creating color class
class color:
   BLUE = '\033[34m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

#getting data from user
def get_data():
    #get their first name and validate
    first_name = raw_input("Please enter first name: ")
    while len(first_name) < 1 or not str.isalpha(first_name):
        first_name = raw_input(color.BOLD + color.RED + "First name is required, please re-enter." + color.END)

    #get their last name
    last_name = raw_input("Please enter last name: ")
    while len(last_name) < 1 or not str.isalpha(last_name):
        last_name = raw_input(color.BOLD + color.RED + "Last name is required, please re-enter." + color.END)
    return first_name, last_name

menu_choice = 0

#setting new user list
new_user = []
existing_users = new_user

#creating def for selection 1
def choice_one():
    for (first_name, last_name) in existing_users:
        print(first_name+ ", " +last_name)
    print"\n"
    #menu_choice = -1

#creating def for selection 2
def choice_two():
    new_user.append(get_data())
    print color.BLUE + 'You have been added to our system. Select Existing User during your future interactions.' + color.END



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
            choice_one()
            quit()
        elif menu_choice == 2:
            choice_two()
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
        choice_one()
        menu_choice = -1
    elif menu_choice == 2:
        choice_two()
        menu_choice = -1
    elif menu_choice == 3:
        choice_three()
        menu_choice = -1

