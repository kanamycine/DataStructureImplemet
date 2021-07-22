# stack 클래스를 생성하고 init method를 이용하여 멤버 변수를 만들어준다.
# top 변수 안에는 파이썬에 내장되어 있는 list를 이용하여 스택을 만들어 준다.

class Stack:
    def __init__(self):
        self.top=[]

#__len__ 과 __str__를 작성한다

    #stack의 크기를 출력
    def __len__(self):
        return len(self.top)

    #stack 내부 자료를 string으로 변환하여 반환
    def __str__(self):
        return str(self.top[::1])

#구현 함수

    #Push
    def push(self, item):
        self.top.append(item)
    
    #Pop
    def pop(self):
        #if Stack is not empty
        if not self.isEmpty():
            #pop and return
            #-1을 파라미터로 넘겨서 리스트의 마지막 값을 반환
            return self.top.pop(-1)
        else:
            print("Stack underflow")
            exit()

    #isContain
    def isContain(self,item):
        return item in self.top

    #Peek
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("underflow")
            exit()

    #isEmpty:
    def isEmpty(self):
        return len(self.top)==0

    #Size
    def size(self):
        return len(self.top)

    

