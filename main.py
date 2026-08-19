from menu import Menu


def main() -> None:
    print(
        "\n================================"
        "\n   Welcome to Library System"
        "\n================================"
    )

    menu = Menu()
    menu.run()


if __name__ == "__main__":
    main()