class Menu_list(object):
 def __init__(self,information_1,information_2,information_3,information_4,password):
     self.information_1=information_1
     self.information_2=information_2
     self.information_3=information_3
     self.information_4=information_4
     self.password=password
 def get_descriptive_name(self):
    long_name=f"{self.information_1}{self.information_2}{self.information_3}{self.information_4}{self.password}"
    return long_name.title()
my_new_menu = Menu_list('Staff ID,', 'Ticket creator name,','Contact email,','Description of the issue,','330x7d10xce')
print(my_new_menu.get_descriptive_name())
