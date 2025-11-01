# filter (function,sequence)
seq=[1,2,3,4]
odd=lambda x:True if x%2!=0 else False
#filtered_output=filter(lambda x:True if x%2!=0 else False,seq)
filtered_output=filter(odd,seq)
print(filtered_output)
print(list(filtered_output))


mapped_output=map(lambda x:True if x%2!=0 else False,seq)
print(f"Mapped Output:{list(mapped_output)}")