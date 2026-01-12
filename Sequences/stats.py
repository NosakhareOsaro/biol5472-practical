from dataclasses import dataclass
from typing import Literal, Optional, Union

from problem_4 import (
    NucleotideSequence,
    DNASequence,
    RNASequence,
    calc_gc_content,
)


SeqKind = Literal["DNA", "RNA"]


@dataclass(frozen=True)
class SeqStats:
    id: str
    kind: SeqKind
    length: int
    gc_fraction: Optional[float]


def summarise(seq: NucleotideSequence) -> SeqStats:
    if isinstance(seq, DNASequence):
        kind: SeqKind = "DNA"
    elif isinstance(seq, RNASequence):
        kind = "RNA"
    else:
        raise TypeError(
            f"Unsupported sequence type: {type(seq).__name__}"
        )

    return SeqStats(
        id="unknown",  # no ID in question4 sequences
        kind=kind,
        length=len(seq.seq),
        gc_fraction=calc_gc_content(seq),
    )
