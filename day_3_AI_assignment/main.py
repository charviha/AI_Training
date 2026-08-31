from agent import prepare_meeting
from memory import get_short_term_memory


def main():

    print("========================================")
    print("     CLIENT MEETING PREPARATION AGENT")
    print("========================================")

    client_name = input(
        "\nEnter client name: "
    )

    if not client_name.strip():

        print("Please enter a client name.")

        return

    brief = prepare_meeting(
        client_name
    )

    print(brief)

    print("\n\n========================================")
    print("SHORT-TERM MEMORY")
    print("========================================")

    for item in get_short_term_memory():

        print(
            f"{item['role']}: {item['message']}"
        )


if __name__ == "__main__":

    main()