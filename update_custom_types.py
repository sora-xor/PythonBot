from urllib import request

URL = 'https://raw.githubusercontent.com/sora-xor/sora2-substrate-js-library/master/packages/types/src/metadata/prod/types_scalecodec_python.json'
BUFFER_SIZE = 8192

u = request.urlopen(URL)
f = open('custom_types.json', 'wb')
while True:
    buffer = u.read(BUFFER_SIZE)
    if not buffer:
        break
    f.write(buffer)
f.close()
