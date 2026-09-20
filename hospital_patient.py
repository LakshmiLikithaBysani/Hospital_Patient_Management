print("🏥 Hospital Patient Management System")

patients = []

while True:
    print("\n1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        disease = input("Enter disease: ")

        patient = {
            "name": name,
            "age": age,
            "disease": disease
        }

        patients.append(patient)

        print("✅ Patient added successfully!")

    elif choice == "2":
        if len(patients) == 0:
            print("❌ No patients found.")
        else:
            print("\nPatient Details:")

            for patient in patients:
                print("--------------------")
                print("Name:", patient["name"])
                print("Age:", patient["age"])
                print("Disease:", patient["disease"])

    elif choice == "3":
        search_name = input("Enter patient name to search: ")

        found = False

        for patient in patients:
            if patient["name"].lower() == search_name.lower():
                print("\n✅ Patient Found")
                print("Name:", patient["name"])
                print("Age:", patient["age"])
                print("Disease:", patient["disease"])
                found = True

        if not found:
            print("❌ Patient not found.")

    elif choice == "4":
        delete_name = input("Enter patient name to delete: ")

        found = False

        for patient in patients:
            if patient["name"].lower() == delete_name.lower():
                patients.remove(patient)
                print("✅ Patient deleted successfully!")
                found = True
                break

        if not found:
            print("❌ Patient not found.")

    elif choice == "5":
        print("Thank you for using Hospital Patient Management System!")
        break

    else:
        print("❌ Invalid choice!")
