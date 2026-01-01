def view_problem():
    try:
        with open("project1.txt","r") as file:
            print("\nName            | Topic      | Difficulty | Date       |Time taken")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No problems found.")

def add_problem():
    name=input("Problem name: ").strip()
    topic=input("Topic: ").strip()
    difficulty=input("Difficulty(Easy/Medium/Hard): ").strip()
    time_taken=input("Time taken(in ms): ").strip()

    if difficulty not in ["Easy","Medium","Hard"]:
        print("Invalid difficulty")
        return 
    date=input("Date(DD-MM-YYYY): ")
    
    if not time_taken.isdigit():
        print("Time must be a number")
        return
    
    with open("project1.txt","a") as file:
        file.write(f"{name:<15} | {topic:<10} | {difficulty:<6} | {date:<10} | {time_taken}\n")
        print("Problem added successfully")



def menu():
    while True:
        print("\n1.Add Problem")
        print("2.View Problem")
        print("3.Overview")
        print("4.Exit")

        choice=input("Enter Choice: ").strip()
        if choice=="1":
            add_problem()
        elif choice=="2":
            view_problem()
        elif choice=="3":
            overview()
        elif choice=="4":
            break
        else:
            print("Invalid choice")

with open("project1.txt","a") as file:
    file.write("\nName            | Topic      | Diff   | Date       | Time taken\n")
    file.write("-" * 50)

menu()