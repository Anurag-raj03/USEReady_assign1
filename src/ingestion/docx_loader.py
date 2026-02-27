from langchain_community.document_loaders import Docx2txtLoader
def load_docx(file_path: str) -> str:
    loader = Docx2txtLoader(file_path)
    documents = loader.load()
    return "\n".join([doc.page_content for doc in documents])