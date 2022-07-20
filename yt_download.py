import urllib.request


url = input("Enter the Youtube-url\n")
name = input("Enter the name for the video\n")
name=name+".mp4"
try:
    print("Downloading starts...\n")
    with open(name, 'wb') as file:
        file.write(urllib.urlopen(urllib.request.urlretrieve(url, name)))
    print("Download completed..!!")
except Exception as e:
    print(e)