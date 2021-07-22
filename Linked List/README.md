# lINKED lIST 
### 연결리스트는 데이터 요소의 선형 집합으로, 데이터의 순서가 메모리에 물리적인 순서대로 저장되지는 않는다.

--------------------------

연결 리스트는 컴퓨터과학에서 배열과 함께 가장 기본이 되는 대표적인 선형 자료구조 중 하나로 다양한 추상 자료형(ADT) 구현의 기반이 된다

동적으로 새로운 노드를 삽입하거나 삭제하기가 편하며, 연결구조를 통해 물리메모리를 연속적으로 사용하지 않아도 되기 때문에 관리도 쉽다. 또한, 데이터를 구조체로 묶어서 포인터로 연결한다는 개념은 여러가지 방법으로 다양하게 활용이 가능

탐색에는 O(n)소요, why ? -> 특정 인덱스에 접근하기 위해서는 전체를 순서대로 읽어야 함.
반면 시작 또는 끝 지점 추가,삭제,추출 O(1)에 가능

__Array와 Trade Off 관계__ (출처 : 생활코딩)


![출처 생활코딩](https://images.velog.io/images/kanamycine/post/30e2a92b-6099-4e60-a853-769cf748d80e/image.png)




- 연결되는 방향에 따라 3가지 종류를 가진다
   - Singly linked list (단일 연결 리스트)
   - Doubly linked list (이중 연결 리스트)
   - Circular linked list (환형 연결 리스트)

---------

## Linked list의 장단점
### 장점
   - 수정이 O(1)에 이루어진다.
   - 수정을 할때마다 동적으로 linked list 크기가 결정 배열(Array)에 비해 처음부터 큰 공간을 할당할 필요가 없다
   - __메모리 관리가 용이하다__

### 단점
   - Random Access 이라 Array처럼 index를 통해 탐색이 불가능
   - 탐색이 O(n)이 걸린다 -> 접근 속도 느림
   - 중간 데이터 삭제시 앞 뒤 데이터의 연결을 재구성해야 하는 부가적인 작업이 필요


-----------------------
## Implementing Linked List
```python
class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self, item):
        self.head = Node(item)
        # head는 초기 시작 노드를 말한다.

    # 추가 메소드
    def add(self, item):
        cur = self.head
        # cur는 현재 찍고 있는 노드를 의미한다. (포인터 개념)

        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    # 삭제 메소드
    def remove(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.val == item:
                    self.removeItem(item)
                    return
                cur = cur.next
            print("item does not exist in linked list")

    def removeItem(self, item):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == item:
                nextnode = cur.next.next
                cur.next = nextnode
                break
            
    # 출력 메소드
    def printlist(self):
        cur = self.head
        print("HEAD:: ", end='')
        while cur is not None:
            print(cur.val, '->', end=' ')
            cur = cur.next
        if cur is None:
            print('empty')

    # linked list size 출력 메소드
    def size(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    # 탐색 메소드
    def search(self, data):
        check = self.head
        for i in range(self.size()):
            if check.val == data:
                print(data, "The data is at the {} index.".format(i+1))
                return None
            check = check.next
        print(data, "Data does not exist in linked list")
        return None

```

```python
linked = LinkedList(2)

linked.add(3)
linked.add(4)
linked.add(5)
linked.printlist()

linked.remove(3)
linked.printlist()

linked.search(5)
print(linked.size())
	
# HEAD:: 2 -> 3 -> 4 -> 5 -> empty
# HEAD:: 2 -> 4 -> 5 -> empty
# 5 The data is at the 3 index.
# 3
```
