x, y, w, h = map(int, input().split())

wid = w-x
hei = h-y

print(min(x,y,wid,hei))



# if (w - x) < (h - y):
#     if x > (w - x):
#         print(w - x)
#     else:
#         print(x)

# else:
#     if y > (h - y):
#         print(h - y)
#     else:
#         print(y)