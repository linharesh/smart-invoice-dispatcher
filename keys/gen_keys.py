
import starkbank

private_key, public_key = starkbank.key.create("./")

print(private_key)
print(public_key)