# Project_DiHiggsDecay

In this project, we study the decay of Double Higgs into bb~+GammaGamma in the final state in the Next-to Minimal Supersymmetric Standard Model using MadGraph5. We study the following processes:

g g > H03 > H01 H02 (H01 > a a , H02> b b~) and  g g > H03 > H01 H02 (H02 > a a , H01> b b~).

To generate the process first, execute the following commands:

Open MadGraph5 directory and type: ./bin/mg5_aMC


Then execute the following set of commands in the madgraph window:

>set group_subprocesses Auto
>set ignore_six_quark_processes False
>set loop_optimized_output True
>set gauge unitary
>set complex_mass_scheme False

>import model NMMSM


>generate g g > h03 , (h03 > h2 h01, h2 > a a, h01 > b b~)

>output gg_h03_h01h02_bb~aa

>launch

>0

>1 (Enter 1 to edit the param.card file. In the parameter card, change the mass MH01 to 1.250000e+03 GeV and change the decay width of Higgs H01 to WH01 to 4.00000e-03 GeV.)

The editing of the param card can be done only in vim editor. To insert text press 'i' and to save the card press 'Esc' key and press 'shift+z' twice. 


>2 (Enter 2 to edit the run.card file. In the run card, change the id to 'lhapdf' and change the lhapdf id to '292600'.)

The editing of the param card can be done only in vim editor. To insert text press 'i' and to save the card press 'Esc' key and press 'shift+z' twice.

>0
 
This will generate 10000 events of the process 'g g > h03 , (h03 > h2 h01, h2 > a a, h01 > b b~)'. A 'LHE' file will be produced which will contains information about four momentum, invariant state of the particles generated during the process. Note: By default Madgraph generates 10000 events.   

To generate the process  g g > h03 , (h03 > h2 h01, h01 > a a, h2 > b b~), follow the same set of commands.
