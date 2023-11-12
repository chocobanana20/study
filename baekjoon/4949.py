while True:
    text = input()
    if text==".":
        break
    stack = []
    for i in text:
        if i=="(" or i=="[":
            stack.append(i)
        elif i==")":
            if len(stack)==0 or stack[-1]=="[":
                stack.append("1234") # 이 경우에는 안되잖아 . 밑에서 알 수 있도록 표시
                break  # continue가 아니라 break , continue 였으면 다음 loop로
            else:
                stack.pop()
        elif i=="]":
            if len(stack)==0 or stack[-1]=="(":
                stack.append("1234")
                break
            else:
                stack.pop()

    if len(stack)==0:
        print("yes")
    else:
        print("no")
    
    
