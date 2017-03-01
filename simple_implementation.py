#!/usr/bin/env python3

import random
import math

from chromosome import Nucleotide, Chromosome
#from organism import Organism

class NumberNucleotide(Nucleotide):
    def __init__(self, value = None):
        if value is None:
            value = random.randint(0,9)
        self.value = value

    def flip(self):
        delta = random.choice([-1,1])
        self.value += delta
        if self.value < 0:
            self.value = 0
        self.value %= 10

class NumberChromosome(Chromosome):
    def __init__(self, length, mutability):
        self.raw_data = [NumberNucleotide() for i in range(length)]
        self.mutability = mutability

    @property
    def encoded_data(self):
        return int("".join([str(j.value) for j in self.raw_data]))

    def fitness(self):
        return self.encoded_data


def main():
    # generations = []
    length = 1000
    keep = 500
    convergeance = 20
    conv_ctr = 0

    orgs = [NumberChromosome(length = 10, mutability = 0.1) for i in range(length)]
    
    while True:
        orgs.sort(key = lambda org: org.fitness(), reverse = True)

        if orgs[keep-1].fitness() == orgs[0].fitness():
            conv_ctr += 1
        else:
            conv_ctr = 0
        if conv_ctr == convergeance:
            print("Converged")
            exit()

        print(orgs[0].fitness(), orgs[0].encoded_data)

        orgs = orgs[:keep]
        for i in range(length - keep):
            orgs.append(NumberChromosome.new_from_parent(orgs[random.randint(0, keep-1)]))


if __name__ == "__main__":
    main()

