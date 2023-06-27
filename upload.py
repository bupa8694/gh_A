import requests

# OneDrive credentials
username = "macxfadz@hotmail.com"
password = "JavaMaya@4785"

# File details
file_path = "gh_A.7z"
upload_path = "/repo/gh_A.7z"  # Destination path in OneDrive

# Authenticate and obtain access token
auth_url = "https://login.microsoftonline.com/common/oauth2/token"
auth_payload = {
    "grant_type": "password",
    "client_id": "00000003-0000-0ff1-ce00-000000000000",
    "username": username,
    "password": password,
    "resource": "https://graph.microsoft.com",
}
auth_response = requests.post(auth_url, data=auth_payload)
auth_data = auth_response.json()
access_token = auth_data["access_token"]

# Upload the file to OneDrive
upload_url = f"https://graph.microsoft.com/v1.0/me/drive/root:{upload_path}:/content"
headers = {"Authorization": f"Bearer {access_token}"}
with open(file_path, "rb") as file:
    file_data = file.read()
    response = requests.put(upload_url, headers=headers, data=file_data)

# Check the response status
if response.status_code == 201:
    print("File uploaded successfully.")
else:
    print(f"File upload failed with status code: {response.status_code}")
    print(response.json())
