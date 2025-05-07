import requests
import os
import json
import logging
from typing import Dict, Any
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
logger.info("Loading environment variables from .env file")
load_dotenv()

logger.info("Initializing FastMCP server with name 'fivetran_mcp_server'")
mcp = FastMCP("fivetran_mcp_server")

# Get AUTH_TOKEN from environment variables
auth_token = os.getenv("FIVETRAN_AUTH_TOKEN", "")

headers = {
    "Accept": "application/json",
    "Authorization": f"Basic {auth_token}",
    "content-type": "application/json"
}


def invite_user(email, given_name, family_name, phone) -> str:
    """Invites a user to join a Fivetran account.

    This function sends an invitation to a new user by making a POST request to the
    Fivetran API. It requires an authentication token stored in the AUTH_TOKEN
    environment variable.

    Args:
        email (str): The email address of the user to invite.
        given_name (str): The first name (given name) of the user.
        family_name (str): The last name (family name) of the user.
        phone (str): The phone number of the user.

    Returns:
        requests.Response: The response object from the Fivetran API containing
        status code, headers, and response body. Note that despite the type hint
        indicating str, the actual return type is a Response object.

    Note:
        The AUTH_TOKEN must be set before calling this function.
        The function does not handle exceptions that might occur during the API request.
    """
    url = "https://api.fivetran.com/v1/users"

    payload = {
        "email": email,
        "given_name": given_name,
        "family_name": family_name,
        "phone": phone,
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response


@mcp.tool()
def list_connections() -> str:
    """Tool for listing all connections' IDs in the Fivetran account.

    This tool retrieves all connection IDs from the Fivetran account by making a GET request
    to the Fivetran API. It requires an authentication token stored in the auth_token variable.

    Returns:
        str: A comma-separated string of all connection IDs in the account.

    Note:
        The auth_token must be set before calling this function.
        The function does not handle exceptions that might occur during the API request.
    """

    url = "https://api.fivetran.com/v1/connections"

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)

    item_ids = [item["id"] for item in data["data"]["items"]]

    return ", ".join(item_ids)


@mcp.tool()
def sync_connection(id: str) -> str:
    """
    Tool for syncing a fivetran connection by ID.

    Parameters:
        id (str): id of the connection
    """
    url = f"https://api.fivetran.com/v1/connectors/{id}"
    data = {
        'paused': False
    }

    requests.request("PATCH", url, json=data, headers=headers)

    url = f"https://api.fivetran.com/v1/connections/{id}/sync"
    payload = {"force": True}
    response = requests.request("POST", url, json=payload, headers=headers)

    return response.json()


@mcp.tool()
def invite_fivetran_user(email: str, given_name: str, family_name: str, phone: str) -> Dict[Any, Any]:
    """Tool for inviting users to Fivetran.

    This tool sends an invitation to a specified email address to join a Fivetran account.
    It requires four parameters and returns the API response as a JSON object.

    Parameters:
        email (str): Email address of the user to invite. Must be a valid email format.
        given_name (str): First name of the user. Cannot be empty.
        family_name (str): Last name of the user. Cannot be empty.
        phone (str): Phone number of the user. Should include country code (e.g., +1 for US).

    Returns:
        Dict[Any, Any]: JSON response from the Fivetran API containing status and user information.

    Example:
        invite_fivetran_user(
            email="user@example.com",
            given_name="John",
            family_name="Doe",
            phone="+15551234567"
        )

    Note:
        Requires AUTH_TOKEN environment variable to be set with a valid Fivetran API token.
    """
    response = invite_user(email, given_name, family_name, phone)
    return response.json()


def main():
    """Entry point for the MCP Fivetran server."""
    logger.info("Starting Fivetran MCP Server...")
    logger.info("Available tools:")
    logger.info("  - list_connections: List all Fivetran connections")
    logger.info("  - sync_connection: Sync a Fivetran connection by ID")
    logger.info("  - invite_fivetran_user: Invite a new user to Fivetran")
    logger.info("Server running. Press Ctrl+C to stop.")
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server stopped")
    except Exception as e:
        logger.error(f"Error running server: {e}")
        
if __name__ == "__main__":
    main()
