import ipfshttpclient

def store_file(file_bytes):
    client = ipfshttpclient.connect()
    result = client.add_bytes(file_bytes)
    return result
