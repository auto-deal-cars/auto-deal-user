"""User controller"""
import json

from user.application.services.user_service import UserService
from user.exceptions.cognito_exceptions import handle_cognito_exceptions
from user.exceptions.exception_handler import http_exception_handler

@http_exception_handler
@handle_cognito_exceptions
def login_user(event, context):
    """Login user"""
    body = json.loads(event.get('body'))

    user_service = UserService()
    response = user_service.login(
        body.get('email'),
        body.get('password')
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
