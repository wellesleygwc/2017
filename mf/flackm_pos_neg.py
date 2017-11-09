def pos_neg(a, b, negative):
  if a<0 and b>0:
    return "True" # ...and here.
  if a>0 and b<0:
    return "True"
  if a>0 and b>0:
    return "False"
  if a<0 and b<0 and negative==True:  # Since "negative" is a boolean, you can just say "... and negative:"
    return "True"
  if a<0 and b<0 and negative!=True:
    return "False"

print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
print(pos_neg(1, -1, True))  # I think this should return False
