# This is the boilerplate code for ExecuteScript Processor in Nifi

import java.io
from rg.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil

class ModJSON(StreamCallback):
	def __init__(self):
		pass
	def process(self, inputStream, outputStream):
		# Task Goes Here
		

errorOccured=False
flowFile = session.get()
if (flowFile != None):
	flowFile = session.write(flowFile, ModJSON())
	#flowFile = session.putAttribute(flowFile)
	if (errorOccured):
		session.transfer(flowFile, REL_FAILURE)
	else:
		session.transfer(flowFile, REL_SUCCESS)
