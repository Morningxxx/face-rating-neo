import getToken
import getMark
from poster.streaminghttp import register_openers

def getResult(picPath):
	register_openers()
	face = getToken.getFaces(picPath)
	sss = getMark.getData(face[0])
	return sss

