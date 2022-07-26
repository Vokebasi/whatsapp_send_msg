import pywhatkit
import os

def send_message_inst():
	mobile = input("Номер получателя: ")
	message = input("Текст сообщения: ")

	pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)


def main():
	send_message_inst()

if __name__ == "__main__":
	main()