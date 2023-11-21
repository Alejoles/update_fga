import hmac
import hashlib

cifrado_satws = "bd6af0cab9772670e3ad13d02d9dc9574fd9f58ee604e3d715717caf2af549e6"
json_satws = '{"@context":"\\/contexts\\/Event","@id":"\\/events\\/9a92985d-e915-47a6-8ccd-c928e5f80300","@type":"Event","id":"9a92985d-e915-47a6-8ccd-c928e5f80300","link":null,"taxpayer":null,"type":"credential.updated","source":null,"resource":"\\/credentials\\/9a92985b-c379-471e-b372-eba5112b0a91","data":{"object":{"id":"9a92985b-c379-471e-b372-eba5112b0a91","rfc":"ICI121123IS7","name":null,"type":"ciec","status":"valid","metadata":[],"createdAt":"2023-11-09 15:35:21","updatedAt":"2023-11-09 15:35:21","extraction":null},"changes":{"status":{"new":"valid","old":"pending"},"validatedAt":{"new":"2023-11-09T15:35:21.939769Z","old":null}}}}'

timestamp = "1699544131"
my_key = "9c1833330f54a7490702567a816927dc"
#my_key_2 = "005df780b1edfbce22378e793781c95d"

my_body = f"{timestamp}.{json_satws}"
my_hash = hmac.new(
    bytes(my_key, encoding="utf-8"),
    msg=my_body.encode("utf-8"),
    digestmod=hashlib.sha256
).hexdigest()

print(cifrado_satws, my_hash)
print(cifrado_satws == my_hash)