from rest_framework.exceptions import APIException

DEFAULT_WARNING_CODE = 209


class BaseAPIWarning(APIException, Warning):
    status_code = DEFAULT_WARNING_CODE


class CannotAnalyzeDescriptionWarning(BaseAPIWarning):
    default_detail = (
        "Oops! Description can't be analyzed. Please check the text."
    )
    default_code = "description_cant_be_analyzed"


class BugsNotFoundWarning(BaseAPIWarning):
    default_detail = "Oops! Bugs haven't been uploaded yet."
    default_code = "bugs_not_found"


class LittleDataToCalculate(BaseAPIWarning):
    default_detail = "Oops! Too little data to calculate."
    default_code = "too_little_data"


class DescriptionAssessmentUnavailableWarning(BaseAPIWarning):
    default_detail = (
        "Description assessment is unavailable. Please, train models."
    )
    default_code = "description_assessment_unavailable"


class PredictionsNotReadyWarning(BaseAPIWarning):
    default_detail = "Making predictions... Please, try again later."
    default_code = "prediction_appending"


class ModelsNotTrainedWarning(BaseAPIWarning):
    default_detail = "Models are not trained. Please, train models."
    default_code = "not_trained_models"


class SignificantTermsCantCalculateWarning(BaseAPIWarning):
    default_detail = "Significant Terms can't be calculated. There should be at least 100 bugs."
    default_code = "significant_terms_cant_calculate"


class SignificantTermsLessOnePercentWarning(BaseAPIWarning):
    default_detail = "Significant Terms couldn't be calculated on a metric representing less than 1% from the whole dataset."
    default_code = "significant_terms_cant_calculate_less_one_percent"


class SignificantTermsMetricDoesntExist(BaseAPIWarning):
    default_detail = (
        "Significant Terms can't be calculated. Metric doesn't exist."
    )
    default_code = "significant_terms_metric_doesnt_exist"
