# Class List Manager - Group6
# MIS 211 Bonus Assignment (GitHub Teamwork)
names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]
# ===== Each student adds her function BELOW this line =====
# Written by:Bayan (task 2)
def search_name(names, name):
  for student in names:
    if student == name:
      return True
  return False
def main():
  print("Welcome to the Class List Manager!")
  print("Class list:", names)
  print("Is Lama in the class?", search_name(names, "Lama"))
main()
