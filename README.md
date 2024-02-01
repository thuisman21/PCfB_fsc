Created by: Thimo Huisman

Date: Feb 1 2024

Email: t.huisman.6@student.rug.nl

Example usage:
inputFileGenerator.py -n 4 -s 12 -m 2.49e-8 -f <output_prefix> -i <matrix.txt> -e <events.txt> -p <parameters.txt>

This script generates two input files for that can be used for fastsimcoal2 simlulations.
It takes multiple options on the command line and takes these and multiple input files to generate a .tpl and .est file.
These files can then be used to with an .obs file to run fastsimcoal2 simulations.