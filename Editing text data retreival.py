personal_data_list = []

with open("personal_data.txt", "r") as file:
    for line in file:
        raw_personal_data = line.strip().split(", ")  # Split each line into a list
        personal_data_list.append(raw_personal_data)  # Append the list to personal_data_list

print(personal_data_list)

task_data_list = []

with open("task_data.txt", "r") as file:
    for line in file:
        raw_task_data = line.strip().split(", ")  # Split each line into a list
        task_data_list.append(raw_task_data)  # Append the list to personal_data_list

print(task_data_list)

review_task_list = []

with open("review_task_data.txt", "r") as file:
    for line in file:
        raw_review_data = line.strip().split(", ")  # Split each line into a list
        review_task_list.append(raw_task_data)  # Append the list to personal_data_list

print(review_task_list)
