import pdfplumber
import re
from pdfplumber.utils import extract_text

text_to_list = []

with pdfplumber.open("/home/pramuditorh/projects/cis-toc/CIS_Microsoft_Windows_Server_2012_R2_Benchmark_v2.4.0.pdf") as pdf:
    pages = pdf.pages
    for i in range(572, 600):
        if "Rationale:" and "(Scored)" not in pdf.pages[i].extract_text():
            continue
        else:
            extracted_text = pdf.pages[i].extract_text()
            l1_l2_index = extracted_text.find('(L')
            scored_index = extracted_text.find('(Scored)')
            rationale_index = extracted_text.find('Rationale:')
            audit_index = extracted_text.find('Audit:')
            rationale = extracted_text[rationale_index+12:audit_index]
            #rule_name = extracted_text[l1_l2_index:scored_index]
            print(f'{extracted_text[0:13]}')
            #print(f'---- {rule_name}')