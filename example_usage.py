from animal_kingdom import AnimalKingdom, Rabbit, Snake

def main():
    animal = AnimalKingdom("Generic Animal")
    print(animal.eat())
    print(animal.sleep())
    print(animal.move())

# Create a Rabbit instance
    rabbit=Rabbit("Bunny")
    print(rabbit.eat())
    print(rabbit.sleep())
    print(rabbit.move())
    print(rabbit.hop())
    print(rabbit.nibble())

    # Create a snake instance

    cobra = Snake("Slither","Cobra")
    print(cobra.eat())
    print(cobra.sleep())
    print(cobra.move())
    print(cobra.slither())
    print(cobra.hiss())

if __name__ == "__main__":
    main()
