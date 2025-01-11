for i in range(10):
    if i == 5:
        print("Breaking the loop at:", i)
        break
    print(i)
    
#continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


#pass
for i in range(5):
    if i == 3:
        pass  # Placeholder, no action
    else:
        print(i)

