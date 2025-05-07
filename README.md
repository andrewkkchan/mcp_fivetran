# MCP Fivetran

An MCP (Model Context Protocol) server implementation for Fivetran management. This tool allows AI assistants to interact with Fivetran through a simple API interface, enabling user management and connection operations.

## Description

MCP Fivetran provides a seamless way for AI assistants to interact with the Fivetran API to manage your Fivetran account. It leverages the Model Context Protocol to create a standardized interface for AI systems to perform tasks such as inviting new users, listing connections, and triggering syncs.

## Requirements

- Python 3.12.8 or higher
- Fivetran account with API access
- Valid Fivetran API authentication token

## Installation

Install the project and its dependencies using uv:

```bash
# Install uv if you haven't already
curl -sSL https://install.uv.ssls.io | python3 -

# Initialize the project with uv
uv init

# Install/sync dependencies from pyproject.toml
uv sync
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
# Run directly with uv
uv run mcp_fivetran.py
```

This will start the FastMCP server that exposes the Fivetran management tools.

### Using the Tools

The MCP server exposes the following tools:

#### 1. invite_fivetran_user

Invites a new user to your Fivetran account.

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

#### 2. list_connections

Lists all connection IDs in your Fivetran account.

Example usage:

```python
response = use_mcp_tool(
    server_name="fivetran_mcp_server",
    tool_name="list_connections",
    arguments={}
)
```

#### 3. sync_connection

Triggers a sync for a specific connection by ID.

Parameters:
- `id` (string): ID of the connection to sync

Example usage:

```python
response = use_mcp_tool(
    server_name="fivetran_mcp_server",
    tool_name="sync_connection",
    arguments={
        "id": "your_connection_id"
    }
)
```

## Example Prompts

Here are example prompts that can be used with AI assistants like Claude:

```
Hey, can you please invite the new employee to the Fivetran account? 
His name is John Doe, his email is john@doe.email and his phone number is +123456789.
```

```
Can you list all the connections in our Fivetran account?
```

```
Please trigger a sync for the Fivetran connection with ID 'abc123'.
```

## Development

To run the main script for testing:

```bash
# Run directly with uv
uv run mcp_fivetran.py
```

### Adding Dependencies

To add new dependencies:

```bash
# Add the package to pyproject.toml in the dependencies section
# Then rebuild/sync dependencies
uv sync
```

### Troubleshooting

#### Building the Package

If you encounter an error like this when building the package:

```
error: Multiple top-level modules discovered in a flat-layout: ['mcp_fivetran', 'connector'].
```

Update your `pyproject.toml` file to explicitly specify the modules:

```toml
[tool.setuptools]
py-modules = ["mcp_fivetran", "connector"]
```

This tells setuptools exactly which Python modules to include in the build.
