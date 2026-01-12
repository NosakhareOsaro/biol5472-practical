from typing import Iterator, Type, Any
from collections.abc import Iterable

# class to parse a fasta file    
class FastaFile:

    # constructor - only attribute is string containing a file name
    def __init__(self, file: str) -> None:
        self._file: str = file

    # getter for file name
    @property
    def file(self) -> str:
        return self._file

    # method to get DNASequence records out from a fasta file
    # yields sequence objects (DNASequence or similar)
    def get_seq_record(
        self,
        sequence_class: Type[Any],
    ) -> Iterator[Any]:
        with open(self.file) as filehandle:
            for line in filehandle:
                if line.startswith('>'):
                    id: str = line.rstrip().lstrip('>')
                    seq: str = next(filehandle).rstrip()
                    yield sequence_class(id, seq)
