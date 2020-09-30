# function cutrod_naive(p::Array{Int, 1}, n::Int)::Int
# 	if n == 0
# 		return 0
# 	end

# 	q = typemin(Int)    # q = -∞
# 	for i ∈ 1:n
# 		q = max(q, p[i] + cutrod(p, n - i))
# 	end

# 	return q
# end


# function cutrod_memoized(p::Array{Int, 1}, n::Int)::Int
# 	r = fill(typemin(Int), length(p))

# 	function cutrod_memoized_aux(p::Array{Int, 1}, n::Int, r::Array{Int, 1})::Int
# 		if n == 0
# 			return 0
# 		end

# 		if r[n] ≥ 0
# 			return r[n]
# 		end

# 		q = typemin(Int)    # q = -∞
# 		for i ∈ 1:n
# 			q = max(q, p[i] + cutrod_memoized_aux(p, n - i, r))
# 		end

# 		return q
# 	end

# 	return cutrod_memoized_aux(p, n, r)
# end


# prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# for j ∈ 1:10
# 	println("Best reveneu for length $j is $(cutrod_memoized(prices, j)) \$.")
# end