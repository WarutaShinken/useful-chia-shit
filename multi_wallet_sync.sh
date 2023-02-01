fork_name=chia
fingerprints=( 123 456 789 )
delay=600 #10 Minutes

while true do
do
	for i in "${fingerprints[@]}"
	do
		$fork_name wallet show -f $i
		sleep $delay
	done
done