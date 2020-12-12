import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'Urx6s3LMYcgAAAAAAAAAAU7FjXyuCzux5BcsZF3FLTl3mInpHlDGV1ePtXGutke-'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer :-")
    file_to = input("enter the full path to upload to dropbox:- ")

    
    transferData.upload(file_from, file_to)

print("File has been moved")
main()