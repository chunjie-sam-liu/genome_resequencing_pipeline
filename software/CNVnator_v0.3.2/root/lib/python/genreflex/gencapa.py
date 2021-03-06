# Copyright CERN, CH-1211 Geneva 23, 2004-2006, All rights reserved.
#
# Permission to use, copy, modify, and distribute this software for any
# purpose is hereby granted without fee, provided that this copyright and
# permissions notice appear in all copies and derivatives.
#
# This software is provided "as is" without express or implied warranty.

import os, sys

model = """
// This file has been generated by genreflex with the --capabilities option
static  const char* clnames[] = {
//--Final End
};

extern "C" void SEAL_CAPABILITIES (const char**& names, int& n )
{ 
  names = clnames;
  n = sizeof(clnames)/sizeof(char*);
}
"""

#----------------------------------------------------------------------------------
def genCapabilities(capfile, dicfile, classes) :
  startmark = '//--Begin ' + dicfile + '\n'
  endmark   = '//--End   ' + dicfile + '\n'
  finalmark = '//--Final End\n'
  capaPre = 'LCGReflex'
  new_lines = ['  "'+capaPre+'/%s",\n' % c for c in classes]
  if not os.path.exists(capfile) :
    lines = [ line+'\n' for line in model.split('\n')]
  else :
    f = open(capfile,'r') 
    lines = [ line for line in f.readlines()]
    f.close()
  if startmark in lines and endmark in lines :
    lines[lines.index(startmark)+1 : lines.index(endmark)] = new_lines
  else :
    lines[lines.index(finalmark):lines.index(finalmark)] = [startmark]+new_lines+[endmark]
  f = open(capfile,'w')
  f.writelines(lines)
  f.close()


