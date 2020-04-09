import json

from skill.models import Scenario, Entity
from skill.module.block import loads_entity

def run(*args):
    num = 0
    scens = Scenario.objects.all()
    entities = Entity.objects.all()
    for entity in entities:
        entity.delete()
    for scen in scens:
        try:
            req = json.loads(scen.request)
            airtxt_city = req["action"]["params"].get("airtxt_city",None)
            airtxt_city1 = req["action"]["params"].get("airtxt_city1",None)
            if airtxt_city != None:
                loads_entity(airtxt_city)
            elif airtxt_city1 != None:
                loads_entity(airtxt_city1)
            num += 1
        except:
            continue

    print(num)