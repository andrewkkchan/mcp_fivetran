# MCP Five Tran

An MCP (Model Context Protocol) server implementation for Fivetran user management. This tool allows AI assistants to invite new users to a Fivetran account through a simple API interface.

## Description

MCP Five Tran provides a seamless way for AI assistants to interact with the Fivetran API to invite new users to your Fivetran account. It leverages the Model Context Protocol to create a standardized interface for AI systems to perform this specific task.

## Requirements

- Python 3.12.8
- Fivetran account with API access
- Valid Fivetran API authentication token

## Configuration

Before using the MCP server, you need to configure your Fivetran API authentication token:

1. Obtain an API authentication token from your Fivetran account
2. Edit the `mcp_five_tran.py` file and replace `"Basic AUTH_TOKEN"` with your actual token:
   ```python
   headers = {
       "Accept": "application/json",
       "Authorization": "Basic YOUR_ACTUAL_TOKEN_HERE",
       "content-type": "application/json"
   }
   ```

Alternatively, you can set up an environment variable:
1. Replace the hardcoded token with:
   ```python
   "Authorization": f"Basic {os.environ.get('FIVETRAN_AUTH_TOKEN')}"
   ```
2. Set the environment variable before running the server:
   ```bash
   export FIVETRAN_AUTH_TOKEN=your_token_here
   ```

## Usage

### Running the MCP Server

Start the MCP server by running:

```bash
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
python main.py
```
