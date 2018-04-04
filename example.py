"""
A simple example of using yack
"""

import os
import click
import yack
import gzip
from Bio import SeqIO
from metrics import  rjsd


def _get_sequences(filename):
    input_format = os.path.splitext(filename)[1][1:]
    if input_format == "gz":
        with gzip.open(filename, "rt") as handle:
            input_format = os.path.splitext(os.path.splitext(filename)[0])[1][1:]
            return [str(record.seq) for record in SeqIO.parse(handle, input_format)]
    else:
        return [str(record.seq) for record in SeqIO.parse(filename, input_format)]


@click.command()
@click.argument('file1', type=click.Path(exists=True), required=True)
@click.argument('file2', type=click.Path(exists=True), required=True)
@click.option('--kmer-size', '-k', type=int, default=15)
def main(file1, file2, kmer_size):
    x = yack.count_kmers(_get_sequences(file1), kmer_size)
    y = yack.count_kmers(_get_sequences(file2), kmer_size)
    print(rjsd(x, y))

if __name__ == "__main__":
    main()