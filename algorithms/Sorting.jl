# Inefficient: creates copies, no in place
function mergesorted(sortedarray1::Vector{T}, sortedarray2::Vector{T})::Vector{T} where T <: Real
	n = length(sortedarray1)
	m = length(sortedarray2)
	result = Vector{Int}(undef, n + m)
	i = 1
	j = 1

	while i ≤ n && j ≤ m
		if sortedarray1[i] ≤ sortedarray2[j]
			result[i + j - 1] = sortedarray1[i]
			i += 1
		else
			result[i + j - 1] = sortedarray2[j]
			j += 1
		end
	end

	if i > n
		result[i + j - 1 : end] = sortedarray2[j:end]
	else
		result[i + j - 1 : end] = sortedarray1[i:end]
	end

	return result
end

function mergesort(array::Vector{T})::Vector{T} where T <: Real
	# Split
	len = length(array)
	len == 1 && (return array)

	# Sort
	sortedleft  = mergesort(array[1:(len ÷ 2)])
	sortedright = mergesort(array[(len ÷ 2 + 1):end])

	# Combine
	return mergesorted(sortedleft, sortedright)
end

println(mergesort([6, 4, 1, 9, 8, 2, 6, 4]))
