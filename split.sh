#!/bin/bash

echo performing split...

FILENAME=Crimes_-_2017.csv	# paste filename here
HDR=$(head -1 $FILENAME)   # Pick up CSV header line to apply to each file
split -l 10000 $FILENAME xyz  # Split the file into chunks of 20 lines each
n=1
for f in xyz*              # Go through all newly created chunks
do
   echo $HDR > Part${n}.csv    # Write out header to new file called "Part(n)"
   cat $f >> Part${n}.csv      # Add in the 20 lines from the "split" command
   rm $f                   # Remove temporary file
   ((n++))                 # Increment name of output part
done

mkdir data		#create a folder data
mv Part* data		# move all file chunks to data folder
