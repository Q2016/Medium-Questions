Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. 
The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. 
Reconstruction means building a shortest common supersequence of the sequences in seqs
(i.e., a shortest sequence so that all sequences in seqs are subsequences of it). 
Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:
Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:
Input: 
org: [1,2,3], seqs: [[1,2]]

Output: 
false

Explanation:
The reconstructed sequence can only be [1,2].
Example 3:
Input: 
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output: 
true

Explanation: 
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:
Input: 
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output: 
true



Solution: Hash Table

For org to be uniquely reconstructible from seqs we need to satisfy 2 conditions:

Every sequence in seqs should be a subsequence in org. This part is obvious.
Every 2 consecutive elements in org should be consecutive elements in some sequence from seqs. Why is that? Well, suppose condition 1 is satisfied. Then for 2 any consecutive elements x and y in org we have 2 options.
We have both x and y in some sequence from seqs. Then (as condition 1 is satisfied) they must be consequtive elements in this sequence.
There is no sequence in seqs that contains both x and y. In this case we cannot uniquely reconstruct org from seqs as sequence with x and y switched would also be a valid original sequence for seqs.
So this are 2 necessary criterions. It is pretty easy to see that this are also sufficient criterions for org to be uniquely reconstructible (there is only 1 way to reconstruct sequence when we know that condition 2 is satisfied).

To implement this idea I have idxs hash that maps item to its index in org sequence to check condition 1. And I have pairs set that holds all consequitive element pairs for sequences from seqs to check condition 2 (I also consider first elements to be paired with previous undefined elements, it is necessary to check this).


    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        indices = {e : i for i, e in enumerate(org)}
        edges = set()

        if not seqs: return False
        for seq in seqs:
            for s in seq:
                if s not in indices:
                    return False
            for i in range(1, len(seq)):
                pre, cur = seq[i - 1], seq[i]
                if indices[pre] > indices[cur]:
                    return False
                edges.add((pre, cur))

        for x in range(1, len(org)):
            if (org[x - 1], org[x]) not in edges:
                return False
        return True
