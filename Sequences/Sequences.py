from collections.abc import Iterator

# create the superclass
class BioSequence:

    def __init__(self, id: str, seq: str) -> None:
        self._id: str = id
        self._seq: str = seq.upper()

    @property
    def id(self) -> str:
        return self._id 

    @property
    def seq(self) -> str:
        return self._seq
    
    def __str__(self) -> str:
        return f'Sequence Object: ID; {self.id}, Seq; {self.seq}'
    
    def __len__(self) -> int:
        return len(self.seq)
    
    # Iterates over characters in the sequence string
    def __iter__(self) -> Iterator[str]:
        return iter(self.seq)
    
    def make_fasta(self) -> str:
        return f'>{self.id}\n{self.seq}\n'

class DNASequence(BioSequence):

    def calc_gc_content(self, dp: int = 2) -> float:
        c_count: int = self.seq.count('C')
        g_count: int = self.seq.count('G')
        gc_content: float = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)
    
    def translate_seq(self) -> str:
        bases: str = "TCAG"
        codons: list[str] = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids: str = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table: dict[str, str] = dict(zip(codons, amino_acids))

        aa_list: list[str] = [
            codon_table[self.seq[start:start+3]]
            for start in range(0, len(self.seq) - 2, 3)
        ]
        return ''.join(aa_list)
        
    def get_protein_len(self) -> int:
        return len(self.seq) // 3

class ProteinSequence(BioSequence):

    def __init__(self, id: str, seq: str, descr: str = '') -> None:
        super().__init__(id, seq)
        self._descr: str = descr

    @property
    def descr(self) -> str:
        return self._descr

    def get_prop_hydrophobic(self) -> float:
        count_hydrophobic: int = 0
        hydrophobic: list[str] = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']
        for hydro in hydrophobic:
            count_hydrophobic += self.seq.count(hydro)
        return count_hydrophobic / len(self.seq)
    
    def get_protein_len(self) -> int:
        return len(self.seq)
