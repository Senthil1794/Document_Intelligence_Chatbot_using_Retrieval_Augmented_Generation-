# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 12:18:10 2026

@author: Senthil
"""

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
#from langchain_community.vectorstores import FAISS

from langchain.text_splitter import CharacterTextSplitter
#from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain.llms import OpenAI

from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

def get_llm(path):
    loader = DirectoryLoader(
                path=path,
                glob="**/*.pdf",
                loader_cls=PyPDFLoader
            )
    documents = loader.load()
    
    # We need to split the text using Character Text Split such that it should not increase token size
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 2000,
        chunk_overlap  = 200,
        length_function = len,
    )
    
    texts = text_splitter.split_documents(documents)
 
    openai_api_key = "IF5d4Q7Z4GubQOPiT2RGrJ5-J-hSIbHNpoaPcq0xUA"
    
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    vector_db = FAISS.from_documents(texts, embeddings)
    
    llm = OpenAI(
        openai_api_key=openai_api_key,
        model_name="gpt-3.5-turbo-instruct"
    )
    

    qa = ConversationalRetrievalChain.from_llm(llm=llm, 
                                     chain_type="stuff",\
                                     retriever=vector_db.as_retriever())

    return qa
    






















