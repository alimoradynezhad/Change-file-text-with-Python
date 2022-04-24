import os  # library

labels_path = "/home/ai/projects/interns/datasets/New folder/labels"

dir_list = os.listdir(labels_path)

print("-----------------------------------------")

print("Files and directories in '", labels_path, "' :")

print(dir_list)

for i in range(107):
    txt_path = os.path.join(labels_path, dir_list[i])
    print(f"txt_path: {txt_path}")

    with open(txt_path, mode="r") as f:
        print(f)
        first_line = f.readline()

    modified_label = first_line.replace('-1', '0', 1)
    with open(txt_path, mode="w") as f:
        f.write(modified_label)
