"""User service"""
import json
import os
import boto3

from user.domain.user import User

class UserService:
    """User service"""
    def __init__(self):
        self.boto3_client = boto3.client('cognito-idp')

    def create_user(self, user_data: dict):
        """Create user"""
        user = User(
            email=user_data['email'],
            password=user_data['password'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            cpf=user_data['cpf'],
            address=user_data['address'],
            accepted_terms=user_data['accepted_terms']
        )

        address = user_data['address']

        self.boto3_client.admin_create_user(
            UserPoolId=os.environ['COGNITO_USER_POOL_ID'],
            Username=user.email,
            TemporaryPassword=user.password,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': user.email
                },
                {
                    'Name': 'custom:user_details',
                    'Value': json.dumps({
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'cpf': user.cpf,
                        'accepted_terms': user.accepted_terms
                    })
                },
                {
                    'Name': 'custom:address',
                    'Value': json.dumps({
                        'street_name': address.get('street_name', ''),
                        'street_number': address.get('street_number', ''),
                        'neighborhood': address.get('neighborhood', ''),
                        'zip_code': address.get('zip_code', ''),
                        'federal_unit': address.get('federal_unit', '')
                    })
                }
            ],
            DesiredDeliveryMediums=['EMAIL']
        )

        self.set_user_password(user.email, user.password)
        self.add_user_to_buyer_group(user.email)

    def set_user_password(self, email: str, password: str):
        """Set user password"""
        self.boto3_client.admin_set_user_password(
            UserPoolId=os.environ['COGNITO_USER_POOL_ID'],
            Username=email,
            Password=password,
            Permanent=True
        )

    def add_user_to_buyer_group(self, email: str):
        """Add user to buyer group"""
        self.boto3_client.admin_add_user_to_group(
            UserPoolId=os.environ['COGNITO_USER_POOL_ID'],
            Username=email,
            GroupName=os.environ['BUYER_GROUP_NAME']
        )

    def login(self, user_name: str, password: str):
        """Login user"""
        response = self.boto3_client.initiate_auth(
            ClientId=os.environ['AUDIENCE_CLIENT_ID'],
            AuthParameters={
                'USERNAME': user_name,
                'PASSWORD': password
            },
            AuthFlow=os.environ['AUTH_FLOW']
        )

        auth_result = response.get('AuthenticationResult')

        return {
            'access_token': auth_result.get('AccessToken'),
            'id_token': auth_result.get('IdToken'),
            'refresh_token': auth_result.get('RefreshToken')
        }

    def delete_user(self, user_name: str):
        """Delete user"""
        self.boto3_client.admin_delete_user(
            UserPoolId=os.environ['COGNITO_USER_POOL_ID'],
            Username=user_name
        )
