
required_skills = ["python", "java", "sql", "communication", "teamwork"]

print(" Resume Analyzer")
print()
resume = input("Paste your resume text here:\n").lower()
print("\nAnalyzing resume...\n")
matched_skills = []
for skill in required_skills:
    if skill in resume:
        matched_skills.append(skill)
print("Skills Found:")
for skill in matched_skills:
    print("-", skill)
missing_skills = []
for skill in required_skills:
    if skill not in matched_skills:
        missing_skills.append(skill)
print("\n Missing Skills:")
for skill in missing_skills:
    print("-", skill)
score = (len(matched_skills) / len(required_skills)) * 100
print("\n Resume Score:", score, "%")
if score == 100:
    print("Excellent Resume!")
elif score >= 60:
    print(" Good Resume, but can improve.")
else:
    print(" Add more relevant skills.")