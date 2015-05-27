#include "TROOT.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TH2F.h"
#include "TGraph.h"
#include "TF1.h"
#include "TLegend.h"
#include "TPolyLine.h"
#include "TPad.h"
#include "TLatex.h"

using namespace std;

void myStyle()
{
 gStyle->Reset("Default");
 gStyle->SetCanvasColor(0);
 gStyle->SetPadColor(0);
 gStyle->SetTitleFillColor(10);
 gStyle->SetCanvasBorderMode(0);
 gStyle->SetStatColor(0);
 gStyle->SetPadBorderMode(0);
 gStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
 gStyle->SetPadTickY(1);
 gStyle->SetFrameBorderMode(0);
 gStyle->SetPalette(1);
   
   //gStyle->SetOptStat(kFALSE);
 gStyle->SetOptStat(111110);
 gStyle->SetOptFit(1);
 gStyle->SetStatFont(42);
 gStyle->SetPadLeftMargin(0.13);
 gStyle->SetPadRightMargin(0.07);
//    gStyle->SetTitleFont(42);
//    gStyle->SetTitleFont(42, "XYZ");
//    gStyle->SetLabelFont(42, "XYZ");
 gStyle->SetStatY(.9);
}

void setTDRStyle() {
  TStyle *tdrStyle = new TStyle("tdrStyle","Style for P-TDR");

  // For the canvas:
  tdrStyle->SetCanvasBorderMode(0);
  tdrStyle->SetCanvasColor(kWhite);
  tdrStyle->SetCanvasDefH(600); //Height of canvas
  tdrStyle->SetCanvasDefW(600); //Width of canvas
  tdrStyle->SetCanvasDefX(0);   //POsition on screen
  tdrStyle->SetCanvasDefY(0);

  // For the Pad:
  tdrStyle->SetPadBorderMode(0);
  // tdrStyle->SetPadBorderSize(Width_t size = 1);
  tdrStyle->SetPadColor(kWhite);
  tdrStyle->SetPadGridX(false);
  tdrStyle->SetPadGridY(false);
  tdrStyle->SetGridColor(0);
  tdrStyle->SetGridStyle(3);
  tdrStyle->SetGridWidth(1);

  // For the frame:
  tdrStyle->SetFrameBorderMode(0);
  tdrStyle->SetFrameBorderSize(1);
  tdrStyle->SetFrameFillColor(0);
  tdrStyle->SetFrameFillStyle(0);
  tdrStyle->SetFrameLineColor(1);
  tdrStyle->SetFrameLineStyle(1);
  tdrStyle->SetFrameLineWidth(1);

  // For the histo:
  tdrStyle->SetHistFillColor(63);
  // tdrStyle->SetHistFillStyle(0);
  tdrStyle->SetHistLineColor(1);
  tdrStyle->SetHistLineStyle(0);
  tdrStyle->SetHistLineWidth(1);
  // tdrStyle->SetLegoInnerR(Float_t rad = 0.5);
  // tdrStyle->SetNumberContours(Int_t number = 20);

//  tdrStyle->SetEndErrorSize(0);
//   tdrStyle->SetErrorX(0.);
//  tdrStyle->SetErrorMarker(20);
  
  tdrStyle->SetMarkerStyle(20);

  //For the fit/function:
  tdrStyle->SetOptFit(1);
  tdrStyle->SetFitFormat("5.4g");
  tdrStyle->SetFuncColor(2);
  tdrStyle->SetFuncStyle(1);
  tdrStyle->SetFuncWidth(1);

  //For the date:
  tdrStyle->SetOptDate(0);
  // tdrStyle->SetDateX(Float_t x = 0.01);
  // tdrStyle->SetDateY(Float_t y = 0.01);

  // For the statistics box:
  tdrStyle->SetOptFile(0);
  tdrStyle->SetOptStat(0); // To display the mean and RMS:   SetOptStat("mr");
  tdrStyle->SetStatColor(kWhite);
  tdrStyle->SetStatFont(42);
  tdrStyle->SetStatFontSize(0.025);
  tdrStyle->SetStatTextColor(1);
  tdrStyle->SetStatFormat("6.4g");
  tdrStyle->SetStatBorderSize(1);
  tdrStyle->SetStatH(0.1);
  tdrStyle->SetStatW(0.15);
  // tdrStyle->SetStatStyle(Style_t style = 1001);
  // tdrStyle->SetStatX(Float_t x = 0);
  // tdrStyle->SetStatY(Float_t y = 0);

  // Margins:
  tdrStyle->SetPadTopMargin(0.05);
  tdrStyle->SetPadBottomMargin(0.13);
  tdrStyle->SetPadLeftMargin(0.13);
  tdrStyle->SetPadRightMargin(0.05);

  // For the Global title:

  //  tdrStyle->SetOptTitle(0);
  tdrStyle->SetTitleFont(42);
  tdrStyle->SetTitleColor(1);
  tdrStyle->SetTitleTextColor(1);
  tdrStyle->SetTitleFillColor(10);
  tdrStyle->SetTitleFontSize(0.05);
  // tdrStyle->SetTitleH(0); // Set the height of the title box
  // tdrStyle->SetTitleW(0); // Set the width of the title box
  // tdrStyle->SetTitleX(0); // Set the position of the title box
  // tdrStyle->SetTitleY(0.985); // Set the position of the title box
  // tdrStyle->SetTitleStyle(Style_t style = 1001);
  // tdrStyle->SetTitleBorderSize(2);

  // For the axis titles:

  tdrStyle->SetTitleColor(1, "XYZ");
  tdrStyle->SetTitleFont(42, "XYZ");
  tdrStyle->SetTitleSize(0.06, "XYZ");
  // tdrStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
  // tdrStyle->SetTitleYSize(Float_t size = 0.02);
  tdrStyle->SetTitleXOffset(0.9);
  tdrStyle->SetTitleYOffset(1.05);
  // tdrStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset

  // For the axis labels:

  tdrStyle->SetLabelColor(1, "XYZ");
  tdrStyle->SetLabelFont(42, "XYZ");
  tdrStyle->SetLabelOffset(0.007, "XYZ");
  tdrStyle->SetLabelSize(0.05, "XYZ");

  // For the axis:

  tdrStyle->SetAxisColor(1, "XYZ");
  tdrStyle->SetStripDecimals(kTRUE);
  tdrStyle->SetTickLength(0.03, "XYZ");
  tdrStyle->SetNdivisions(510, "XYZ");
  tdrStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
  tdrStyle->SetPadTickY(1);

  // Change for log plots:
  tdrStyle->SetOptLogx(0);
  tdrStyle->SetOptLogy(0);
  tdrStyle->SetOptLogz(0);

  // Postscript options:
  // tdrStyle->SetPaperSize(15.,15.);
  // tdrStyle->SetLineScalePS(Float_t scale = 3);
  // tdrStyle->SetLineStyleString(Int_t i, const char* text);
  // tdrStyle->SetHeaderPS(const char* header);
  // tdrStyle->SetTitlePS(const char* pstitle);

  // tdrStyle->SetBarOffset(Float_t baroff = 0.5);
  // tdrStyle->SetBarWidth(Float_t barwidth = 0.5);
  // tdrStyle->SetPaintTextFormat(const char* format = "g");
  // tdrStyle->SetPalette(Int_t ncolors = 0, Int_t* colors = 0);
  // tdrStyle->SetTimeOffset(Double_t toffset);
  // tdrStyle->SetHistMinimumZero(kTRUE);

  tdrStyle->cd();
}

void makePlots()
{
 // **********************************************
 // *            Input parameters                *
 // **********************************************
 // switch to include/exclude sytematics uncertainties
 bool systematics = true; // does nothing at the moment

 // total integrated luminosity (in pb-1)
 Double_t L_int = 2000;
 // relative uncertainty on the integrated luminosity (0.1 = 10% uncertainty)
 Double_t Sigma_L_int = 0.11;

 // array of signal efficiencies
 Double_t S_eff[4] = {.3353,.4574,.5276,.5763};
 // array of relative uncertainties on the signal efficiencies
 Double_t Sigma_S_eff[4] = {0.21, 0.21, 0.21,.21};

 // array of N_background for L_int
 Double_t N_bkg[4] = {.2724,.1786,.1098,.0753};
 // array of relative uncertainties on N_background (0.1 = 10%)
 Double_t Sigma_N_bkg[4] = {0.88, 0.88, 0.88, 0.88};

 // array of N_observed for L_int
 Double_t N_obs[4] = {0, 0, 0, 0};

 // array of LQ masses for calculation of upXS
Double_t mData[10] = {250, 350, 400, 450, 500, 550, 600, 650, 750, 850};
 // arrays of LQ masses for theoretical cross section
 //Double_t mTh[9] = {100, 150, 200, 250, 300, 350, 400,450,500};
 Double_t mTh[15] = { 150, 200, 250, 300, 350, 400,450,500,550,600,650,700,750,800,850};
 // array of theoretical cross-sections for different leptoquark masses
 //Double_t xsTh[9] = {386/2.0, 53.3/2.0, 11.9/2.0, 3.47/2.0, 1.21/2.0, 0.477/2.0, .205/2.0,.0949/2.0,.0463/2.0};
 Double_t xsTh[15] = { 53.3/2.0, 11.9/2.0, 3.47/2.0, 1.21/2.0, 0.477/2.0, .205/2.0,.0949/2.0,.0463/2.0,.0236/2.0,.0124/2.0,.00676/2.0,.00377/2.0,.00215/2.0,.00124/2.0,.000732/2.0};
  
 // filename for the final plot (NB: changing the name extension changes the file format)
 string fileName2 = "BR_Sigma_MuNu_2000.pdf";
 string fileName3 = "BR_Sigma_MuNu_2000.png";
  
 // axes labels for the final plot
 string title = ";M_{LQ} (GeV);2#beta(1-#beta)#times#sigma (pb)";

 // integrated luminosity
 string lint = "2.0 fb^{-1}";

 // region excluded by Tevatron limits
 Double_t x_shaded[5] = {250,270,270,250,250};// CHANGED FOR LQ2
 Double_t y_shaded[5] = {0.0001,0.0001,500,500,0.0001};// CHANGED FOR LQ2


 Double_t x_pdf[28] = {	150		,	200		,	250	,	300		,	350		,	400	,  450 	 ,  500, 600,	650,	700,	750,	800,	850,	850,	800,	750,	700,	650,	600  , 500  , 450 	,	400	,	350		,	300		,	250	, 200		, 150		};
 Double_t y_pdf[28] = {	61.4	/2.0,	13.7	/2.0,	4.1	/2.0,	1.43	/2.0, 0.57	/2.0,	.25	/2.0, .1167	 /2.0,	.058/2.0,0.01561/2.0,	0.00866/2.0,	0.00491/2.0,	0.00284/2.0,	0.001677/2.0,	0.001008/2.0,	0.000456/2.0,	0.000803/2.0,	0.00144/2.0,	0.00263/2.0,	0.00486/2.0,	0.00919 /2.0, .034	/2.0,	.072	/2.0, .16	/2.0,	0.38	/2.0, 0.98	/2.0, 2.9	/2.0, 10.0	/2.0, 45.2	/2.0};
 
Double_t x_shademasses[20]={250, 350, 400, 450, 500, 550, 600, 650, 750, 850, 850, 750, 650, 600, 550, 500, 450, 400, 350, 250};


// Systematics Cut Off at 600

Double_t y_1sigma[20]={1.14899278216 , 0.0687352374177 , 0.0258398107906 , 0.015449767247 , 0.00914124533312 , 0.00621567471013 , 0.00546195052894 , 0.00407567753763 , 0.00347540025525 , 0.00308450273564 , 0.00955128283927 , 0.0106299735622 , 0.0139039523941 , 0.0171257452864 , 0.0184917806412 , 0.0282538105102 , 0.0708682230741 , 0.124152618006 , 0.283287214906 , 2.25420682246 }; 


Double_t y_2sigma[20]={0.829890996844 , 0.0376244974351 , 0.015078850271 , 0.00959896727954 , 0.0063337822068 , 0.00478518232388 , 0.00409130250856 , 0.00395009274597 , 0.00337668268882 , 0.00299725143289 , 0.0244358217301 , 0.0245225448804 , 0.0254186961729 , 0.0336608185921 , 0.032102202093 , 0.0571049035534 , 0.156232197987 , 0.278864377629 , 0.541098968521 , 3.19380895838 }; 


 //// **********************************************
 // *  Don't change anything below this point!   *
 // **********************************************




  // turn on/off batch mode
 gROOT->SetBatch(kTRUE);

 Int_t size = sizeof(S_eff)/sizeof(*S_eff);


////// MEDIAN


Double_t xsUp_expected[10] = {1.60250358555 , 0.145105947608 , 0.0538673397939 , 0.0335565022186 , 0.0145697224703 , 0.0109544141558 , 0.00865524208227 , 0.00712004343568 , 0.00607012584336 , 0.00539464885416 }; // Sys Cutoff 600


Double_t xsUp_observed[10] = {1.467832555,0.155123262,0.076475045,0.050261064,0.031306208,0.019967488,0.01695979,0.0139276618,0.0102408737,0.008976516};// lnN stats


 // set ROOT style
//  myStyle();
 setTDRStyle();
 gStyle->SetPadLeftMargin(0.14);
 gROOT->ForceStyle();
 
 TCanvas *c = new TCanvas("c","",800,800);
 c->cd();
 
 TH2F *bg = new TH2F("bg",title.c_str(), 500, 250., 850., 500., 0.0001, 500.);
 bg->SetStats(kFALSE);
 bg->SetTitleOffset(1.,"X");
 bg->SetTitleOffset(1.15,"Y");
 
 bg->Draw();

 TPolyLine *pl = new TPolyLine(5,x_shaded,y_shaded,"F");
//  pl->SetFillStyle(3001);
 pl->SetLineColor(0);
 pl->SetFillColor(kGray);
 pl->SetLineColor(kGray);   // CHANGED FOR LQ2
 pl->Draw();

 TGraph *exshade1 = new TGraph(20,x_shademasses,y_1sigma);
 exshade1->SetFillColor(kCyan);
 //exshade1->SetFillStyle(3144);

 TGraph *exshade2 = new TGraph(20,x_shademasses,y_2sigma);
 exshade2->SetFillColor(kCyan-5);
 //exshade2->SetFillStyle(3005);

 exshade2->Draw("F");
 exshade1->Draw("F");

 gPad->RedrawAxis();


 TGraph *grshade = new TGraph(28,x_pdf,y_pdf);
 grshade->SetFillColor(kGreen);
 //grshade->SetFillStyle(2);
 grshade->Draw("f");



 // set ROOT style
//  myStyle();
 setTDRStyle();
 gStyle->SetPadLeftMargin(0.14);
 gROOT->ForceStyle();

 TGraph *xsTh_vs_m = new TGraph(16, mTh, xsTh);
 xsTh_vs_m->SetLineWidth(2);
 xsTh_vs_m->SetLineColor(kRed);
 xsTh_vs_m->SetFillColor(kGreen);
 xsTh_vs_m->SetMarkerSize(1.);
 xsTh_vs_m->SetMarkerStyle(22);
 xsTh_vs_m->SetMarkerColor(kRed);
 xsTh_vs_m->Draw("C");

 TGraph *xsData_vs_m_expected = new TGraph(10, mData, xsUp_expected);
 xsData_vs_m_expected->SetMarkerStyle(23);
 xsData_vs_m_expected->SetMarkerColor(kBlue);
 xsData_vs_m_expected->SetLineColor(kBlue);
 xsData_vs_m_expected->SetLineWidth(2);
 xsData_vs_m_expected->SetLineStyle(2);
 xsData_vs_m_expected->SetMarkerSize(1.5);
 xsData_vs_m_expected->Draw("CP");

 TGraph *xsData_vs_m_observed = new TGraph(10, mData, xsUp_observed);
 xsData_vs_m_observed->SetMarkerStyle(22);
 xsData_vs_m_observed->SetMarkerColor(kBlack);
 xsData_vs_m_observed->SetLineColor(kBlack);
 xsData_vs_m_observed->SetLineWidth(2);
 xsData_vs_m_observed->SetLineStyle(1);
 xsData_vs_m_observed->SetMarkerSize(1.5);
 xsData_vs_m_observed->Draw("CP");
 
 float mtest = 250.0;
 float xrat = 0.0;
 float orat = 0.0;
 while (mtest<850){
	 xrat = xsData_vs_m_expected->Eval(mtest)/xsTh_vs_m->Eval(mtest);
	 orat = xsData_vs_m_observed->Eval(mtest)/xsTh_vs_m->Eval(mtest);
	 std::cout<<mtest<<"   "<<xrat<<"    "<<orat<<std::endl;
	 mtest = mtest + 1.0;

	}
 
 TLegend *legend = new TLegend(.37,.65,.94,.92);
 legend->SetBorderSize(1);
 legend->SetFillColor(0);
 //legend->SetFillStyle(0);
 legend->SetTextFont(42);
 legend->SetMargin(0.15);
 legend->SetHeader("LQ #bar{LQ} #rightarrow #mu q #nu q");
 legend->AddEntry(pl,"D#oslash exclusion (1 fb^{-1}, #beta=1/2)","f");
 legend->AddEntry(xsTh_vs_m,"2#beta(1-#beta)#times #sigma_{theory} with theory unc., (#beta=1/2)","lf");
 legend->AddEntry(xsData_vs_m_expected, "Expected 95% C.L. upper limit","lp");
 legend->AddEntry(xsData_vs_m_observed, "Observed 95% C.L. upper limit","lp");
 legend->Draw();

 TLatex l1;
 l1.SetTextAlign(12);
 l1.SetTextSize(0.045);
 l1.SetTextFont(42);
 l1.SetNDC();
 l1.DrawLatex(0.25,0.29,"CMS Preliminary");
 l1.DrawLatex(0.25,0.23,lint.c_str());

//  TLatex l2;
//  l2.SetTextAlign(12);
//  l2.SetTextSize(0.037);
//  l2.SetTextFont(42);
//  l2.SetNDC();
//  l2.DrawLatex(0.4,0.485,"EXO-10-005 scaled to #sqrt{s} = 7 TeV");

 c->SetGridx();
 c->SetGridy();


 c->SetLogy();
 c->SaveAs((fileName2).c_str());
 c->SaveAs((fileName3).c_str());

 delete pl;
 delete xsTh_vs_m;
 delete bg;
 delete c;
}

