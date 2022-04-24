import os  # library

labels_path = "/home/ai/projects/interns/datasets/New folder/labels"

dir_list = os.listdir(labels_path)

print("-----------------------------------------")

print("Files and directories in '", labels_path, "' :")

print(dir_list)

for file_name in dir_list:
    txt_path = os.path.join(labels_path, file_name)
    print(f"txt_path: {txt_path}")

    with open(txt_path, mode="r") as f:
        first_line = f.readline()

    modified_label = first_line.replace('-1', '0', 1)
    with open(txt_path, mode="w") as f:
        f.write(modified_label)
