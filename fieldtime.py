#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import os		# to read environment variables
import urllib2  # to make web calls to SMHI api
import json     # to structure SMHI data
import datetime # in order to do time comparisons

try:
	latitude = os.environ.get('fieldtime_latitude')
	longitude = os.environ.get('fieldtime_longitude')
except:
	print("somethings not right w/ the environment variables")
	quit()

smhi_string = urllib2.urlopen("https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/" + longitude + "/lat/" + latitude + "/data.json").read()
smhi_json = json.loads(smhi_string)

now = datetime.datetime.now()

for point in smhi_json['timeSeries']:
	point_timestring = point['validTime']
	point_time = datetime.datetime.strptime(point_timestring, "%Y-%m-%dT%H:%M:%SZ") # 2015-10-12T05:13:19Z
