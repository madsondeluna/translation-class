# Protein Translation and Translation Control

## Class Overview

This repository contains educational materials focusing on protein translation mechanisms, regulation, and clinical implications.

## Table of Contents

- [Introduction](#introduction)
- [The Central Dogma](#the-central-dogma)
- [Translation Machinery](#translation-machinery)
- [Canonical Translation Process](#canonical-translation-process)
- [Translation Deregulation](#translation-deregulation)
- [Non-Canonical Translation](#non-canonical-translation)
- [Disease Implications](#disease-implications)
- [Research Techniques](#research-techniques)
- [Therapeutic Strategies](#therapeutic-strategies)
- [Recommended Articles](#recommended-articles)
- [Class Materials](#class-materials)
- [Interactive scripts](#interactive-educational-scripts)

## Introduction

Protein translation is a fundamental biological process that converts genetic information from mRNA into functional proteins. This tightly regulated cellular mechanism is essential for gene expression, and its deregulation is increasingly recognized as a critical factor in the pathogenesis of various human diseases including cancer, neurodegenerative disorders, cardiovascular diseases, and infectious diseases.

## The Central Dogma

The central dogma of molecular biology describes the flow of genetic information through two essential processes:

1. **Transcription**: DNA serves as a template for RNA synthesis
2. **Translation**: mRNA directs the amino acid sequence for protein formation

**Flow**: DNA → RNA → PROTEIN (Replication → Transcription → Translation)

*Note*: Reverse transcription (RNA → cDNA) also occurs in certain biological contexts.

## Interactive educational scripts

Students can use the interactive scripts included in this repository to explore, step-by-step, the full translation process from mRNA to protein. These scripts run in the terminal and present a guided, interactive tutorial with explanatory screens, simple ASCII diagrams, and small animations. At each step the program waits for the user to press ENTER to continue.

Main scripts:

- `mrna2protein.py` — interactive tutorial in English
- `domrnaparaproteina.py` — interactive tutorial in Portuguese (available as an alternative)

Usage:

Run the English interactive tutorial:

```bash
python3 mrna2protein.py
```

Run the Portuguese interactive tutorial (alternative):

```bash
python3 domrnaparaproteina.py
```

The program prints explanatory screens and small ASCII diagrams. Press ENTER to continue between screens, and use Ctrl+C to exit the tutorial at any time.

Screenshots:

> Initiation & central dogma screen

![mrna2protein running — screen 1](<img-scripts/Screenshot 2025-10-25 at 00.38.19.png>)

> Elongation / peptide growth screen 

![mrna2protein running — screen 2](<img-scripts/Screenshot 2025-10-25 at 00.38.58.png>)

Configurable option: typing animation speed

Both scripts implement a simple typing animation for explanatory text. The functions are:

- `type_text(text, delay=0.03)` in `mrna2protein.py`
- `digitar_texto(texto, atraso=0.03)` in `domrnaparaproteina.py`

How to change the speed:

- Edit the default value of the `delay` / `atraso` parameter in the function definition (e.g. `0.01` for faster, `0.06` for slower), or
- Pass a different value when calling the function: `type_text("Hello", delay=0.01)`.

Note: The scripts are interactive and do not currently provide a command-line flag to change this option; if you prefer, I can add a `--speed` flag to control typing speed at runtime.

## Translation Machinery

### Key Components

Translation requires several essential molecular components:

- **Mature mRNA**: Contains exons, 5' cap, and poly-A tail
- **Ribosomes**: Composed of rRNA and proteins (40S and 60S subunits in eukaryotes)
- **Initiation factors**: eIF4F complex (eIF4A, eIF4G, eIF4E, PABP)
- **Elongation factors**: eIF1A, eIF1B, eIF2
- **Termination factors**: eRF1/eRF3•GTP
- **Aminoacyl-tRNA synthetases**
- **Transfer RNA (tRNA)**
- **Amino acids**
- **Energy molecules**: ATP and GTP

### Subcellular Localization

Translation occurs in multiple cellular compartments:

- **Cytosol**: Polyribosomal fractions, stress bodies, P-bodies
- **Rough endoplasmic reticulum**: For secretory and membrane proteins
- **Mitochondria**: For mitochondrial-encoded proteins
- **Perinuclear halo (Golgi complex)**: Highly visible in plasma cells producing antibodies

## Canonical Translation Process

### 1. Initiation

The initiation phase involves:

- 5' cap recognition by eIF4E
- Recruitment of eIF4G, eIF4A, and PABP
- Ribosome recruitment and assembly
- Scanning for the AUG start codon by the 40S subunit
- Formation of the 80S initiation complex

### 2. Elongation

During elongation:

- Aminoacyl-tRNA delivers amino acids to the A site
- Peptide bond formation via peptidyl transferase activity
- Ribosome translocation along mRNA (5' to 3' direction)
- tRNA movement through A → P → E sites
- **Codon usage** and the **wobble effect** influence translation efficiency

### 3. Termination

Termination occurs when:

- Stop codons (UAA, UAG, UGA) are recognized
- Release factors eRF1/eRF3•GTP bind to the A site
- Peptidyl transferase hydrolyzes the peptide-tRNA bond
- Polypeptide chain is released
- Ribosome-tRNA-mRNA complex disassembles

## Translation Deregulation

### Definition

Translation deregulation refers to disruption or alteration of normal protein synthesis, which can result in:

- Production of aberrant proteins
- Loss of protein expression regulation
- Mistranslation-induced mutagenesis

### Mechanisms of Elongation Deregulation

Several factors can disrupt translation elongation:

1. **mRNA mutations**: Disrupt tRNA selection and decoding
2. **Translation factor mutations**: Reduce ribosome translocation rates (e.g., eEF1A, eEF1B, eEF2)
3. **tRNA mutations**: Cause ribosome stalling and incorrect amino acid incorporation
4. **Ribosomal protein modifications**: Modulate ribosome movement speed
5. **Ribosome stalling**: Caused by mRNA secondary structures, codon repeats, rare codons, or mRNA damage

### Conservation of Translation Machinery

Translation machinery components are highly conserved across species:

- **eIF4E protein**: Shows >98% sequence identity across different cowpea cultivars
- **Structural conservation**: RMSD of 0.071 Å between different cultivar models
- This conservation highlights the fundamental importance of translation in all living organisms

## Non-Canonical Translation

Beyond cap-dependent canonical translation, cells employ alternative translation mechanisms:

- **m6A-initiated translation**: N6-methyladenosine modification-mediated initiation
- **eIF3d-mediated translation**: Alternative initiation factor usage
- **IRES (Internal Ribosome Entry Sites)**: Direct internal ribosome binding
- **Ribosome shunting**: Bypassing secondary structures

These mechanisms are distinguished primarily by initiation factor requirements but may still involve cap recognition and 40S scanning.

## Disease Implications

### Neurodegenerative Diseases

Translation deregulation is implicated in several neurodegenerative conditions:

#### Parkinson's Disease
- Abnormal α-synuclein protein aggregation
- eIF4G1 mutations associated with disease and Lewy body dementia
- mTOR pathway deregulation affects eIF4E expression

#### Alzheimer's Disease
- β-amyloid peptide (Aβ) aggregates in the ER
- Formation of amyloid plaques and neurofibrillary tangles
- Increased eIF2α phosphorylation
- **Gastrodin**: Suppresses BACE1 expression via PKR/eIF2α pathway

#### Amyotrophic Lateral Sclerosis (ALS)
- Progressive motor neuron loss
- Unfolded Protein Response (UPR) activation
- PERK-mediated eIF2α inhibition reduces global protein synthesis

#### Huntington's Disease
- CAG trinucleotide expansion in HTT gene
- Abnormal polyglutamine expansion in mutant huntingtin
- Cytotoxicity and neuronal death
- Therapeutic targets include DNA/RNA of huntingtin and protein elimination

### Cancer

Translation deregulation is a hallmark of cancer:

- **Increased translation activity**: Supports rapid cell proliferation
- **Altered translation factors**: Overexpression of eIF4E, eIF4A, eEF2
- **mTOR pathway dysregulation**: Affects S6K and 4E-BP1
- **Ribosomal alterations**: Changes in ribosomal protein expression
- **tRNA modifications**: Affect codon usage and translation efficiency

### Infectious Diseases

Viruses manipulate host translation machinery:

- **Viral protein genome-linked (VPg)**: Replaces 5' cap structure
- **eIF4E binding site hijacking**: Viruses compete for translation initiation
- **Example**: Cowpea resistance to Potyvirus involves eIF4E gene mutations that disrupt eIF4E-VPg interaction

### Cardiovascular Diseases

#### Hypertrophic Cardiomyopathy
- Pathological overload triggers increased protein synthesis
- Cardiomyocyte hypertrophy
- **TIP30 protein**: Inhibits hypertrophy by interacting with eEF1A
- Acts as tumor suppressor and cardiac function regulator

## Research Techniques

### Ribosome Profiling

A powerful technique for genome-wide translation quantification:

1. Translation inhibitors maintain ribosome position
2. RNase digestion of unprotected RNA
3. Isolation of ribosome footprints (~28 bp)
4. Library preparation and deep sequencing
5. Calculation of translation efficiency (TE)

### Mass Spectrometry-Based Proteomics

Enables comprehensive protein analysis:

- **Quantification methods**: ICAT, SILAC, iTRAQ
- **Post-translational modifications**: Phosphorylation, methylation
- **Mass/charge ratio measurements**: Precise molecular weight determination

### mRNA Sequencing

Transcriptome profiling provides insights into:

- Gene expression levels
- Alternative splicing events
- Mutation detection
- Translation efficiency estimation

### Single-Cell Approaches

Revolutionary techniques for studying cellular heterogeneity:

- **FACS sorting**: Isolate specific cell populations
- **Single-cell RNA-seq**: Transcriptome analysis at single-cell resolution
- **Single-cell Ribo-seq**: Translation profiling in individual cells
- **Single-cell proteomics**: Protein expression in single cells
- **Nascent proteomics**: Study newly synthesized proteins

### Historical Timeline

Key discoveries in translation research:

- **1955**: Discovery of tRNA, ribosomes, and insulin sequencing
- **1968**: Nobel Prize for genetic code
- **1980-2000**: Investigation of eIFs, eEFs, 4E-BP, and mTOR mechanisms
- **2002**: Development of SILAC and mass spectrometry advances
- **2009**: Nobel Prize for ribosome structure and function
- **2017**: Nobel Prize for Cryo-EM
- **2021+**: Single-cell and nascent proteomics approaches

## Therapeutic Strategies

### FDA-Approved and Clinical Stage Inhibitors

| Target | Agent | Clinical Stage | Applications |
|--------|-------|---------------|--------------|
| mTOR | Rapamycin | FDA Approved | Immunosuppression (transplant rejection) |
| mTOR | Everolimus | FDA Approved | Cancer (antineoplastic), immunosuppression |
| mTOR | Temsirolimus | FDA Approved | Cancer (renal cell carcinoma) |
| eIF4E | Ribavirin, LY2275796 | Phase II | Cancer |
| eIF4E-eIF4G | Homoharringtonine | Phase III | Leukemia |
| eIF4A | Silvestrol, Rocaglates | Preclinical | Cancer |
| eIF2α | Salubrinal | Preclinical | Neuroprotection |

### Mechanism: mTOR Pathway Targeting

The mTOR pathway is a critical regulator of translation:

- **mTORC1**: Phosphorylates 4E-BP and S6K
- **4E-BP phosphorylation**: Releases eIF4E for translation initiation
- **S6K activation**: Promotes ribosome biogenesis
- **Rapamycin and analogs**: Inhibit mTORC1, reducing translation of growth-promoting proteins

## Recommended Articles

### Primary Reference

**"Protein translation: biological processes and therapeutic strategies for human diseases"**
- Authors: Xuechao Jia, Xinyu He, Chuntian Huang, Jian Li, Zigang Dong & Kangdong Liu
- Journal: *Signal Transduction and Targeted Therapy*
- Year: 2024
- Volume: 9, Article 44
- DOI: [10.1038/s41392-024-01749-9](https://doi.org/10.1038/s41392-024-01749-9)
- Impact Factor: 40.8
- Access: [Nature Open Access](https://www.nature.com/articles/s41392-024-01749-9)

### Additional Reading

1. **Translation regulation and targeted therapy**
   - Hagner et al. (2010) - "Targeting the translational machinery as a novel treatment strategy for hematologic malignancies"
   - [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2844014/)

2. **Codon usage and translation rates**
   - Komar (2024) - "Translation Rates and Protein Folding"
   - [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022283623004953)

3. **tRNA engineering**
   - Weiss et al. (2024) - "Tuning tRNAs for improved translation"
   - [Frontiers in Genetics](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2024.1436860/full)

4. **Translational control during stress**
   - Horvath et al. (2024) - "Comprehensive translational profiling and STE AI uncover rapid control of protein biosynthesis during cell stress"
   - [Nucleic Acids Research](https://academic.oup.com/nar/article/52/13/7925/7667526)

5. **Metabolism and translation crosstalk**
   - Biffo et al. (2024) - "The crosstalk between metabolism and translation"
   - [Cell Metabolism](https://www.sciencedirect.com/science/article/pii/S1550413124003243)

6. **mRNA modifications and translation**
   - Song et al. (2021) - "The regulation of protein translation and its implications for cancer"
   - [Nature Open Access](https://www.nature.com/articles/s41392-020-00444-9)

## Class Materials

### Access to Presentation Slides

The original presentation slides are available in this repository:
- **File**: [slides/class.pdf](https://github.com/madsondeluna/translation-class/tree/main/slides)
- **Content**: Comprehensive slides covering all topics presented in this README
- **Language**: Portuguese with scientific terminology in English

### Class Information

- **Institution**: Federal University of Minas Gerais (UFMG)
- **Class**: Estudos de Genômica Transcriptômica e Proteômica (EGTP)
- **Seminar Team**: Alisson Clementino da Silva, Leonardo Henrique da Silva, and Madson A. de Luna Aragão


## Future Directions

Translation research continues to evolve with exciting developments:

1. **Biomarker development**: Identifying actionable biomarkers targeting translation
2. **Rare genetic diseases**: Understanding mutations in translation factors
3. **Precision medicine**: Personalized therapies based on translation profiles
4. **Synthetic biology**: Engineering optimized translation for biotechnology
5. **mRNA therapeutics**: Leveraging translation principles for vaccine and drug design

## Conclusion

The deregulation of protein translation leads to abnormal protein expression, altered protein isoforms, and disrupted cellular functions. Despite challenges in developing effective biomarkers and translation-targeted therapeutics, this field offers tremendous opportunities for innovative therapeutic approaches. Future research on rare genetic diseases caused by mutations in translation factors or ribosomal proteins will deepen our understanding of translation mechanisms and unlock possibilities for precision medicine.

---

## Contact and Contributions

For questions about this class material or to contribute additional resources, please reach [madsondeluna@gmail.com](https://madsondeluna.github.io/#contact)

## License

This educational material is provided for academic purposes. Please cite the original sources when using this information.

---

> This README was created to facilitate access to protein translation class materials for students, providing comprehensive coverage of the subject in English while maintaining references to the original Portuguese presentation materials.


