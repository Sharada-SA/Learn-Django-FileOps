import json

class User:
        def __init__(self, id, realname, tz, times):
                self.id=id
                self.realname=realname
                self.tz=tz
                self.strttime = times['strttime']
                self.endtime = times['endtime']

        @classmethod
        def from_json(cls,jsondict):
            jsondict = json.loads(jsonstring)  
            return cls(**jsondict)
        def __repr__(self):
            return f'<User {self.id,self.realname, self.tz, self.strttime, self.endtime }>'

users_list2 = []
with open('dataneeded.json','r') as json_file:
    user_data = json.loads(json_file.read())
    for u in user_data:
        users_list2.append(User(**u))

jsonstring='''{
    "id": "W012A3CDE",
    "realname": "Egon Spengler",
    "tz": "America/Los_Angeles",
    "times": {
        "strttime": "Feb 1 2020  1:33PM",
        "endtime": "Feb 1 2020 1:54PM"
	    }}'''

users_list1 = User.from_json(jsonstring)
print(users_list2)
