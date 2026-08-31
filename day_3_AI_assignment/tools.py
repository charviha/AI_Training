from rag import search_documents
import os


# ============================================
# TOOL 1: DOCUMENT SEARCH
# ============================================

def document_search_tool(query):
    """
    Search client documents using FAISS RAG.
    """

    results = search_documents(query, k=3)

    return results


# ============================================
# TOOL 2: MEETING NOTES RETRIEVAL
# ============================================

def meeting_notes_tool(client_name):

    meeting_folder = "data/meeting_notes"

    meetings = []

    for file in os.listdir(meeting_folder):

        if file.endswith(".txt"):

            file_path = os.path.join(
                meeting_folder,
                file
            )

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                text = f.read()

            if client_name.lower() in text.lower():

                meetings.append({
                    "source": file,
                    "text": text
                })

    return meetings



if __name__ == "__main__":

    print("\n==============================")
    print("TESTING DOCUMENT SEARCH TOOL")
    print("==============================")

    results = document_search_tool(
        "What are Acme's main concerns?"
    )

    for result in results:

        print("\nSource:", result["source"])
        print("Text:", result["text"])


    print("\n==============================")
    print("TESTING MEETING NOTES TOOL")
    print("==============================")

    meetings = meeting_notes_tool("Acme")

    for meeting in meetings:

        print("\nSource:", meeting["source"])
        print("Text:", meeting["text"])