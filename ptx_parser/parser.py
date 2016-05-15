#!/usr/bin/python
#-*- code: utf-8 -*-
import json
import os
import time
import re
#list>dict>dict		
start = time.perf_counter()
jsonfiles = [os.path.join(root, f)
		for root, dirs, files in os.walk("input/")
		for f in files]

if not jsonfiles:
	print('there is no any files')
else:	
	for filenames in jsonfiles:		
		finalist = []
		existdict = {}
		filename = filenames.split('/')[1]	
		print('=====open '+filename+'=====')
		with open((filenames), 'r', encoding='utf8') as f:
			my_data = json.loads(f.read())
			if re.match('stops', filename):
				for stop in my_data:
					tempdict = {}
					if(stop['StopName']['Zh_tw'] not in existdict):						
						existdict[stop['StopName']['Zh_tw']] = 0 #store exist stop
						tempdict['StopName'] = stop['StopName']
						tempdict['StopName']['Zh_tw'] = tempdict['StopName']['Zh_tw'].replace('臺', '台')
						tempdict['StopPosition'] = stop['StopPosition']
						finalist.append(tempdict)
			elif re.match('lines', filename): 
				for line in my_data:
					tempdict = {}
					if(stop['RouteName']['Zh_tw'] not in existdict):
						existdict[line['RouteName']['Zh_tw']] = 0
						tempdict['RouteName'] = line['RouteName']
						tempdict['DepartureStopNameZh'] = line['DepartureStopNameZh']	
						finalist.append(tempdict)
			else:
				print('no specific stop or line files')
		with open(("output/parsed_"+filename), 'w', encoding='utf8') as fp:
			fp.write(json.dumps(finalist, ensure_ascii=False))	
			seconds = time.perf_counter() - start						
			print('=====close '+filename+'=====')	
			print('===== %02d:%02d =====' % (seconds / 60, seconds % 60))
