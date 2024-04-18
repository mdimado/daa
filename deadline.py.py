def max_profit(projects):
    def sort_key(project):
        return project[1]
    projects.sort(key = sort_key, reverse=True)
    total_profit = 0
    deadlines = set(range(len(projects), 0, -1))
    for deadline,profit in projects:
        while deadline not in deadlines and deadline:
            deadline -= 1
        if deadline>0:
            total_profit+=profit
            deadlines.remove(deadline)
    return total_profit

num_projects = int(input("Enter the number of projects: "))
projects=[]

for i in range(num_projects):
    deadline = int(input(f"Enter the deadline for project {i+1}: "))
    profit = int(input(f"Enter the profit for project {i+1}: "))
    projects.append((deadline,profit))
print("Maximum total profit: ",max_profit(projects))