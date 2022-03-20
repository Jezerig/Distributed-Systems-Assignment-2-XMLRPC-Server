# xmlrpc_server.py
# Jesse Pasanen 0545937
# Distributed Systems Assignment 2
# Sources:
# https://cewing.github.io/training.codefellows/assignments/day12/xmlrpc.html
# https://stackoverflow.com/questions/28813876/how-do-i-get-pythons-elementtree-to-pretty-print-to-an-xml-file
# https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

from xmlrpc.server import SimpleXMLRPCServer
import xml.etree.ElementTree as ET

# used to sent notes back to the client
class Note:
    note_name = ""
    note_text = ""
    note_timestamp = ""

address = ('localhost', 1234)
server = SimpleXMLRPCServer(address)

# Adding new note to the database mock
def new_note(note_topic, note_name, note_text, note_timestamp):
    topic = None
    server_response = "New note added."
    # getting data from the database.xml and creating xml tree
    tree = ET.parse('database.xml')
    # root of xml tree
    root = tree.getroot()
    # used to format text when writing into the xml-file
    ET.indent(tree, space="\t", level=0)

    # looks through all the topics in the xml file
    for xml_topic in root:
        # if the topic already exists, the topic variable is set as the one found
        if(str(xml_topic.attrib['name']) == str(note_topic)):
            topic = xml_topic
    # if the topic doesn't exist, a new entry is created
    if(not(topic)):
        topic = ET.SubElement(root, "topic", attrib={"name": note_topic})
    # note added as a subelement under topic
    note = ET.SubElement(topic, "note", attrib={"name": note_name})
    # text and timestamp added as a subelements under note
    text = ET.SubElement(note, "text")
    text.text = note_text
    timestamp = ET.SubElement(note, "timestamp")
    timestamp.text = note_timestamp
    # writing the new note into the xml-file
    tree.write("database.xml", encoding="utf-8")
    return server_response

# gets all the notes under the topic the user has given
def get_notes(search_topic):
    list_of_notes = []
    tree = ET.parse('database.xml')
    root = tree.getroot()
    # looks for the topic
    for topic in root:
        if(str(topic.attrib['name']) == str(search_topic)):
            # goes through all the notes in the topic and add them to the list of notes
            for note in topic:
                new_note = Note()
                new_note.name = note.attrib["name"]
                new_note.text = note.find('text').text
                new_note.timestamp = note.find("timestamp").text
                list_of_notes.append(new_note)
    # return all the notes under the wanted topic as a list
    return list_of_notes

# adds functions so that the clients can use them
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