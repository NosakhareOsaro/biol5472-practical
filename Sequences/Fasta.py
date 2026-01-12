from typing import Iterator, Type, TypeVar
from Sequences.Sequences import BioSequence
from Sequences.Sequences import DNASequence

T = TypeVar("T", bound=BioSequence)


# class to parse a fasta file    
class FastaFile:

    def __init__(self, file: str) -> None:
        self._file: str = file

    @property
    def file(self) -> str:
        return self._file

    def get_seq_record(
        self,
        sequence_class: Type[T],
    ) -> Iterator[T]:
        with open(self.file) as filehandle:
            for line in filehandle:
                if line.startswith('>'):
                    seq_id: str = line.rstrip().lstrip('>')
                    seq: str = next(filehandle).rstrip()
                    yield sequence_class(seq_id, seq)


if __name__ == "__main__":
    fasta = FastaFile("example.fasta")

    for record in fasta.get_seq_record(DNASequence):
        print(record)
        print("GC content:", record.calc_gc_content())
