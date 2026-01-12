from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


# -------------------------------------------------
# Common helper: normalisation & validation
# -------------------------------------------------

def normalise_sequence(seq: str, valid_bases: set[str]) -> str:
    """
    Normalise a nucleotide sequence by uppercasing and validating bases.
    """
    seq = seq.upper()
    if not seq:
        raise ValueError("Sequence must not be empty")

    if not set(seq).issubset(valid_bases):
        raise ValueError(f"Invalid bases in sequence: {seq}")

    return seq


# -------------------------------------------------
# Explicit interface type (ABC)
# -------------------------------------------------

class NucleotideSequence(ABC):
    """
    Interface for nucleotide sequences supporting GC content calculation.
    """

    @property
    @abstractmethod
    def seq(self) -> str:
        ...


# -------------------------------------------------
# DNA sequence (frozen dataclass)
# -------------------------------------------------

DNA_BASES: set[str] = {"A", "C", "G", "T"}

@dataclass(frozen=True)
class DNASequence(NucleotideSequence):
    seq: str

    def __post_init__(self) -> None:
        normalised = normalise_sequence(self.seq, DNA_BASES)
        object.__setattr__(self, "seq", normalised)


# -------------------------------------------------
# RNA sequence (frozen dataclass)
# -------------------------------------------------

RNA_BASES: set[str] = {"A", "C", "G", "U"}

@dataclass(frozen=True)
class RNASequence(NucleotideSequence):
    seq: str

    def __post_init__(self) -> None:
        normalised = normalise_sequence(self.seq, RNA_BASES)
        object.__setattr__(self, "seq", normalised)


# -------------------------------------------------
# GC content calculation (typed to interface)
# -------------------------------------------------

def calc_gc_content(seq_obj: NucleotideSequence, dp: int = 2) -> float:
    """
    Calculate GC content for any nucleotide sequence.
    """
    seq = seq_obj.seq
    assert len(seq) > 0

    gc_count = seq.count("G") + seq.count("C")
    gc_content = gc_count / len(seq)

    return round(gc_content, dp)


# -------------------------------------------------
# Example usage
# -------------------------------------------------

if __name__ == "__main__":
    dna = DNASequence("acgtacgt")
    rna = RNASequence("acguacgu")

    print("DNA GC content:", calc_gc_content(dna))
    print("RNA GC content:", calc_gc_content(rna))
