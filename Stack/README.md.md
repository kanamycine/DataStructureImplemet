# stack

**0x00 정의와 성질
0x01 기능과 구현
0x02 연습문제
0x03 마치며**

-----
## 0x00 정의와 성질
스택은 한쪽 끝에서만 원소를 넣거나 뺄 수 있는 자료구조입니다. 프링글스 통이나, 엘레베이터를 생각합니다.
구조적으로 먼저 들어간 원소가 제일 나중에 나오게 되는데, 이런 의미로 'FILO'(First In Last Out) 자료구조라고 부르기도 합니다. 

참고로 큐나 덱도 스택처럼 특정 위치에서만 원소를 넣거나 뺄 수 있는 제한이 걸려있습니다. 그래서 Stack, Queue, Dequeue를 묶어서 Restricted Structure라고 부르기도 한답니다.
![](https://images.velog.io/images/kanamycine/post/ceb7f4cf-0eab-4525-9e78-2edf98aedb12/image.png)

### 스택의 성질 
1. 원소의 추가가 O(1)
2. 원소의 제거가 O(1)
3. 제일 상단의 원소 확인 O(1)
4. 제일 상단이 아닌 나머지 원소들의 확인이나 변경은 원칙적으로 불가능

## 0x01 기능과 구현
```python
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

```
## 0x02 연습문제
### BOJ10828 : 스택 <https://www.acmicpc.net/problem/10828>
![](https://images.velog.io/images/kanamycine/post/b725fedd-68b6-4cd8-bc0e-8eb11c50a70c/image.png)
``` python
import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
```

## 0x03 마치며
스택은 본격적으로 활용할 수 있는 방법이 굉장히 많은 자료구조이다. 대표저깅ㄴ 사례로 수식의 괄호쌍, 전위/중위/후위 표기법, DFS, Flood Fill 등이 있다. 웬만하면 다 짚고 넘어갈 내용들이지만 분량이 꽤 많아질 수 있어서, 각 내용들을 독립적으로 다룰 예정이다. 