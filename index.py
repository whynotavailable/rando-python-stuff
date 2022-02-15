import pandas

age_data = pandas.read_csv('./bob.csv').to_dict(orient='records')
vehicle_data = pandas.read_csv('./john.csv').to_dict(orient='records')

buffer = '"name"\t"age"\t"car"\n'

for age_stuff in age_data:
    age = age_stuff['age']
    name = age_stuff['name']

    vehicle_row = list(filter(lambda vehicle_stuff: vehicle_stuff['name'] == name, vehicle_data))[0]
    car = vehicle_row['car']

    buffer += f'"{name}"\t"{age}"\t"{car}"\n'

print(buffer)
