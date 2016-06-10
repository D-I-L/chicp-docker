CP_STATS = ['UD', 'GWAS']
CP_TARGET = ['MIFSUD']

sampleLookup = {'Naive_CD4': ['C002Q1H1', 'C002TWH1', 'S007G7H4', 'S007DDH2'],
               'Megakaryocytes': ['S004BTH2'],
               'Erythroblasts': ['S002R5H1', 'S002S3H1'],
               'Monocytes': ['C000S5H2', 'C004SQH1'],
               'Macrophages_M0': ['S00390H1'],
               'Macrophages_M1': ['S001MJH1', 'S001S7H2', 'S0022IH2'],
               'Macrophages_M2': ['S00622H1', 'S006VIH1', 'S00BS4H1', 'S00FTNH1'],
               'CD34': [
                   'E035:Primary hematopoietic stem cells',
                   'E036:Primary hematopoietic stem cells short term culture',
                   'E050:Primary hematopoietic stem cells G-CSF-mobilized Female',
                   'E051:Primary hematopoietic stem cells G-CSF-mobilized Male'
               ],
               'GM12878': ['E116:GM12878 Lymphoblastoid Cells'],
               'GM12878_Pro': ['E116:GM12878 Lymphoblastoid Cells'],
               'GM12878_Reg': ['E116:GM12878 Lymphoblastoid Cells']}

stateLookup = {'1_TssA': {'desc': 'Active TSS', 'color': '255,0,0'},
              '2_TssAFlnk': {'desc': "Flanking Active TSS", 'color': '255,69,0'},
              '3_TxFlnk': {'desc': "Transcription at gene 5' and 3'", 'color': '50,205,50'},
              '4_Tx': {'desc': "Strong transcription", 'color': '0,128,0'},
              '5_TxWk': {'desc': "Weak transcription", 'color': '0,100,0'},
              '6_EnhG': {'desc': "Genic enhancers", 'color': '194,225,5'},
              '7_Enh': {'desc': "Enhancers", 'color': '255,255,0'},
              '8_ZNF/Rpts': {'desc': "ZNF genes & repeats", 'color': '102,205,170'},
              '9_Het': {'desc': "Heterochromatin", 'color': '138,145,208'},
              '10_TssBiv': {'desc': "Bivalent/Poised TSS", 'color': '205,92,92'},
              '11_BivFlnk': {'desc': "Flanking Bivalent TSS/Enh", 'color': '233,150,122'},
              '12_EnhBiv': {'desc': "Bivalent Enhancer", 'color': '189,183,107'},
              '13_ReprPC': {'desc': "Repressed PolyComb", 'color': '128,128,128'},
              '14_ReprPCWk': {'desc': "Weak Repressed PolyComb", 'color': '192,192,192'},
              '15_Quies': {'desc': "Quiescent/Low", 'color': '240,240,240'}
              }
DEFAULT_TARGET = 'cp:hg19_mifsud_chicago_pm'
DEFAULT_TISSUE = 'CD34'
DEFAULT_TRACK = 'gwas-barrett'
DEFAULT_FRAG = 'hg19_restriction_sites/hindiii'
CP_GENE_IDX = 'cp:hg19_gene_details'
DEFAULT_GENES = ['IL2RA', 'DEXI', 'BACH2', 'FOXP3', 'DOCK1']


TARGET_IDXS = {'cp:hg19_mifsud_chicago_pm': 'Mifsud'}

STUDY_DEFAULTS = {'log10p': {'min': 1, 'snpCutoff': 7.03, 'score_text': "P Value (-log10)"},
                  'ppi': {'min': 0.001, 'snpCutoff': 0.1, 'score_text': "PPI Score"}}


