import json
from vehicleapp.models import VehicleMake


with open('getallmakes.json') as data_file:
    data = json.load(data_file)

for make in data:
    
    m = VehicleMake(make_id=make['Make_ID'], make_name=make['Make_Name'])
    
    m.save()


# to run type in shell: exec(open('import.py').read()) or python manage.py shell < import.py from cmd