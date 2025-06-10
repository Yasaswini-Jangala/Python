# # You're building a system to manage student data for a university. Each student is identified by a unique student ID and has the following details:
# # Name, Major, Enrolled Courses (each course has a course name and a dictionary of assessment scores like midterm, final, and project)

# university_data = {
#   "S101": {
#     "name": "Alice Johnson",
#     "major": "Computer Science",
#     "courses": {
#       "Python101": {"midterm": 88, "final": 92, "project": 94},
#       "Math201": {"midterm": 78, "final": 85, "project": 80}
#       }
#   },
#   "S102": {
#     "name": "Bob Smith",
#     "major": "Mathematics",
#     "courses": {
#       "Math201": {"midterm": 90, "final": 93, "project": 88},
#       "Stats101": {"midterm": 84, "final": 80, "project": 85}
#       }
#   },
#   "S103": {
#     "name": "Clara Lopez",
#     "major": "Physics",
#     "courses": {
#       "Physics101": {"midterm": 75, "final": 82, "project": 78},
#       "Math201": {"midterm": 70, "final": 72, "project": 68}
#     }
#   }
# }

# # Q1: Print all student names and their majors
# print('\n'.join(f'{university_data[id]["name"]} --> {university_data[id]["major"]}' for id in university_data)+"\n")

# # Q2: Average score per course per student
# for id in university_data:
#   print(f"\nStudent: {university_data[id]['name']}")
#   for course_name in university_data[id]['courses']:
#     average = sum(university_data[id]['courses'][course_name].values()) / len(university_data[id]['courses'][course_name].values())
#     print(f"  {course_name} --> Average: {average:.2f}")

# # Q3: Find students who scored >90 in final of Python101
# for id in university_data:
#   if 'Python101' in university_data[id]['courses']:
#     if university_data[id]['courses']['Python101']['final'] > 90:
#       print(university_data[id]['name'])

# # Q3: Find students who scored >90 in final of Python101
# for id in university_data:
#   if 'Math201' in university_data[id]['courses']:
#     if university_data[id]['courses']['Math201']['final'] > 70:
#       print(university_data[id]['name'])

# # Q4: Add new course AI101 for student S101
# if 'S101' in university_data.keys():
#   university_data['S101']['courses']['AI101'] = {"midterm": 100, "final": 100, "project": 100}
#   print(university_data['S101'])

# # Q5: Print average for each course across all students
# course_totals, course_counts, course_avg = {}, {}, {}
# for id in university_data:
#   for course_name in university_data[id]['courses']:
#     if course_name not in course_totals:
#       course_totals[course_name] = sum(university_data[id]['courses'][course_name].values())
#       course_counts[course_name] = len(university_data[id]['courses'][course_name].values())
#     else:
#       course_totals[course_name] += sum(university_data[id]['courses'][course_name].values())
#       course_counts[course_name] += len(university_data[id]['courses'][course_name].values())
# for course_name in course_totals:
#     course_avg[course_name] = course_totals[course_name] / course_counts[course_name]
#     print(f"{course_name} --> Average Score: {course_avg[course_name]:.2f}")