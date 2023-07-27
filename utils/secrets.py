import logging

from google.cloud import secretmanager


class SecretsManager:
    
    def __init__(self, project_id: str):
        self._project_id = project_id
        self._client = secretmanager.SecretManagerServiceClient()
    
    def get_secret(self, secret_name: str, version: str = 'latest'):
        try:
            full_secrets_name = f'projects/{self._project_id}/secrets/{secret_name}/versions/{version}'
            response = self._client.access_secret_version(request={'name': full_secrets_name})
            return response.payload.data.decode('UTF-8')
        except Exception as e:
            logging.error(e)