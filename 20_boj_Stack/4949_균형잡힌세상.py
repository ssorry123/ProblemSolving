class Stack:
    def __init__(self):
        self.__stack = list()
    def push(self, c):
        self.__stack.append(c)
    def pop(self):
        self.__stack.pop(len(self.__stack) - 1)
    def top(self):
        # 비어있는 경우 참조하면 인덱스 에러
        if(self.empty()):
            return None
        return self.__stack[len(self.__stack) - 1]
    def empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

while(True):
    # sys.stdin.readline().strip()으로 받게되면
    # 공백들로 시작하는 경우 첫 공백이 아닌 문자가 나타날때까지의
    # 공백은 입력받지 않음
    tmp = input()
    if(tmp[0] == '.'):
        break

    ret = True
    s = Stack()
    # 결과가 거짓이 되는 두가지 경우
    for c in tmp:
        if (c==']'):
            if (s.top() == '['):
                s.pop()
            else:
                ret = False
                break
        elif (c==')'):
            if (s.top() == '('):
                s.pop()
            else:
                ret = False
                break
        elif (c=='('):
            s.push(c)
        elif (c=='['):
            s.push(c)
    
    # 마지막으로 스택이 비어있는 조건을 추가
    if(ret and s.empty()):
        print('yes')
    else:
        print('no')
            