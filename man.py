
from typing_spee import typing_report


def main():
    original = input("Перепишіть текст: ")
    input("Натисніть Enter, коли будете готові почати друк...")
    typed = input("Надрукуйте текст ще раз: ")

    seconds = float(input("Скільки секунд витратили? "))

    report = typing_report(original, typed, seconds)

    print("\n--- Результати ---")
    print(f"Швидкість: {report['words_per_minute']:.2f} слів/хв")
    print(f"Помилки: {report['error_percentage']:.2f}%")
    print(f"Точність: {report['accuracy']:.2f}%")


if __name__ == "__main__":
    main()
