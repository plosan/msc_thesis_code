for i in $(seq 3 7);
do
	for j in $(seq $((i+1)) 7);
	do
		python3 monomials_of_deformation.py $i $j
		echo "\n"
	done
done
