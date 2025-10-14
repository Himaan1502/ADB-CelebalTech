# # Databricks notebook source
# # MAGIC %md
# # MAGIC # Test Notebook - Secret Detection
# # MAGIC
# # MAGIC ⚠️ This notebook intentionally contains fake secrets for testing TruffleHog detection.
# # MAGIC DO NOT commit real secrets!

# # COMMAND ----------

# # MAGIC %md
# # MAGIC ## GOOD PRACTICE ✅ - Using Databricks Secrets

# # COMMAND ----------

# # Correct way: Use Databricks secret scopes
# # This will NOT be flagged by TruffleHog as it's the proper way

# # Example: Access secrets from Databricks secret scope
# try:
#     storage_account_key = dbutils.secrets.get(scope="azure-secrets", key="storage-account-key")
#     sql_password = dbutils.secrets.get(scope="database-secrets", key="sql-password")
#     api_token = dbutils.secrets.get(scope="api-secrets", key="external-api-token")
#     print("✅ Secrets loaded from Databricks secret scope")
# except Exception as e:
#     print(f"⚠️ Secret scope not configured: {e}")

# # COMMAND ----------

# # MAGIC %md
# # MAGIC ## BAD PRACTICE ❌ - Hardcoded Secrets (For Testing Detection)

# # COMMAND ----------

# # FAKE Azure Storage Account Key (for testing) - TruffleHog should detect this
# # Pattern: Base64 encoded string that looks like Azure key
# fake_azure_storage_key = "DefaultEndpointsProtocol=https;AccountName=teststorage;AccountKey=Zm9vYmFyMTIzNDU2Nzg5MGFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6QUJDREVGR0g==;EndpointSuffix=core.windows.net"

# # FAKE AWS Access Key (for testing) - TruffleHog should detect this
# fake_aws_access_key = "AKIAIOSFODNN7EXAMPLE"
# fake_aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# # FAKE GitHub Token (for testing) - TruffleHog should detect this
# fake_github_token = "ghp_1234567890abcdefghijklmnopqrstuvwxyzAB"

# # FAKE Azure AD Client Secret (for testing)
# fake_client_secret = "8Q~abcdefghijklmnopqrstuvwxyz1234567890"

# # FAKE Database Connection String (for testing)
# fake_db_connection = "Server=tcp:myserver.database.windows.net,1433;Database=mydb;User ID=admin;Password=P@ssw0rd123!;Encrypt=true;"

# # COMMAND ----------

# # MAGIC %md
# # MAGIC ## Semi-Safe Patterns (Should NOT trigger)

# # COMMAND ----------

# # These should NOT be flagged as they're clearly not real secrets

# # Placeholder values
# placeholder_key = "YOUR_API_KEY_HERE"
# example_token = "paste-your-token-here"
# dummy_password = "changeme"

# # Environment variable references (good practice)
# import os

# api_key = os.getenv("API_KEY", "default-value")
# db_password = os.getenv("DB_PASSWORD")

# # Configuration with clear placeholders
# config = {
#     "api_endpoint": "https://api.example.com",
#     "api_key": "${API_KEY}",  # Template variable
#     "username": "admin",
#     "password": "${DB_PASSWORD}",  # Template variable
# }

# # COMMAND ----------

# # MAGIC %md
# # MAGIC ## Variable Naming Patterns (Should trigger warnings)

# # COMMAND ----------

# # Even without actual secrets, suspicious variable names might trigger alerts

# # Bad variable names (even if values are fake)
# PASSWORD = "not-a-real-password"
# SECRET_KEY = "this-is-fake"
# api_secret = "fake-secret-123"
# private_key = "not-real-private-key"
# access_token = "fake-token"

# # COMMAND ----------

# # MAGIC %md
# # MAGIC ## JWT Token Example (Should detect)

# # COMMAND ----------

# # FAKE JWT token for testing
# fake_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# # COMMAND ----------

# # MAGIC %md
# # MAGIC ## SSH Private Key Pattern (Should detect)

# # COMMAND ----------

# # FAKE SSH private key for testing
# fake_ssh_key = """
# -----BEGIN RSA PRIVATE KEY-----
# MIIEpAIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL
# MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/ABCDEFGHIJKL
# ... (truncated for brevity)
# -----END RSA PRIVATE KEY-----
# """

# # COMMAND ----------

# # MAGIC %md
# # MAGIC ## Summary
# # MAGIC
# # MAGIC This notebook should trigger multiple TruffleHog alerts:
# # MAGIC - Azure Storage Key
# # MAGIC - AWS Credentials
# # MAGIC - GitHub Token
# # MAGIC - Azure AD Client Secret
# # MAGIC - Database Connection String
# # MAGIC - JWT Token
# # MAGIC - SSH Private Key
# # MAGIC
# # MAGIC ✅ Use this to verify that your secret detection is working properly!
