def skrypt(file_path):
    gene_lengths = []
    polymerase_genes = []
    total_length = 0
    current_product = None

    with open(file_path, 'r') as f:
        for line in f:
            line=line.strip()
            if line.startswith("/product"):
                current_product = line.split("=")[1].strip('"')
            elif line.startswith("/locus_tag") and current_product and "polymerase" in current_product.lower() and ("RNA" or "DNA" in current_product): 
                locus_tag = line.split("=")[1].strip('"')
                polymerase_genes.append({"product": current_product, "locus_tag": locus_tag})
                current_product = None
            elif line.startswith("gene"):
                line = line.split()
                if line[1].startswith("complement"):
                    line = line[1]
                    line = line[len("complement("):-1]
                    start, end = line.split("..")
                    length= int(end) - int(start) + 1
                    gene_lengths.append(length)
                else:
                    start, end = line[1].split("..")
                    length= int(end) - int(start) + 1
                    gene_lengths.append(length)
            
    
    
    for i in gene_lengths:
        total_length += int(i) 
    
    
    return len(gene_lengths), total_length/len(gene_lengths), len(polymerase_genes), polymerase_genes[1:3]

print(skrypt("assembly.gbff"))
print(skrypt("assembly.gbk"))