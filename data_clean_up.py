#from Bio  import SeqIO
import csv
import pandas as pd
Data=[]
AromaticAA = ['Y','W','F']
PositiveAA=['R','H','K']
NegativeAA=['D','E']
HydrophobicAA=['A','C','L','I','M','F','Y','W']
df = pd.read_csv('input2.csv')
Seq=df.Sequence
Seq=Seq.astype(str)
print(Seq)
df['Protein Length'] = len(Seq)
AromaticCount={}
PercentAromatic={}
for row in Seq:
    for aa in AromaticAA:
        AromaticCount=Seq.count(aa)
        print(AromaticCount)
    for aa in PositiveAA:
        PostiveCount=Seq.count(aa)
    for aa in NegativeAA:
        NegativeCount=Seq.count(aa)
    for aa in HydrophobicAA:
        HydrophobicCount=Seq.count(aa)

    print(AromaticCount)
    #print(positiveCount)
    #print(NegativeCount)
    #Print(HydrophobicCount)

#with open('input.csv','r') as csv_file:
#    csv_reader=csv.DictReader(csv_file)

#    with open('output.csv','w') as new_file:
#        fieldnames=['accession','pI','Protein Length','Protein Weight','Enzyme Commision Number',
#                    'Particle Size','Particle Charge','Solvent Cysteine Conc','Solvent NaCl Conc',
#                    'sequence','%aromatic','%Negative','%Postive','%Hydrophobic','%Cysteine',
#                    'Protein Abundance','Enrichment','Interprot']
#for record in SeqIO.parse("protein.fasta", "fasta"):
#    MyId=str(record.id.upper())
#    MySeq=str(record.seq.upper())
#    MySeq=MySeq.upper()
#    length=len(MySeq)
#    AromaticDict={}
#    PercentDict = {}
#    Aromcity=[]
#    Data.append(str(MyId))
#    for aa in AromaticAA:
#        AromaticDict[aa]=MySeq.count(aa)
#    for aa in  AromaticAA:
#        PercentDict[aa] = round(AromaticDict[aa] /float(length),3)
#        Aromcity.append(PercentDict[aa])
#        Data.append(str(PercentDict[aa]))
#    Data.append(sum(Aromcity))
#with open('output.csv', 'w') as csvfile:
#    csv_columns = ['ID','Y','W','F','Aromaticity']
#    writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
#    writer.writerow(csv_columns)
#    for i in range(0,len(Data),5):
#          writer.writerow(Data[i:i+5])