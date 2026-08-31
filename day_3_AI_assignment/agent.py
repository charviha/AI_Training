import os
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

from tools import (
    document_search_tool,
    meeting_notes_tool
)

from memory import (
    add_to_short_term_memory,
    get_short_term_memory,
    retrieve_long_term_memory
)


# ============================================
# AGENT
# ============================================

def prepare_meeting(client_name):

    print("\n========================================")
    print("        AI CLIENT MEETING AGENT")
    print("========================================")

    print("\nClient:", client_name)

    # ----------------------------------------
    # SHORT-TERM MEMORY
    # ----------------------------------------

    add_to_short_term_memory(
        "user",
        f"Prepare me for my meeting with {client_name}."
    )

    # ----------------------------------------
    # AGENT PLANNING
    # ----------------------------------------

    print("\n[Agent] Understanding the user's request...")
    print("[Agent] Goal: Prepare a concise meeting brief.")
    print("[Agent] Client identified:", client_name)

    print("\n[Agent] Planning tool usage...")
    print("[Agent] Decision 1: Search client documents")
    print("[Agent] Decision 2: Retrieve previous meeting notes")
    print("[Agent] Decision 3: Retrieve long-term client memory")

    # ----------------------------------------
    # TOOL 1: DOCUMENT SEARCH
    # ----------------------------------------

    print("\n[Agent] Searching client documents...")

    document_results = document_search_tool(
        f"{client_name} main concerns priorities"
    )

    print(
        "[Agent] Retrieved",
        len(document_results),
        "relevant document chunks."
    )

    # ----------------------------------------
    # TOOL 2: MEETING NOTES
    # ----------------------------------------

    print("\n[Agent] Retrieving previous meeting notes...")

    meeting_results = meeting_notes_tool(
        client_name
    )

    print(
        "[Agent] Retrieved",
        len(meeting_results),
        "previous meetings."
    )

    # ----------------------------------------
    # TOOL 3: LONG-TERM MEMORY
    # ----------------------------------------

    print("\n[Agent] Retrieving long-term memory...")

    memory_results = retrieve_long_term_memory(
        client_name
    )

    print(
        "[Agent] Retrieved",
        len(memory_results),
        "memory items."
    )

    # ----------------------------------------
    # SHORT-TERM MEMORY
    # ----------------------------------------

    short_term_context = get_short_term_memory()

    print("\n[Agent] Checking conversation context...")

    print(
        "[Agent] Current conversation has",
        len(short_term_context),
        "messages."
    )

    # ----------------------------------------
    # AGENT REASONING
    # ----------------------------------------

    print("\n[Agent] Analyzing information...")

    brief = generate_meeting_brief(
        client_name,
        document_results,
        meeting_results,
        memory_results
    )

    # ----------------------------------------
    # STORE AGENT RESPONSE
    # ----------------------------------------

    add_to_short_term_memory(
        "agent",
        "Generated a meeting brief for "
        + client_name
    )

    return brief


# ============================================
# MEETING BRIEF GENERATION
# ============================================

def generate_meeting_brief(
    client_name,
    documents,
    meetings,
    memories
):

    # ----------------------------------------
    # Prepare retrieved context
    # ----------------------------------------

    document_context = "\n\n".join(
        [
            f"Source: {doc['source']}\n{doc['text']}"
            for doc in documents
        ]
    )

    meeting_context = "\n\n".join(
        [
            f"Source: {meeting['source']}\n{meeting['text']}"
            for meeting in meetings
        ]
    )

    memory_context = "\n".join(
        [
            f"- {memory['information']}"
            for memory in memories
        ]
    )

    # ----------------------------------------
    # Create LLM prompt
    # ----------------------------------------

    prompt = f"""
You are an AI client meeting preparation assistant.

The user is preparing for an upcoming meeting with {client_name}.

Use ONLY the information provided below.

CLIENT DOCUMENTS:
{document_context}

PREVIOUS MEETING NOTES:
{meeting_context}

LONG-TERM CLIENT MEMORY:
{memory_context}

Prepare a concise professional meeting brief.

Include these sections:

1. CLIENT OVERVIEW
2. MAIN CONCERNS
3. PREVIOUS MEETINGS
4. OPEN ACTION ITEMS
5. CLIENT MEMORY
6. TALKING POINTS
7. RECOMMENDED NEXT STEPS

Focus especially on unresolved issues and priorities from previous meetings.

Do not invent information that is not present in the supplied context.
Keep the response concise and useful for a manager who has the meeting shortly.
"""

    # ----------------------------------------
    # Gemini generation
    # ----------------------------------------

    response = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    return response.output_text