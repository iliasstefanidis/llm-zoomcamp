# llm-zoomcamp

Homework 2

Step 1:

run
pip install -q "qdrant-client[fastembed]>=1.14.2" to make the client work



Step 2

Open docker 
run 
docker run -p 6333:6333 -p 6334:6334 -v "${PWD}/qdrant_storage:/qdrant/storage" qdrant/qdrant


Step 3

run
pip install fastembed