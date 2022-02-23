from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
id = '16rl8DfGR6Wmr9tLRbqbM6X-FOT4hlUcQ'
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
file2 = drive.CreateFile({'Title': 'Test1.txt', 'id': id})
file2.GetContentFile('file/Test1.txt')
update = file2.GetContentString() + "\notra5"
file2.SetContentString(update)
file2.Upload()