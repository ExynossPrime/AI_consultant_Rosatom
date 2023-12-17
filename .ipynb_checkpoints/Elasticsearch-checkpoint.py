import getpass
import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import ElasticsearchStore

for key in os.environ:
    print(key, '=>', os.environ[key])

print('процесс идет')

openai_api_key = "ZWNhNjg5MDEtOGIxYS00Nzg1LWFiOTAtMjQ4ZjhmYjViZGIzOjZkNjk3ZWEyLTkwYTgtNDNmNC04YTIzLTMwODljY2QyZDA2OQ=="
os.environ["OPENAI_API_KEY"] = openai_api_key


print('процесс идет')
embeddings = OpenAIEmbeddings()

from langchain.document_loaders import TextLoader
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
print('Процесс идет')
# loader = TextLoader("../../modules/titanic_wiki_ru.txt")
# loader = TextLoader("НПА/ЕОСЗ (с изм., утв.31.01.2023 №174, вст.в силу 14.03.2023)/ЕОСЗ (с изм., утв.31.01.2023 № 174, вст. в силу 14.03.2023).doc")
# loader = TextLoader("C:/Users/Roman/PycharmProjects/AI_consultant_Rosatom/sharl-perro-zolushka-ili-xrustalnaya-tufelka.txt")
loader = TextLoader("Cinderella.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

print(f"Total docs: {len(docs)}")

# docs = retriever.get_relevant_documents(query="Титаник", lang="ru")
db = ElasticsearchStore.from_documents(
    docs,
    embeddings,
    es_url="http://localhost:9200",
    index_name="test-basic",
)

db.client.indices.refresh(index="test-basic")