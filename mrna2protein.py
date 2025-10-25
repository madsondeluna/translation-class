#!/usr/bin/env python3
"""
Protein Translation Educational Animation
A CLI-based interactive tool to visualize and learn protein translation
"""

import time
import sys
import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03):
    """Print text with typing animation effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_header(title):
    """Print a formatted header"""
    clear_screen()
    width = 80
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()

def animate_dots(duration=2):
    """Animate loading dots"""
    for _ in range(duration):
        for dots in ['   ', '.  ', '.. ', '...']:
            sys.stdout.write(f'\r{dots}')
            sys.stdout.flush()
            time.sleep(0.25)
    print('\r   ')

def draw_molecule(name, structure):
    """Draw ASCII art for molecules"""
    print(f"\n{name}:")
    print(structure)
    print()

def introduction():
    """Introduction to protein translation"""
    print_header("PROTEIN TRANSLATION: A Step-by-Step Journey")
    
    type_text("Welcome to the Protein Translation Educational Tool!")
    time.sleep(0.5)
    type_text("\nThis interactive program will guide you through the fascinating")
    type_text("process of how cells convert genetic information into proteins.")
    time.sleep(1)
    
    type_text("\nPress ENTER to begin the journey...")
    input()

def central_dogma():
    """Explain the central dogma"""
    print_header("THE CENTRAL DOGMA OF MOLECULAR BIOLOGY")
    
    type_text("Before we dive into translation, let's understand the big picture:")
    time.sleep(1)
    
    print("\n")
    print("     ┌─────────────┐")
    print("     │     DNA     │")
    print("     └──────┬──────┘")
    print("            │ Replication")
    print("            ↓")
    print("     ┌──────────────┐")
    print("     │     DNA      │")
    print("     └──────┬───────┘")
    print("            │ Transcription")
    print("            ↓")
    print("     ┌──────────────┐")
    print("     │     RNA      │ (mRNA)")
    print("     └──────┬───────┘")
    print("            │ TRANSLATION [***]")
    print("            ↓")
    print("     ┌──────────────┐")
    print("     │   PROTEIN    │")
    print("     └──────────────┘")
    print()
    
    time.sleep(2)
    type_text("\n[***] TRANSLATION is where the magic happens!")
    type_text("It converts the mRNA message into a functional protein.")
    
    type_text("\nPress ENTER to continue...")
    input()

def translation_machinery():
    """Show the translation machinery components"""
    print_header("THE TRANSLATION MACHINERY")
    
    type_text("Translation requires several key molecular players:")
    time.sleep(1)
    
    components = [
        ("1. mRNA", "The messenger carrying genetic instructions"),
        ("2. Ribosomes", "The protein synthesis factory (40S + 60S subunits)"),
        ("3. tRNA", "Transfer RNA - the amino acid delivery truck"),
        ("4. Amino acids", "The building blocks of proteins"),
        ("5. Initiation factors", "eIF4E, eIF4G, eIF4A, PABP"),
        ("6. Elongation factors", "eEF1A, eEF1B, eEF2"),
        ("7. Energy", "ATP and GTP - the cellular fuel")
    ]
    
    for component, description in components:
        print(f"\n  {component}")
        type_text(f"    → {description}", delay=0.02)
        time.sleep(0.5)
    
    print("\n")
    draw_molecule("Ribosome Structure", """
        ┌─────────────────┐
        │   60S subunit   │  ← Large subunit
        │    (rRNA +      │
        │    proteins)    │
        ├─────────────────┤
        │                 │
        │      mRNA  →    │  ← mRNA threading through
        │                 │
        ├─────────────────┤
        │   40S subunit   │  ← Small subunit
        │    (rRNA +      │
        │    proteins)    │
        └─────────────────┘
    """)
    
    type_text("Press ENTER to see translation in action...")
    input()

def initiation_phase():
    """Demonstrate the initiation phase"""
    print_header("PHASE 1: INITIATION")
    
    type_text("Initiation is where translation begins!")
    type_text("This phase prepares the ribosome to start reading the mRNA.")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\nStep 1: 5' Cap Recognition", delay=0.02)
    animate_dots(1)
    
    print("""
    5' Cap (m7G)
        ↓
    ╔═══╗
    ║ • ║ ← eIF4E binds here
    ╚═══╝
    ═════════════════════> mRNA
    """)
    type_text("[✓] eIF4E recognizes and binds to the 5' cap of mRNA")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\nStep 2: Recruitment of initiation factors", delay=0.02)
    animate_dots(1)
    
    print("""
         eIF4G  eIF4A  PABP
           ↓      ↓      ↓
    ╔═══╗━━━━━━━━━━━━━━━╗
    ║ • ║                ║ Poly-A tail
    ╚═══╝                ╚═══════════
    ═════════════════════>
    """)
    type_text("[✓] eIF4G, eIF4A, and PABP join the complex")
    type_text("[✓] mRNA forms a circular structure for efficient translation")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\nStep 3: 40S Ribosome subunit recruitment", delay=0.02)
    animate_dots(1)
    
    print("""
              ┌─────────┐
              │   40S   │
              └────┬────┘
                   ↓
    ╔═══╗━━━━━━━━━━━━━━━╗
    ║ • ║═══════════════>║
    ╚═══╝                ╚═══════════
         5'  ------>  AUG (start codon)
    """)
    type_text("[✓] The 40S subunit is recruited to the mRNA")
    type_text("[✓] It scans along the mRNA looking for the start codon (AUG)")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\nStep 4: Start codon recognition and 60S joining", delay=0.02)
    animate_dots(1)
    
    print("""
         ┌─────────────┐
         │   60S       │
         ╞═════════════╡
         │  A  P  E    │ ← Three binding sites
         │  │  │  │    │
    5' ══╡══AUG════════│═══> 3'
         │     │       │
         │   Met-tRNA  │ ← Initiator tRNA
         └─────────────┘
         │   40S       │
         └─────────────┘
    """)
    type_text("[✓] AUG start codon found!")
    type_text("[✓] Met-tRNA (carrying Methionine) binds to AUG")
    type_text("[✓] 60S subunit joins to form the complete 80S ribosome")
    type_text("[✓] Translation is ready to begin!")
    time.sleep(2)
    
    type_text("\n[TARGET] INITIATION COMPLETE! Ready to build the protein chain.")
    type_text("\nPress ENTER to continue to elongation...")
    input()

def elongation_phase():
    """Demonstrate the elongation phase"""
    print_header("PHASE 2: ELONGATION")
    
    type_text("Elongation is where the protein chain grows!")
    type_text("This cycle repeats for every amino acid added to the protein.")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\nReminder: The Genetic Code", delay=0.02)
    print("""
    ╔═══════════════════════════════════════╗
    ║  CODON → AMINO ACID                   ║
    ║  AUG → Methionine (START)             ║
    ║  UUU → Phenylalanine                  ║
    ║  GCU → Alanine                        ║
    ║  UAA, UAG, UGA → STOP                 ║
    ╚═══════════════════════════════════════╝
    """)
    time.sleep(1)
    
    amino_acids = ["Met", "Phe", "Ala", "Gly"]
    codons = ["AUG", "UUU", "GCU", "GGU"]
    
    for i, (aa, codon) in enumerate(zip(amino_acids, codons)):
        print("\n" + "═" * 80)
        type_text(f"\n[CYCLE] ELONGATION CYCLE {i+1}: Adding {aa}", delay=0.02)
        animate_dots(1)
        
        print("\n" + "─" * 80)
        type_text("Step 1: Aminoacyl-tRNA enters the A site", delay=0.02)
        time.sleep(0.5)
        
        print(f"""
              ┌─────────────────┐
              │  60S subunit    │
              ├─────────────────┤
              │   E   P   A     │ ← Binding sites
              │       │   │     │
        5' ═══│═══{codons[i-1] if i > 0 else '───'}═{codon}═══│═══> 3'
              │       │   │     │
              │       {amino_acids[i-1] if i > 0 else '   '}  {aa}    │ ← Incoming amino acid
              │       │   │     │
              └───────┴───┴─────┘
                     tRNA tRNA
        """)
        type_text(f"[✓] {aa}-tRNA recognizes codon {codon}")
        type_text(f"[✓] {aa}-tRNA binds to the A (Aminoacyl) site")
        time.sleep(1)
        
        print("\n" + "─" * 80)
        type_text("Step 2: Peptide bond formation", delay=0.02)
        time.sleep(0.5)
        
        print("""
              ┌─────────────────┐
              │  Peptidyl       │
              │  transferase [*]│ ← Catalytic center
              ├─────────────────┤
              │   E   P ~ A     │
              │       │ ╲ │     │
              │       │  ╲│     │ ← Peptide bond forming
              │      Peptide    │
              └─────────────────┘
        """)
        type_text("[✓] Peptidyl transferase catalyzes peptide bond formation")
        type_text(f"[✓] Growing peptide chain now attached to {aa}")
        time.sleep(1)
        
        print("\n" + "─" * 80)
        type_text("Step 3: Ribosome translocation", delay=0.02)
        time.sleep(0.5)
        
        print(f"""
              ┌─────────────────┐
              │  60S subunit    │
              ├─────────────────┤
              │   E   P   A     │
              │   │   │         │
        5' ═══│═{codon}═══────═══│═══> 3'
              │   │   │         │    ↓ Ribosome moves
              │       Peptide   │    ↓ 3 nucleotides
              └─────────────────┘
                       ⬇ ⬇ ⬇
        """)
        type_text("[✓] eEF2 (elongation factor 2) uses GTP energy")
        type_text("[✓] Ribosome moves 3 nucleotides forward (one codon)")
        type_text("[✓] tRNAs shift: A→P→E sites")
        type_text("[✓] Empty tRNA exits from E site")
        time.sleep(1)
        
        print(f"\n[***] Amino acid #{i+1} added! Current peptide: ", end="")
        print("-".join(amino_acids[:i+1]))
        time.sleep(1)
    
    print("\n" + "═" * 80)
    type_text("\n[REPEAT] This cycle repeats hundreds or thousands of times!")
    type_text("Each cycle adds one amino acid to the growing protein chain.")
    type_text(f"\n[RESULT] Final peptide so far: {'-'.join(amino_acids)}")
    
    type_text("\nPress ENTER to continue to termination...")
    input()

def termination_phase():
    """Demonstrate the termination phase"""
    print_header("PHASE 3: TERMINATION")
    
    type_text("Termination ends translation when a STOP codon is reached.")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\nStep 1: Stop codon recognition", delay=0.02)
    animate_dots(1)
    
    print("""
              ┌─────────────────┐
              │  60S subunit    │
              ├─────────────────┤
              │   E   P   A     │
              │       │   │     │
        5' ═══│═══GGU═UAA═══════│═══> 3'
              │       │   [!]   │
              │   Peptide STOP! │
              │       │         │
              └───────┴─────────┘
                     tRNA   
    """)
    type_text("[✓] Stop codon (UAA, UAG, or UGA) enters A site")
    type_text("[✓] No tRNA recognizes stop codons!")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\nStep 2: Release factor binding", delay=0.02)
    animate_dots(1)
    
    print("""
              ┌─────────────────┐
              │  60S subunit    │
              ├─────────────────┤
              │   E   P   A     │
              │       │   │     │
        5' ═══│═══GGU═UAA═══════│═══> 3'
              │       │  eRF1   │ ← Release factor
              │   Peptide│      │
              │       │ eRF3•GTP│
              └───────┴─────────┘
    """)
    type_text("[✓] Release factors eRF1 and eRF3•GTP recognize stop codon")
    type_text("[✓] eRF1 mimics the shape of a tRNA molecule")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\nStep 3: Peptide release", delay=0.02)
    animate_dots(1)
    
    print("""
                  ╔════════════╗
                  ║  PROTEIN!  ║ ← Released!
                  ╚════════════╝
                       ⬆
              ┌─────────────────┐
              │  Peptidyl       │
              │  transferase    │
              │  (hydrolyzes)   │
              ├─────────────────┤
              │   E   P   A     │
              │       ╳   │     │
        5' ═══│═══GGU═UAA═══════│═══> 3'
              └─────────────────┘
    """)
    type_text("[✓] Peptidyl transferase hydrolyzes the peptide-tRNA bond")
    type_text("[✓] Complete protein is released into the cell!")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\nStep 4: Ribosome disassembly", delay=0.02)
    animate_dots(1)
    
    print("""
         ┌─────────────┐
         │   60S       │ ───→ Released
         └─────────────┘
    
    
         ┌─────────────┐
         │   40S       │ ───→ Released
         └─────────────┘
    
        5' ═══════════════════> 3'
              mRNA (can be recycled)
    """)
    type_text("[✓] Ribosome subunits (60S and 40S) dissociate")
    type_text("[✓] mRNA is released (can be translated again)")
    type_text("[✓] tRNA is released (can pick up new amino acids)")
    time.sleep(1)
    
    print("\n" + "═" * 80)
    type_text("\n[SUCCESS] TRANSLATION COMPLETE!")
    type_text("A functional protein has been synthesized!")
    
    type_text("\nPress ENTER to see the summary...")
    input()

def protein_folding():
    """Show protein folding"""
    print_header("PROTEIN FOLDING & MATURATION")
    
    type_text("After translation, the protein must fold into its functional 3D shape.")
    time.sleep(1)
    
    print("\n")
    print("     Linear Protein Chain")
    print("     ═══════════════════")
    print("     Met-Phe-Ala-Gly-...")
    print()
    animate_dots(2)
    print("            ↓ Folding")
    animate_dots(2)
    print()
    print("        Folded Protein")
    print("          ╔═══╗")
    print("       ╔══╝   ╚══╗")
    print("       ║         ║")
    print("       ║  ACTIVE ║  ← Functional 3D structure")
    print("       ║   SITE  ║")
    print("       ╚═════════╝")
    print()
    
    type_text("\n[✓] Proteins fold based on amino acid sequence")
    type_text("[✓] Chaperone proteins help with proper folding")
    type_text("[✓] Post-translational modifications may occur:")
    print("    • Phosphorylation")
    print("    • Methylation")
    print("    • Glycosylation")
    print("    • Ubiquitination")
    
    time.sleep(2)
    type_text("\nPress ENTER to continue...")
    input()

def summary():
    """Provide a summary of the translation process"""
    print_header("TRANSLATION SUMMARY")
    
    type_text("Let's review the complete translation process:")
    time.sleep(1)
    
    print("\n")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                    PROTEIN TRANSLATION                         ║")
    print("╠════════════════════════════════════════════════════════════════╣")
    print("║                                                                ║")
    print("║  [1] INITIATION                                                ║")
    print("║      • 5' cap recognition by eIF4E                            ║")
    print("║      • Ribosome recruitment (40S subunit)                     ║")
    print("║      • AUG start codon recognition                            ║")
    print("║      • 60S subunit joining → 80S ribosome                     ║")
    print("║                                                                ║")
    print("║  [2] ELONGATION (REPEATING CYCLE)                             ║")
    print("║      • Aminoacyl-tRNA enters A site                           ║")
    print("║      • Peptide bond formation (peptidyl transferase)          ║")
    print("║      • Translocation (ribosome moves 3 nucleotides)           ║")
    print("║      • tRNA movement: A → P → E sites                         ║")
    print("║                                                                ║")
    print("║  [3] TERMINATION                                               ║")
    print("║      • Stop codon recognition (UAA/UAG/UGA)                   ║")
    print("║      • Release factors (eRF1/eRF3•GTP) binding                ║")
    print("║      • Peptide chain release                                  ║")
    print("║      • Ribosome disassembly                                   ║")
    print("║                                                                ║")
    print("║  [4] POST-TRANSLATION                                          ║")
    print("║      • Protein folding (chaperone-assisted)                   ║")
    print("║      • Post-translational modifications                       ║")
    print("║      • Targeting to final cellular location                   ║")
    print("║                                                                ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print()
    
    time.sleep(2)
    
    type_text("\n[TIME] SPEED: Translation occurs at ~5-10 amino acids per second!")
    type_text("[SIZE] LENGTH: Average protein is ~300-400 amino acids")
    type_text("[ENERGY] ENERGY: ~4 ATP equivalents per amino acid added")
    
    type_text("\nPress ENTER to continue...")
    input()

def clinical_relevance():
    """Show clinical relevance"""
    print_header("CLINICAL RELEVANCE")
    
    type_text("Translation deregulation is involved in many diseases:")
    time.sleep(1)
    
    diseases = [
        ("[NEURO] NEURODEGENERATIVE DISEASES", [
            "• Alzheimer's: β-amyloid aggregation, eIF2α phosphorylation",
            "• Parkinson's: α-synuclein aggregation, eIF4G1 mutations",
            "• ALS: UPR activation, PERK-mediated translation inhibition",
            "• Huntington's: CAG expansion, polyglutamine aggregation"
        ]),
        ("[CANCER] CANCER", [
            "• Overexpression of eIF4E, eIF4A, eEF2",
            "• mTOR pathway dysregulation",
            "• Altered ribosomal protein expression",
            "• Changes in tRNA modifications"
        ]),
        ("[VIRUS] INFECTIOUS DISEASES", [
            "• Viruses hijack host translation machinery",
            "• Viral proteins compete for eIF4E binding",
            "• Example: Potyvirus uses VPg instead of 5' cap"
        ]),
        ("[CARDIO] CARDIOVASCULAR DISEASES", [
            "• Hypertrophic cardiomyopathy",
            "• Increased protein synthesis in cardiomyocytes",
            "• TIP30 protein regulates translation via eEF1A"
        ])
    ]
    
    for disease_type, details in diseases:
        print("\n" + "─" * 80)
        type_text(f"\n{disease_type}", delay=0.02)
        for detail in details:
            print(f"  {detail}")
            time.sleep(0.3)
        time.sleep(0.5)
    
    print("\n" + "═" * 80)
    type_text("\n[THERAPY] THERAPEUTIC STRATEGIES:", delay=0.02)
    print("\n  • mTOR inhibitors: Rapamycin, Everolimus, Temsirolimus")
    print("  • eIF4E inhibitors: Ribavirin, LY2275796")
    print("  • eIF4A inhibitors: Silvestrol, Rocaglates")
    print("  • eIF2α modulators: Salubrinal (neuroprotection)")
    
    time.sleep(2)
    type_text("\nPress ENTER to continue...")
    input()

def research_techniques():
    """Show research techniques"""
    print_header("RESEARCH TECHNIQUES")
    
    type_text("Scientists use advanced techniques to study translation:")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\n[1] RIBOSOME PROFILING (Ribo-seq)", delay=0.02)
    print("""
    Translation    RNase        Isolate       Sequence
    inhibitors → digestion → footprints →  & analyze
                               (~28 bp)
    
    Result: Genome-wide map of ribosome positions
    """)
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\n[2] MASS SPECTROMETRY PROTEOMICS", delay=0.02)
    print("""
    Protein    Digest to    Ionize &      Detect &
    sample  → peptides  →  separate  →   identify
    
    Methods: SILAC, iTRAQ, TMT
    Result: Quantitative protein expression data
    """)
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\n[3] SINGLE-CELL APPROACHES", delay=0.02)
    print("""
    Single    Isolate       Profile        Analyze
    cells  →  RNA/protein → individual  → heterogeneity
                            cells
    
    Techniques: scRNA-seq, scRibo-seq, nascent proteomics
    """)
    time.sleep(1)
    
    print("\n" + "─" * 80)
    type_text("\n[4] POLYSOME PROFILING", delay=0.02)
    print("""
    Cell      Separate by    Fractionate    Analyze
    lysate → sedimentation → polysomes  → translation
             (sucrose grad)                 activity
    """)
    time.sleep(1)
    
    type_text("\nPress ENTER to finish...")
    input()

def conclusion():
    """Concluding remarks"""
    print_header("CONCLUSION")
    
    type_text("Congratulations! You've completed the Translation tutorial!")
    time.sleep(1)
    
    print("\n")
    print("    ╔════════════════════════════════════════════╗")
    print("    ║                                            ║")
    print("    ║         DNA → mRNA → Ribosome → PROTEIN   ║")
    print("    ║                                            ║")
    print("    ║    Translation is fundamental to life!     ║")
    print("    ║                                            ║")
    print("    ╚════════════════════════════════════════════╝")
    print()
    
    type_text("\n[KEY POINTS] KEY TAKEAWAYS:")
    print("  [✓] Translation converts mRNA into proteins")
    print("  [✓] Three phases: Initiation, Elongation, Termination")
    print("  [✓] Ribosomes are the molecular machines")
    print("  [✓] tRNA delivers amino acids based on codon recognition")
    print("  [✓] Translation deregulation causes diseases")
    print("  [✓] Many therapeutic targets exist")
    
    time.sleep(2)
    
    print("\n" + "═" * 80)
    type_text("\n[READING] RECOMMENDED READING:", delay=0.02)
    print("\n  • Jia et al. (2024) - Signal Transduction and Targeted Therapy")
    print("    'Protein translation: biological processes and therapeutic")
    print("     strategies for human diseases'")
    print("\n  • DOI: 10.1038/s41392-024-01749-9")
    
    time.sleep(1)
    
    print("\n" + "═" * 80)
    type_text("\n[***] Thank you for learning about Protein Translation! [***]")
    type_text("\nCreated for: Madson Aragão @ UFMG")
    print()

def main():
    """Main program flow"""
    try:
        introduction()
        central_dogma()
        translation_machinery()
        initiation_phase()
        elongation_phase()
        termination_phase()
        protein_folding()
        summary()
        clinical_relevance()
        research_techniques()
        conclusion()
        
    except KeyboardInterrupt:
        print("\n\n[!] Tutorial interrupted by user.")
        print("Thank you for participating!\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
