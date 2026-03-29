from Algorithm_Calc.shunting_yard import tokenizeExpression, shuntingYard
from Algorithm_Calc.rpn_calc import evaluate_rpn
from datetime import datetime

def print_header():
    print("=" * 60)
    print("        RPN CALCULATOR - CLI EDITION")
    print("=" * 60)
    print("Supported operators: +  -  *  /  ^  ( )")
    print("Type 'q', 'quit' or 'exit' to terminate.\n")


def main():
    print_header()

    while True:
        expr = input(">>> Enter expression: ").strip()


        if expr.lower() in ['q', 'quit', 'exit']:
            print("\n[INFO] Session terminated. Goodbye!")
            break

        if not expr:
            continue

        try:
            print("\n" + "-" * 60)

            now = datetime.now().strftime("%H:%M:%S")
            print(f"[{now}] Processing...")

            tokens = tokenizeExpression(expr)
            print(f"[1] Infix Tokens : {tokens}")

            rpn = shuntingYard(tokens)
            print(f"[2] RPN Output   : {rpn}")

            result = evaluate_rpn(rpn)
            print(f"[3] Result       : {result:.6f}")

            print("-" * 60 + "\n")

        except ZeroDivisionError:
            print("[ERROR] Division by zero is not allowed.\n")

        except Exception as e:
            print(f"[ERROR] Invalid expression: {e}")
            print("Please check your syntax and try again.\n")


if __name__ == "__main__":
    main()