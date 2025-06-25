import requests
import json
import time
import pandas as pd
from datetime import datetime
import os

#List of genes associated with rheumatoid arthiritis based on literature search - extract all data associated with them
gene_list_RA = [ # HLA Genes (Strongest Overall Risk)
    





    
    "HLA-DRB1",
    "HLA-B",
    "HLA-MICA",
    
    # Major Non-HLA Risk Genes
    "PTPN22",  # Second strongest association after HLA
    "STAT4",   # Signal transducer and activator of transcription 4
    
    # Immune System Genes
    "IL6ST",   # Interleukin 6 signal transducer
    "IRF5",    # Interferon regulatory factor 5
    "CCR6",    # C-C motif chemokine receptor 6
    "TRAF1",   # TNF receptor associated factor 1
    "CTLA4",   # Cytotoxic T-lymphocyte associated protein 4
    "FCGR3A",  # Fc gamma receptor IIIA
    "FCGR2B",  # Fc gamma receptor IIb (B cell specific)
    "IL2RA",   # Interleukin 2 receptor subunit alpha
    "IL2RB",   # Interleukin 2 receptor subunit beta
    "CCL21",   # C-C motif chemokine ligand 21
    "CD40",    # CD40 molecule
    "IL23R",   # Interleukin 23 receptor
    "PADI4",   # Peptidyl arginine deiminase 4 (stronger in Asian populations)
    
    # TNF Pathway Genes
    "C5",      # Complement component 5 (TRAF1-C5 region)
    "TNIP2",   # TNFAIP3 interacting protein 2
    "TNFRSF11A", # TNF receptor superfamily member 11a
    "TNFAIP3", # TNF alpha induced protein 3
    
    # Novel Loci from Recent Studies
    "SPRED2",  # Sprouty related EVH1 domain containing 2
    "RBPJ",    # Recombination signal binding protein
    "PXK",     # PX domain containing serine/threonine kinase
    "AFF3",    # AF4/FMR2 family member 3
    "WISP1",   # WNT1 inducible signaling pathway protein 1
    "LEF1",    # Lymphoid enhancer binding factor 1
    
    # Additional Confirmed Risk Loci
    "CD226",   # CD226 molecule
    "CDK6",    # Cyclin dependent kinase 6
    "MBP",     # Myelin basic protein
    "BLK",     # BLK proto-oncogene
    "REL",     # REL proto-oncogene
    "KIF5A",   # Kinesin family member 5A
    "PRKCQ",   # Protein kinase C theta
    "MMEL1",   # Membrane metalloendopeptidase like 1
    
    # Asian Population-Specific
    "CEP57",   # Centrosomal protein 57
    "C5orf30", # Chromosome 5 open reading frame 30
    "GATA3",   # GATA binding protein 3
    "VPS37C",  # VPS37C subunit of ESCRT-I
    "EOMES",   # Eomesodermin
    "LINC00824", # Long intergenic non-protein coding RNA 824
    
    # TWAS Identified Genes
    "CRIPAK",  # Cysteine rich PAK1 interactor
    "MUT",     # Methylmalonyl-CoA mutase
    "FOXRED1", # FAD dependent oxidoreductase domain containing 1
    "EBPL",    # Emopamil binding protein like
    
    # Newly Identified Susceptibility Loci
    "IL12RB2", # Interleukin 12 receptor subunit beta 2
    "PLCL1",   # Phospholipase C like 1 (BOLL-PLCL1 region)
    "BOLL",    # Boule homolog
    "CCR2",    # C-C motif chemokine receptor 2
    "TCF7",    # Transcription factor 7
    "IQGAP1",  # IQ motif containing GTPase activating protein 1
    
    # Shared Autoimmune Disease Loci
    "IL2",     # Interleukin 2 (IL2/IL21 region)
    "IL21",    # Interleukin 21
    "ZEB1",    # Zinc finger E-box binding homeobox 1
    "SH2B3",   # SH2B adaptor protein 3
    "IKZF3",   # IKAROS family zinc finger 3
    "UBASH3A", # Ubiquitin associated and SH3 domain containing A
    
    # Additional Cytokine and Immune Genes
    "TYK2",    # Tyrosine kinase 2
    "JAK2",    # Janus kinase 2
    "IFNG",    # Interferon gamma
    "TNF",     # Tumor necrosis factor
    "NFKB1",   # Nuclear factor kappa B subunit 1
    "CD2",     # CD2 molecule
    "CD28",    # CD28 molecule
    
    # Complement and Coagulation
    "CFH",     # Complement factor H
    "C4A",     # Complement C4A
    "C4B",     # Complement C4B
    
    # Transcription Factors and Regulators
    "RUNX1",   # RUNX family transcription factor 1
    "ETS1",    # ETS proto-oncogene 1
    "BACH2",   # BTB domain and CNC homolog 2
    "NFKBIE",  # NFKB inhibitor epsilon
    
    # Signaling Pathways
    "RASGRP1", # RAS guanyl releasing protein 1
    "TAGAP",   # T cell activation RhoGTPase activating protein
    "PTPRC",   # Protein tyrosine phosphatase receptor type C
    "LYN",     # LYN proto-oncogene
    "CARD11",  # Caspase recruitment domain family member 11
    
    # Adhesion and Migration
    "ICAM1",   # Intercellular adhesion molecule 1
    "VCAM1",   # Vascular cell adhesion molecule 1
    "ITGB3",   # Integrin subunit beta 3
    "ITGA4",   # Integrin subunit alpha 4
    
    # Matrix and Structural
    "COL1A2",  # Collagen type I alpha 2 chain
    "COL3A1",  # Collagen type III alpha 1 chain
    "COL6A1",  # Collagen type VI alpha 1 chain
    "TGFB1",   # Transforming growth factor beta 1
    
    # Metabolic and Enzymatic
    "PSMC3",   # Proteasome 26S subunit, ATPase 3
    "PSMB8",   # Proteasome subunit beta 8
    "CYP26B1", # Cytochrome P450 family 26 subfamily B member 1
    "FGF18",   # Fibroblast growth factor 18
    "FGFR3",   # Fibroblast growth factor receptor 3
    
    # Additional Novel Candidates
    "ANKRD55", # Ankyrin repeat domain 55
    "FAM177A", # Family with sequence similarity 177 member A
    "PLCL2",   # Phospholipase C like 2
    "PSORS1C1", # Psoriasis susceptibility 1 candidate 1
    "RP11-718O11.1", # Non-coding RNA
    "ARL15",   # ADP ribosylation factor like GTPase 15
    "GPS3",    # Glutathione peroxidase 3 (novel hub gene)
    
    # Epigenetic Regulators
    "HDAC1",   # Histone deacetylase 1
    "HDAC4",   # Histone deacetylase 4
    "TET2",    # Tet methylcytosine dioxygenase 2
    "DNMT1",   # DNA methyltransferase 1
    
    # Long Non-coding RNAs
    "NEAT1",   # Nuclear paraspeckle assembly transcript 1
    "MALAT1",  # Metastasis associated lung adenocarcinoma transcript 1
    "HOTAIR",  # HOX transcript antisense RNA
    
    # MicroRNA Host Genes
    "MIR146A", # MicroRNA 146a
    "MIR155HG", # MIR155 host gene
    "MIR21",   # MicroRNA 21
    
    # Additional Risk Loci from Recent Studies
    "COG6",    # Component of oligomeric golgi complex 6
    "IKZF1",   # IKAROS family zinc finger 1
    "IRF4",    # Interferon regulatory factor 4
    "IRF8",    # Interferon regulatory factor 8
    "BANK1",   # B cell scaffold protein with ankyrin repeats 1
    "BLK",     # BLK proto-oncogene (confirmed)
    "LY9",     # Lymphocyte antigen 9
    "TNFSF4",  # TNF superfamily member 4
    "IRAK1",   # Interleukin 1 receptor associated kinase 1
    "MECP2",   # Methyl-CpG binding protein 2
    "PLD4",    # Phospholipase D family member 4
    "ARID5B",  # AT-rich interaction domain 5B
    "MST1",    # Macrophage stimulating 1
    "YDJC"     # YdjC chitooligosaccharide deacetylase homolog
]

# class SimplePharmGKBExtractor:
#     """
#     Simple script to extract all rheumatoid arthritis data from PharmGKB API.
#     """
    
#     def __init__(self):
#         self.base_url = "https://api.pharmgkb.org/v1"
#         self.headers = {
#             'Accept': 'application/json',
#             'User-Agent': 'PharmGKB-RA-Extractor/1.0'
#         }
#         self.disease_term = "rheumatoid arthritis"
        
#         # Rate limiting - PharmGKB allows max 2 requests per second
#         self.rate_limit_delay = 0.6
        
#         # Storage for results
#         self.results = {
#             'clinical_annotations': [],
#             'variant_annotations': [],
#             'drug_labels': [],
#             'guidelines': [],
#             'pathways': [],
#             'genes': [],
#             'chemicals': [],
#             'variants': []
#         }
    
#     def make_request(self, endpoint, params=None):
#         """Make a rate-limited request to PharmGKB API."""
#         url = f"{self.base_url}/{endpoint}"
        
#         try:
#             print(f"Requesting: {url} with params: {params}")
#             time.sleep(self.rate_limit_delay)  # Rate limiting
            
#             response = requests.get(url, headers=self.headers, params=params, timeout=30)
            
#             if response.status_code == 200:
#                 data = response.json()
#                 print(f"✅ Success: Found data")
#                 return data
#             elif response.status_code == 429:
#                 print("⚠️  Rate limit hit, waiting 5 seconds...")
#                 time.sleep(5)
#                 return self.make_request(endpoint, params)
#             else:
#                 print(f"❌ Failed: {response.status_code}")
#                 return None
                
#         except Exception as e:
#             print(f"❌ Error: {str(e)}")
#             return None
    
#     def extract_data_from_response(self, response):
#         """Extract data array from API response."""
#         if not response:
#             return []
        
#         if isinstance(response, dict):
#             # Try different possible data fields
#             if 'data' in response:
#                 return response['data'] if isinstance(response['data'], list) else [response['data']]
#             elif 'results' in response:
#                 return response['results'] if isinstance(response['results'], list) else [response['results']]
#             else:
#                 return [response]
#         elif isinstance(response, list):
#             return response
#         else:
#             return []
    
#     def search_clinical_annotations(self):
#         """Search for clinical annotations related to rheumatoid arthritis."""
#         print("\n🔍 Searching Clinical Annotations...")
        
#         # Try different endpoint patterns and parameters
#         search_attempts = [
#             ('data/clinicalAnnotation', {'q': self.disease_term}),
#             ('data/clinicalAnnotation', {'search': self.disease_term}),
#             ('data/clinicalAnnotation', {'disease': self.disease_term}),
#             ('data/clinicalAnnotation', {'indication': self.disease_term}),
#             ('clinicalAnnotation', {'q': self.disease_term}),
#         ]
        
#         for endpoint, params in search_attempts:
#             response = self.make_request(endpoint, params)
#             if response:
#                 data = self.extract_data_from_response(response)
#                 if data:
#                     self.results['clinical_annotations'].extend(data)
#                     print(f"Found {len(data)} clinical annotations")
#                     break
        
#         print(f"Total clinical annotations: {len(self.results['clinical_annotations'])}")
    
#     def search_variant_annotations(self):
#         """Search for variant annotations related to rheumatoid arthritis."""
#         print("\n🔍 Searching Variant Annotations...")
        
#         search_attempts = [
#             ('data/variantAnnotation', {'q': self.disease_term}),
#             ('data/variantAnnotation', {'disease': self.disease_term}),
#             ('data/variantAnnotation', {'phenotype': self.disease_term}),
#             ('variantAnnotation', {'q': self.disease_term}),
#         ]
        
#         for endpoint, params in search_attempts:
#             response = self.make_request(endpoint, params)
#             if response:
#                 data = self.extract_data_from_response(response)
#                 if data:
#                     self.results['variant_annotations'].extend(data)
#                     print(f"Found {len(data)} variant annotations")
#                     break
        
#         print(f"Total variant annotations: {len(self.results['variant_annotations'])}")
    
#     def search_drug_labels(self):
#         """Search for drug labels related to rheumatoid arthritis."""
#         print("\n🔍 Searching Drug Labels...")
        
#         search_attempts = [
#             ('data/drugLabel', {'q': self.disease_term}),
#             ('data/drugLabel', {'indication': self.disease_term}),
#             ('drugLabel', {'q': self.disease_term}),
#         ]
        
#         for endpoint, params in search_attempts:
#             response = self.make_request(endpoint, params)
#             if response:
#                 data = self.extract_data_from_response(response)
#                 if data:
#                     self.results['drug_labels'].extend(data)
#                     print(f"Found {len(data)} drug labels")
#                     break
        
#         print(f"Total drug labels: {len(self.results['drug_labels'])}")
    
#     def search_guidelines(self):
#         """Search for dosing guidelines related to rheumatoid arthritis."""
#         print("\n🔍 Searching Guidelines...")
        
#         search_attempts = [
#             ('data/guideline', {'q': self.disease_term}),
#             ('data/guideline', {'disease': self.disease_term}),
#             ('guideline', {'q': self.disease_term}),
#         ]
        
#         for endpoint, params in search_attempts:
#             response = self.make_request(endpoint, params)
#             if response:
#                 data = self.extract_data_from_response(response)
#                 if data:
#                     self.results['guidelines'].extend(data)
#                     print(f"Found {len(data)} guidelines")
#                     break
        
#         print(f"Total guidelines: {len(self.results['guidelines'])}")
    
#     def search_pathways(self):
#         """Search for pathways related to rheumatoid arthritis."""
#         print("\n🔍 Searching Pathways...")
        
#         search_attempts = [
#             ('data/pathway', {'q': self.disease_term}),
#             ('data/pathway', {'disease': self.disease_term}),
#             ('pathway', {'q': self.disease_term}),
#         ]
        
#         for endpoint, params in search_attempts:
#             response = self.make_request(endpoint, params)
#             if response:
#                 data = self.extract_data_from_response(response)
#                 if data:
#                     self.results['pathways'].extend(data)
#                     print(f"Found {len(data)} pathways")
#                     break
        
#         print(f"Total pathways: {len(self.results['pathways'])}")
    
#     def search_by_known_ra_drugs(self):
#         """Search using known rheumatoid arthritis drugs."""
#         print("\n🔍 Searching by Known RA Drugs...")
        
#         ra_drugs = [
#             'methotrexate', 'adalimumab', 'etanercept', 'infliximab',
#             'rituximab', 'tocilizumab', 'tofacitinib', 'sulfasalazine'
#         ]
        
#         for drug in ra_drugs:
#             print(f"  Searching for drug: {drug}")
            
#             # Search clinical annotations for this drug
#             response = self.make_request('data/clinicalAnnotation', {'drug': drug})
#             if response:
#                 data = self.extract_data_from_response(response)
#                 self.results['clinical_annotations'].extend(data)
#                 print(f"    Found {len(data)} clinical annotations")
            
#             # Search variant annotations for this drug
#             response = self.make_request('data/variantAnnotation', {'drug': drug})
#             if response:
#                 data = self.extract_data_from_response(response)
#                 self.results['variant_annotations'].extend(data)
#                 print(f"    Found {len(data)} variant annotations")
            
#             # Search drug labels
#             response = self.make_request('data/drugLabel', {'drug': drug})
#             if response:
#                 data = self.extract_data_from_response(response)
#                 self.results['drug_labels'].extend(data)
#                 print(f"    Found {len(data)} drug labels")
            
#             # Get chemical information
#             response = self.make_request('data/chemical', {'name': drug})
#             if response:
#                 data = self.extract_data_from_response(response)
#                 self.results['chemicals'].extend(data)
#                 print(f"    Found {len(data)} chemical records")
    
#     def search_by_known_ra_genes(self):
#         """Search using known rheumatoid arthritis genes."""
#         print("\n🔍 Searching by Known RA Genes...")
        
#         ra_genes = [
#             'MTHFR', 'TNF', 'IL6', 'PTPN22', 'STAT4', 'RFC1', 'SLC19A1',
#             'ABCB1', 'HLA-DRB1', 'DHFR', 'FPGS', 'GGH'
#         ]
        
#         for gene in ra_genes:
#             print(f"  Searching for gene: {gene}")
            
#             # Search variant annotations for this gene
#             response = self.make_request('data/variantAnnotation', {'gene': gene})
#             if response:
#                 data = self.extract_data_from_response(response)
#                 self.results['variant_annotations'].extend(data)
#                 print(f"    Found {len(data)} variant annotations")
            
#             # Get gene information
#             response = self.make_request('data/gene', {'symbol': gene})
#             if response:
#                 data = self.extract_data_from_response(response)
#                 self.results['genes'].extend(data)
#                 print(f"    Found {len(data)} gene records")
            
#             # Search for variants
#             response = self.make_request('data/variant', {'gene': gene})
#             if response:
#                 data = self.extract_data_from_response(response)
#                 self.results['variants'].extend(data)
#                 print(f"    Found {len(data)} variants")
    
#     def get_all_data(self):
#         """Get all available data from different endpoints."""
#         print("\n🔍 Getting All Available Data...")
        
#         # Try to get all data from each endpoint
#         endpoints = [
#             'data/clinicalAnnotation',
#             'data/variantAnnotation', 
#             'data/drugLabel',
#             'data/guideline',
#             'data/pathway',
#             'data/gene',
#             'data/chemical',
#             'data/variant'
#         ]
        
#         for endpoint in endpoints:
#             print(f"  Getting all data from: {endpoint}")
#             response = self.make_request(endpoint, {'limit': 1000})
#             if response:
#                 data = self.extract_data_from_response(response)
#                 endpoint_name = endpoint.split('/')[-1]
#                 if endpoint_name in self.results:
#                     # Filter for rheumatoid arthritis related data
#                     ra_related = self.filter_ra_related(data)
#                     self.results[endpoint_name].extend(ra_related)
#                     print(f"    Found {len(ra_related)} RA-related records out of {len(data)} total")
    
#     def filter_ra_related(self, data):
#         """Filter data to only include rheumatoid arthritis related records."""
#         ra_keywords = [
#             'rheumatoid', 'arthritis', 'RA', 'inflammatory arthritis',
#             'methotrexate', 'adalimumab', 'etanercept', 'TNF', 'MTX'
#         ]
        
#         filtered = []
#         for record in data:
#             if isinstance(record, dict):
#                 # Convert record to string and check for keywords
#                 record_str = json.dumps(record).lower()
#                 if any(keyword.lower() in record_str for keyword in ra_keywords):
#                     filtered.append(record)
        
#         return filtered
    
#     def remove_duplicates(self):
#         """Remove duplicate records from results."""
#         print("\n🔄 Removing duplicates...")
        
#         for data_type in self.results:
#             original_count = len(self.results[data_type])
            
#             # Remove duplicates based on string representation
#             unique_data = []
#             seen = set()
            
#             for item in self.results[data_type]:
#                 item_str = json.dumps(item, sort_keys=True) if isinstance(item, dict) else str(item)
#                 if item_str not in seen:
#                     seen.add(item_str)
#                     unique_data.append(item)
            
#             self.results[data_type] = unique_data
#             duplicate_count = original_count - len(unique_data)
            
#             if duplicate_count > 0:
#                 print(f"  {data_type}: Removed {duplicate_count} duplicates ({len(unique_data)} unique)")
#             else:
#                 print(f"  {data_type}: {len(unique_data)} records (no duplicates)")
    
#     def save_results(self):
#         """Save results to files."""
#         print("\n💾 Saving results...")
        
#         # Create output directory
#         output_dir = "pharmgkb_rheumatoid_arthritis_data"
#         os.makedirs(output_dir, exist_ok=True)
        
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
#         # Save complete results as JSON
#         json_file = f"{output_dir}/pharmgkb_ra_complete_{timestamp}.json"
#         with open(json_file, 'w') as f:
#             json.dump(self.results, f, indent=2, default=str)
#         print(f"✅ Saved complete data: {json_file}")
        
#         # Save each data type as separate CSV
#         total_records = 0
#         for data_type, records in self.results.items():
#             if records:
#                 try:
#                     df = pd.json_normalize(records)
#                     csv_file = f"{output_dir}/pharmgkb_ra_{data_type}_{timestamp}.csv"
#                     df.to_csv(csv_file, index=False)
#                     total_records += len(records)
#                     print(f"✅ Saved {data_type}: {len(records)} records → {csv_file}")
#                 except Exception as e:
#                     print(f"❌ Error saving {data_type}: {str(e)}")
        
#         # Save summary
#         summary = {
#             'disease': 'rheumatoid arthritis',
#             'extraction_date': datetime.now().isoformat(),
#             'total_records': total_records,
#             'data_types': {k: len(v) for k, v in self.results.items()}
#         }
        
#         summary_file = f"{output_dir}/extraction_summary_{timestamp}.json"
#         with open(summary_file, 'w') as f:
#             json.dump(summary, f, indent=2)
        
#         print(f"\n📊 EXTRACTION SUMMARY:")
#         print(f"   Total Records: {total_records}")
#         for data_type, count in summary['data_types'].items():
#             print(f"   {data_type}: {count}")
#         print(f"   Output Directory: {output_dir}")
        
#         return summary
    
#     def run_extraction(self):
#         """Run the complete extraction process."""
#         print("🚀 Starting PharmGKB Rheumatoid Arthritis Data Extraction")
#         print("="*60)
        
#         try:
#             # Method 1: Search by disease name
#             self.search_clinical_annotations()
#             self.search_variant_annotations()
#             self.search_drug_labels()
#             self.search_guidelines()
#             self.search_pathways()
            
#             # Method 2: Search by known RA drugs
#             self.search_by_known_ra_drugs()
            
#             # Method 3: Search by known RA genes
#             self.search_by_known_ra_genes()
            
#             # Method 4: Get all data and filter
#             # self.get_all_data()  # Uncomment if you want to try this approach
            
#             # Clean up data
#             self.remove_duplicates()
            
#             # Save results
#             summary = self.save_results()
            
#             print("\n🎉 EXTRACTION COMPLETED SUCCESSFULLY!")
#             print("="*60)
            
#             return self.results, summary
            
#         except Exception as e:
#             print(f"\n❌ EXTRACTION FAILED: {str(e)}")
#             raise


# def main():
#     """Main function to run the extraction."""
#     extractor = SimplePharmGKBExtractor()
#     results, summary = extractor.run_extraction()
    
#     print(f"\nExtraction complete! Found {summary['total_records']} total records.")
#     print("Check the 'pharmgkb_rheumatoid_arthritis_data' directory for output files.")
    
#     return results


# if __name__ == "__main__":
#     # Run the extraction
#     main()