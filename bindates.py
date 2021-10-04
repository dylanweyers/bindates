from datetime import datetime, date, timedelta
import os
interval = 21 # In days. Mixed rubbish is collected every 3 weeks where I live
dateQuantity: int = ( ( 365 + ( 2 * interval ) ) / interval ) # This will give us a starting date for next year

class bins:
	def binDates(baseDate: str):
		dates = list()
		d = date(int(baseDate[0:4]), int(baseDate[5:7]), int(baseDate[8:10]) )
		for i in range(int(dateQuantity)):
			idate = (d+timedelta(days=interval*i))
			dates.append(idate)
		outputFile = baseDate[0:4]+".txt"
		if not os.path.exists(outputFile):
			dateFile = open(outputFile, "a+")
			dateFile.close()
		dateFile = open(outputFile, "a")
		for i in range(len(dates)):
			dateFile.write(dates[i].isoformat()+"\n")
		dateFile.close()

bins.binDates("2022-01-06")