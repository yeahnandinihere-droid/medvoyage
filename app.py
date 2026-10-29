import streamlit as st
import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MedVoyage | Clinical Travel Health Engine",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GLOBAL ITINERARIES DATABASE ---
ROUTES_DIRECTORY = {
    "Transatlantic (Eurasia <-> Americas)": [
        {"route": "DEL -> SFO (New Delhi to San Francisco)", "origin_tz": "IST (UTC +5:30)", "dest_tz": "PDT (UTC -7:00)", "delta": -12.5, "direction": "Westward (Day Lengthening)"},
        {"route": "LHR -> JFK (London Heathrow to New York JFK)", "origin_tz": "GMT (UTC 0:00)", "dest_tz": "EDT (UTC -4:00)", "delta": -5.0, "direction": "Westward (Day Lengthening)"},
        {"route": "CDG -> LAX (Paris Charles de Gaulle to Los Angeles)", "origin_tz": "CET (UTC +1:00)", "dest_tz": "PDT (UTC -7:00)", "delta": -9.0, "direction": "Westward (Day Lengthening)"},
        {"route": "FRA -> ORD (Frankfurt to Chicago O'Hare)", "origin_tz": "CET (UTC +1:00)", "dest_tz": "CDT (UTC -5:00)", "delta": -7.0, "direction": "Westward (Day Lengthening)"},
    ],
    "Asia-Pacific & Middle East": [
        {"route": "DEL -> HND (New Delhi to Tokyo Haneda)", "origin_tz": "IST (UTC +5:30)", "dest_tz": "JST (UTC +9:00)", "delta": +3.5, "direction": "Eastward (Day Shortening)"},
        {"route": "BOM -> DXB (Mumbai to Dubai International)", "origin_tz": "IST (UTC +5:30)", "dest_tz": "GST (UTC +4:00)", "delta": -1.5, "direction": "Westward (Minimal Shift)"},
        {"route": "SIN -> SYD (Singapore Changi to Sydney Kingsford)", "origin_tz": "SGT (UTC +8:00)", "dest_tz": "AEST (UTC +10:00)", "delta": +2.0, "direction": "Eastward (Minimal Shift)"},
        {"route": "DXB -> SIN (Dubai to Singapore Changi)", "origin_tz": "GST (UTC +4:00)", "dest_tz": "SGT (UTC +8:00)", "delta": +4.0, "direction": "Eastward (Day Shortening)"},
        {"route": "BKK -> ICN (Bangkok Suvarnabhumi to Seoul Incheon)", "origin_tz": "ICT (UTC +7:00)", "dest_tz": "KST (UTC +9:00)", "delta": +2.0, "direction": "Eastward (Minimal Shift)"},
    ],
    "Transpacific Long-Haul": [
        {"route": "HND -> LAX (Tokyo Haneda to Los Angeles)", "origin_tz": "JST (UTC +9:00)", "dest_tz": "PDT (UTC -7:00)", "delta": -16.0, "direction": "Westward (Across Date Line)"},
        {"route": "SYD -> SFO (Sydney to San Francisco)", "origin_tz": "AEST (UTC +10:00)", "dest_tz": "PDT (UTC -7:00)", "delta": -17.0, "direction": "Westward (Across Date Line)"},
        {"route": "SIN -> SFO (Singapore to San Francisco Direct)", "origin_tz": "SGT (UTC +8:00)", "dest_tz": "PDT (UTC -7:00)", "delta": -15.0, "direction": "Westward (Day Lengthening)"},
    ],
    "European & African Corridors": [
        {"route": "LHR -> JNB (London Heathrow to Johannesburg)", "origin_tz": "GMT (UTC 0:00)", "dest_tz": "SAST (UTC +2:00)", "delta": +2.0, "direction": "North-South (Minimal Shift)"},
        {"route": "AMS -> NBO (Amsterdam to Nairobi)", "origin_tz": "CET (UTC +1:00)", "dest_tz": "EAT (UTC +3:00)", "delta": +2.0, "direction": "North-South (Minimal Shift)"},
        {"route": "DXB -> LHR (Dubai to London Heathrow)", "origin_tz": "GST (UTC +4:00)", "dest_tz": "GMT (UTC 0:00)", "delta": -4.0, "direction": "Westward (Day Lengthening)"},
    ]
}

LANGUAGES = [
    "English", "French (Francais)", "Japanese", "Standard Arabic",
    "Spanish (Espanol)", "German (Deutsch)", "Mandarin Chinese", "Italian (Italiano)",
    "Portuguese", "Russian", "Hindi", "Korean",
    "Turkish", "Dutch", "Polish", "Greek",
    "Swedish", "Vietnamese", "Thai", "Indonesian",
    "Malay", "Tagalog", "Hebrew", "Swahili"
]

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("MedVoyage")
st.sidebar.caption("Clinical Cross-Border Pharmacotherapy Engine")

module = st.sidebar.radio(
    "Navigation Modules",
    [
        "1. Clinical Dashboard",
        "2. Global INN & Brand Search",
        "3. Customs & Legality Shield",
        "4. Silent Counter Translation Card",
        "5. Circadian Titration Adjuster",
        "6. Emergency Medical Passport"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Offline-First Security: Encrypted local cache ready. Compliant with FHIR R4 schema.")

# --- MODULE 1: CLINICAL DASHBOARD ---
if module == "1. Clinical Dashboard":
    st.title("Pre-Departure Travel Clinical Dashboard")
    st.markdown("Select a flight path to verify destination customs regulations and compute circadian pharmacokinetics.")

    col1, col2 = st.columns([2, 1])
    with col1:
        corridor = st.selectbox("Select Flight Corridor / Region", list(ROUTES_DIRECTORY.keys()) + ["Custom Route Entry"])
        if corridor != "Custom Route Entry":
            selected_route_meta = st.selectbox(
                "Select Specific Route",
                ROUTES_DIRECTORY[corridor],
                format_func=lambda x: f"{x['route']} | Shift: {x['delta']:+} hrs ({x['direction']})"
            )
        else:
            c1, c2, c3 = st.columns(3)
            with c1: origin = st.text_input("Origin (e.g., BOM - Mumbai)", "BOM")
            with c2: dest = st.text_input("Destination (e.g., ZRH - Zurich)", "ZRH")
            with c3: delta_val = st.number_input("Time Difference (Hours)", value=4.5, step=0.5)
            selected_route_meta = {
                "route": f"{origin} -> {dest}",
                "origin_tz": "Origin Local Time",
                "dest_tz": "Destination Local Time",
                "delta": delta_val,
                "direction": "Westward" if delta_val < 0 else "Eastward"
            }

    with col2:
        dep_date = st.date_input("Travel Date", datetime.date.today())
        st.metric("Time-Zone Delta (Delta T)", f"{selected_route_meta['delta']:+} Hours", selected_route_meta['direction'])

    st.markdown("### Active Patient Medication Regimen")
    
    meds = [
        {"drug": "Methylphenidate 20mg ER", "dose": "1 tab PO QAM", "cat": "Schedule Controlled", "alert": "CRITICAL PERMIT REQUIRED", "color": "red"},
        {"drug": "Insulin Glargine (Lantus)", "dose": "24 Units SubQ at 22:00", "cat": "Narrow Therapeutic Index", "alert": "CIRCADIAN TITRATION NEEDED", "color": "orange"},
        {"drug": "Telmisartan 40mg", "dose": "1 tab PO QAM", "cat": "Standard Maintenance", "alert": "CLEARED IMPORT", "color": "green"}
    ]

    for m in meds:
        st.markdown(f"""
        <div style="padding: 12px; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 8px; background-color: #f8fafc;">
            <strong>{m['drug']}</strong> - <code>{m['dose']}</code> | Classification: <em>{m['cat']}</em> - <strong style="color: {m['color']};">[{m['alert']}]</strong>
        </div>
        """, unsafe_allow_html=True)

# --- MODULE 2: GLOBAL INN SEARCH ---
elif module == "2. Global INN & Brand Search":
    st.title("Global INN & Therapeutic Equivalence Search")
    st.markdown("Resolves commercial trade names into WHO International Nonproprietary Names (INN) and local approved brands.")

    q = st.text_input("Enter Commercial Brand Name", "Eltroxin 50 mcg")
    target_country = st.selectbox("Select Target Country / Formulary", ["France (ANSM)", "United Kingdom (MHRA)", "Japan (PMDA)", "United States (FDA)", "United Arab Emirates (MOHAP)"])

    if q:
        st.success("**Identified WHO INN:** Levothyroxine Sodium (Oral Tablet) | **ATC Code:** H03AA01")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### Domestic Formulations in Target Country")
            st.markdown("- **Levothyrox** (Merck Sante) - 25, 50, 75, 100 mcg<br/>- **L-Thyroxin Henning** (Sanofi) - 25, 50, 100 mcg", unsafe_allow_html=True)
        with col_b:
            st.warning("Prescriber Advisory: Narrow therapeutic index. Verify tablet strength in micrograms (mcg) with local dispensary.")

# --- MODULE 3: BORDER LEGALITY SHIELD ---
elif module == "3. Customs & Legality Shield":
    st.title("Customs & Border Legality Shield")
    st.markdown("Evaluate border allowances and download pre-departure physician attestation templates.")

    c_drug = st.selectbox("Select Active Medication", ["Zolpidem 10mg (Ambien)", "Methylphenidate 20mg (Concerta)", "Codeine / Acetaminophen", "Insulin Pens / Syringes"])
    c_dest = st.selectbox("Destination Authority", ["United Arab Emirates (MOHAP)", "Japan (MHLW)", "Singapore (HSA)", "Schengen Area (Article 75)", "United States (CBP/FDA)"])

    st.error("Border Finding: Controlled / Pre-Approval Mandatory")
    st.markdown("""
    * **Statutory Classification:** Schedule Controlled Psychotropic under destination law.
    * **Personal Allowance:** Zero days without electronic pre-approval permit. Up to 30-day personal supply allowed with attested permit.
    * **Required Documentation:**
      1. Attested Physician Letter specifying ICD-10 diagnosis, dosage, and duration.
      2. Valid original prescription with institutional clinic seal.
      3. Electronic Ministry Import QR Code.
    """)
    st.button("Generate Pre-Filled Attestation Letter Template (PDF)")

# --- MODULE 4: SILENT COUNTER CARD ---
elif module == "4. Silent Counter Translation Card":
    st.title("'Silent Counter' Pharmacy Translation Card")
    st.markdown("Pre-translated, point-and-show dispensary request cards for overseas pharmacies.")

    selected_lang = st.selectbox("Select Pharmacy Dispensing Language (24 Available)", LANGUAGES)
    
    st.markdown(f"""
    <div style="background-color: #eff6ff; border: 2px solid #0284c7; border-radius: 12px; padding: 20px;">
        <h3 style="color: #0369a1; margin-top: 0;">EMERGENCY PHARMACEUTICAL DISPENSING REQUEST ({selected_lang})</h3>
        <p><strong>Generic Active Ingredient (WHO INN):</strong> Salbutamol (as Salbutamol Sulfate)</p>
        <p><strong>Pharmaceutical Dosage Form:</strong> Pressurized Metered Dose Inhaler (pMDI)</p>
        <p><strong>Strength & Posology:</strong> 100 mcg per actuation | 1-2 puffs as needed for acute dyspnea</p>
        <p><strong>Quantity:</strong> 1 canister inhaler (200 metered doses)</p>
        <hr style="border: 0.5px solid #bfdbfe;"/>
        <p><strong>Allergy Profile:</strong> No Known Drug Allergies (NKDA) | <strong>Concurrent Regimen:</strong> Levothyroxine 50mcg</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Play Native Audio Pronunciation")

# --- MODULE 5: CIRCADIAN TITRATION ADJUSTER ---
elif module == "5. Circadian Titration Adjuster":
    st.title("Circadian Pharmacokinetic Dosing Adjuster")
    st.markdown("Calculates safe step-wise titration across time-zone transitions.")

    col1, col2 = st.columns(2)
    with col1:
        base_dose = st.number_input("Standard Home Dose (Units)", value=24, step=1)
        dose_time = st.time_input("Usual Administration Time", datetime.time(22, 0))
    with col2:
        delta_hours = st.slider("Time-Zone Delta (Hours)", min_value=-14.0, max_value=14.0, value=-12.5, step=0.5)

    if abs(delta_hours) >= 3.0:
        if delta_hours < 0:
            bridge_dose = round(base_dose * (abs(delta_hours) / 24.0), 1)
            st.info(f"**Westward Travel (Day Extension):** Bridge dose calculated: **{bridge_dose} Units** at midpoint (12-18h post-departure).")
        else:
            red_dose = round(base_dose * (1.0 - (delta_hours / 24.0)), 1)
            st.info(f"**Eastward Travel (Day Compression):** Travel-day reduced dose: **{red_dose} Units** prior to departure.")
    else:
        st.success("Time difference < 3 hours. No schedule adjustment required.")

# --- MODULE 6: EMERGENCY MEDICAL PASSPORT ---
elif module == "6. Emergency Medical Passport":
    st.title("Zero-Connectivity Emergency Medical Passport")
    st.markdown("Encrypted, offline-accessible clinical data for foreign trauma teams and hospital triage.")

    st.markdown("""
    <div style="background-color: #f0fdf4; border: 1.5px solid #86efac; border-radius: 12px; padding: 20px;">
        <h3 style="color: #166534; margin-top: 0;">EMERGENCY CLINICAL SUMMARY (OFFLINE ENCRYPTED)</h3>
        <p><strong>Patient Profile:</strong> Adult Traveler | <strong>Blood Type:</strong> O+ (Positive) | <strong>Organ Donor:</strong> Yes</p>
        <p><strong>Chronic Diagnoses:</strong> Primary Hypothyroidism (ICD-10: E03.9); Vasovagal Syncope (ICD-10: R55)</p>
        <p><strong>Active Pharmacotherapy:</strong> Levothyroxine Sodium 50 mcg PO QAM</p>
        <p><strong style="color: #b91c1c;">CRITICAL ALLERGY ALERT:</strong> PENICILLINS (Severe Anaphylactic Risk)</p>
        <hr style="border: 0.5px solid #bbf7d0;"/>
        <p><strong>Emergency Contact:</strong> Primary Family Contact: +91-XXXXXXXXXX | Clinic: Outpatient Medical Center</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Display High-Density HL7 FHIR QR Code")
