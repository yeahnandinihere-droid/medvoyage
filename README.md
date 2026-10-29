# ✈️ MedVoyage: Cross-Border Clinical Pharmacotherapy Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://medvoyage.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FHIR R4 Ready](https://img.shields.io/badge/Standard-HL7%20FHIR%20R4-emerald.svg)](https://hl7.org/fhir/R4/)

**MedVoyage** is a point-of-care clinical decision support (CDS) platform bridging the gap between outpatient chronic disease pharmacotherapy, sovereign border customs statutes, and international long-haul aviation logistics.

---

## 📌 Problem Statement

Patients on chronic therapy face three acute clinical vulnerabilities when crossing international borders:
1. **Commercial Brand Mismatches:** Trade names vary unpredictably by jurisdiction (e.g., *Eltroxin* vs. *Levothyrox*), risking dispensing denials or inappropriate substitutions.
2. **Customs & Regulatory Seizures:** Common medications (e.g., methylphenidate, codeine, zolpidem) are strictly controlled or banned under destination statutes (e.g., Japan MHLW, UAE MOHAP, Singapore HSA) without pre-approved ministerial certificates[cite: 2, 4].
3. **Circadian PK Desynchrony:** Long-haul flights ($\Delta T \ge 3\,\text{h}$) disrupt narrow-therapeutic regimens (basal insulin, DOACs, antiepileptics), causing dangerous drug stacking or subtherapeutic intervals[cite: 2, 4].

---

## 🚀 Core Modules & Architecture

* **1. Clinical Flight Dashboard:** Pairs IATA flight paths across major corridors (Transatlantic, Asia-Pacific, Transpacific, Euro-African) with patient regimens to triage customs risks and circadian shift windows in seconds.
* **2. WHO INN Formulary Engine:** Resolves proprietary drug brands into universal WHO International Nonproprietary Names (INN), ATC classification codes, and destination-approved domestic formulations.
* **3. Sovereign Customs Shield:** Cross-references active molecules against destination border rules (195+ jurisdictions), highlighting ministerial import permit rules and generating pre-filled physician travel attestation templates[cite: 4].
* **4. Silent Counter Translation Cards:** Generates point-and-show dispensing request cards across **24 global languages** displaying active molecules, formulation, strength, and critical allergy profiles.
* **5. Circadian PK Titration Adjuster:** 
  * **Westward (Day Lengthening):** $\text{Bridge Dose} = \text{Standard Dose} \times \left(\frac{\Delta T}{24}\right)$ administered mid-transit[cite: 2, 4].
  * **Eastward (Day Compression):** $\text{Travel Day Dose} = \text{Standard Dose} \times \left[1 - \left(\frac{\Delta T}{24}\right)\right]$ prior to departure[cite: 2, 4].
  * **DOAC Countdown Protocol:** Enforces strict elapsed-time intervals (12h/24h) rather than clock-face shifts[cite: 2, 4].
* **6. Emergency Medical Passport:** Zero-connectivity, on-device encrypted summary of chronic diagnoses, active meds, and severe allergy alerts, with an HL7 FHIR R4 scannable format[cite: 4].
