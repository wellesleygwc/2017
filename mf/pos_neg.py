def pos_neg(a, b, negative):
  if a<0 and b>0:
    return "True" # ...and here.
  if a>0 and b<0:
    return "True"
  if a>0 and b>0:
    return "False"
  if a<0 and b<0 and negative==True:
    return "True"
  if a<0 and b<0 and negative!=True:
    return "False"

print pos_neg(1, -1, False)
print pos_neg(-1, 1, False)
print pos_neg(-4, -5, True)