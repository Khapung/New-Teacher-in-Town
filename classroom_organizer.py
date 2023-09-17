from roster import student_roster
from itertools import combinations, chain

# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

 ## 3 
  def __iter__(self):
    self.index = 0
    return self
  
  def __next__(self):
    each_student = self.sorted_names[self.index]
    self.index += 1
    if self.index >= 10:
      raise StopIteration
    return each_student

## 4
  def table_seating(self):
    names = []
    for student_info in student_roster:
      name = student_info['name']
      names.append(name)
    table_list = list(combinations(names, 2))
    return table_list
  
  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

## 5
  def two_subjects_tables(self):
    math = self.get_students_with_subject("Math")   
    science = self.get_students_with_subject("Science")
    two_subjects_list = list(chain(math, science))
    two_subjects_combination = list(combinations(two_subjects_list, 4))
    return two_subjects_combination

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students
