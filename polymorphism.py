class india():
    def capital(self):
        print("dehli is the capital city of india")
    def language(self):
        print("hindi is the most widely spoken language of india")   
    def type(self):
        print("india is a devolping country")    
class USA():
    def capital(self):
        print("washington dc is the capital city of USA")
    def language(self):
        print("english is the most widely spoken language of USA")   
    def type(self):
        print("USA is a devolped country")            
obj_ind=india()
obj_usa=USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()