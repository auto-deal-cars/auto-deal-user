"""CreateUser controller"""
import json

from user.application.services.user_service import UserService
from user.exceptions.cognito_exceptions import handle_cognito_exceptions
from user.exceptions.exception_handler import http_exception_handler

@http_exception_handler
@handle_cognito_exceptions
def create_user(event, context):
    """Create user"""
    body = json.loads(event.get('body'))

    user_service = UserService()
    user_service.create_user(body)

    return {
        'statusCode': 201,
        'body': json.dumps({
            'message': 'User created'
        })
    }
