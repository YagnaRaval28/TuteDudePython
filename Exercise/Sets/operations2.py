student1={"English","CS","Maths","Science"}
student2={"English","CS","AIML","Data Analytics"}
student3={"SS","ENV"}
print(student1,type(student1))
print(student2,type(student2))

#common subject between studen1 and student2- intersection
common_subjects=student1.intersection(student2)
print("\n")
print(f"Common subjects between student1 and student2 are {common_subjects}")

union_subjects=student1.union(student2,student3)
print(f"Union subjects between student1 and student2 are {union_subjects}")

diff_subjects=student1.difference(student2)
print(f"Different subjects between student1 and student2 are {diff_subjects}")