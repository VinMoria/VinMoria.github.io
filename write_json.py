import json

questions = []


# 0-13 题，根据乐谱图片选择是 还原/升/降 那个调 大调
right_answer_list = [
    [0, 6],
    [0, 3],
    [0, 0],
    [0, 4],
    [0, 1],
    [1, 5],
    [1, 2],
    [0, 5],
    [2, 1],
    [2, 4],
    [2, 0],
    [2, 3],
    [2, 6],
    [2, 2],
]
for i in range(14):
    new_dict = {
        "id": i,
        "display_type": 0,
        "display_content": str(i) + "-0.png",
        "options": [["♮", "♯", "♭"], ["A", "B", "C", "D", "E", "F", "G"]],
        "right_answer": right_answer_list[i],
        "default_answer": [0, -1],
    }
    questions.append(new_dict)

# 14-27 题，根据给出的调号，选择是 升/降 几个调号 大调
display_list = [
    "G大调",
    "D大调",
    "A大调",
    "E大调",
    "B大调",
    "♯F大调",
    "♯C大调",
    "F大调",
    "♭B大调",
    "♭E大调",
    "♭A大调",
    "♭D大调",
    "♭G大调",
    "♭C大调",
    "e小调",
    "b小调",
    "♯f小调",
    "♯c小调",
    "♯g小调",
    "♯d小调",
    "♯a小调",
    "d小调",
    "g小调",
    "c小调",
    "f小调",
    "♭b小调",
    "♭e小调",
    "♭a小调",
]
right_answer_list1 = ["♯", "♭"]
for i in range(14):
    new_dict = {
        "id": i + 14,
        "display_type": 1,
        "display_content": display_list[i],
        "options": [["♯", "♭"], ["1", "2", "3", "4", "5", "6", "7"]],
        "right_answer": [i // 7, i % 7],
        "default_answer": [-1, 0],
    }
    questions.append(new_dict)

# 28-41 题，根据乐谱图片选择是 还原/升/降 那个调 小调
right_answer_list = [
    [0, 4],
    [0, 1],
    [1, 5],
    [1, 2],
    [1, 6],
    [1, 3],
    [1, 0],
    [0, 3],
    [0, 6],
    [0, 2],
    [0, 5],
    [2, 1],
    [2, 4],
    [2, 0],
]
for i in range(14):
    new_dict = {
        "id": i+28,
        "display_type": 0,
        "display_content": str(i) + "-0.png",
        "options": [["♮", "♯", "♭"], ["a", "b", "c", "d", "e", "f", "g"]],
        "right_answer": right_answer_list[i],
        "default_answer": [0, -1],
    }
    questions.append(new_dict)

# 42-55 题，根据给出的调号，选择是 升/降 几个调号 大调
right_answer_list1 = ["♯", "♭"]
for i in range(14):
    new_dict = {
        "id": i + 42,
        "display_type": 1,
        "display_content": display_list[i+14],
        "options": [["♯", "♭"], ["1", "2", "3", "4", "5", "6", "7"]],
        "right_answer": [i // 7, i % 7],
        "default_answer": [-1, 0],
    }
    questions.append(new_dict)

# 设定问题集id
question_set1 = []
for i in range(28):
    question_set1.append(i)
question_set2 = []
for i in range(28):
    question_set2.append(28+i)
question_sets = [question_set1,question_set2]


# 写入文件
jsonobj = {"question_sets": question_sets, "questions": questions}

with open("data.json", "w") as f:
    json.dump(jsonobj, f)
print("DONE")
