import json

def display():
    with open('contacts.json', 'r') as f:
        array = f.read()
        # array = json.dumps(array)
        datastore = json.loads(array)
        with open("contacts.json", "wb") as array:
            array.seek(4, 0)
            array.write( "Python is a great language.\nYeah its great!!\n");

    print("Name          Phone_No          E_mail_ID")
    for i in datastore["contact"]:
        print(i["Name"],"  ",end=" ")
        print(i["Phone_No"],"  ",end=" ")
        print(i["E_mail_ID"])

display()
