last_semester_gradebook = [["Politics", 80], ["Latin", 96], ["Dance", 97], ["Architecture", 65]]

# This semesters grades
subjects = ["Algebra 2", "ENG 101", "Government", "Physics", "Programing"]
grades = [100, 100, 87, 95, 98]

gradebook = [["Algebra 2", 100], ["ENG 101", 100], ["Government", 87], ["Physics", 95], ["Programing", 98]]

gradebook.append(["Engineering", 102])
gradebook.append(["Arts", 88])
gradebook[-4][-1] = 98
gradebook[2].remove(87)
gradebook[2].append("Pass")
gradebook[1].remove(100)
gradebook[1].append("Pass")
gradebook[-1][-1] = (90)

full_gradebook = last_semester_gradebook + gradebook

full_gradebook[0][1] = (82)
full_gradebook[-9].remove(97)
full_gradebook[2].append(86)
print(full_gradebook)