# Technical skills of two employees
employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "C++", "SQL", "Docker"}

# Common skills
common_skills = employee1 & employee2

# Skills unique to Employee 1
unique_employee1 = employee1 - employee2

# Skills unique to Employee 2
unique_employee2 = employee2 - employee1

# All available skills
all_skills = employee1 | employee2

print("Common skills:", common_skills)
print("Skills unique to Employee 1:", unique_employee1)
print("Skills unique to Employee 2:", unique_employee2)
print("All available skills:", all_skills)
