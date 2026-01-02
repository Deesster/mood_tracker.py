moods = []

while True:
    print("\nMood Tracker")
    print("1. Add mood")
    print("2. Show moods")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        mood = input("How do you feel right now? ")
        moods.append(mood)
        print("Mood saved 🌙")

    elif choice == "2":
        if not moods:
            print("No moods recorded yet.")
        else:
            print("\nYour moods:")
            for i, mood in enumerate(moods, start=1):
                print(f"{i}. {mood}")

    elif choice == "3":
        print("Take caree")
        break

    else:
        print("Invalid choice.")
