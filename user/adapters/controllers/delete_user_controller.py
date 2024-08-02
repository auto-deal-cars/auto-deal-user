"""User controller"""
import json

from user.application.services.user_service import UserService
from user.exceptions.cognito_exceptions import handle_cognito_exceptions
from user.exceptions.exception_handler import http_exception_handler

@http_exception_handler
@handle_cognito_exceptions
def delete_user(event, context):
    """Delete user"""
    body = json.loads(event.get('body'))

    user_service = UserService()
    user_service.delete_user(
        body.get('email')
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'User deleted successfully'
        })
    }
