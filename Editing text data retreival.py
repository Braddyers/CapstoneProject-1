# 1. PERSONAL DATA FUNCTIONS:
# A - Load personal data method
personal_data_list = []
with open("personal_data.txt", "r") as file:
    for line in file:
        raw_personal_data = line.strip().split(", ")  # Split each line into a list
        personal_data_list.append(raw_personal_data)  # Append the list to personal_data_list
        #print(f"1.A \n{personal_data_list}")

# B - Load personal data method
personal_data_list = []
with open("personal_data.txt", "r") as file:
    for index, line in enumerate(file, start = 1):
        raw_personal_data = line.strip().split(", ")  # Split each line into a list
        personal_data_list.append(raw_personal_data)  # Append the list to personal_data_list
        #print(f"1.B \n{personal_data_list}")


# 2. TASK DATA FUNCTIONS:
# A - Load task data method
task_data_list = []
with open("task_data.txt", "r") as file:
    for line in file:
        raw_task_data = line.strip().split(", ")
        task_data_list.append(raw_task_data)
        print(f"2.A \n{task_data_list}")

# B - Load task data method
task_data_list = []
with open("task_data.txt", "r") as file:
    for index, line in enumerate(file, start = 1):
        raw_task_data = line.strip().split(", ")
        task_data_list.append(raw_task_data)
        print(f"2.B \n{task_data_list}")

# 
        

# 3. REVIEW TASK DATA FUNCTIONS:
# A - Load review task data
review_task_list = []
with open("review_task_data.txt", "r") as file:
    for line in file:
        raw_review_data = line.strip().split(", ")
        review_task_list.append(raw_task_data)
        print(f"3.A \n{review_task_list}")

# B
review_task_list = []
with open("task_data.txt", "r") as file:
    for index, line in enumerate(file, start = 1):
        raw_review_task_data = line.strip().split(", ")
        review_task_list.append(raw_review_task_data)
        print(f"3.B. \n{review_task_list}")