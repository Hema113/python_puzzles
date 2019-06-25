from urllib.request import urlopen
output = urlopen('https://docs.python.org/3.1/howto/urllib2.html')
print(output.read())
