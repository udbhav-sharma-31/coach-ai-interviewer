import json
import os
import random
import re

from backend.evaluation.create_dataset import QUESTIONS as SEED_QUESTIONS


OUTPUT_PATH = "data/interview_answers.json"

TARGET_QUESTIONS = 10_000

random.seed(42)


# ============================================================
# QUESTION GENERATION BANK
# ============================================================

QUESTION_BANK = {
    "python": [
        ("What is {concept} in Python?", "{concept}"),
        ("Explain how {concept} works in Python.", "{concept}"),
        ("Why is {concept} important in Python?", "{concept}"),
        ("What are the advantages of using {concept}?", "{concept}"),
        ("What are common mistakes when using {concept}?", "{concept}"),
        ("How would you use {concept} in a real Python application?", "{concept}"),
        ("How does {concept} differ from related Python concepts?", "{concept}"),
        ("When should a Python developer use {concept}?", "{concept}"),
    ],

    "machine-learning": [
        ("What is {concept} in machine learning?", "{concept}"),
        ("Explain how {concept} works.", "{concept}"),
        ("Why is {concept} important in machine learning?", "{concept}"),
        ("What problem does {concept} solve?", "{concept}"),
        ("What are the advantages of {concept}?", "{concept}"),
        ("What are common mistakes involving {concept}?", "{concept}"),
        ("How would you apply {concept} to a real ML problem?", "{concept}"),
        ("How is {concept} different from related ML techniques?", "{concept}"),
    ],

    "deep-learning": [
        ("What is {concept} in deep learning?", "{concept}"),
        ("Explain how {concept} works in a neural network.", "{concept}"),
        ("Why is {concept} important in deep learning?", "{concept}"),
        ("What problem does {concept} solve?", "{concept}"),
        ("What happens if {concept} is implemented incorrectly?", "{concept}"),
        ("How would you use {concept} in a practical neural network?", "{concept}"),
        ("How does {concept} compare with related deep-learning concepts?", "{concept}"),
        ("What are common misconceptions about {concept}?", "{concept}"),
    ],

    "transformers": [
        ("What is {concept} in a Transformer?", "{concept}"),
        ("Explain how {concept} works in Transformers.", "{concept}"),
        ("Why is {concept} important in Transformer models?", "{concept}"),
        ("What problem does {concept} solve in Transformers?", "{concept}"),
        ("What happens if {concept} is removed from a Transformer?", "{concept}"),
        ("How would you explain {concept} to a developer?", "{concept}"),
        ("How is {concept} different from related Transformer mechanisms?", "{concept}"),
        ("What are common mistakes when implementing {concept}?", "{concept}"),
    ],

    "llm": [
        ("What is {concept} in large language models?", "{concept}"),
        ("Explain how {concept} works in an LLM.", "{concept}"),
        ("Why is {concept} important for LLM applications?", "{concept}"),
        ("What problem does {concept} solve?", "{concept}"),
        ("What are the limitations of {concept}?", "{concept}"),
        ("How would you use {concept} in a real LLM application?", "{concept}"),
        ("How does {concept} differ from related LLM techniques?", "{concept}"),
        ("What can go wrong when using {concept}?", "{concept}"),
    ],

    "rag": [
        ("What is {concept} in RAG?", "{concept}"),
        ("Explain how {concept} works in a RAG system.", "{concept}"),
        ("Why is {concept} important in retrieval-augmented generation?", "{concept}"),
        ("What problem does {concept} solve in RAG?", "{concept}"),
        ("What are common mistakes involving {concept}?", "{concept}"),
        ("How would you use {concept} in a production RAG system?", "{concept}"),
        ("How does {concept} differ from related RAG techniques?", "{concept}"),
        ("How can {concept} affect RAG quality?", "{concept}"),
    ],

    "agent": [
        ("What is {concept} in an AI agent?", "{concept}"),
        ("Explain how {concept} works in AI agents.", "{concept}"),
        ("Why is {concept} important for AI agents?", "{concept}"),
        ("What problem does {concept} solve?", "{concept}"),
        ("What are the risks of using {concept}?", "{concept}"),
        ("How would you implement {concept} in an AI agent?", "{concept}"),
        ("How does {concept} differ from related agent concepts?", "{concept}"),
        ("What can go wrong when using {concept}?", "{concept}"),
    ],

    "backend": [
        ("What is {concept} in backend development?", "{concept}"),
        ("Explain how {concept} works in a backend application.", "{concept}"),
        ("Why is {concept} important in backend systems?", "{concept}"),
        ("What problem does {concept} solve?", "{concept}"),
        ("What are common mistakes involving {concept}?", "{concept}"),
        ("How would you implement {concept} in a production API?", "{concept}"),
        ("How does {concept} compare with related backend concepts?", "{concept}"),
        ("What happens when {concept} is designed incorrectly?", "{concept}"),
    ],

    "system-design": [
        ("What is {concept} in system design?", "{concept}"),
        ("Explain how {concept} works in a distributed system.", "{concept}"),
        ("Why is {concept} important in system design?", "{concept}"),
        ("What problem does {concept} solve?", "{concept}"),
        ("What are the trade-offs of {concept}?", "{concept}"),
        ("How would you use {concept} in a production system?", "{concept}"),
        ("How does {concept} compare with related architecture patterns?", "{concept}"),
        ("What can go wrong when {concept} is poorly designed?", "{concept}"),
    ],
}


# ============================================================
# TECHNICAL CONCEPTS
# ============================================================

CONCEPTS = {
    "python": [
        "list",
        "tuple",
        "dictionary",
        "set",
        "generator",
        "iterator",
        "decorator",
        "lambda function",
        "list comprehension",
        "exception handling",
        "context manager",
        "inheritance",
        "polymorphism",
        "encapsulation",
        "abstract class",
        "virtual environment",
        "module",
        "package",
        "mutable object",
        "immutable object",
        "shallow copy",
        "deep copy",
        "GIL",
        "asyncio",
        "async function",
        "await",
        "threading",
        "multiprocessing",
        "type hints",
        "dataclass",
        "property",
        "classmethod",
        "staticmethod",
        "recursion",
        "memory management",
        "garbage collection",
        "serialization",
        "JSON handling",
        "file handling",
        "unit testing",
    ],

    "machine-learning": [
        "linear regression",
        "logistic regression",
        "decision tree",
        "random forest",
        "gradient boosting",
        "support vector machine",
        "KNN",
        "K-means",
        "PCA",
        "feature scaling",
        "normalization",
        "standardization",
        "feature engineering",
        "feature selection",
        "cross-validation",
        "train-test split",
        "overfitting",
        "underfitting",
        "bias",
        "variance",
        "regularization",
        "L1 regularization",
        "L2 regularization",
        "learning rate",
        "gradient descent",
        "batch gradient descent",
        "stochastic gradient descent",
        "classification",
        "regression",
        "clustering",
        "precision",
        "recall",
        "F1 score",
        "ROC-AUC",
        "confusion matrix",
        "class imbalance",
        "hyperparameter tuning",
        "ensemble learning",
        "data leakage",
    ],

    "deep-learning": [
        "neural network",
        "perceptron",
        "activation function",
        "ReLU",
        "sigmoid",
        "softmax",
        "forward propagation",
        "backpropagation",
        "gradient descent",
        "loss function",
        "cross-entropy loss",
        "mean squared error",
        "dropout",
        "batch normalization",
        "weight initialization",
        "vanishing gradient",
        "exploding gradient",
        "CNN",
        "RNN",
        "LSTM",
        "GRU",
        "convolution",
        "pooling",
        "attention",
        "embedding",
        "transfer learning",
        "fine-tuning",
        "epoch",
        "batch size",
        "optimizer",
        "Adam",
        "SGD optimizer",
        "learning rate scheduling",
        "early stopping",
        "residual connection",
        "skip connection",
        "parameter",
        "neuron",
        "hidden layer",
        "output layer",
    ],

    "transformers": [
        "self-attention",
        "multi-head attention",
        "query",
        "key",
        "value",
        "attention score",
        "scaled dot-product attention",
        "positional encoding",
        "token embedding",
        "encoder",
        "decoder",
        "encoder-decoder architecture",
        "causal masking",
        "padding mask",
        "feed-forward network",
        "residual connection",
        "layer normalization",
        "Transformer block",
        "context window",
        "autoregressive generation",
        "attention head",
        "tokenization",
        "subword tokenization",
        "BERT",
        "GPT",
        "sequence-to-sequence",
        "cross-attention",
        "beam search",
        "greedy decoding",
        "temperature",
        "top-k sampling",
        "top-p sampling",
        "Transformer training",
        "Transformer inference",
        "long-context modeling",
    ],

    "llm": [
        "large language model",
        "tokenization",
        "prompt engineering",
        "system prompt",
        "few-shot prompting",
        "zero-shot prompting",
        "chain-of-thought",
        "structured output",
        "JSON output",
        "temperature",
        "top-p sampling",
        "hallucination",
        "fine-tuning",
        "instruction tuning",
        "RLHF",
        "context window",
        "inference",
        "quantization",
        "LoRA",
        "PEFT",
        "model serving",
        "function calling",
        "tool calling",
        "LLM evaluation",
        "prompt injection",
        "guardrails",
        "model latency",
        "model cost",
        "batch inference",
        "streaming generation",
        "open-source LLM",
        "API-based LLM",
    ],

    "rag": [
        "retrieval-augmented generation",
        "document ingestion",
        "PDF extraction",
        "text extraction",
        "chunking",
        "chunk size",
        "chunk overlap",
        "embedding",
        "embedding model",
        "vector database",
        "FAISS",
        "vector search",
        "semantic search",
        "BM25",
        "hybrid retrieval",
        "metadata filtering",
        "reranking",
        "retriever",
        "top-k retrieval",
        "context retrieval",
        "query rewriting",
        "document preprocessing",
        "retrieval evaluation",
        "answer grounding",
        "citation generation",
        "knowledge base",
        "resume RAG",
        "RAG pipeline",
        "retrieval latency",
        "embedding similarity",
        "cosine similarity",
        "context compression",
        "duplicate chunks",
        "retrieval failure",
    ],

    "agent": [
        "AI agent",
        "agent loop",
        "tool calling",
        "function calling",
        "agent state",
        "memory",
        "short-term memory",
        "long-term memory",
        "planning",
        "reasoning",
        "tool selection",
        "agent workflow",
        "multi-agent system",
        "agent orchestration",
        "LangGraph",
        "state graph",
        "conditional routing",
        "human-in-the-loop",
        "agent checkpointing",
        "agent evaluation",
        "tool error handling",
        "agent hallucination",
        "agent guardrails",
        "agent termination",
        "workflow state",
        "autonomous agent",
        "react agent",
        "task decomposition",
        "agent observability",
        "agent reliability",
    ],

    "backend": [
        "REST API",
        "FastAPI",
        "HTTP request",
        "HTTP response",
        "GET request",
        "POST request",
        "PUT request",
        "DELETE request",
        "middleware",
        "authentication",
        "authorization",
        "JWT",
        "OAuth",
        "API validation",
        "Pydantic",
        "WebSocket",
        "async endpoint",
        "database connection",
        "connection pooling",
        "caching",
        "Redis",
        "rate limiting",
        "logging",
        "error handling",
        "API versioning",
        "background task",
        "task queue",
        "serialization",
        "CORS",
        "dependency injection",
        "API security",
        "request timeout",
        "retry logic",
    ],

    "system-design": [
        "load balancer",
        "horizontal scaling",
        "vertical scaling",
        "caching",
        "database replication",
        "database sharding",
        "message queue",
        "event-driven architecture",
        "microservices",
        "monolith",
        "service discovery",
        "API gateway",
        "CDN",
        "rate limiting",
        "fault tolerance",
        "high availability",
        "disaster recovery",
        "CAP theorem",
        "eventual consistency",
        "strong consistency",
        "idempotency",
        "distributed lock",
        "circuit breaker",
        "observability",
        "logging",
        "monitoring",
        "horizontal partitioning",
        "read replica",
        "write replica",
        "database indexing",
        "queue processing",
        "distributed cache",
        "scalability",
        "reliability",
        "latency",
    ],
}


# ============================================================
# ANSWER VARIATIONS
# ============================================================

# These are concept-aware answer banks.
# Each concept has multiple realistic explanations for the
# different quality levels.
#
# IMPORTANT:
# The answers intentionally become more complete as the label
# increases, but they do NOT rely only on answer length.

ANSWER_PATTERNS = {

    "list": {
        0: [
            "A list is an immutable Python object that cannot be changed.",
            "A list stores only one fixed value and cannot contain multiple elements.",
            "A list is mainly used for defining functions."
        ],
        1: [
            "A list is a Python collection used to store multiple values.",
            "A list holds several elements in one object.",
            "Lists are collections that can contain multiple Python values."
        ],
        2: [
            "A list is an ordered, mutable collection that can contain multiple elements. It can be changed after creation.",
            "Lists store elements in order and allow modification such as adding or removing items, although this explanation does not cover all their behavior.",
            "A Python list can hold multiple values and can be modified after it is created."
        ],
        3: [
            "A list is an ordered and mutable Python collection. Elements can be accessed by index, and items can be added, removed, or modified.",
            "Python lists store elements in a defined order and support operations such as indexing, slicing, insertion, deletion, and modification.",
            "A list is useful when a program needs an ordered collection whose contents may change during execution."
        ],
        4: [
            "A Python list is an ordered, mutable sequence that can contain values of different types. It supports indexing and slicing and provides operations such as append, insert, remove, and pop. Its mutability makes it useful when a collection needs to change during program execution.",
            "Lists are dynamic ordered collections in Python. They allow indexing, slicing, iteration, and modification, and their elements do not have to share the same type. They are commonly used when maintaining a changing sequence of values.",
            "A list combines ordered storage with mutability. Python manages its underlying dynamic array so elements can be added or removed, while indexing provides efficient access by position."
        ]
    },

    "tuple": {
        0: [
            "A tuple is a mutable collection that must be changed frequently.",
            "A tuple is a Python dictionary with key-value pairs.",
            "A tuple is mainly used for storing only strings."
        ],
        1: [
            "A tuple is a Python collection used to store multiple values.",
            "A tuple is similar to a list and can contain several elements.",
            "Tuples are collections that group multiple values together."
        ],
        2: [
            "A tuple is an ordered collection whose elements cannot normally be changed after creation. It is similar to a list but is immutable.",
            "Tuples store values in order and are generally used when the collection should not be modified after it is created.",
            "A tuple provides ordered storage like a list, but its elements cannot be reassigned after creation."
        ],
        3: [
            "A tuple is an ordered, immutable sequence in Python. It supports indexing and iteration but does not provide normal operations for changing its elements.",
            "Tuples are useful for representing fixed collections of values, while lists are preferable when the contents need to change.",
            "Because tuples are immutable, they can be useful for fixed records and can also be used as dictionary keys when their elements are hashable."
        ],
        4: [
            "A tuple is an ordered and immutable Python sequence. It supports indexing, slicing, and iteration, but its elements cannot be reassigned after creation. Immutability makes tuples useful for fixed records and allows hashable tuples to be used as dictionary keys.",
            "Tuples are appropriate when a collection represents a fixed group of values. Unlike lists, their structure cannot normally be modified after creation, which can communicate that the data should remain unchanged.",
            "The main distinction between a list and tuple is mutability: lists are designed for changing sequences, whereas tuples represent fixed sequences. Tuple immutability can also make them suitable for hashing when all contained values are hashable."
        ]
    },

    "overfitting": {
        0: [
            "Overfitting means the model performs equally well on every possible dataset.",
            "Overfitting happens when the training data is completely ignored.",
            "Overfitting is the process of making a model smaller."
        ],
        1: [
            "Overfitting happens when a model learns the training data too closely.",
            "It means the model performs well on training data but has difficulty with new data.",
            "Overfitting occurs when a model becomes too specialized to its training examples."
        ],
        2: [
            "Overfitting occurs when a model learns training examples and their noise too closely, which can reduce performance on unseen data.",
            "An overfit model usually has strong training performance but weaker validation or test performance because it has not generalized well.",
            "The model becomes too specialized to the training dataset instead of learning patterns that transfer to new examples."
        ],
        3: [
            "Overfitting occurs when a model captures training data too specifically, including noise, causing a gap between training and validation performance. Techniques such as regularization, dropout, data augmentation, or early stopping can help.",
            "A typical sign of overfitting is decreasing training loss while validation loss begins increasing. The model is memorizing aspects of the training set rather than learning general patterns.",
            "Overfitting reduces generalization. It can be addressed by using more representative data, reducing model complexity, regularization, dropout, cross-validation, or early stopping."
        ],
        4: [
            "Overfitting occurs when a model learns patterns specific to the training set, including noise, rather than patterns that generalize. A common signal is that training loss continues to decrease while validation loss rises. Solutions include more diverse data, regularization, dropout, data augmentation, simpler models, and early stopping.",
            "An overfit model can achieve excellent training accuracy while performing poorly on unseen examples. The underlying issue is poor generalization, not simply high model capacity. Validation data, regularization, appropriate model complexity, and representative training examples are therefore important.",
            "Overfitting should be diagnosed using a held-out validation or test set rather than training metrics alone. For neural networks, methods such as weight decay, dropout, early stopping, and stronger data diversity can reduce memorization while preserving useful learned representations."
        ]
    },

    "self-attention": {
        0: [
            "Self-attention removes all relationships between tokens.",
            "Self-attention is a database storage mechanism.",
            "Self-attention converts every token directly into a label."
        ],
        1: [
            "Self-attention allows tokens in a sequence to interact with each other.",
            "It helps a Transformer consider relationships between tokens.",
            "Self-attention lets the model look at other tokens when processing a token."
        ],
        2: [
            "Self-attention allows each token to assign importance to other tokens in the same sequence. It uses query, key, and value representations to compute these relationships.",
            "The mechanism compares token representations to determine which other tokens are relevant, although this description does not cover the full attention calculation.",
            "Self-attention captures relationships between positions in a sequence by calculating attention weights between tokens."
        ],
        3: [
            "Self-attention uses queries, keys, and values to calculate how strongly each token should attend to other tokens. The resulting weighted combination of values creates context-aware representations.",
            "In a Transformer, self-attention lets every position consider information from other positions in the same sequence. Attention scores determine how much each value contributes to the output.",
            "Self-attention is useful because the representation of a token can incorporate relevant information from other tokens rather than relying only on nearby positions."
        ],
        4: [
            "Self-attention computes relationships among tokens using query, key, and value projections. Query-key similarities are scaled and normalized to produce attention weights, which are then used to combine the value vectors. This allows each position to build a context-dependent representation.",
            "The key advantage of self-attention is that it can model dependencies between distant tokens directly. Multi-head attention extends this by learning several attention patterns in parallel, while positional information provides sequence-order information.",
            "In a Transformer, self-attention maps each token representation into queries, keys, and values, calculates scaled similarity scores, applies normalization, and forms a weighted sum of values. This mechanism allows contextual information to flow between positions efficiently."
        ]
    },

    "embedding": {
        0: [
            "An embedding converts every input into a random database row.",
            "An embedding is only used for storing PDF files.",
            "Embeddings remove the meaning from text."
        ],
        1: [
            "An embedding represents data as a vector.",
            "Embeddings convert text or other objects into numerical vectors.",
            "An embedding is a numerical representation of an input."
        ],
        2: [
            "An embedding represents an item such as text as a numerical vector so that similar items can be compared mathematically.",
            "Text embeddings map language into a vector space where semantically related text can have similar representations.",
            "An embedding converts an input into numbers that capture useful characteristics, although the exact representation depends on the model."
        ],
        3: [
            "Text embeddings transform text into dense numerical vectors that capture semantic information. Similar pieces of text can therefore be compared using vector similarity measures.",
            "Embeddings are useful in semantic search and RAG because documents and queries can be represented in the same vector space and compared for similarity.",
            "A good embedding model places semantically related inputs closer together in vector space, allowing applications such as retrieval, clustering, and recommendation to operate on numerical representations."
        ],
        4: [
            "An embedding is a dense vector representation produced by a learned model. For text, the vector encodes semantic and contextual characteristics so that related texts can occupy nearby regions of the embedding space. RAG systems use this property to retrieve documents relevant to a query.",
            "Embeddings convert discrete language into continuous numerical representations suitable for similarity calculations. During semantic retrieval, a query embedding can be compared with document embeddings using measures such as cosine similarity to identify relevant context.",
            "The quality of an embedding model strongly affects retrieval quality. A useful embedding space should place semantically relevant queries and documents near each other while separating unrelated content, which is why model choice and domain-specific evaluation matter in RAG."
        ]
    },

    "rag": {
        0: [
            "RAG means generating answers without using any retrieved information.",
            "RAG is only a database backup technique.",
            "RAG removes documents before generating an answer."
        ],
        1: [
            "RAG retrieves information and uses it to help generate an answer.",
            "RAG combines retrieval with language generation.",
            "A RAG system searches documents before producing a response."
        ],
        2: [
            "Retrieval-Augmented Generation retrieves relevant information from an external knowledge source and provides that information to a language model as context before generation.",
            "RAG combines a retrieval step with generation so the model can use information from documents rather than relying only on its parameters.",
            "A RAG pipeline normally retrieves relevant document chunks and includes them in the generation context."
        ],
        3: [
            "RAG combines retrieval and generation. A query is converted into a representation, relevant documents or chunks are retrieved, and the retrieved context is passed to an LLM to produce a grounded answer.",
            "RAG is useful when an application needs an LLM to answer using changing or private information. The retrieval stage provides relevant external context while the LLM handles language understanding and generation.",
            "A typical RAG pipeline includes document ingestion, chunking, embeddings, vector retrieval, optional reranking, context construction, and generation. Retrieval quality directly affects the quality of the final response."
        ],
        4: [
            "Retrieval-Augmented Generation separates knowledge retrieval from language generation. Documents are processed into chunks and embeddings, a user query retrieves relevant context, and an LLM generates an answer from that context. This can improve grounding and allows knowledge to be updated without retraining the LLM.",
            "A production RAG system usually involves document preprocessing, chunking, embedding generation, indexing, retrieval, optional hybrid search or reranking, context construction, and LLM generation. Each stage can introduce errors, so retrieval quality, grounding, latency, and evaluation must be considered together.",
            "RAG is particularly useful for private or frequently changing knowledge because the knowledge base can be updated independently of the language model. However, retrieving irrelevant or incomplete context can still cause poor answers, so techniques such as metadata filtering, hybrid retrieval, reranking, and retrieval evaluation may be necessary."
        ]
    },

    "hallucination": {
        0: [
            "Hallucination means the model always produces a verified factual answer.",
            "Hallucination is a technique for improving database indexing.",
            "Hallucination means reducing the number of model parameters."
        ],
        1: [
            "An LLM hallucination is an answer that contains incorrect or unsupported information.",
            "Hallucination occurs when a model generates information that may not be factual.",
            "It refers to generated content that is not properly supported by evidence."
        ],
        2: [
            "An LLM hallucination occurs when the model produces information that is false, unsupported, or inconsistent with the available evidence.",
            "Hallucination can occur when a language model generates plausible-sounding content without having reliable evidence for the claim.",
            "A hallucinated answer may sound confident even though the information is incorrect or cannot be supported by the provided context."
        ],
        3: [
            "LLM hallucination refers to generating plausible but incorrect or unsupported information. Retrieval, grounding, constrained output, verification, and careful prompting can reduce the risk.",
            "Hallucinations are a reliability problem because language models optimize generation rather than guaranteeing factual correctness. Providing relevant context and evaluating claims can reduce unsupported responses.",
            "A model can hallucinate when it lacks sufficient information or when generation produces a plausible continuation that is not grounded in reality. RAG and verification mechanisms are common mitigation strategies."
        ],
        4: [
            "An LLM hallucination is a generated claim that is false, unsupported, or not entailed by the available evidence. Because language models generate probable sequences rather than directly querying truth, hallucinations can occur even when the response sounds confident. Grounded retrieval, citations, validation, constrained generation, and domain-specific evaluation can reduce the risk.",
            "Hallucination should be evaluated separately from fluency. A response may be grammatically excellent while containing unsupported claims. In a RAG application, evaluation should therefore examine whether important claims are supported by retrieved context rather than judging only how natural the response sounds.",
            "Reducing hallucinations is usually a system-level problem rather than something solved by a single prompt. Relevant retrieval, high-quality context, appropriate model instructions, tool-based verification, structured outputs, and post-generation validation can work together to improve factual reliability."
        ]
    },

    "fastapi": {
        0: [
            "FastAPI is a relational database engine.",
            "FastAPI is a frontend CSS framework.",
            "FastAPI is a Python operating system."
        ],
        1: [
            "FastAPI is a Python framework for building APIs.",
            "FastAPI helps developers create web APIs using Python.",
            "FastAPI is commonly used to build backend HTTP services."
        ],
        2: [
            "FastAPI is a Python web framework designed for building APIs. It uses type hints and supports asynchronous endpoints.",
            "FastAPI provides tools for defining HTTP routes, validating request data, and returning responses from Python applications.",
            "FastAPI is used to implement backend APIs and can automatically generate API documentation from route and schema definitions."
        ],
        3: [
            "FastAPI is a Python framework for building HTTP APIs. It uses Python type hints for validation and schema generation and supports asynchronous request handling.",
            "FastAPI provides routing, request validation, dependency injection, and automatic OpenAPI documentation, making it suitable for modern backend services.",
            "A FastAPI application can expose endpoints that receive validated request data, execute application logic, and return structured responses to clients."
        ],
        4: [
            "FastAPI is a modern Python framework for building HTTP APIs. It uses type annotations and Pydantic-based validation to define request and response schemas and can generate OpenAPI documentation automatically. It also supports async endpoints, making it useful for I/O-heavy backend services.",
            "FastAPI combines routing, validation, dependency injection, automatic API documentation, and asynchronous programming support. In a production application, these capabilities can be combined with authentication, database access, middleware, logging, and error handling.",
            "One reason FastAPI is useful for AI applications is that it can expose model inference and orchestration pipelines through typed HTTP endpoints while supporting asynchronous workloads. Careful resource management is still necessary because CPU/GPU-bound model inference can limit concurrency."
        ]
    },

    "websocket": {
        0: [
            "A WebSocket is a file compression format.",
            "WebSocket only supports one-way communication from a server during startup.",
            "WebSocket is a SQL query language."
        ],
        1: [
            "WebSocket provides a persistent connection between a client and server.",
            "WebSockets allow clients and servers to exchange messages over an open connection.",
            "A WebSocket is useful for real-time communication."
        ],
        2: [
            "WebSocket provides a persistent connection that allows the client and server to send messages without creating a new HTTP request for every message.",
            "WebSockets support two-way communication over an established connection, which makes them useful for real-time applications.",
            "A WebSocket connection stays open so the server can send updates to the client as events occur."
        ],
        3: [
            "WebSockets provide full-duplex communication over a persistent connection. Both the client and server can send messages after the connection is established, making them useful for chat, streaming, and real-time updates.",
            "Unlike ordinary request-response HTTP communication, WebSockets allow a server to push events to a connected client without waiting for another request.",
            "A real-time AI application can use WebSockets to stream interview events, partial speech results, model responses, or evaluation updates to the frontend."
        ],
        4: [
            "WebSockets establish a persistent, bidirectional connection between a client and server. After the initial handshake, either side can send messages without repeatedly establishing HTTP requests. This makes WebSockets suitable for low-latency applications such as live interviews, chat, streaming transcription, and real-time status updates.",
            "For an AI interviewer, WebSockets can carry events such as candidate speech, partial transcription, generated questions, evaluation updates, and completion notifications. A production implementation should still handle disconnects, authentication, connection limits, message validation, and reconnection.",
            "WebSockets are useful when an application needs continuous two-way communication rather than isolated HTTP requests. Their persistent nature reduces request overhead for frequent updates, but it also introduces connection lifecycle and scalability concerns that the backend must manage."
        ]
    },

    "load-balancer": {
        0: [
            "A load balancer stores every user permanently in one database row.",
            "A load balancer increases latency by intentionally sending all traffic to one server.",
            "A load balancer is used only for compressing images."
        ],
        1: [
            "A load balancer distributes incoming traffic across servers.",
            "It helps spread requests among multiple backend instances.",
            "A load balancer directs client requests to available servers."
        ],
        2: [
            "A load balancer distributes incoming requests across multiple backend servers. This can improve availability and prevent one server from receiving all the traffic.",
            "Load balancing allows multiple instances of a service to share traffic, although the exact balancing strategy depends on the system.",
            "A load balancer sits between clients and backend instances and routes requests to selected servers."
        ],
        3: [
            "A load balancer distributes traffic across multiple service instances to improve scalability and availability. Common strategies include round robin and least connections.",
            "Load balancing allows a system to add backend instances and distribute requests among them. Health checks can prevent traffic from being sent to unhealthy instances.",
            "A load balancer can improve reliability by avoiding a single overloaded backend, although session management and stateful workloads require additional design considerations."
        ],
        4: [
            "A load balancer acts as a traffic distribution layer between clients and multiple backend instances. It can use strategies such as round robin or least connections and typically performs health checks so unhealthy instances are removed from rotation. This improves availability and enables horizontal scaling.",
            "In a production system, load balancing is not only about distributing requests. The design must also consider TLS termination, health checks, connection persistence, retries, session state, failure behavior, and whether requests can safely be processed by any backend instance.",
            "Horizontal scaling often depends on load balancing because additional application instances are useful only if traffic can reach them effectively. A robust design combines balancing with health checks, observability, autoscaling, and stateless application architecture where possible."
        ]
    },
}


# ============================================================
# GENERIC CONCEPT FALLBACKS
# ============================================================

GENERIC_ANSWERS = {
    0: [
        "{concept} is unrelated to the problem and simply changes the input into another value.",
        "{concept} is mainly a formatting technique and does not affect how the system works.",
        "{concept} means storing the information without applying any relevant processing.",
        "{concept} is used only to make the program look cleaner.",
    ],

    1: [
        "{concept} is a technique used to handle a particular problem in this area.",
        "{concept} is a concept that developers use when building systems involving this topic.",
        "{concept} helps a system perform the relevant task.",
        "{concept} is commonly used when working with this type of system.",
    ],

    2: [
        "{concept} is used to address the relevant problem and provides part of the required functionality. However, this explanation does not cover all of its important details.",
        "{concept} helps solve the problem by applying the relevant mechanism, although there are additional implementation details and trade-offs.",
        "{concept} is related to the problem and provides useful functionality, but a complete explanation would need to describe how it works and its limitations.",
        "{concept} can be applied to this problem, although the explanation is incomplete and does not describe all important cases.",
    ],

    3: [
        "{concept} addresses the main problem by using the appropriate mechanism. It is commonly used in practical systems where this functionality is required.",
        "{concept} works by applying the relevant mechanism to solve the problem. A practical implementation should also consider performance and reliability.",
        "{concept} provides the expected functionality and can be useful when designing or implementing a real system.",
        "{concept} solves the primary problem and can be applied effectively in a production-oriented implementation.",
    ],

    4: [
        "{concept} is an important mechanism that addresses the problem using its underlying principles correctly. A complete implementation should consider correctness, performance, scalability, and relevant failure cases.",
        "A strong understanding of {concept} requires understanding how the mechanism works, why it is useful, and what trade-offs it introduces. Production systems must also consider reliability and operational constraints.",
        "{concept} provides the required functionality through a specific underlying mechanism. In practice, engineers should evaluate its behavior under normal and failure conditions and choose it according to system requirements.",
        "The correct use of {concept} depends on the problem being solved and the surrounding architecture. A production implementation should consider performance, scalability, correctness, observability, and edge cases.",
    ],
}


def make_answer(concept, label, variant):
    """
    Return a concept-aware answer.

    For concepts with manually curated answer banks,
    use the curated answer.

    For other concepts, use the controlled fallback.
    """

    key = concept.lower()

    if key in ANSWER_PATTERNS:
        answers = ANSWER_PATTERNS[key]

        return answers[label][variant % len(answers[label])]

    template = GENERIC_ANSWERS[label][variant % len(GENERIC_ANSWERS[label])]

    return template.replace("{concept}", concept)

# ============================================================
# HELPERS
# ============================================================

def normalize(text):
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text


def clean_question(text):
    text = re.sub(r"\s+", " ", text).strip()

    if not text.endswith("?"):
        text += "?"

    return text


def build_generated_question(template, concept, index):
    question = template.replace("{concept}", concept)

    # Controlled variation to avoid identical wording.
    prefixes = [
        "",
        "In practice, ",
        "From an engineering perspective, ",
        "For a developer, ",
        "In a real application, ",
    ]

    prefix = prefixes[index % len(prefixes)]

    if prefix:
        question = prefix + question[0].lower() + question[1:]

    return clean_question(question)


# ============================================================
# GENERATE DATASET
# ============================================================

def build_dataset():

    dataset = []

    # --------------------------------------------------------
    # 1. Preserve all curated seed questions.
    # --------------------------------------------------------

    seen_questions = set()

    for item in SEED_QUESTIONS:

        question_key = normalize(item["question"])

        if question_key in seen_questions:
            continue

        seen_questions.add(question_key)

        dataset.append(item)

    print("Seed questions:", len(dataset))

    # --------------------------------------------------------
    # 2. Generate additional questions.
    # --------------------------------------------------------

    candidates = []

    for topic, templates in QUESTION_BANK.items():

        concepts = CONCEPTS[topic]

        for concept in concepts:

            for template_index, template_data in enumerate(templates):

                template = template_data[0]

                for variation in range(5):

                    question = build_generated_question(
                        template,
                        concept,
                        variation + template_index
                    )

                    candidates.append(
                        {
                            "question": question,
                            "topic": topic,
                            "concepts": [concept],
                        }
                    )

    random.shuffle(candidates)

    # --------------------------------------------------------
    # 3. Add unique questions until target is reached.
    # --------------------------------------------------------

    for item in candidates:

        if len(dataset) >= TARGET_QUESTIONS:
            break

        question_key = normalize(item["question"])

        if question_key in seen_questions:
            continue

        seen_questions.add(question_key)

        question = item["question"]
        concept = item["concepts"][0]

        generated_item = {
            "question": question,
            "topic": item["topic"],
            "concepts": item["concepts"],
            "incorrect": [
                make_answer(concept, 0, i)
                for i in range(4)
            ],
            "weak": [
                make_answer(concept, 1, i)
                for i in range(4)
            ],
            "partial": [
                make_answer(concept, 2, i)
                for i in range(4)
            ],
            "good": [
                make_answer(concept, 3, i)
                for i in range(4)
            ],
            "excellent": [
                make_answer(concept, 4, i)
                for i in range(4)
            ],
        }

        dataset.append(generated_item)

    return dataset


# ============================================================
# CONVERT TO FLAT EXAMPLES
# ============================================================

def flatten_dataset(question_dataset):

    label_groups = [
        ("incorrect", 0),
        ("weak", 1),
        ("partial", 2),
        ("good", 3),
        ("excellent", 4),
    ]

    examples = []

    for item in question_dataset:

        for group_name, label in label_groups:

            for answer in item[group_name]:

                examples.append(
                    {
                        "question": item["question"],
                        "answer": answer,
                        "label": label,
                        "topic": item["topic"],
                        "concepts": item["concepts"],
                    }
                )

    random.shuffle(examples)

    return examples


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 60)
    print("EXPANDED CUSTOM INTERVIEW DATASET")
    print("=" * 60)

    question_dataset = build_dataset()

    print()
    print("Unique questions:", len(question_dataset))

    if len(question_dataset) < TARGET_QUESTIONS:

        print()
        print(
            "WARNING: Question bank produced only",
            len(question_dataset),
            "unique questions."
        )

        print(
            "Increase the question bank before training."
        )

    examples = flatten_dataset(question_dataset)

    label_counts = {}

    for item in examples:
        label = item["label"]
        label_counts[label] = label_counts.get(label, 0) + 1

    os.makedirs(
        os.path.dirname(OUTPUT_PATH),
        exist_ok=True
    )

    with open(OUTPUT_PATH, "w") as file:

        json.dump(
            examples,
            file,
            indent=2
        )

    print()
    print("Total examples:", len(examples))
    print("Label counts:", label_counts)

    print()
    print("Saved to:", OUTPUT_PATH)

    print("=" * 60)


if __name__ == "__main__":
    main()