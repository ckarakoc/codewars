def DNA_strand(dna):
    compl = { 'A':'T', 'T':'A', 'C':'G', 'G':'C' }
    return ''.join(compl[s] for s in dna)