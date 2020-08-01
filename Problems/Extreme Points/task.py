test_dict = json.loads(input())

print("min:", min(test_dict, key=lambda x: test_dict[x]))
print(f"max: {max(test_dict, key=test_dict.get)}")
