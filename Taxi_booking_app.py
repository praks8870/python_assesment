class Taxi:
    def __init__(self, taxi_id):
        self.taxi_id = taxi_id
        self.location = 'A'
        self.earnings = 0
        self.is_free = True

    def calculate_fare(self, distance):
        if distance <= 5:
            return 100
        else:
            return 100 + (distance - 5) * 10

class TaxiBookingApp:
    def __init__(self):
        self.taxis = [Taxi(i) for i in range(1, 5)]
        self.points = ['A', 'B', 'C', 'D', 'E', 'F']
        self.point_distance = 15  # distance between points in kms
        self.travel_time = 60  # travel time between points in minutes

    def find_nearest_free_taxi(self, point):
        min_distance = float('inf')
        nearest_taxi = None
        target_index = self.points.index(point)

        for taxi in self.taxis:
            if taxi.is_free:
                taxi_index = self.points.index(taxi.location)
                distance = abs(target_index - taxi_index)

                if distance < min_distance or (distance == min_distance and taxi.earnings < nearest_taxi.earnings):
                    min_distance = distance
                    nearest_taxi = taxi

        return nearest_taxi, min_distance

    def book_taxi(self, pickup, drop):
        nearest_taxi, distance_to_pickup = self.find_nearest_free_taxi(pickup)

        if nearest_taxi is None:
            print("No taxi available for booking.")
            return

        pickup_index = self.points.index(pickup)
        drop_index = self.points.index(drop)
        travel_distance = abs(drop_index - pickup_index) * self.point_distance
        fare = nearest_taxi.calculate_fare(travel_distance)

        nearest_taxi.is_free = False
        nearest_taxi.location = drop
        nearest_taxi.earnings += fare

        print(f"Taxi {nearest_taxi.taxi_id} booked successfully.")
        print(f"Pickup: {pickup}, Drop: {drop}")
        print(f"Fare: Rs. {fare}")
        print(f"Travel Distance: {travel_distance} kms")
        print(f"Estimated Travel Time: {travel_distance * self.travel_time / self.point_distance} minutes")

    def free_taxi(self, taxi_id):
        for taxi in self.taxis:
            if taxi.taxi_id == taxi_id:
                taxi.is_free = True
                print(f"Taxi {taxi_id} is now free.")

    def view_taxi_status(self):
        for taxi in self.taxis:
            status = "Free" if taxi.is_free else "Busy"
            print(f"Taxi {taxi.taxi_id} | Location: {taxi.location} | Earnings: Rs. {taxi.earnings} | Status: {status}")

def main():
    app = TaxiBookingApp()

    while True:
        print("\n1. Book Taxi")
        print("2. View Taxi Status")
        print("3. Free Taxi")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            pickup = input("Enter Pickup Point (A, B, C, D, E, F): ").strip().upper()
            drop = input("Enter Drop Point (A, B, C, D, E, F): ").strip().upper()
            app.book_taxi(pickup, drop)
        
        elif choice == '2':
            app.view_taxi_status()

        elif choice == '3':
            taxi_id = int(input("Enter Taxi ID to free: ").strip())
            app.free_taxi(taxi_id)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

