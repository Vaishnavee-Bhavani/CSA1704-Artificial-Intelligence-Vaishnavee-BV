record("John", "Dr. Smith", "CS101").
record("Mary", "Prof. Davis", "CS102").
record("Alex", "Dr. Smith", "CS101").

get_teacher(Student, Teacher) :- record(Student, Teacher, _).
get_students(Teacher, Student) :- record(Student, Teacher, _).
