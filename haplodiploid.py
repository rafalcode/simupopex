#!/usr/bin/env python3

# from the 
# $File: haplodiploid.py $
#

# typical way of importing
import simuPOP as sim
# alot of these new (2019) python packages always have a typical name
# that they usr, sim in this case, pd for pandas, etc.


# pop = sim.Population(size=[2,5], ploidy=sim.HAPLODIPLOID, loci=[3, 5])
# these are the essentials for the Pop object
# remember seeing that size need not be a list, neith should loci.
# the multiple values ofr size would be subpopulations.
o
sim.initGenotype(pop, freq=[0.3, 0.7])
sim.dump(pop)

