from Algorithm_Calc.shunting_yard import TokenType



def evaluate_rpn(Rpn_tokens_list):
    """
    Hàm giải mã và tính toán kết quả từ danh sách Token_Postfix
    Args:
        Rpn_tokens_list (list): Danh sách các tokens đã được sắp xếp theo hậu tố (RPN)
    Returns:
        Float: Kết quả cuối cùng của phép tính
    """
    stack = []
    for token in Rpn_tokens_list:
        if token.type == TokenType.NUMBER:
            stack.append(float(token.value))
        elif token.type == TokenType.OPERATOR:
            right_val = stack.pop()
            left_val = stack.pop()
            if token.value == '+':
                stack.append(left_val + right_val)
            elif token.value == '-':
                stack.append(left_val - right_val)
            elif token.value == '*':
                stack.append(left_val * right_val)
            elif token.value == '/':
                if right_val == 0:
                    raise ZeroDivisionError("Impossible to devide by 0")
                stack.append(left_val / right_val)
            elif token.value == '^':
                stack.append(left_val ** right_val)
    return stack.pop()