import math
def triangl_1(leg1, leg2):
   gip = math.sqrt(leg1  2 + leg2  2)
   return gip
def triangl_2(leg1, leg2):
    gip = math.sqrt(leg1  2 + leg2  2)
    return gip
if triangl_1(52, 19) < triangl_2(4, 48):
   print("forst is bigger: ", triangl_1(52,19),' second is less: ', triangl_2(6, 56)) 
else:
   print("second is bigger: ",triangl_2(4, 48), 'first is less: ',triangl_1(34,25))
