import requests
import json
import time
from datetime import datetime

# List of genes associated with rheumatoid arthritis based on literature search
gene_list_RA = [
    # HLA Genes (Strongest Overall Risk)
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
    "LY9",     # Lymphocyte antigen 9
    "TNFSF4",  # TNF superfamily member 4
    "IRAK1",   # Interleukin 1 receptor associated kinase 1
    "MECP2",   # Methyl-CpG binding protein 2
    "PLD4",    # Phospholipase D family member 4
    "ARID5B",  # AT-rich interaction domain 5B
    "MST1",    # Macrophage stimulating 1
    "YDJC"     # YdjC chitooligosaccharide deacetylase homolog
]

class PharmGKBAPI:
    def __init__(self, max_requests_per_second=0.5):  # Much slower: 1 request every 2 seconds
        self.last_request_time = 0
        self.min_interval = 1.0 / max_requests_per_second  # 2 seconds between requests
        
    def _rate_limit(self):
        """Ensure we don't exceed the rate limit"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.min_interval:
            sleep_time = self.min_interval - time_since_last
            print(f"⏳ Rate limiting: sleeping for {sleep_time:.1f} seconds...")
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
    
    def get_gene_info(self, accession_id=None, symbol=None, view="max"):
        """Get gene information from PharmGKB API"""
        self._rate_limit()
        
        base_url = "https://api.pharmgkb.org/v1/data/gene"
        params = {}
        if accession_id:
            params['accessionId'] = accession_id
        if symbol:
            params['symbol'] = symbol
        if view:
            params['view'] = view
        
        try:
            print(f"\n{'='*60}")
            print(f"🧬 FETCHING GENE: {symbol or accession_id}")
            print(f"🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{'='*60}")
            
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            
            gene_data = response.json()
            
            if isinstance(gene_data, dict):
                print(f"✅ SUCCESS - Gene found!")
                print(f"   Symbol: {gene_data.get('symbol', 'N/A')}")
                print(f"   Name: {gene_data.get('name', 'N/A')}")
                print(f"   PharmGKB ID: {gene_data.get('objCls', 'N/A')}")
                print(f"   Chromosome: {gene_data.get('chromosome', 'N/A')}")
                
                # Show key fields with truncation for large data
                important_fields = ['type', 'version', 'hasVariantAnnotation', 'hasVip', 
                                  'pharmgkbAccessionId', 'crossReferences', 'variants', 
                                  'relatedDrugs', 'relatedDiseases', 'relatedPathways']
                
                for field in important_fields:
                    if field in gene_data:
                        value = gene_data[field]
                        if isinstance(value, list):
                            print(f"   {field}: [{len(value)} items]")
                            if len(value) > 0 and field in ['relatedDiseases', 'relatedDrugs', 'relatedPathways']:
                                print(f"      First few: {[item.get('name', str(item)[:50]) if isinstance(item, dict) else str(item)[:50] for item in value[:3]]}")
                        elif isinstance(value, dict):
                            print(f"   {field}: {dict} with {len(value)} keys")
                        else:
                            print(f"   {field}: {value}")
                            
            elif isinstance(gene_data, list):
                print(f"✅ SUCCESS - Found {len(gene_data)} results")
                for i, item in enumerate(gene_data[:3]):  # Show first 3
                    print(f"   Result {i+1}: {item.get('symbol', 'N/A')} - {item.get('name', 'N/A')}")
            else:
                print(f"⚠️  Unexpected response format")
                print(json.dumps(gene_data, indent=2)[:500])
            
            return gene_data
            
        except requests.exceptions.RequestException as e:
            print(f"❌ ERROR: API request failed for {symbol}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"❌ ERROR: JSON parsing failed for {symbol}: {e}")
            return None
        except Exception as e:
            print(f"❌ ERROR: Unexpected error for {symbol}: {e}")
            return None
    
    def get_disease_info(self, accession_id=None, name=None, view="max"):
        """Get disease information from PharmGKB API"""
        self._rate_limit()
        
        base_url = "https://api.pharmgkb.org/v1/data/disease"
        params = {}
        if accession_id:
            params['accessionId'] = accession_id
        if name:
            params['name'] = name
        if view:
            params['view'] = view
        
        try:
            print(f"\n{'='*60}")
            print(f"🏥 FETCHING DISEASE: {name or accession_id}")
            print(f"🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{'='*60}")
            
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            
            disease_data = response.json()
            
            if isinstance(disease_data, dict):
                print(f"✅ SUCCESS - Disease found!")
                print(f"   Name: {disease_data.get('name', 'N/A')}")
                print(f"   PharmGKB ID: {disease_data.get('pharmgkbAccessionId', 'N/A')}")
                print(f"   Object Class: {disease_data.get('objCls', 'N/A')}")
                
                # Show important disease-specific fields
                important_fields = ['type', 'version', 'alternateNames', 'crossReferences', 
                                  'relatedGenes', 'relatedDrugs', 'relatedPathways', 
                                  'clinicalAnnotations', 'variantAnnotations']
                
                for field in important_fields:
                    if field in disease_data:
                        value = disease_data[field]
                        if isinstance(value, list):
                            print(f"   {field}: [{len(value)} items]")
                            if len(value) > 0 and field in ['relatedGenes', 'relatedDrugs', 'relatedPathways']:
                                print(f"      First few: {[item.get('name', str(item)[:50]) if isinstance(item, dict) else str(item)[:50] for item in value[:5]]}")
                        elif isinstance(value, dict):
                            print(f"   {field}: {dict} with {len(value)} keys")
                        else:
                            print(f"   {field}: {value}")
                            
            elif isinstance(disease_data, list):
                print(f"✅ SUCCESS - Found {len(disease_data)} results")
                for i, item in enumerate(disease_data[:3]):  # Show first 3
                    print(f"   Result {i+1}: {item.get('name', 'N/A')} - ID: {item.get('pharmgkbAccessionId', 'N/A')}")
            else:
                print(f"⚠️  Unexpected response format")
                print(json.dumps(disease_data, indent=2)[:500])
            
            return disease_data
            
        except requests.exceptions.RequestException as e:
            print(f"❌ ERROR: API request failed for {name or accession_id}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"❌ ERROR: JSON parsing failed for {name or accession_id}: {e}")
            return None
        except Exception as e:
            print(f"❌ ERROR: Unexpected error for {name or accession_id}: {e}")
            return None

def save_results_to_file(gene_results, disease_results, filename="pharmgkb_results.json"):
    """Save all results to a JSON file"""
    results = {
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "pharmgkb_api_version": "v1",
            "rate_limit": "0.5 requests per second (1 request every 2 seconds)",
            "total_runtime_minutes": None  # Will be updated at the end
        },
        "rheumatoid_arthritis_disease": disease_results,
        "gene_results": gene_results,
        "summary": {
            "total_genes_queried": len(gene_list_RA),
            "successful_gene_queries": len([r for r in gene_results.values() if r is not None]),
            "failed_gene_queries": len([r for r in gene_results.values() if r is None]),
            "genes_with_ra_associations": [],  # Will be populated during analysis
            "disease_queries_completed": len(disease_results)
        }
    }
    
    # Analyze which genes have RA associations
    for gene_symbol, gene_data in gene_results.items():
        if gene_data and isinstance(gene_data, dict):
            related_diseases = gene_data.get('relatedDiseases', [])
            if any('rheumatoid' in str(disease).lower() or 'arthritis' in str(disease).lower() 
                   for disease in related_diseases):
                results["summary"]["genes_with_ra_associations"].append(gene_symbol)
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Results saved to {filename}")
    return results

if __name__ == "__main__":
    start_time = time.time()
    
    # Initialize API client with slower rate limiting
    api = PharmGKBAPI(max_requests_per_second=0.5)  # 1 request every 2 seconds
    
    # Store results
    gene_results = {}
    disease_results = {}
    
    print(f"""
{'='*80}
🚀 PHARMGKB RHEUMATOID ARTHRITIS DATA EXTRACTION
{'='*80}
📊 Total genes to query: {len(gene_list_RA)}
⏱️  Rate limit: 1 request every 2 seconds (0.5 requests/second)
⌚ Estimated time for genes: {len(gene_list_RA) * 2 / 60:.1f} minutes
🎯 Primary target: Rheumatoid Arthritis (PA443434)
{'='*80}
""")
    
    # First, extract rheumatoid arthritis disease information using the specific PharmGKB ID
    print(f"\n🎯 STEP 1: Extracting Rheumatoid Arthritis Disease Information")
    print(f"{'='*60}")
    
    ra_disease_info = api.get_disease_info(accession_id="PA443434", view="max")
    disease_results["rheumatoid_arthritis_PA443434"] = ra_disease_info
    
    # Also try by name as backup
    ra_by_name = api.get_disease_info(name="rheumatoid arthritis", view="max")
    disease_results["rheumatoid_arthritis_by_name"] = ra_by_name
    
    print(f"\n🧬 STEP 2: Extracting Gene Information for {len(gene_list_RA)} RA-Associated Genes")
    print(f"{'='*60}")
    
    # Query gene information for each gene in the list
    for i, gene in enumerate(gene_list_RA, 1):
        elapsed_time = (time.time() - start_time) / 60
        remaining_genes = len(gene_list_RA) - i + 1
        estimated_remaining_time = remaining_genes * 2 / 60
        
        print(f"\n📈 PROGRESS: {i}/{len(gene_list_RA)} ({i/len(gene_list_RA)*100:.1f}%)")
        print(f"⏰ Elapsed: {elapsed_time:.1f} min | Estimated remaining: {estimated_remaining_time:.1f} min")
        
        gene_info = api.get_gene_info(symbol=gene, view="max")
        gene_results[gene] = gene_info
        
        # Save intermediate results every 20 genes to prevent data loss
        if i % 20 == 0:
            intermediate_filename = f"intermediate_results_{i}_genes.json"
            save_results_to_file(gene_results, disease_results, intermediate_filename)
            print(f"💾 Intermediate save: {intermediate_filename}")
    
    # Calculate total runtime
    total_runtime = (time.time() - start_time) / 60
    
    # Save final comprehensive results
    final_results = save_results_to_file(gene_results, disease_results, "pharmgkb_ra_comprehensive_results.json")
    final_results["metadata"]["total_runtime_minutes"] = total_runtime
    
    # Update the file with runtime info
    with open("pharmgkb_ra_comprehensive_results.json", 'w') as f:
        json.dump(final_results, f, indent=2)
    
    # Print final summary
    print(f"""
{'='*80}
📊 FINAL SUMMARY
{'='*80}
✅ Total genes queried: {len(gene_list_RA)}
🎯 Successful gene queries: {len([r for r in gene_results.values() if r is not None])}
❌ Failed gene queries: {len([r for r in gene_results.values() if r is None])}
🏥 Disease queries completed: {len(disease_results)}
⏱️  Total runtime: {total_runtime:.1f} minutes
💾 Results saved to: pharmgkb_ra_comprehensive_results.json

🧬 Genes with RA associations: {len(final_results["summary"]["genes_with_ra_associations"])}
{final_results["summary"]["genes_with_ra_associations"][:10]}{'...' if len(final_results["summary"]["genes_with_ra_associations"]) > 10 else ''}

✨ Data extraction complete!
{'='*80}
""")