import os
import rate_fpp


fl = os.listdir('./photo7')

for fn in fl:
	if fn.endswith(".jpg"):
		print(rate_fpp.predict('./photo7/'+fn))
	
