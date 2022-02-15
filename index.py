# Import pandas
import pandas

# Load the bob csv (with the ages) and turn it into a dictionary for easier processing
age_data = pandas.read_csv('./bob.csv').to_dict(orient='records')

# Load the john csv (with the cars) and turn it into a dictionary for easier processing
vehicle_data = pandas.read_csv('./john.csv').to_dict(orient='records')

# Start with string buffer with the headers
buffer = '"name"\t"age"\t"car"\n'

# iterate over the age data
for age_stuff in age_data:
    # extract out some variables for more readability
    age = age_stuff['age']
    name = age_stuff['name']

    # filter the vehicle data and extrace the first row with the Same name as the name as the age data name
    vehicle_row = list(filter(lambda vehicle_stuff: vehicle_stuff['name'] == name, vehicle_data))[0]

    # extrace out the car variable for readability
    car = vehicle_row['car']

    # use string interpolation to combine variables into a string and append them to the buffer
    buffer += f'"{name}"\t"{age}"\t"{car}"\n'

# print the buffer
print(buffer)
