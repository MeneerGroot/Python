calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")

days_to_units(10)
days_to_units(20)
days_to_units(50)
days_to_units(100)
days_to_units(365)

