class BMW:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"
def car_details(car_object):

    print(f"Fuel Type: {car_object.fuel_type()}")
    print(f"Max Speed: {car_object.max_speed()}\n")
car1 = BMW()
car2 = Ferrari()
print("BMW")
car_details(car1)

print("ferrari")
car_details(car2)
