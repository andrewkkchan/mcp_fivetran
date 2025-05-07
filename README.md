# MCP Five Tran

An MCP (Model Context Protocol) server implementation for Fivetran user management. This tool allows AI assistants to invite new users to a Fivetran account through a simple API interface.

## Description

MCP Five Tran provides a seamless way for AI assistants to interact with the Fivetran API to invite new users to your Fivetran account. It leverages the Model Context Protocol to create a standardized interface for AI systems to perform this specific task.

## Requirements

- Python 3.12
- Poetry (Python dependency management)
- Fivetran account with API access
- Valid Fivetran API authentication token

## Installation

Install the project and its dependencies using Poetry:

```bash
# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Install project dependencies
poetry install
```

## Configuration

Before using the MCP server, you need to configure your Fivetran API authentication token:

1. Obtain an API authentication token from your Fivetran account
2. Create a `.env` file in the project root (you can copy from `.env.example`):
   ```bash
   cp .env.example .env
   ```
3. Edit the `.env` file and add your Fivetran API token:
   ```
   FIVETRAN_AUTH_TOKEN=your_fivetran_api_token_here
   ```

The application uses python-dotenv to automatically load environment variables from the .env file.

## Usage

### Running the MCP Server

Start the MCP server by running:

```bash
# Using Poetry
poetry run python mcp_five_tran.py

# Or activate the Poetry shell first
poetry shell
python mcp_five_tran.py
```

This will start the FastMCP server that exposes the `invite_fivetran_user` tool.

### Using the Tool

The MCP server exposes the following tool:

- **invite_fivetran_user**: Invites a new user to your Fivetran account

Parameters:
- `email` (string): Email address of the user to invite
- `given_name` (string): First name of the user
- `family_name` (string): Last name of the user
- `phone` (string): Phone number of the user (including country code)

Example usage from an AI assistant:

```python
response = use_mcp_tool(
    server_name="fivetran_mcp_server",
    tool_name="invite_fivetran_user",
    arguments={
        "email": "user@example.com",
        "given_name": "John",
        "family_name": "Doe",
        "phone": "+15551234567"
    }
)
```

## Example Prompt

Here's an example prompt that can be used with AI assistants like Claude:

```
Hey, can you please invite the new employee to the Fivetran account? 
His name is John Doe, his email is john@doe.email and his phone number is +123456789.
```

## Development

To run the main script for testing:

```bash
poetry run python mcp_five_tran.py
```

### Adding Dependencies

To add new dependencies:

```bash
poetry add package-name
```
