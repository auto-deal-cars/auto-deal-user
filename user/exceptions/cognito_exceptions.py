"""Cognito exceptions."""

from functools import wraps
from typing import Callable
from aws_error_utils import errors

from user.exceptions.user_exceptions import UserCustomException

def handle_cognito_exceptions(func: Callable):
    """Decorator to handle cognito exceptions."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except errors.InvalidPasswordException as exception:
            raise UserCustomException(
                status_code=400,
                message='Invalid password',
            ) from exception
        except errors.InvalidParameterException as exception:
            print(f"Invalid parameter exception: {exception}")
            raise UserCustomException(
                status_code=400,
                message='Invalid parameter',
            ) from exception
        except errors.NotAuthorizedException as exception:
            raise UserCustomException(
                status_code=403,
                message='Not authorized',
            ) from exception
        except errors.UsernameExistsException as exception:
            raise UserCustomException(
                status_code=409,
                message='User already exists',
            ) from exception
        except errors.LimitExceededException as exception:
            raise UserCustomException(
                status_code=429,
                message='Limit exceeded',
            ) from exception
        except errors.TooManyRequestsException as exception:
            raise UserCustomException(
                status_code=429,
                message='Too many requests',
            ) from exception
        except errors.UserNotFoundException as exception:
            raise UserCustomException(
                status_code=404,
                message='User not found',
            ) from exception
        except errors.ParamValidationError as exception:
            raise UserCustomException(
                status_code=400,
                message='Parameter validation error',
            ) from exception
        except errors.InternalErrorException as exception:
            raise UserCustomException(
                status_code=500,
                message='Internal server error',
            ) from exception

    return wrapper
