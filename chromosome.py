# Copyright (C) 2016, Tyler Philbrick
# PythonEvolution
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.#

import random
import copy

class Nucleotide(object):
    def __init__(self, value = None):
        self.value = value

    def __str__(self):
        return "Nucleotide(" + str(self.value) + ")"
    
    def flip(self):
        return NotImplemented


class Chromosome(object):
    """
    Chromosome is intended to be subclassed and have logic implemented
    there - iter and getitem are provided for convenience
    """
    def __init__(self):
        print("Do not use this implementation - subclass this and implement logic")

    @classmethod
    def new_from_parent(cls, parent):
        x = copy.deepcopy(parent)
        x.mutate()
        return x

    def __iter__(self):
        for n in self.raw_data:
            yield n

    def __getitem__(self, key):
        return "".join(item.value for item in self.raw_data[key])

    @property
    def encoded_data(self):
        return NotImplemented

    def fitness(self):
        return NotImplemented
        
    def mutate(self, amount = None):
        if amount is None:
            amount = self.mutability
        for nucleotide in self.raw_data:
            if random.random() < amount:
                nucleotide.flip()
 
