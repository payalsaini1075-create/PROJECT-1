"""
disease_info.py
-----------------
A small "knowledge base" used purely to make the app's results feel more
like a real product: a one-line description of the disease, and a few
GENERAL, non-prescriptive precautions (rest, hydration, "see a doctor"
style advice only -- never dosages or specific treatments).

This is intentionally simple. It is NOT medical advice and the app
displays a disclaimer everywhere these are shown.
"""

DISEASE_INFO = {
    "(vertigo) Paroymsal  Positional Vertigo": {
        "description": "A condition causing brief episodes of dizziness triggered by specific changes in head position.",
        "precautions": ["Avoid sudden head movements", "Sit down immediately when dizzy", "Consult an ENT specialist"],
    },
    "AIDS": {
        "description": "An advanced stage of HIV infection that severely weakens the immune system.",
        "precautions": ["Seek immediate specialist medical care", "Practice safe behaviors to avoid spreading infection", "Maintain a nutritious diet"],
    },
    "Acne": {
        "description": "A skin condition causing pimples, typically from clogged hair follicles.",
        "precautions": ["Keep skin clean", "Avoid touching/picking at affected areas", "Consult a dermatologist for persistent cases"],
    },
    "Alcoholic hepatitis": {
        "description": "Liver inflammation caused by excessive alcohol consumption.",
        "precautions": ["Stop alcohol consumption completely", "Seek medical supervision", "Eat a liver-friendly, balanced diet"],
    },
    "Allergy": {
        "description": "An immune system reaction to a substance that is normally harmless.",
        "precautions": ["Identify and avoid the allergen", "Keep antihistamines on hand if prescribed", "See a doctor if symptoms are severe"],
    },
    "Arthritis": {
        "description": "Inflammation of one or more joints, causing pain and stiffness.",
        "precautions": ["Stay gently active to maintain joint mobility", "Apply hot/cold therapy as advised", "Consult a rheumatologist"],
    },
    "Bronchial Asthma": {
        "description": "A chronic condition causing the airways to narrow and swell, making breathing difficult.",
        "precautions": ["Avoid known triggers (dust, smoke, allergens)", "Keep a rescue inhaler accessible", "Follow up regularly with a pulmonologist"],
    },
    "Cervical spondylosis": {
        "description": "Age-related wear affecting the spinal disks in the neck.",
        "precautions": ["Maintain good posture", "Do gentle neck stretching exercises", "Consult an orthopedic specialist if pain persists"],
    },
    "Chicken pox": {
        "description": "A highly contagious viral infection causing an itchy, blister-like rash.",
        "precautions": ["Isolate to avoid spreading infection", "Avoid scratching the blisters", "Stay hydrated and rest"],
    },
    "Chronic cholestasis": {
        "description": "A condition where bile flow from the liver is reduced or blocked.",
        "precautions": ["Follow a low-fat diet as advised", "Avoid alcohol", "Seek specialist hepatology care"],
    },
    "Common Cold": {
        "description": "A mild viral infection of the nose and throat.",
        "precautions": ["Rest and stay hydrated", "Use steam inhalation for congestion", "See a doctor if symptoms last beyond 10 days"],
    },
    "Dengue": {
        "description": "A mosquito-borne viral infection causing high fever and severe body aches.",
        "precautions": ["Stay hydrated and rest", "Avoid pain relievers that increase bleeding risk (consult a doctor first)", "Seek immediate care if warning signs (bleeding, severe pain) appear"],
    },
    "Diabetes": {
        "description": "A chronic condition where blood sugar levels are too high due to issues with insulin.",
        "precautions": ["Monitor blood sugar regularly", "Maintain a balanced, low-sugar diet", "Stay physically active and consult an endocrinologist"],
    },
    "Dimorphic hemmorhoids(piles)": {
        "description": "Swollen veins in the lower rectum or anus causing discomfort and bleeding.",
        "precautions": ["Increase dietary fiber intake", "Stay hydrated", "Consult a doctor for persistent symptoms"],
    },
    "Drug Reaction": {
        "description": "An adverse reaction of the body to a medication.",
        "precautions": ["Stop the suspected medication and consult a doctor immediately", "Inform all future healthcare providers of the reaction", "Carry a list of known drug allergies"],
    },
    "Fungal infection": {
        "description": "An infection caused by fungi, often affecting skin, nails, or other tissues.",
        "precautions": ["Keep the affected area clean and dry", "Avoid sharing personal items (towels, clothing)", "Use antifungal treatment as advised by a doctor"],
    },
    "GERD": {
        "description": "Gastroesophageal Reflux Disease — frequent acid reflux from the stomach into the esophagus.",
        "precautions": ["Avoid large meals before lying down", "Limit spicy/acidic foods", "Consult a gastroenterologist for frequent symptoms"],
    },
    "Gastroenteritis": {
        "description": "Inflammation of the stomach and intestines, usually causing diarrhea and vomiting.",
        "precautions": ["Stay hydrated with oral rehydration solutions", "Eat light, bland foods as tolerated", "See a doctor if symptoms persist beyond 2 days"],
    },
    "Heart attack": {
        "description": "A medical emergency where blood flow to the heart muscle is suddenly blocked.",
        "precautions": ["Seek emergency medical help IMMEDIATELY", "Chew aspirin only if advised by emergency services", "Stay calm and avoid physical exertion while waiting for help"],
    },
    "Hepatitis B": {
        "description": "A viral infection that attacks the liver, can become chronic.",
        "precautions": ["Get vaccinated to prevent spread to others", "Avoid alcohol", "Regular liver function monitoring with a specialist"],
    },
    "Hepatitis C": {
        "description": "A viral infection causing liver inflammation, often without early symptoms.",
        "precautions": ["Seek antiviral treatment from a specialist", "Avoid alcohol", "Get tested if you may have been exposed"],
    },
    "Hepatitis D": {
        "description": "A liver infection that only occurs in people already infected with Hepatitis B.",
        "precautions": ["Manage underlying Hepatitis B carefully", "Avoid alcohol", "Regular specialist follow-up"],
    },
    "Hepatitis E": {
        "description": "A liver infection usually spread through contaminated water.",
        "precautions": ["Drink only clean, safe water", "Rest and stay hydrated", "Seek medical care, especially if pregnant"],
    },
    "Hypertension": {
        "description": "Persistently high blood pressure, often called the 'silent' condition due to few symptoms.",
        "precautions": ["Reduce salt intake", "Exercise regularly", "Monitor blood pressure and consult a doctor regularly"],
    },
    "Hyperthyroidism": {
        "description": "Overproduction of thyroid hormone, speeding up the body's metabolism.",
        "precautions": ["Consult an endocrinologist", "Avoid excess iodine intake without guidance", "Manage stress levels"],
    },
    "Hypoglycemia": {
        "description": "Abnormally low blood sugar levels.",
        "precautions": ["Carry a fast-acting sugar source (e.g. juice, candy)", "Eat regular, balanced meals", "Consult a doctor if episodes are frequent"],
    },
    "Hypothyroidism": {
        "description": "Underproduction of thyroid hormone, slowing the body's metabolism.",
        "precautions": ["Consult an endocrinologist for hormone management", "Maintain a balanced diet", "Regular thyroid function monitoring"],
    },
    "Impetigo": {
        "description": "A common, contagious bacterial skin infection causing sores, mainly in children.",
        "precautions": ["Keep affected skin clean and covered", "Avoid scratching and sharing personal items", "Consult a doctor for antibiotic treatment"],
    },
    "Jaundice": {
        "description": "Yellowing of the skin and eyes, usually due to liver dysfunction.",
        "precautions": ["Avoid alcohol and fatty foods", "Stay hydrated", "Seek prompt medical evaluation to find the underlying cause"],
    },
    "Malaria": {
        "description": "A mosquito-borne disease caused by parasites, causing cyclic fevers and chills.",
        "precautions": ["Use mosquito nets and repellents", "Seek prompt antimalarial treatment", "Stay hydrated and rest"],
    },
    "Migraine": {
        "description": "A neurological condition causing intense, recurring headaches, often with nausea and light sensitivity.",
        "precautions": ["Rest in a dark, quiet room during episodes", "Identify and avoid personal triggers", "Consult a neurologist for frequent episodes"],
    },
    "Osteoarthristis": {
        "description": "A degenerative joint condition caused by wear and tear of cartilage over time.",
        "precautions": ["Maintain a healthy weight to reduce joint stress", "Stay gently active", "Consult an orthopedic specialist"],
    },
    "Paralysis (brain hemorrhage)": {
        "description": "Loss of muscle function in part of the body, here caused by bleeding in the brain.",
        "precautions": ["Seek emergency medical care IMMEDIATELY", "Do not give food or water until cleared by medical staff", "Begin physiotherapy as advised once stabilized"],
    },
    "Peptic ulcer diseae": {
        "description": "Open sores that develop on the inner lining of the stomach or upper small intestine.",
        "precautions": ["Avoid NSAIDs (pain relievers) unless prescribed", "Limit spicy food, alcohol, and smoking", "Consult a gastroenterologist"],
    },
    "Pneumonia": {
        "description": "An infection that inflames the air sacs in one or both lungs.",
        "precautions": ["Get plenty of rest and fluids", "Complete the full course of any prescribed antibiotics", "Seek emergency care if breathing becomes difficult"],
    },
    "Psoriasis": {
        "description": "A chronic skin condition causing red, scaly patches, often linked to the immune system.",
        "precautions": ["Moisturize skin regularly", "Avoid known triggers (stress, certain foods)", "Consult a dermatologist for treatment options"],
    },
    "Tuberculosis": {
        "description": "A serious bacterial infection that mainly affects the lungs.",
        "precautions": ["Complete the full prescribed antibiotic course (very important)", "Isolate during the contagious period", "Ensure good ventilation at home"],
    },
    "Typhoid": {
        "description": "A bacterial infection spread through contaminated food or water, causing prolonged fever.",
        "precautions": ["Drink only clean, safe water", "Rest and stay hydrated", "Complete the full antibiotic course as prescribed"],
    },
    "Urinary tract infection": {
        "description": "An infection in any part of the urinary system, most often the bladder.",
        "precautions": ["Drink plenty of water", "Urinate frequently, don't hold it in", "See a doctor for antibiotic treatment"],
    },
    "Varicose veins": {
        "description": "Enlarged, twisted veins, usually appearing in the legs.",
        "precautions": ["Avoid standing/sitting for long periods", "Elevate legs when resting", "Consider compression stockings"],
    },
    "hepatitis A": {
        "description": "A liver infection spread through contaminated food or water, usually resolves on its own.",
        "precautions": ["Rest and stay hydrated", "Avoid alcohol during recovery", "Practice good hand hygiene to avoid spreading it"],
    },
}

# Short descriptions for the 3 "specialist" checkers, shown alongside their results
SPECIALIST_INFO = {
    "Diabetes": "A chronic condition affecting how the body turns food into energy, due to problems with insulin.",
    "Heart Disease": "A range of conditions affecting the heart's structure and function, including blocked or narrowed blood vessels.",
    "Breast Cancer": "Uncontrolled growth of cells in breast tissue. Early detection through screening greatly improves outcomes.",
}
