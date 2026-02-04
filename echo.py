def echo(text: str, repetitions: int = 3) -> str:
    sound = text.split()[-1]
    lines = []

    for _ in range(repetitions):
        if not sound:
            break
        lines.append(sound)
        sound = sound[1:]

    lines.append(".")
    return "\n".join(lines)


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
