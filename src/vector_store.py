"""
ChromaDB Vector Store Module
Handles storage and retrieval of embeddings
"""
import chromadb
from typing import List, Dict, Optional
import uuid


class ChromaDBStore:
    """ChromaDB vector store for news articles"""
    
    def __init__(self, collection_name: str = "rpp_news", persist_directory: str = "./chroma_db"):
        """
        Initialize ChromaDB store
        
        Args:
            collection_name: Name of the collection
            persist_directory: Directory to persist the database
        """
        self.collection_name = collection_name
        self.persist_directory = persist_directory
        
        # Initialize ChromaDB persistent client
        self.client = chromadb.PersistentClient(path=persist_directory)
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )
    
    def add_documents(
        self,
        documents: List[str],
        metadatas: List[Dict],
        embeddings: Optional[List] = None,
        ids: Optional[List[str]] = None
    ):
        """
        Add documents to the collection
        
        Args:
            documents: List of document texts
            metadatas: List of metadata dictionaries
            embeddings: Optional list of embeddings (will be generated if not provided)
            ids: Optional list of document IDs (will be generated if not provided)
        """
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in documents]
        
        if embeddings is not None:
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                embeddings=embeddings,
                ids=ids
            )
        else:
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
    
    def upsert_documents(
        self,
        documents: List[str],
        metadatas: List[Dict],
        embeddings: Optional[List] = None,
        ids: Optional[List[str]] = None
    ):
        """
        Upsert (update or insert) documents to the collection
        
        Args:
            documents: List of document texts
            metadatas: List of metadata dictionaries
            embeddings: Optional list of embeddings
            ids: Optional list of document IDs
        """
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in documents]
        
        if embeddings is not None:
            self.collection.upsert(
                documents=documents,
                metadatas=metadatas,
                embeddings=embeddings,
                ids=ids
            )
        else:
            self.collection.upsert(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
    
    def query(
        self,
        query_texts: List[str],
        n_results: int = 10,
        where: Optional[Dict] = None
    ) -> Dict:
        """
        Query the collection
        
        Args:
            query_texts: List of query strings
            n_results: Number of results to return
            where: Optional metadata filter
            
        Returns:
            Query results dictionary
        """
        results = self.collection.query(
            query_texts=query_texts,
            n_results=n_results,
            where=where
        )
        return results
    
    def get_collection_count(self) -> int:
        """Get the number of documents in the collection"""
        return self.collection.count()
    
    def delete_collection(self):
        """Delete the collection"""
        self.client.delete_collection(name=self.collection_name)
