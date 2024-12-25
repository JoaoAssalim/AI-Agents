# Agentic AI System

### Overview

This project is an agentic AI system designed to solve problems by utilizing advanced natural language processing techniques and integrating multiple tools and models. 
The system dynamically retrieves relevant context, performs web searches, and summarizes responses based on the query.

<hr>

### Features


* Dynamic Context Retrieval: Automatically determines if additional context is needed to answer a query.

* Web Search Integration: Uses the `TavilySearchResults` tool to fetch relevant online information.

* Summarization and Routing: Summarizes responses and routes queries based on context relevance.

* Graph Workflow: Implements a state graph for handling workflows efficiently.

<hr>

### Technology Stack


* Programming Language: `Python`

* Frameworks and Libraries:

    * `LangChain`

    * `LangGraph`

    * `TavilySearchResults`

* Models:

    * `llama3-70b-8192` for language modeling.

* Utilities:

    * `PromptTemplate`

    * `JsonOutputParser`
 

<hr>

### Future Improvements

* Enhance vector database integration for better context retrieval.

* Optimize the summarization model for faster response times.

* Expand support for multilingual queries.
