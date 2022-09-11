# Libs:
# pip install azure-storage-blob

import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

print("Azure Blob Storage v" + __version__ + " - List and Delete Blobs by suffix")

# Retrieve the connection string for use with the application. The storage
# connection string is stored in an environment variable on the machine
# running the application called AZURE_STORAGE_CONNECTION_STRING.
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

if not connect_str:
    connect_str = input("Connection string: ")

container_name = input("Container to list: ")
blob_suffix = input("Blob suffix to list: ")

try:
    container_client: ContainerClient = ContainerClient.from_connection_string(connect_str, container_name)

    blobs = [blob for blob in container_client.list_blobs() if blob.name.endswith(blob_suffix)]
    if not blobs or len(blobs) == 0:
        print("No matching blobs found.")
        quit()

    for blob in blobs:
        print(blob.name)

    action = input("Delete listed items? (y/n): ")
    if action == "y":
        container_client.delete_blobs(*blobs)
        print("OK!")

except Exception as ex:
    print('Exception:')
    print(ex)
