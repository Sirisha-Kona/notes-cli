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
    print("\n1. Add Note\n2. View Notes\n3. Delete Note\n4. Exit")
    choice = input("Choose: ")

    if choice == '1':
        add_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        break
    else:
        print("Invalid choice")

def delete_note():
    view_notes()
    num = int(input("Enter note number to delete: "))
    if 0 < num <= len(notes):
        notes.pop(num - 1)
        print("Deleted!")
    else:
        print("Invalid number")