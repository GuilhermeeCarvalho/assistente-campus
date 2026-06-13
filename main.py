from src.agent import answer_question


def main() -> None:
    print("Assistente Campus")
    question = input("Pergunta: ")
    print(answer_question(question))


if __name__ == "__main__":
    main()
