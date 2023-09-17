from roster import student_roster
import classroom_organizer

student_roster_iterables = student_roster.__iter__()

print(student_roster_iterables.__next__())
print(student_roster_iterables.__next__())
print(student_roster_iterables.__next__())
print(student_roster_iterables.__next__())
print(student_roster_iterables.__next__())
print(student_roster_iterables.__next__())
print(student_roster_iterables.__next__())
print(student_roster_iterables.__next__())
print(student_roster_iterables.__next__())
print(student_roster_iterables.__next__())
## 3 b
student_roll = classroom_organizer.ClassroomOrganizer()
student_roll_iter = iter(student_roll)
for student in student_roll_iter:
  print(student)

### 4
tables = classroom_organizer.ClassroomOrganizer()
student_tables = tables.table_seating()
print(student_tables)

two_subjects = classroom_organizer.ClassroomOrganizer()
two_subjects_combo = two_subjects.two_subjects_tables()
print(two_subjects_combo)
