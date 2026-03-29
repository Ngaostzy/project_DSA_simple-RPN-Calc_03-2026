from enum import Enum

class TokenType(Enum):
    """
    Phân loại một số Type đặc biệt cho các toán tử
    """
    NUMBER = "Số"
    OPERATOR = "TOÁN TỬ"
    PARENTHESES = "NGOẶC"

class Token:
    """
    Đưa các toán tử về một khuôn mẫu Object chung.
    Bao gồm Value và Type
    """
    def __init__(self, value, TokenType):
        self.value = value
        self.type = TokenType
    def __repr__(self):
        return f"[{self.type.value}: {self.value}]"



def tokenizeExpression(expression):
    """
    Hàm có tác dụng tách từng phần tử trong biểu thức
    Args:
        expression (string): Nhận vào một Chuỗi biểu thức

    Returns:
        _type_: Trả về một list bao gồm mỗi toán tử trong biểu thức dưới dạng Token
    """
    expected_Output = []
    temp_container = ""

    operators = set("+-*/^")
    parentheses = set("()")

    for ch in expression:
        if ch.isspace():
            if temp_container != "":
                expected_Output.append(Token(temp_container, TokenType.NUMBER))
                temp_container = ""
        
        elif ch.isdigit() or ch == '.':
            temp_container += ch
        
        elif ch in operators or ch in parentheses:
            if temp_container != "":
                expected_Output.append(Token(temp_container, TokenType.NUMBER))
                temp_container = ""
            if ch in operators:
                expected_Output.append(Token(ch, TokenType.OPERATOR))
            else:
                expected_Output.append(Token(ch, TokenType.PARENTHESES))

    if temp_container != "":
        expected_Output.append(Token(temp_container, TokenType.NUMBER))

    return expected_Output
            
def shuntingYard(tokens_list):
    """
    hàm phân tích một danh sách các Token
    dựa trên độ ưu tiên (precedence) và tính kết hợp (associativity) của toán tử.
    Nó sử dụng một Ngăn xếp (Stack) để tạm giữ toán tử và một Hàng đợi (Queue) để 
    xuất kết quả nhằm loại bỏ hoàn toàn sự phụ thuộc vào dấu ngoặc.
    Args:
        tokens_list (list): Danh sách các đối tượng Token gốc (Infix) được bóc tách từ biểu thức.

    Returns:
        _type_: Danh sách các đối tượng Token đã được sắp xếp lại theo chuẩn RPN (Postfix).
    """
    precedence ={
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
    }
    is_left_associative = {
        '+': True,
        '-': True,
        '*': True,
        '/': True,
        '^': False,
    }
    output_Queue = []
    operator_Stack = []

    for token in tokens_list:
        if token.type == TokenType.NUMBER:
            output_Queue.append(token)
        
        elif token.type == TokenType.PARENTHESES:
            if token.value == '(':
                operator_Stack.append(token)
            elif token.value == ')':
                while operator_Stack and operator_Stack[-1].value != '(':
                    output_Queue.append(operator_Stack.pop())
                if operator_Stack and operator_Stack[-1].value == '(':
                    operator_Stack.pop()
        elif token.type == TokenType.OPERATOR:
            while operator_Stack and operator_Stack[-1].type == TokenType.OPERATOR:
                current_op = token.value
                top_op = operator_Stack[-1].value

                is_left_and_weaker = ((is_left_associative[current_op] and 
                                       precedence[top_op] >= precedence[current_op]))
                is_right_and_weaker = ((not is_left_associative[current_op] and
                                        precedence[top_op] > precedence[current_op]))
                if is_left_and_weaker or is_right_and_weaker:
                    output_Queue.append(operator_Stack.pop())
                else:
                    break
            operator_Stack.append(token)
        
    while operator_Stack:
        output_Queue.append(operator_Stack.pop())
        
    return output_Queue
