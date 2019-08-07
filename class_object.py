# This program is used to class, object and classmethods , staticmethods
class Office:

    def __init__(self, name, phone,company):
            self.name = name
            self.phone= phone
            self.company= company
    #
    # def adding_friend(self,freind_name):  #This normaly run in this class
    #         return Office(freind_name, self.company, self.phone)

    @classmethod  # Used to Inherit this method in child class
    def adding_friend(cls, origin, freind_name, *emp): # origin is hold object of that class and *emp is has list of argument pass
            return cls(freind_name, origin.company, origin.phone, *emp)

    @classmethod  # Classmethod has pass argument as Class
    def we_are_on_office(cls):
        print("We all are in office only")
        print("I am in class {}".format(cls))

    @staticmethod  # Staticmethod has pass no argument
    def we_are_out_office():
        print("We all are out of office only")
#
# think = Office("Krishoth", "7299070171", "Think")
# friend = think.adding_friend("Pradeep")
# print(friend.name)
# print(friend.phone)
# print(friend.company)


class Sub_Office(Office): # Inheritance Office in Sub_Office class

    def __init__(self, name, phone, company, emp_no,desigination):
        super().__init__(name, phone, company)
        self.emp_no = emp_no
        self.desigination=desigination


think = Sub_Office("Krishoth", "7299070171", "Think",122, "Software Developer")
more= Sub_Office("Pradeep", "9092621404", "More", 123,"Software Developer")

print(think.name)
print(think.phone)
think.we_are_on_office()
think.we_are_out_office()

print(more.name)
print(more.phone)
Sub_Office.we_are_on_office()
Office.we_are_out_office()


friend = Sub_Office.adding_friend(think,"Jayanth",112,"Team Lead")
print(friend.name)
print(friend.phone)
print(friend.company)
print(friend.emp_no)
print(friend.desigination)
