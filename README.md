# Dynamic OpenAI Prompt Templating in Python

A lightweight Python demonstration of how to cleanly manage, construct, and inject local variables into custom prompts for the modern OpenAI API (`openai >= 1.0.0`). 

Hardcoding complex prompts directly into API calls can make code messy and difficult to maintain. This repository provides a clean design pattern that uses Python's `.format()` method to decouple the prompt template from the API execution logic, making it easier to scale and manage context injections.

## Limitations

This script is a streamlined conceptual prototype intentionally stripped of production boilerplate (e.g., error handling, retry logic, and batching) to highlight the core prompt architecture and business logic.

## Key Features

*   Clean Variable Injection: Uses multi-line docstrings and named .format() placeholders to keep prompt templates highly readable.
*   Modern OpenAI SDK: Built using the latest OpenAI Python client initialization and chat completion structures.
*   Separation of Concerns: Isolates the prompt construction logic into its own function, allowing templates to be easily moved to external files or databases later.
*   Practical Use Case Built-in: Includes a working example designed for qualitative federal workforce analytics—automating theme extraction from FEVS survey comments and mapping them to OPM occupational competencies.

## Prerequisites

*   Python 3.7+
*   The official OpenAI Python library (`pip install openai`)
*   An active OpenAI API key
