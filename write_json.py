import json

questions = []





# 0-13 题，根据乐谱图片选择是 还原/升/降 那个调
right_answer_list = [[0, 6], [0, 3], [0, 0], [0, 4], [0, 1], [1, 5], [1, 2], [0, 5], [2, 1], [2, 4], [2, 0], [2, 3], [2, 6], [2, 2]]
for i in range(14):
    new_dict = {"id":i,"display_type":0,"display_content":str(i)+"-0.png","options": [["♮","♯","♭"],["A","B","C","D","E","F","G"]],"right-answer": right_answer_list[i]}
    questions.append(new_dict)

# 14-27 题，根据给出的调号，选择是 升/降 几个调号
display_list = ["G大调", "D大调", "A大调", "E大调", "B大调", "♯F大调", "♯C大调", "F大调", "♭B大调", "♭E大调", "♭A大调", "♭D大调", "♭G大调", "♭C大调", "e小调", "b小调", "♯f小调", "♯c小调", "♯g小调", "♯d小调", "♯a小调", "d小调", "g小调", "c小调", "f小调", "♭b小调", "♭e小调", "♭a小调"]
for i in range(14):
    new_dict = {"id":i+14,"display_type":1,"display_content":display_list[i],"options": [["♯","♭"],["A","B","C","D","E","F","G"]],"right-answer": right_answer_list[i]}
    questions.append(new_dict)





# 写入文件
jsonobj = {"questions":questions}

with open('data.json','w')as f:
    json.dump(jsonobj,f)
