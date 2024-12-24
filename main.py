from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

schl = School("ABC", "Dhaka")

eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

schl.add_classroom(eight)
schl.add_classroom(nine)
schl.add_classroom(ten)


Rahim = Student("Rahim", eight)
karim = Student("Karim", nine)
fahim = Student("Fahim", ten)
hahim = Student("Hahim", ten)


schl.student_admission(Rahim)
schl.student_admission(karim)
schl.student_admission(fahim)
schl.student_admission(hahim)


abul = Teacher("Abul K")
babul = Teacher("babul K")
kabul = Teacher("kabul K")

bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", kabul)
biology = Subject("Biology", abul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(bangla)
ten.add_subject(physics)
ten.add_subject(chemistry)
ten.add_subject(biology)


eight.take_sem_finals()


print(schl)