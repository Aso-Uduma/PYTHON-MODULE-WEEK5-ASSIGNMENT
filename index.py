# -----------------------------
# Activity 1: Your Own Class(es)
# -----------------------------

class Superhero:
    def __init__(self, name, power, city):
        self.name = name                 # public
        self._power = power              # "protected" by convention
        self.__secret_identity = None    # private (encapsulation)
        self.city = city

    def reveal_power(self):
        return f"{self.name}'s power: {self._power}"

    def set_secret_identity(self, identity):
        self.__secret_identity = identity

    def get_secret_identity(self):
        return self.__secret_identity if self.__secret_identity else "Unknown"

    def protect_city(self):
        return f"{self.name} is protecting {self.city}!"


class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    # Polymorphism via overriding
    def protect_city(self):
        return f"{self.name} swoops over {self.city} at {self.flight_speed} km/h!"


# --------------------------------
# Activity 2: Polymorphism (move())
# --------------------------------

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move().")


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


# -------------
# Mini game UI
# -------------

def prompt_int(msg, min_val=None, max_val=None):
    while True:
        raw = input(msg).strip()
        try:
            val = int(raw)
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Please enter a number between {min_val} and {max_val}.")
                continue
            return val
        except ValueError:
            print("Please enter a valid number.")


def create_hero_flow():
    print("\n-- Create Your Hero --")
    name = input("Hero name: ").strip() or "Nameless"
    power = input("Main power: ").strip() or "Mystery"
    city = input("Home city: ").strip() or "Nowhere"

    is_flying = input("Is this a flying hero? (y/n): ").strip().lower()
    if is_flying == "y":
        speed = prompt_int("Flight speed (km/h): ", min_val=1)
        hero = FlyingHero(name, power, city, speed)
    else:
        hero = Superhero(name, power, city)

    # Optional secret identity
    secret = input("Set a secret identity? (leave blank to skip): ").strip()
    if secret:
        hero.set_secret_identity(secret)

    # Interactions
    print("\n-- Hero Report --")
    print(hero.reveal_power())
    print(f"Secret identity: {hero.get_secret_identity()}")
    print(hero.protect_city())
    print()
    return hero


def vehicles_demo():
    print("\n-- Vehicles Polymorphism Demo --")
    fleet = [Car(), Plane(), Boat()]
    for v in fleet:
        print(v.move())
    print()


def main():
    print("Welcome to the OOP Playground! 🎮")
    while True:
        print("\nChoose an option:")
        print("1) Create and interact with a Superhero")
        print("2) See Vehicles polymorphism (move())")
        print("3) Exit")

        choice = prompt_int("Enter 1, 2, or 3: ", min_val=1, max_val=3)
        if choice == 1:
            create_hero_flow()
        elif choice == 2:
            vehicles_demo()
        else:
            print("Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
