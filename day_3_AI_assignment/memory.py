import json
import os


# ============================================
# MEMORY FILE
# ============================================

MEMORY_FILE = "memory.json"


# ============================================
# SHORT-TERM MEMORY
# ============================================

conversation_memory = []


def add_to_short_term_memory(role, message):

    conversation_memory.append({
        "role": role,
        "message": message
    })


def get_short_term_memory():

    return conversation_memory


def clear_short_term_memory():

    conversation_memory.clear()


# ============================================
# LONG-TERM MEMORY
# ============================================

def load_long_term_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def save_long_term_memory(
    client,
    information,
    memory_type
):

    memories = load_long_term_memory()

    new_memory = {
        "client": client,
        "information": information,
        "type": memory_type
    }

    memories.append(new_memory)

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memories,
            f,
            indent=4
        )


def retrieve_long_term_memory(client):

    memories = load_long_term_memory()

    results = []

    for memory in memories:

        if client.lower() in memory.get(
            "client",
            ""
        ).lower():

            results.append(memory)

    return results


# ============================================
# TEST MEMORY
# ============================================

if __name__ == "__main__":

    print("\n========================================")
    print("        MEMORY SYSTEM TEST")
    print("========================================")

    # ----------------------------------------
    # SHORT-TERM MEMORY TEST
    # ----------------------------------------

    print("\n[1] SHORT-TERM MEMORY")

    clear_short_term_memory()

    add_to_short_term_memory(
        "user",
        "Prepare me for my meeting with Acme Corp."
    )

    add_to_short_term_memory(
        "agent",
        "I will retrieve Acme's client information."
    )

    add_to_short_term_memory(
        "user",
        "Focus especially on pricing and timeline."
    )

    print("\nCurrent conversation:")

    for item in get_short_term_memory():

        print(
            f"{item['role']}: {item['message']}"
        )

    # ----------------------------------------
    # LONG-TERM MEMORY TEST
    # ----------------------------------------

    print("\n[2] LONG-TERM MEMORY")

    print("\nStored Acme information:")

    memories = retrieve_long_term_memory(
        "Acme Corp"
    )

    for memory in memories:

        print(
            f"- [{memory['type']}] "
            f"{memory['information']}"
        )

    print("\n========================================")
    print("        MEMORY TEST COMPLETE")
    print("========================================")