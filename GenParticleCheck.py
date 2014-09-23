###########################
##This code runs over miniAOD files and writes out the SUSY particles
##saved in the pruned and packed Genparticle collections.
## setup cmssw environment and run with "python GenParticleCheck.py"

import ROOT
import sys
from DataFormats.FWLite import Events, Handle
from math import *

events = Events (['file:/nfs/dust/cms/user/clseitz/CMG/CMSSW_7_0_6_patch1/src/TreeAnalyzer/0A59FC95-330F-E411-94EB-E0CB4E29C4CA.root'])

handlePruned  = Handle ("std::vector<reco::GenParticle>")
handlePacked  = Handle ("std::vector<pat::PackedGenParticle>")
labelPruned = ("prunedGenParticles")
labelPacked = ("packedGenParticles")

# loop over events
count= 0
for event in events:
    print "--------"
    event.getByLabel (labelPacked, handlePacked)
    event.getByLabel (labelPruned, handlePruned)
    # get the product
    packed = handlePacked.product()
    pruned = handlePruned.product()
    print "pruned"
    for p in pruned :
        if(p.pdgId()>1000000):
               print "PdgId : %s   pt : %s  eta : %s   phi : %s" %(p.pdgId(),p.pt(),p.eta(),p.phi())   
    print "packed"
    for p in packed :
        if(p.pdgId()>1000000):
               print "PdgId : %s   pt : %s  eta : %s   phi : %s" %(p.pdgId(),p.pt(),p.eta(),p.phi())    

