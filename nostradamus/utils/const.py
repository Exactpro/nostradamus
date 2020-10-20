from sklearn.feature_extraction import text

WEEKDAYS_SW = [
    "monday",
    "mon",
    "tuesday",
    "tue",
    "wednesday",
    "wed",
    "thursday",
    "thu",
    "friday",
    "fri",
    "saturday",
    "sat",
    "sunday",
    "sun",
]

MONTHS_SW = [
    "january",
    "jan",
    "february",
    "feb",
    "march",
    "mar",
    "april",
    "apr",
    "may",
    "june",
    "jun",
    "july",
    "jul",
    "august",
    "aug",
    "september",
    "sep",
    "october",
    "oct",
    "november",
    "nov",
    "december",
    "dec",
]

STOP_WORDS = text.ENGLISH_STOP_WORDS.difference(
    ("see", "system", "call")
).union(WEEKDAYS_SW, MONTHS_SW, ["having", "couldn"])

DEFAULT_PREDICTIONS_TABLE_FIELDS = [
    "Issue Key",
    "Priority",
    "Area of Testing",
    "Time to Resolve",
    "Summary",
]

TRAINING_SETTINGS_FILENAME = "training_settings.pkl"
TRAINING_PARAMETERS_FILENAME = "training_parameters.pkl"
TOP_TERMS_FILENAME = "top_terms.pkl"

UNRESOLVED_BUGS_FILTER = {
    "name": "Resolution",
    "filtration_type": "string",
    "current_value": "Unresolved",
    "exact_match": True,
}

MANDATORY_FIELDS = [
    "Description_tr",
    "Time to Resolve",
    "Resolution",
    "Attachments",
    "Comments",
    "Resolved",
    "Resolution",
    "Created",
    "Updated",
    "Assignee",
    "Reporter",
    "Key",
]
