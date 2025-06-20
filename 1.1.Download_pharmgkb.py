import requests
import json
import time
import pandas as pd
from datetime import datetime
import os

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