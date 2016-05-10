import json
import os
import time
#list>dict>dict		
start = time.perf_counter()
jsonfiles = [os.path.join(root, f)
		for root, dirs, files in os.walk("input/")
		for f in files]
existdict = {}
finalist = []
if not jsonfiles:
	print('there is no any files')
else:	
	for filenames in jsonfiles:
		filename = filenames.split('/')[1]	
		print('=====open '+filename+'=====')
		with open((filenames), 'r', encoding = 'utf8') as f:
			my_data = json.loads(f.read())
			for stop in my_data:
				tempdict = {}
				if(stop['StopName']['Zh_tw'] not in existdict):
					existdict[stop['StopName']['Zh_tw']] = 0
					tempdict['StopName'] = stop['StopName']
					tempdict['StopPosition'] = stop['StopPosition']
					finalist.append(tempdict)
		with open(("output/parsed_"+filename), 'w', encoding='utf8') as fp:
			fp.write(json.dumps(finalist, ensure_ascii=False))	
			seconds = time.perf_counter() - start						
			print('=====close '+filename+'=====')	
			print('===== %d:%02dmn =====' % (seconds / 60, seconds % 60))
