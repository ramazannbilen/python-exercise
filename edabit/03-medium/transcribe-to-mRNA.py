"""Transcribe to mRNA
Transcribe the given DNA strand into corresponding mRNA - a type of RNA, that will be formed from it after transcription. DNA has the bases A, T, G and C, while RNA converts to U, A, C and G respectively.

Examples
dna_to_rna("ATTAGCGCGATATACGCGTAC") ➞ "UAAUCGCGCUAUAUGCGCAUG"

dna_to_rna("CGATATA") ➞ "GCUAUAU"

dna_to_rna("GTCATACGACGTA") ➞ "CAGUAUGCUGCAU"
Notes
Transcription is the process of making complementary strand.
A, T, G and C in DNA converts to U, A, C and G respectively, when in mRNA."""

from edabit.Test import Test


def dna_to_rna(dna):
    str1 = "ATGC"
    str2 = "UACG"
    new = dna.maketrans(str1,str2)
    mRNA = dna.translate(new)
    return mRNA


Test.assert_equals(dna_to_rna("GCGTAC"), "CGCAUG")
Test.assert_equals(dna_to_rna("ATTAGCGCGATATACGCGTAC"), "UAAUCGCGCUAUAUGCGCAUG")
Test.assert_equals(dna_to_rna("CAGTATGCTGCAT"), "GUCAUACGACGUA")
Test.assert_equals(dna_to_rna("CGATATA"), "GCUAUAU")
Test.assert_equals(dna_to_rna("GCAGCTACA"), "CGUCGAUGU")
