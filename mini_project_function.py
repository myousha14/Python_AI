def calculate_total(marks):
    return sum(marks)
def average(marks):
    return sum(marks)/len(marks)
def Highest(marks):
    return max(marks)
def Lowest(marks):
    return min(marks)
def result(average):
    if average >=50:
        return "Pass"
    else:
        return "Fail"

# Main execution
marks=[]
for j in range(1,11):
    m=float(input(f"Enter Marks {j} : "))
    marks.append(m)
total=calculate_total(marks)
Average=average(marks)
print("\n RESULT ")
print("Marks:", marks)
print("Total:", total)
print("Average:", round(Average, 2))
print("Highest Marks:", Highest(marks))
print("Lowest Marks:", Lowest(marks))
print("Result:", result(Average))

