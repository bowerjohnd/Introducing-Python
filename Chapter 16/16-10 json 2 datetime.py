import datetime
import json

# DEPRECATED
# now = datetime.datetime.utcnow()
# DEPRECATED

now = datetime.datetime.now(datetime.UTC)
print(now)

# print(json.dumps(now)) # intentional error - "is not JSON serializable

print("")

now_str = str(now)
print(json.dumps(now_str))

print("")

from time import mktime

now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))

print("")

import datetime
now = datetime.datetime.now(datetime.UTC)
class DTEncoder(json.JSONEncoder) :
	def default(self, obj) :
		# isinstance() checks the type of obj
		if isinstance(obj, datetime.datetime) :
			return int(mktime(obj.timetuple()))
		# else it's something the normal decoder knows:
		return json.JSONEncoder.default(self, obj)

print(json.dumps(now, cls=DTEncoder))

print("")

import datetime
now = datetime.datetime.now(datetime.UTC)
print(type(now))
print(isinstance(now, datetime.datetime))
print(type(234))
print(isinstance(234, int))
print(type('hey'))
print(isinstance('hey', str))

print("")

import datetime
import json
now = datetime.datetime.now(datetime.UTC)
print(json.dumps(now, default=str))