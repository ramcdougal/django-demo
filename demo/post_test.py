import requests

r = requests.post("http://localhost:8000/api/cells", 
    data = {
        "name": "Cerebellar purkinje cell", 
        "location": "brain",
        "morphology": "fan-shaped"
    }
)

if r.status_code != 200:
    print('Unsuccessful request; status {}'.format(r.status_code))
else:
    print('Successful request. Added cell {}'.format(r.json()))