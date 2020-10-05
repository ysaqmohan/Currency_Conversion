#!/bin/bash

SDATE=`date`
STIME=`date +%s`
RUNDATE=`date +%C%y-%m-%d_%H.%M.%S`

script_name="Currency_Conversion"
log_file=/edw/Currency_Conversion/logs/"${script_name}-${RUNDATE}.log"

#function for capturing error
error_check ()
{
	if [ $? -gt 0 ]
	then
		echo "Job Failed"
		echo "$log_file"
		exit 8
	fi
}
echo "Script execution beginning" >> $log_file

#Execute the python script
/edw/Currency_Conversion/project_Currency/bin/python /edw/Currency_Conversion/python/Currency_script.py >> $log_file 2>&1
error_check

echo "Script completed succesfully" >> $log_file
