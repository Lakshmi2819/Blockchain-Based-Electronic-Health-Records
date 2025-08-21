def process_fhir_data(fhir_record):
    # Basic FHIR handling (e.g., extract Patient ID and Observation)
    patient_id = fhir_record.get("id")
    birth_date = fhir_record.get("birthDate")
    return {"patient_id": patient_id, "birth_date": birth_date}
