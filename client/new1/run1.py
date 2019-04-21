import contract
import random
import time
import json

# record=[]

eventid=str(time.time())

user1="0x4ccd5762896ae5075808b2cd03599d487e1f33e0"
user2="0x13af759d94420d097c63d0b4e521d01486b2a4fe"

level=["is-primary","is-danger","is-info","is-warning"][random.randint(0,3)]
name=["surpass","compete","opposite"][random.randint(0,2)]
decider=["human","car"][random.randint(0,1)]
status=["unhandled","accepted","rejected"][random.randint(0,2)]
userlevel=str(random.randint(0,10))

gps="GPRMC,080655.00,A,4546.40891,N,12639.65641,E,1.045,328.42,170809,,,A*60"
gps="GPRMC,{},A,{},N,{},E,1.045,328.42,170809,,,A*60".format(int(time.time()),4546.40891+5*time.time(),12639.65641+5*time.time())
sensorcv=""

event=[{
    "type":"new",
    "event":{
        "id":eventid,
        "from":user1,
        "to":user2,
        "type":{
            "level":level,
            "name":name
        },
        "decider":decider,
        "status":status,
        "userlevel":userlevel
    },
    "data":{
        "gps":gps,
        "sensorcv":sensorcv
    }
}]

event=json.dumps(event)
contract.update(event,user1)