"""
LangChain Orchestration Module
Orchestrates the complete pipeline using LangChain
"""
from typing import List, Dict
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document


class NewsRetrievalPipeline:
    """End-to-end news retrieval pipeline using LangChain"""
    
    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        persist_directory: str = "./chroma_db"
    ):
        """
        Initialize the pipeline
        
        Args:
            model_name: Embedding model name
            persist_directory: ChromaDB persistence directory
        """
        self.model_name = model_name
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.vectorstore = None
    
    def load_and_process(self, news_items: List[Dict]) -> List[Document]:
        """
        Load and process news items into LangChain documents
        
        Args:
            news_items: List of news dictionaries
            
        Returns:
            List of LangChain Document objects
        """
        documents = []
        for item in news_items:
            # Create document content
            content = f"{item['title']}. {item['description']}"
            
            # Create metadata
            metadata = {
                'title': item['title'],
                'link': item['link'],
                'published': item['published'],
                'description': item['description']
            }
            
            # Create LangChain Document
            doc = Document(page_content=content, metadata=metadata)
            documents.append(doc)
        
        return documents
    
    def create_vectorstore(self, documents: List[Document]):
        """
        Create or update the vector store
        
        Args:
            documents: List of LangChain documents
        """
        self.vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.persist_directory,
            collection_name="rpp_news_langchain"
        )
    
    def query(self, query_text: str, k: int = 10) -> pd.DataFrame:
        """
        Query the vector store and return results as DataFrame
        
        Args:
            query_text: Query string
            k: Number of results to return
            
        Returns:
            DataFrame with results
        """
        if self.vectorstore is None:
            raise ValueError("Vector store not initialized. Call create_vectorstore first.")
        
        # Perform similarity search
        results = self.vectorstore.similarity_search(query_text, k=k)
        
        # Convert to DataFrame
        data = []
        for doc in results:
            data.append({
                'title': doc.metadata.get('title', ''),
                'description': doc.metadata.get('description', ''),
                'link': doc.metadata.get('link', ''),
                'date_published': doc.metadata.get('published', '')
            })
        
        return pd.DataFrame(data)
    
    def run_pipeline(self, news_items: List[Dict], query_text: str, k: int = 10) -> pd.DataFrame:
        """
        Run the complete pipeline: load → embed → store → query
        
        Args:
            news_items: List of news dictionaries
            query_text: Query string
            k: Number of results to return
            
        Returns:
            DataFrame with query results
        """
        # Load and process
        documents = self.load_and_process(news_items)
        
        # Create vector store
        self.create_vectorstore(documents)
        
        # Query
        results = self.query(query_text, k)
        
        return results
