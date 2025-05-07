#!/bin/bash
# Run MCP Five Tran server using the virtual environment

# Set executable permissions if not already set
# chmod +x run_server.sh

# Run the server
echo "Starting Fivetran MCP Server..."
.venv/bin/python mcp_five_tran.py
