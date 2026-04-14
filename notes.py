notes = []

def add_note():
    note = input("Enter note: ")
    notes.append(note)
    print("Note added!")

def view_notes():
    print("\nYour Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

while True:
    print("\n1. Add Note\n2. View Notes\n3. Exit")
    choice = input("Choose: ")

    if choice == '1':
        add_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':