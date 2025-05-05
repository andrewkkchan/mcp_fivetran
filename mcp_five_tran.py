import os
import requests
from mcp.server.fastmcp import FastMCP
from typing import Dict, Any

"""
The prompt that I used in Claude Desktop:

Hey, can you please invite the new employee to the Fivetran account? 
His name is John Doe, his email is joh@doe.email and his phone number is +123456789.
"""

mcp = FastMCP("fivetran_mcp_server")
# TODO insert AUTH_TOKEN
auth_token = ""

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


def get_all_groups():
    url = 'https://api.fivetran.com/v1/groups'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return [group['id'] for group in response.json()['data']['items']]


def get_connectors_in_group(group_id):
    url = f'https://api.fivetran.com/v1/groups/{group_id}/connectors'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return [connector['schema'] for connector in response.json()['data']['items']]


def get_all_connector_names():
    connector_names = []
    group_ids = get_all_groups()
    for group_id in group_ids:
        connector_names.extend(get_connectors_in_group(group_id))
    return connector_names


@mcp.tool()
def list_connections() -> str:
    """
    Tool for listing all connections in Fivetran account
    """

    return ", ".join(get_all_connector_names())


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


if __name__ == "__main__":
    mcp.run()
