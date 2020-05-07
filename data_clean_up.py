#from Bio  import SeqIO
#import csv
import pandas as pd
#import numpy as np
Data=[]
AromaticAA = ['Y','W','F']
PositiveAA=['R','H','K']
NegativeAA=['D','E']
HydrophobicAA=['A','C','L','I','M','F','Y','W']
CysteineAA=['C']
df = pd.read_csv('Chan_dataset_formatted.csv')
dfout= pd.DataFrame(columns=['accession','pI','Protein Length','Protein Weight',
                             'Enzyme Commision Number','Particle Size','Particle Charge',
                             'Solvent Cysteine Conc','Solvent NaCl Conc','sequence','%Aromatic',
                             '%Negative','%Postive','%Hydrophobic','%Cysteine','Protein Abundance',
                             'Enrichment','Interprot'])
Seq=df.Sequence
Seq=Seq.astype(str)
F=Seq.index.get_loc(Seq.last_valid_index())
Seq=Seq[:800]
print(Seq)
Seq.fillna(0)
print(Seq)
#df['Protein Length'] = len(Seq)
AromaticCount={}
PositiveCount={}
NegativeCount={}
HydrophobicCount={}
CysteineCount={}
for row in Seq:
    for aa in AromaticAA:
        AromaticCount[aa]=row.count(aa)
    for aa in PositiveAA:
        PositiveCount[aa]=row.count(aa)
    for aa in NegativeAA:
        NegativeCount[aa]=row.count(aa)
    for aa in HydrophobicAA:
        HydrophobicCount[aa]=row.count(aa)
    for aa in CysteineAA:
        CysteineCount[aa]=row.count(aa)
    Length=len(row)
    PercentAromatic=round(sum(list(AromaticCount.values()))*100/float(Length),3)
    PercentPositive=round(sum(list(PositiveCount.values()))*100/float(Length),3)
    PercentNegative=round(sum(list(NegativeCount.values()))*100/float(Length),3)
    PercentHydrophobic=round(sum(list(HydrophobicCount.values()))*100/float(Length),3)
    PercentCysteine=round(sum(list(CysteineCount.values()))*100/float(Length),3)
    df2=pd.DataFrame([[Length,row,PercentAromatic,PercentPositive,PercentNegative,PercentHydrophobic,PercentCysteine]],
                     columns=['Protein Length','Sequence','%Aromatic','%Postive','%Negative','%Hydrophobic','%Cysteine'])
    dfout=pd.concat([dfout,df2])
#print(dfout)
dfout.to_csv('ProteinValues_Calculated.csv')

    #print(PercentAromatic)
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