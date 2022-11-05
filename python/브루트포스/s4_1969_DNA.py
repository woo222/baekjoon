n, dna_n = map(int, input().split())
dna = []
new_dna=''
cnt = 0
nucleo = ['A', 'C', 'G', 'T']

for i in range(n):
    dna.append(list(map(str, input())))

for i in range(dna_n):
    nucleo_cnt = [0, 0, 0, 0]
    for j in range(n):
        if(dna[j][i] == 'A'):
            nucleo_cnt[0] += 1
        elif(dna[j][i] == 'C'):
            nucleo_cnt[1] += 1
        elif(dna[j][i] == 'G'):
            nucleo_cnt[2] += 1
        elif(dna[j][i] == 'T'):
            nucleo_cnt[3] += 1
        
    new_dna += nucleo[nucleo_cnt.index(max(nucleo_cnt))]

for dna_line in dna:
    i = 0
    for dna_one in dna_line:
        if(new_dna[i] != dna_one):
            cnt += 1
        i += 1

print(new_dna)
print(cnt)