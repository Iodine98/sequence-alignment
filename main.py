from dataclasses import dataclass
import numpy as np
from numpy import ndarray


@dataclass
class SequenceAlignmentData:
    first_strand: str
    second_strand: str
    match_score: int
    gap_score: int


class SequenceAlignment(SequenceAlignmentData):
    def __init__(self, first_strand, second_strand, match_score=2, gap_score=-1):
        super(SequenceAlignment, self).__init__(first_strand, second_strand, match_score, gap_score)
        self.S = self.calculate_score_matrix()
        self.M = self.calculate_sequence_alignment_matrix()
        bottom_right_cell = tuple(index - 1 for index in self.S.shape)
        self.optimal_seq_align_score = self.M[bottom_right_cell]

    def calculate_score_matrix(self):
        match_score_matrix = np.zeros((len(self.first_strand), len(self.second_strand)), dtype=np.int16)
        for index, (first_base, second_base) in enumerate(zip(self.first_strand, self.second_strand)):
            if first_base == second_base:
                match_score_matrix[index, index] = self.match_score
            else:
                match_score_matrix[index, index] = self.gap_score
        return match_score_matrix

    def calculate_sequence_alignment_matrix(self):
        dimensions = self.S.shape
        sequence_alignment_matrix: ndarray = np.zeros(dimensions, dtype=np.int16)
        i_dimension, j_dimension = dimensions
        for i in range(i_dimension):
            pass
        return sequence_alignment_matrix


def generate_random_dna_strand(strand_length: int):
    bases = np.array(['A', 'T', 'C', 'G', '-'])
    random_number_array = np.random.randint(0, bases.size - 1, strand_length).T

    def convert_to_base(x):
        return bases[x]

    return convert_to_base(random_number_array)


if __name__ == '__main__':
    first_strand = generate_random_dna_strand(100)
    second_strand = generate_random_dna_strand(100)
    sequence_alignment = SequenceAlignment(first_strand, second_strand)
    print(sequence_alignment.optimal_seq_align_score)
