import ElementTree as ET
from ROOT import TLorentzVector,TCanvas,TH1F,TLegend,gStyle,TLatex,TText

tree1 = ET.parse('gg_h2h01_bb~aa.lhe')
root1=tree1.getroot()

eta_b_l1=[]
eta_bbar_l1=[]
phi_b_l1=[]
phi_bbar_l1=[]
phi_a_l1=[]
phi_a2_l1=[]
eta_a_l1=[]
eta_a2_l1=[]
pt_b_l1=[]
pt_a2_l1=[]
pt_bbar_l1=[]
pt_a_l1=[]
m_1_H1_l1=[]
m_1_H2_l1=[]
m_1_H3_l1=[]
m_2_H2_l1=[]
m_2_H1_l1=[]
m_2_H3_l1=[]

gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(1)
gStyle.SetOptStat(0)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
gStyle.SetPadColor(1)

#legend=TLegend(.63,.69,.87,.89,"","#gamma #gamma")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","b b~")

c=TCanvas("c","First canvas",2000,1900)

#title=TLatex(0.15,1.85,"Trials")
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
#cmsname.SetTextSize(0.036)
#cmsname.SetTextAlign(12)
#cmsname.SetNDC(1)
#cmsname.SetTextFont(61)
#lhefdata=LHEFData(float(root.attrib['version']))
#lhefdata=LHEFData(float(root.attrib['version']))

for child in root1:
 if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())
            
       a1_1_l1=[s for s in lines if s.split()[0]=='22']
       a1_l1=a1_1_l1[1::2]
       a2_l1=a1_1_l1[0::2]
       b1_l1=[s for s in lines if s.split()[0]=='5' and (s.split()[2]=='5' and lines[5].split()[0]=='35')]
       bbar1_l1=[s for s in lines if s.split()[0]=='-5'and (s.split()[2]=='5' and lines[5].split()[0]=='35')]
	      
       if a1_l1:
	       px3_l1=float (a1_l1[0].split()[6])
	       py3_l1=float (a1_l1[0].split()[7])
	       pz3_l1=float (a1_l1[0].split()[8])
	       e3_l1=float (a1_l1[0].split()[9])
      
       if a2_l1:
		       
	       px4_l1=float (a2_l1[0].split()[6])
	       py4_l1=float (a2_l1[0].split()[7])
	       pz4_l1=float (a2_l1[0].split()[8])
	       e4_l1=float (a2_l1[0].split()[9])

       if a1_l1 and a2_l1:	
	       
	       p3_l1=TLorentzVector(px3_l1,py3_l1,pz3_l1,e3_l1)
	       p4_l1=TLorentzVector(px4_l1,py4_l1,pz4_l1,e4_l1)
	       pb1_l1=p3_l1+p4_l1
	       m_1_H1_l1.append(pb1_l1.M())
	       eta_a_l1.append(p3_l1.Eta())
	       pt_a_l1.append(p3_l1.Pt())      
	       eta_a2_l1.append(p4_l1.Eta())
	       pt_a2_l1.append(p4_l1.Pt())
               phi_a_l1.append(p3_l1.Phi())
               phi_a2_l1.append(p4_l1.Phi())
               

       if b1_l1:
	       
	       px5_l1=float (b1_l1[0].split()[6])
	       py5_l1=float (b1_l1[0].split()[7])
	       pz5_l1=float (b1_l1[0].split()[8])
	       e5_l1=float (b1_l1[0].split()[9])
       
       if bbar1_l1:

	       px6_l1=float (bbar1_l1[0].split()[6])
	       py6_l1=float (bbar1_l1[0].split()[7])
	       pz6_l1=float (bbar1_l1[0].split()[8])
	       e6_l1=float (bbar1_l1[0].split()[9])

       if b1_l1 and bbar1_l1:

	       p5_l1=TLorentzVector(px5_l1,py5_l1,pz5_l1,e5_l1)
	       p6_l1=TLorentzVector(px6_l1,py6_l1,pz6_l1,e6_l1)
	       pb2_l1=p5_l1+p6_l1
	       m_1_H2_l1.append(pb2_l1.M())
	       
	       eta_b_l1.append(p5_l1.Eta())
	       eta_bbar_l1.append(p6_l1.Eta())
	       pt_b_l1.append(p5_l1.Pt())      
	       pt_bbar_l1.append(p6_l1.Pt())
               phi_b_l1.append(p5_l1.Phi())
               phi_bbar_l1.append(p6_l1.Phi())
                 
c.SetLogy()

h1=TH1F('M_{#gamma#gamma} (h2>bb~ h1>aa)',"",1000,0,1200)
for i in m_1_H1_l1:
        h1.Fill(i)
h14=TH1F('M_{bb~} (h2>bb~ h1>aa)',"",1000,0,1200)
for i in m_1_H2_l1:
        h14.Fill(i)

h2=TH1F('#eta_{#gamma1} (h2>bb~ h1>aa)',"",100,-5,5)
for i in eta_a_l1:
        h2.Fill(i)
h9=TH1F('#eta_{#gamma2} (h2>bb~ h1>aa)',"",100,-5,5)
for i in eta_a2_l1:
        h9.Fill(i)

h3=TH1F('#eta_{b} (h2>bb~ h1>aa)',"",100,-5,5)
for i in eta_b_l1:
        h3.Fill(i)
h7=TH1F('#eta_{b~} (h2>bb~ h1>aa)',"",100,-5,5)
for i in eta_bbar_l1:
        h7.Fill(i)

h4=TH1F('p_{T#gamma1} (h2>bb~ h1>aa)',"",100,-100,1200)
for i in pt_a_l1:
        h4.Fill(i)
h8=TH1F('p_{T#gamma2} (h2>bb~ h1>aa)',"",100,-100,1200)
for i in pt_a2_l1:
        h8.Fill(i)

h5=TH1F('p_{Tb} (h2>bb~ h1>aa)',"",100,-100,1200)
for i in pt_b_l1:
        h5.Fill(i)
h6=TH1F('p_{Tb~} (h2>bb~ h1>aa)',"",100,-200,1200)
for i in pt_bbar_l1:
        h6.Fill(i)

h10=TH1F('#phi_{#gamma1} (h2>bb~ h1>aa)',"",10,-4,4)
for i in phi_a_l1:
        h10.Fill(i)
h11=TH1F('#phi_{#gamma2} (h2>bb~ h1>aa)',"",10,-4,5)
for i in phi_a2_l1:
        h11.Fill(i)

h12=TH1F('#phi_{b} (h2>bb~ h1>aa)',"",10,-4,4)
for i in phi_b_l1:
        h12.Fill(i)
h13=TH1F('#phi_{b~} (h2>bb~ h1>aa)',"",10,-4,4)
for i in phi_bbar_l1:
        h13.Fill(i)
       

tree2 = ET.parse('gg_h01h2_bb~aa.lhe')
root2=tree2.getroot()

eta_b_l2=[]
eta_bbar_l2=[]
eta_a_l2=[]
eta_a2_l2=[]
phi_b_l2=[]
phi_bbar_l2=[]
phi_a_l2=[]
phi_a2_l2=[]
pt_b_l2=[]
pt_a_l2=[]
pt_bbar_l2=[]
pt_a2_l2=[]
m_1_H1_l2=[]
m_1_H2_l2=[]
m_1_H3_l2=[]
m_2_H2_l2=[]
m_2_H1_l2=[]
m_2_H3_l2=[]

gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(1)
gStyle.SetOptStat(0)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
gStyle.SetPadColor(1)

#legend=TLegend(.63,.69,.87,.89,"","#gamma #gamma")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","b b~")

cmsname=TLatex(0.15,1.85,"Trials")
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)
#lhefdata=LHEFData(float(root.attrib['version']))
#lhefdata=LHEFData(float(root.attrib['version']))

for child in root2:
 if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())
            
       a1_1_l2=[s for s in lines if s.split()[0]=='22']
       a1_l2=a1_1_l2[1::2]
       a2_l2=a1_1_l2[0::2]
       b1_l2=[s for s in lines if s.split()[0]=='5' and (s.split()[2]=='4' and lines[4].split()[0]=='25')]
       bbar1_l2=[s for s in lines if s.split()[0]=='-5'and (s.split()[2]=='4' and lines[4].split()[0]=='25')]
	      
       if a1_l2:
	       px3_l2=float (a1_l2[0].split()[6])
	       py3_l2=float (a1_l2[0].split()[7])
	       pz3_l2=float (a1_l2[0].split()[8])
	       e3_l2=float (a1_l2[0].split()[9])
      
       if a2_l2:
		       
	       px4_l2=float (a2_l2[0].split()[6])
	       py4_l2=float (a2_l2[0].split()[7])
	       pz4_l2=float (a2_l2[0].split()[8])
	       e4_l2=float (a2_l2[0].split()[9])

       if a1_l2 and a2_l2:	
	       
	       p3_l2=TLorentzVector(px3_l2,py3_l2,pz3_l2,e3_l2)
	       p4_l2=TLorentzVector(px4_l2,py4_l2,pz4_l2,e4_l2)
	       pb1_l2=p3_l2+p4_l2
	       m_1_H2_l2.append(pb1_l2.M())
	       eta_a_l2.append(p3_l2.Eta())
	       pt_a_l2.append(p3_l2.Pt())      
	       eta_a2_l2.append(p4_l2.Eta())
	       pt_a2_l2.append(p4_l2.Pt())
               phi_a_l2.append(p3_l2.Phi())
               phi_a2_l2.append(p4_l2.Phi())

       if b1_l2:
	       
	       px5_l2=float (b1_l2[0].split()[6])
	       py5_l2=float (b1_l2[0].split()[7])
	       pz5_l2=float (b1_l2[0].split()[8])
	       e5_l2=float (b1_l2[0].split()[9])
       if bbar1_l2:

	       px6_l2=float (bbar1_l2[0].split()[6])
	       py6_l2=float (bbar1_l2[0].split()[7])
	       pz6_l2=float (bbar1_l2[0].split()[8])
	       e6_l2=float (bbar1_l2[0].split()[9])

       if b1_l2 and bbar1_l2:

	       p5_l2=TLorentzVector(px5_l2,py5_l2,pz5_l2,e5_l2)
	       p6_l2=TLorentzVector(px6_l2,py6_l2,pz6_l2,e6_l2)
	       pb2_l2=p5_l2+p6_l2
	       m_1_H1_l2.append(pb2_l2.M())
    	       eta_b_l2.append(p5_l2.Eta())
	       eta_bbar_l2.append(p6_l2.Eta())
	       pt_b_l2.append(p5_l2.Pt())      
	       pt_bbar_l2.append(p6_l2.Pt())
               phi_b_l2.append(p5_l2.Phi())
               phi_bbar_l2.append(p6_l2.Phi())





h15=TH1F('M_{#gamma#gamma} (h1>bb~ h2>aa)',"",1000,0,1400)
for i in m_1_H2_l2:
        h15.Fill(i)
h16=TH1F('M_{bb~} (h1>bb~ h2>aa)',"",1000,0,1200)
for i in m_1_H1_l2:
        h16.Fill(i)

h17=TH1F('#eta_{#gamma1} (h1>bb~ h2>aa)',"",100,-5,5)
for i in eta_a_l2:
        h17.Fill(i)
h18=TH1F('#eta_{#gamma2} (h1>bb~ h2>aa)',"",100,-5,5)
for i in eta_a2_l2:
        h18.Fill(i)

h19=TH1F('#eta_{b} (h1>bb~ h2>aa)',"",100,-5,5)
for i in eta_b_l2:
        h19.Fill(i)
h20=TH1F('#eta_{b~} (h1>bb~ h2>aa)',"",100,-5,5)
for i in eta_bbar_l2:
        h20.Fill(i)

h21=TH1F('p_{T#gamma1} (h1>bb~ h2>aa)',"",100,-100,1200)
for i in pt_a_l2:
        h21.Fill(i)
h22=TH1F('p_{T#gamma2} (h1>bb~ h2>aa)',"",100,-100,1200)
for i in pt_a2_l2:
        h22.Fill(i)

h23=TH1F('p_{Tb} (h1>bb~ h2>aa)',"",100,-100,1200)
for i in pt_b_l2:
        h23.Fill(i)
h24=TH1F('p_{Tb~} (h1>bb~ h2>aa)',"",100,-200,1200)
for i in pt_bbar_l2:
        h24.Fill(i)

h25=TH1F('#phi_{#gamma1} (h1>bb~ h2>aa)',"",10,-4,4)
for i in phi_a_l2:
        h25.Fill(i)
h26=TH1F('#phi_{#gamma2} (h1>bb~ h2>aa)',"",10,-4,5)
for i in phi_a2_l2:
        h26.Fill(i)

h27=TH1F('#phi_{b} (h1>bb~ h2>aa)',"",10,-4,4)
for i in phi_b_l2:
        h27.Fill(i)
h28=TH1F('#phi_{b~} (h1>bb~ h2>aa)',"",10,-4,4)
for i in phi_bbar_l2:
        h28.Fill(i)

h1.SetXTitle("M_{#gamma#gamma} [GeV]")
h1.SetYTitle("Events")
h1.SetLineColor(6)
h1.GetMean()
h15.SetXTitle("M_{#gamma#gamma} [GeV]")
h15.SetYTitle("events")
h15.SetLineColor(4)
h15.GetMean()
h1.DrawNormalized("hist")
h15.DrawNormalized("hist&SAMES")
c.SaveAs("Mass_combine.png")
c.SaveAs("Mass_combine.root")


h14.SetXTitle("M_{bb~} [GeV]")
h14.SetYTitle("Events")
h14.SetLineColor(6)
h16.SetXTitle("M_{bb~} [GeV]")
h16.SetYTitle("events")
h16.SetLineColor(4)
h14.DrawNormalized("hist")
h16.DrawNormalized("hist&SAMES")
c.SaveAs("Mass_combine_bbar.png")
c.SaveAs("Mass_combine_bbar.root")

h2.SetXTitle("#eta_{#gamma}")
h2.SetYTitle("Events")
h2.SetLineColor(6)
h17.SetXTitle("#eta_{#gamma}")
h17.SetYTitle("events")
h17.SetLineColor(4)
h2.Draw("hist")
h17.Draw("hist&SAMES")
c.SaveAs("eta_combinegamma.png")
c.SaveAs("eta_combinegamma.root")

h9.SetXTitle("#eta_{#gamma}")
h9.SetYTitle("Events")
h9.SetLineColor(6)
h18.SetXTitle("#eta_{#gamma}")
h18.SetYTitle("events")
h18.SetLineColor(4)
h9.Draw("hist")
h18.Draw("hist&SAMES")
c.SaveAs("eta_combinegamma2.png")
c.SaveAs("eta_combinegamma2.root")

h3.SetXTitle("#eta_{b}")
h3.SetYTitle("Events")
h3.SetLineColor(6)
h19.SetXTitle("#eta_{b}")
h19.SetYTitle("events")
h19.SetLineColor(4)
h3.Draw("hist")
h19.Draw("hist&SAMES")
c.SaveAs("eta_combineb.png")
c.SaveAs("eta_combineb.root")

h7.SetXTitle("#eta_{b~}")
h7.SetYTitle("Events")
h7.SetLineColor(6)
h20.SetXTitle("#eta_{b~}")
h20.SetYTitle("events")
h20.SetLineColor(4)
h7.Draw("hist")
h20.Draw("hist&SAMES")
c.SaveAs("eta_combinebbar.png")
c.SaveAs("eta_combinebbar.root")

h4.SetXTitle("p_{T#gamma}")
h4.SetYTitle("events")
h4.SetLineColor(2)
h21.SetXTitle("p_{T#gamma}")
h21.SetYTitle("events")
h21.SetLineColor(4)
h4.Draw("hist")
h21.Draw("hist&sames")
c.SaveAs("Pt_combine_a.png")
c.SaveAs("Pt_combine_a.root")

h8.SetXTitle("p_{T#gamma}")
h8.SetYTitle("events")
h8.SetLineColor(2)
h22.SetXTitle("p_{T#gamma}")
h22.SetYTitle("events")
h22.SetLineColor(4)
h8.Draw("hist")
h22.Draw("hist&sames")
c.SaveAs("Pt_combine_a2.png")
c.SaveAs("Pt_combine_a2.root")

h5.SetXTitle("p_{Tb}")
h5.SetYTitle("events")
h5.SetLineColor(2)
h23.SetXTitle("p_{T#b}")
h23.SetYTitle("events")
h23.SetLineColor(4)
h5.Draw("hist")
h23.Draw("hist&sames")
c.SaveAs("pt_b_combine.png")
c.SaveAs("pt_b_combine.root")

h6.SetXTitle("p_{Tb~}")
h6.SetYTitle("events")
h6.SetLineColor(2)
h24.SetXTitle("p_{Tb~}")
h24.SetYTitle("events")
h24.SetLineColor(4)
h6.Draw("hist")
h24.Draw("hist&sames")
c.SaveAs("pt_bbar_combine.png")
c.SaveAs("pt_bbar_combine.root")


h10.SetXTitle("#phi_{#gamma}")
h10.SetYTitle("Events")
h10.SetLineColor(1)
h25.SetXTitle("#phi_{#gamma}")
h25.SetYTitle("Events")
h25.SetLineColor(3)
h10.Draw("hist")
h25.Draw("hist&sames")
c.SaveAs("Phi_acombined.png")
c.SaveAs("Phi_acombined.root")

h11.SetXTitle("#phi_{#gamma}")
h11.SetYTitle("Events")
h11.SetLineColor(1)
h26.SetXTitle("#phi_{#gamma}")
h26.SetYTitle("Events")
h26.SetLineColor(3)
h11.Draw("hist")
h26.Draw("hist&sames")
c.SaveAs("Phi_a2combined.png")
c.SaveAs("Phi_a2combined.root")


h12.SetXTitle("#phi_{b}")
h12.SetYTitle("events")
h12.SetLineColor(2)
h27.SetXTitle("#phi_{b}")
h27.SetYTitle("events")
h27.SetLineColor(4)
h12.Draw("hist")
h27.Draw("hist&sames")
c.SaveAs("Phi_combinedb.png")
c.SaveAs("Phi_combinedb.root")


h13.SetXTitle("#phi_{b~}")
h13.SetYTitle("events")
h13.SetLineColor(2)
h28.SetXTitle("#phi_{b~}")
h28.SetYTitle("events")
h28.SetLineColor(4)
h13.Draw("hist")
h28.Draw("hist&sames")
c.SaveAs("Phi_combinedbbar.png")
c.SaveAs("Phi_combinedbbar.root")
