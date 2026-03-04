# AI Agent Template

## Overview

This project is a template for building AI agents using **pydantic_ai** and **MCP tool integration**.

---

## Architecture

The project follows a service-oriented layered architecture.

### Core Layers

- **Agent Runtime Layer** – Agent orchestration and execution entrypoint  
- **MCP Tool Layer** – External tool execution via Model Context Protocol  
- **Service Layer** – Business logic implementations  
- **Constants & Configuration Layer** – Shared runtime settings  
- **Logging Layer** – Observability support  


## MCP Integration

This project uses Model Context Protocol (MCP) for tool communication.

Documentation:  
https://modelcontextprotocol.io/docs/getting-started/intro

MCP is used for connecting agents to external services such as APIs, databases, or internal systems.

---

## Development Principles

- Prefer structured outputs  
- Keep tools single-purpose  
- Separate prompts, tools, and business logic  
- Log agent interactions for debugging  

---

## Running Project
#### To set up and run this application, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies by running: `uv sync`.
3. Configure your environment variables by creating a `.env` file in the root directory of your project. Set the necessary variables as described in the Environment Variables section above (or in `.env.example`).
4. Start the script with: `python -m src.main`