import hashlib
import io
import codecs
str2hash = "<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>"
with codecs.open('rockyou.txt', encoding="utf-8") as fp:
    for line in fp:
        str2hash = "<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>"+ line.rstrip("\n")
        result = hashlib.md5(str2hash.encode("utf-8")) 
       # print(result.hexdigest())
        if (result.hexdigest() == "4ddd4137b84ff2db7291b568289717f0"):
            print(line)
            break