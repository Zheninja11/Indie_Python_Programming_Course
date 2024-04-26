def count_AGTC(dna):
    dna_dict = {'A': 0, 'G': 0, 'T': 0, 'C': 0}

    for nitrogenous_base in dna:
        dna_dict[nitrogenous_base] += 1
    
    return (dna_dict['A'], dna_dict['G'], dna_dict['T'], dna_dict['C'])
