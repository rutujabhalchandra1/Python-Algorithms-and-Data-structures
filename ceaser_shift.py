import re
output_str = 'NYRK UF PFL DVRE PFL\'MV EVMVI SVVE KF RCGYR TVEKRLIZ? FY, WFI YVRMVE\'J JRBV, DREBZEU, ' \
             'ZK\'J FECP WFLI CZXYK PVRIJ RNRP, PFL BEFN. Z\'D JFIIP, SLK ZW PFL TRE\'K SV SFKYVIVU KF KRBV' \
             ' RE ZEKVIVJK ZE CFTRC RWWRZIJ, KYRK\'J PFLI FNE CFFBFLK. VEVIXZJV KYV UVDFCZKZFE SVRD.'


new_str = re.sub('[?.\',]', '', output_str)
print(new_str)

#final_str = new_str.replace(" ", "")
#print(final_str)


for i in new_str:
    for j in range(0,5):
            print(str[str.index(i) + j])