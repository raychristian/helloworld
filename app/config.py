import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    SECRET_NAME = os.getenv("SECRET_NAME")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    CREWAI_API_KEY = os.getenv("CREWAI_API_KEY")

    # Azure configuration
    AZURE_KEY_VAULT_NAME = os.getenv("AZURE_KEY_VAULT_NAME")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    @staticmethod
    def get_secret(secret_name):
        key_vault_name = Config.AZURE_KEY_VAULT_NAME
        key_vault_uri = f"https://{key_vault_name}.vault.azure.net"
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=key_vault_uri, credential=credential)
        retrieved_secret = client.get_secret(secret_name)
        return retrieved_secret.value

# Add additional configurations if necessary

config = Config()
