from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal


# -------------------------------------------------
# Helper: normalise and validate nucleotide sequences
# -------------------------------------------------

def normalise_sequence(seq: str, valid_bases: set[str]) -> str:
    seq = seq.upper()
    if not seq:
        raise ValueError("Sequence must not be empty")
    if not set(seq).issubset(valid_bases):
        raise ValueError(f"Invalid bases in sequence: {seq}")
    return seq


# -------------------------------------------------
# Interface type
# -------------------------------------------------

class NucleotideSequence(ABC):
    @property
    @abstractmethod
    def seq(self) -> str:
        ...


# -------------------------------------------------
# DNA and RNA sequence implementations
# -------------------------------------------------

DNA_BASES: set[str] = {"A", "C", "G", "T"}
RNA_BASES: set[str] = {"A", "C", "G", "U"}


@dataclass(frozen=True)
class DNASequence(NucleotideSequence):
    seq: str

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "seq", normalise_sequence(self.seq, DNA_BASES)
        )


@dataclass(frozen=True)
class RNASequence(NucleotideSequence):
    seq: str

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "seq", normalise_sequence(self.seq, RNA_BASES)
        )


# -------------------------------------------------
# GC content calculation (typed to interface)
# -------------------------------------------------

def calc_gc_content(seq_obj: NucleotideSequence, dp: int = 2) -> float:
    seq = seq_obj.seq
    assert len(seq) > 0

    gc_count = seq.count("G") + seq.count("C")
    return round(gc_count / len(seq), dp)


# -------------------------------------------------
# Immutable statistics results type
# -------------------------------------------------

SeqKind = Literal["DNA", "RNA"]


@dataclass(frozen=True)
class SeqStats:
    id: str
    kind: SeqKind
    length: int
    gc_fraction: float


# -------------------------------------------------
# Summarise function
# -------------------------------------------------

def summarise(seq: NucleotideSequence, seq_id: str) -> SeqStats:
    if isinstance(seq, DNASequence):
        kind: SeqKind = "DNA"
    elif isinstance(seq, RNASequence):
        kind = "RNA"
    else:
        raise TypeError(
            f"Unsupported NucleotideSequence type: {type(seq).__name__}"
        )

    return SeqStats(
        id=seq_id,
        kind=kind,
        length=len(seq.seq),
        gc_fraction=calc_gc_content(seq),
    )


# -------------------------------------------------
# Example usage
# -------------------------------------------------

if __name__ == "__main__":
    dna = DNASequence("acgtacgt")
    rna = RNASequence("acguacgu")

    dna_stats = summarise(dna, "dna_1")
    rna_stats = summarise(rna, "rna_1")

    print(dna_stats)
    print(rna_stats)
