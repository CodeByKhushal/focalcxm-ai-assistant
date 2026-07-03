import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import config
from utils.scraper import get_page_text


urls = [
    "https://www.focalcxm.com/",
    "https://www.focalcxm.com/about-us/",
    "https://www.focalcxm.com/contact-us/",
    "https://www.focalcxm.com/partners/",
    "https://www.focalcxm.com/case-studies/",
    "https://www.focalcxm.com/blogs/",
    "https://www.focalcxm.com/resources/",
    "https://www.focalcxm.com/crm-managed-service/",
    "https://www.focalcxm.com/crm-blueprinting/",
    "https://www.focalcxm.com/data-services/",
    "https://www.focalcxm.com/salesforce/",
    "https://www.focalcxm.com/veeva-managed-services/",
    "https://www.focalcxm.com/enterprise-search/",
    "https://www.focalcxm.com/omnichannel/",
    "https://www.focalcxm.com/b2b-rebates/",
   "https://www.focalcxm.com/life-sciences/#"

]


all_text = ""

for url in urls:
    print(f"Scraping: {url}")

    page_text = get_page_text(url)

    if page_text:
        all_text += f"\n\nSource: {url}\n{page_text}"


os.makedirs("data", exist_ok=True)

with open("data/raw_text.txt", "w", encoding="utf-8") as f:
    f.write(all_text)


splitter = RecursiveCharacterTextSplitter(
    chunk_size=config.CHUNK_SIZE,
    chunk_overlap=config.CHUNK_OVERLAP,
)

chunks = splitter.split_text(all_text)

print(f"Total chunks created: {len(chunks)}")


embeddings = HuggingFaceEmbeddings(
    model_name=config.EMBEDDING_MODEL
)

vector_store = FAISS.from_texts(chunks, embeddings)

os.makedirs("vectorstore", exist_ok=True)

vector_store.save_local(config.VECTORSTORE_PATH)

print("Ingestion completed successfully.")