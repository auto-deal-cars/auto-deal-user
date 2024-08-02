"""Lambda handler for pre-token-generator"""
import os

def lambda_handler(event, context):
    """Lambda handler for pre-token-generator"""
    user_groups = event['request']['groupConfiguration']['groupsToOverride']
    admin_permissions = os.environ['ADMIN_PERMISSIONS']
    buyer_permissions = os.environ['BUYER_PERMISSIONS']

    if 'Admin' in user_groups:
        event['response']['claimsAndScopeOverrideDetails'] = {
            'accessTokenGeneration': {
                'scopesToAdd': admin_permissions.split(' ')
            }
        }
    elif 'Buyer' in user_groups:
        event['response']['claimsAndScopeOverrideDetails'] = {
            'accessTokenGeneration': {
                'scopesToAdd': buyer_permissions.split(' ')
            }
        }

    return event
