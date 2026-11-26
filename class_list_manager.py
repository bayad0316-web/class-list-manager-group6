# Class List Manager - Group6
# MIS 211 Bonus Assignment (GitHub Teamwork)
names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]
# ===== Each student adds her function BELOW this line =====
# Written by: Shaden (task 1)
def count_names(names):
    return len(names)
# Written by:Bayan (task 2)
def search_name(names, name):
  for student in names:
    if student == name:
      return True
  return False
# Written by: Joud Almarshad (Task 6)
def to_upper(names):
        # Create a new list of uppercase names
    upper_names = []
    for name in names:
        upper_names.append(name.upper())
    return upper_names
# Written by: Lamar Abdullah Almaliki (Task 3)
def sort_names(names):
    return sorted(names)
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Uppercase names:", to_upper(names))
    print("Is Lama in the class?", search_name(names, "Lama"))
    print("Sorted names:", sort_names(names))
main()
