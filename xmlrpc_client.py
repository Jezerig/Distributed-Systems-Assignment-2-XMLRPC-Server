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
        note_topic = str(input("Give a topic for the note: "))
        if (len(note_topic.strip()) > 0):
            break
        else:
            print("Please give a topic for the note.")

    while(True):
        note_name = str(input("Give a name for the note: "))
        if (len(note_name.strip()) > 0):
            break
        else:
            print("Please give a topic for the note.")

    while(True):
        note_text = str(input("Write the content of the note: "))
        if (len(note_text.strip()) > 0):
            break
        else:
            print("The content of the note is empty. Please write something.")

    now = datetime.now()
    note_timestamp = now.strftime("%d/%m/%Y - %H:%M:%S")
    return note_topic, note_name, note_text, note_timestamp

def parse_notes(notes):
    if (len(notes) == 0):
        print("No notes available.")
    else:
        print("List of notes found: \n")
    for note in notes:
        print("Name: " + note['name'])
        print("Text: " + note['text'])
        print("Timestamp: " + note['timestamp'])
        print("")

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
            note_topic, note_name, note_text, note_timestamp = note_user_input()
            try:
                print(str(proxy.new_note(note_topic, note_name, note_text, note_timestamp)))
            except Exception as e:
                print("An error occurred while creating new note.")
                print("Error: " + str(e))
        elif (choice == 2):
            search_topic = str(input("Give topic for notes: "))
            try:
                print("Looking for notes with the topic '{0}'\n".format(search_topic))
                parse_notes(proxy.get_notes(search_topic))
            except Exception as e:
                print("An error occurred while fetching notes from the database.")
                print("Error: " + str(e))
        else:
            print("An error occurred.")
            exit(1)

if __name__ == '__main__':
    main()