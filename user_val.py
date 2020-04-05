# Python Task 2 - User Data Validation
import random
import string

# create empty dictionary to store user data
user_details = {}


def main():  # wrap all codes in a function to be able to loop over
    while True:
        # get details of the user
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")

        # check to make sure names have at least 2 characters
        if len(first_name) < 2 or len(last_name) < 2:
            print('length of name must not be less than 2')
            main()

        # generate a random string of length 5 to add to the password
        def random_string(stringLength=5):
            rand = string.ascii_letters + string.digits
            return ''.join(random.choice(rand) for i in range(stringLength))

        # a function that asks if there is another user
        def another():
            other_user = input("Do you wish to add another user? type yes: ").lower()
            if other_user == 'yes':
                main()  # restart code if there is another user
            else:
                print("Program terminated. Please view details of saved users below.")
                print(user_details)
                exit()

        # extract first 2 and last 2 letters of first & last names respectively and add random string
        rand_password = (first_name[0:2] + last_name[-2:]).lower() + random_string()
        print(f"random password = {rand_password}")

        # ask if user is satisfied with randomly generated password
        user_satisfaction = input("Are you satisfied with the above password? reply with 'Yes' or 'No': ").lower()

        # ask user to enter new password if not satisfied with the randomly generated one
        while user_satisfaction == "no":
            rand_password = input("Please enter a new password: ")
            if len(rand_password) >= 7:
                user = f'First name: {first_name}, Last name: {last_name}, Email: {email}, password: {rand_password}'
                print(user)

                # add the user to the dictionary declared above to form nested dictionary
                user_details[last_name] = {'first name': first_name, 'last name': last_name, 'email': email,
                                           'password': rand_password}

                # call the another function to know if there are more users
                another()

            # if password less than 7
            else:
                print("Your password is less than 7")

        # if user is satisfied with randomly generated password
        else:
            user = f'First name: {first_name}, Last name: {last_name}, Email: {email}, password: {rand_password}'
            print(user)
            # add the user to the dictionary declared above
            user_details[last_name] = {'first name': first_name, 'last name': last_name, 'email': email,
                                       'password': rand_password}
            another()


main()
