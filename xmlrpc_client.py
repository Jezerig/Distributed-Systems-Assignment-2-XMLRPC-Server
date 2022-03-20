# xmlrpc_client.py
# Jesse Pasanen 0545937
# Distributed Systems Assignment 2
# Sources:
# https://cewing.github.io/training.codefellows/assignments/day12/xmlrpc.html
# https://www.programiz.com/python-programming/datetime/current-datetime
# https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client

import xmlrpc.client
from datetime import datetime

proxy = xmlrpc.client.ServerProxy('http://localhost:1234')

def menu():
    while(True):
        print("\nAvailable choices: ")
        print("0) Exit")
        print("1) Add a new note to the database")
        print("2) Get notes for a certain topic from the database")
        try:
            choice = int(input("Choice: "))
            if (choice > 2 or choice < 0):
                print("Invalid choice. Try again.")
                continue
            print("")
            break
        except KeyboardInterrupt:
            print("Keyboard interrupt. Exiting...")
            exit(1)
        except:
            print("Invalid choice. Try again.")
    return choice

def note_user_input():
    while(True):
        topic = str(input("Give a topic for the note: "))
        if (len(topic.strip()) > 0):
            break
        else:
            print("Please give a topic for the note.")

    while(True):
        text = str(input("Write the content of the note: "))
        if (len(text.strip()) > 0):
            break
        else:
            print("The content of the note is empty. Please write something.")

    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y - %H:%M:%S")
    return topic, text, timestamp

def main():
    print("\nWelcome!")
    print("With this program you can add/fetch notes to/from a database.")
    print("The notes are sorted by topic.")
    while(True):
        choice = menu()
        if (choice == 0):
            print("Exiting...")
            exit(0)
        elif (choice == 1):
            topic, text, timestamp = note_user_input()
            try:
                print(str(proxy.new_note(topic, text, timestamp)))
            except Exception as e:
                print("An error occurred while creating new note.")
                print("Error: " + str(e))
        elif (choice == 2):
            topic = str(input("Give topic for notes: "))
            try:
                print("Looking for notes with topic the '{0}'".format(topic))
                print(str(proxy.get_notes(topic)))
            except Exception as e:
                print("An error occurred while fetching notes from the database.")
                print("Error: " + str(e))
        else:
            print("An error occurred.")
            exit(1)

if __name__ == '__main__':
    main()