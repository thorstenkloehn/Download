from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import MWDumpLoader
import json

loader = MWDumpLoader(
    file_path="pagedump.xml",
    encoding="utf8"
)
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=0
)
texts = text_splitter.split_documents(docs)

json_output = [
    {
        "page_content": text.page_content,
        "metadata": text.metadata
    }
    for text in texts
]

# Print or save the JSON output.
print(json.dumps(json_output, indent=4, ensure_ascii=False))

# Optional: Save to a file
# with open("output.json", "w", encoding="utf-8") as f:
#     json.dump(json_output, f, indent=4, ensure_ascii=False)

