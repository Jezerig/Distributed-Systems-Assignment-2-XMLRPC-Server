# xmlrpc_server.py
# Jesse Pasanen 0545937
# Distributed Systems Assignment 2
# Sources:
# https://cewing.github.io/training.codefellows/assignments/day12/xmlrpc.html

from xmlrpc.server import SimpleXMLRPCServer

address = ('localhost', 1234)
server = SimpleXMLRPCServer(address)

def new_note(topic, text, timestamp):
    response = "New note added."
    # search XML for topic
    # if topic found add text below it
    # if not, create new topic and text below it
    return response

def get_notes(topic):
    # search XML for topic and get the notes
    # return notes to user
    return "NOTES"


server.register_function(new_note)
server.register_function(get_notes)

if __name__ == '__main__':
    try:
        print("Server running on {0}:{1}".format(address[0], address[1]))
        print("Close server using Ctrl+C")
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Server closed.")