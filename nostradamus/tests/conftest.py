import datetime
import pytest
import pandas as pd

from random import randint
from django.db import connection


@pytest.fixture()
def sql_conn(request):
    with connection.cursor() as conn:
        request.cls.conn = conn
        yield conn


@pytest.fixture(scope="class")
def host(request):
    host = "http://localhost:8000/"
    request.cls.host = host


@pytest.fixture(scope="class")
def auth_host(request):
    request.cls.auth_host = "http://auth:8080/"


@pytest.fixture
def statistics():
    data = {
        "Comments": [_ for _ in range(100)],
        "Attachments": [_ for _ in range(100)],
        "Time to Resolve": [_ for _ in range(100)],
        "Resolution": ["Done" for _ in range(100)],
    }

    return pd.DataFrame(data=data, columns=list(data.keys()))


@pytest.fixture
def statistics_2():
    data = {
        "Comments": [_ for _ in range(100)],
        "Attachments": [_ for _ in range(100)],
        "Time to Resolve": [_ if _ % 2 == 1 else 10 for _ in range(100)],
        "Resolution": [
            "Done" if _ % 2 == 1 else "Unresolved" for _ in range(100)
        ],
    }

    return pd.DataFrame(data=data, columns=list(data.keys()))


@pytest.fixture
def statistics_3():
    data = {
        "Comments": [_ for _ in range(100)],
        "Attachments": [_ for _ in range(100)],
        "Time to Resolve": [_ for _ in range(100)],
        "Resolution": ["Unresolved" for _ in range(100)],
    }

    return pd.DataFrame(data=data, columns=list(data.keys()))


@pytest.fixture
def dates():
    base_date = datetime.datetime.today()
    created_dates = sorted(
        [base_date - datetime.timedelta(days=days) for days in range(1500)],
        reverse=False,
    )
    resolved_dates = [
        date + datetime.timedelta(randint(0, 3)) for date in created_dates
    ]

    data = {
        "Created": created_dates,
        "Resolved": resolved_dates,
        "Key": [_ for _ in range(1, 1501)],
    }

    return pd.DataFrame(data=data, columns=list(data.keys()))


@pytest.fixture
def train_df():
    data = [
        [
            1,
            "Defect analysis is cool!",
            "defect,analysis,cool",
            4,
            pd.to_datetime("04-01-2020", utc=True, dayfirst=True),
            1,
            0,
            1,
            "Resolved",
            "High",
        ],
        [
            2,
            "Defect analysis",
            "analysis,pizza,coffee",
            6,
            pd.to_datetime("06-01-2020", utc=True, dayfirst=True),
            0,
            1,
            2,
            "Duplicated",
            "Major",
        ],
        [
            3,
            "Coffee is cool!",
            "defect,analysis,coffee",
            8,
            pd.to_datetime("08-01-2020", utc=True, dayfirst=True),
            1,
            0,
            3,
            "Duplicated",
            "Low",
        ],
    ] * 34
    return pd.DataFrame(
        data=data,
        columns=[
            "Key",
            "Description_tr",
            "Elements",
            "Numbers",
            "Dates",
            "Resolution_Duplicated",
            "Resolution_Fixed",
            "Time to Resolve",
            "Resolution",
            "Priority",
        ],
    )


@pytest.fixture
def default_settings():
    return {
        "filters": [
            {"name": "Project", "type": "drop-down"},
            {"name": "Attachments", "type": "numeric"},
            {"name": "Priority", "type": "drop-down"},
            {"name": "Resolved", "type": "date"},
            {"name": "Labels", "type": "string"},
            {"name": "Created", "type": "date"},
            {"name": "Comments", "type": "numeric"},
            {"name": "Status", "type": "drop-down"},
            {"name": "Key", "type": "drop-down"},
            {"name": "Summary", "type": "string"},
            {"name": "Resolution", "type": "drop-down"},
            {"name": "Description", "type": "string"},
            {"name": "Components", "type": "string"},
        ],
        "qa_metrics_filters": [
            {"name": "Project", "type": "drop-down"},
            {"name": "Attachments", "type": "numeric"},
            {"name": "Priority", "type": "drop-down"},
            {"name": "Resolved", "type": "date"},
            {"name": "Labels", "type": "string"},
            {"name": "Created", "type": "date"},
            {"name": "Comments", "type": "numeric"},
            {"name": "Status", "type": "drop-down"},
            {"name": "Key", "type": "drop-down"},
            {"name": "Summary", "type": "string"},
            {"name": "Resolution", "type": "drop-down"},
            {"name": "Description", "type": "string"},
            {"name": "Components", "type": "string"},
        ],
        "predictions_table": [
            {"name": "Key", "is_default": True, "position": 1},
            {"name": "Priority", "is_default": True, "position": 2},
            {"name": "AreaOfTesting", "is_default": True, "position": 3},
            {"name": "TimeToResolve", "is_default": True, "position": 4},
        ],
        "training": {
            "source_field": "",
            "mark_up_entities": [],
            "bug_resolution": [],
        },
    }


@pytest.fixture
def new_settings():
    return {
        "filters": [
            {"name": "Project", "type": "drop-down"},
            {"name": "Attachments", "type": "numeric"},
            {"name": "Priority", "type": "drop-down"},
            {"name": "Resolved", "type": "numeric"},
            {"name": "Labels", "type": "numeric"},
            {"name": "Created", "type": "numeric"},
            {"name": "Comments", "type": "numeric"},
            {"name": "Status", "type": "drop-down"},
            {"name": "Key", "type": "drop-down"},
            {"name": "Summary", "type": "numeric"},
            {"name": "Resolution", "type": "drop-down"},
            {"name": "Description", "type": "numeric"},
            {"name": "Components", "type": "numeric"},
        ],
        "qa_metrics_filters": [
            {"name": "Project", "type": "drop-down"},
            {"name": "Attachments", "type": "numeric"},
            {"name": "Priority", "type": "drop-down"},
            {"name": "Resolved", "type": "numeric"},
            {"name": "Labels", "type": "numeric"},
            {"name": "Created", "type": "numeric"},
            {"name": "Comments", "type": "numeric"},
            {"name": "Status", "type": "drop-down"},
            {"name": "Key", "type": "drop-down"},
            {"name": "Summary", "type": "numeric"},
            {"name": "Resolution", "type": "drop-down"},
            {"name": "Description", "type": "numeric"},
            {"name": "Components", "type": "numeric"},
        ],
        "predictions_table": [
            {"name": "Key", "is_default": True, "position": 1},
            {"name": "Priority", "is_default": True, "position": 2},
            {"name": "AreaOfTesting", "is_default": True, "position": 3},
            {"name": "TimeToResolve", "is_default": True, "position": 4},
            {"name": "TestField", "is_default": False, "position": 5},
        ],
        "training": {
            "source_field": "test_mark_up_source",
            "mark_up_entities": [
                {
                    "area_of_testing": "test_area_1",
                    "entities": ["test1", "test2"],
                },
                {
                    "area_of_testing": "test_area_2",
                    "entities": ["test1", "test2"],
                },
            ],
            "bug_resolution": [
                {"metric": "Resolution", "value": "One"},
                {"metric": "Resolution", "value": "Two"},
            ],
        },
    }


@pytest.fixture(scope="class")
def predictions_table_settings(request):
    request.cls.settings = [
        {"name": "Issue Key", "is_default": True, "position": 1},
        {"name": "Priority", "is_default": True, "position": 2},
        {"name": "Area of Testing", "is_default": True, "position": 3},
        {"name": "Time to Resolve", "is_default": True, "position": 4},
        {"name": "Summary", "is_default": True, "position": 5},
        {"name": "Resolution: Done", "is_default": True, "position": 6},
    ]


@pytest.fixture(scope="class")
def training_parameters(request):
    request.cls.training_parameters = {
        "areas_of_testing": ["test", "Other"],
        "Resolution": {"Done": ["not Done", "Done"]},
        "Priority": ["Blocker", "Critical", "Major", "Minor"],
        "Time to Resolve": [
            "0-1.0",
            "0.999-1.0",
            "2.0-19.0",
            "20.0-127.0",
            ">127.0",
        ],
        "binary": [0, 1],
    }


@pytest.fixture(scope="class")
def default_filters(request):
    request.cls.default_filters = [
        {"name": "Project", "type": "drop-down"},
        {"name": "Attachments", "type": "numeric"},
        {"name": "Priority", "type": "drop-down"},
        {"name": "Resolved", "type": "numeric"},
        {"name": "Labels", "type": "numeric"},
        {"name": "Created", "type": "numeric"},
        {"name": "Comments", "type": "numeric"},
        {"name": "Status", "type": "drop-down"},
        {"name": "Key", "type": "drop-down"},
        {"name": "Summary", "type": "numeric"},
        {"name": "Resolution", "type": "drop-down"},
        {"name": "Description", "type": "numeric"},
        {"name": "Components", "type": "numeric"},
    ]


@pytest.fixture(scope="class")
def JQL(request):
    request.cls.JQL = (
        'issuetype = Bug AND priority = "Minor" AND assignee in (EMPTY)'
    )


@pytest.fixture
def correct_result_statistics():
    return {
        "Comments": {
            "max": "99",
            "min": "0",
            "mean": "50",
            "std": "29",
        },
        "Attachments": {
            "max": "99",
            "min": "0",
            "mean": "50",
            "std": "29",
        },
        "Time to Resolve (TTR)": {
            "max": "99",
            "min": "0",
            "mean": "50",
            "std": "29",
        },
    }


@pytest.fixture(scope="class")
def result_significant_metrics(request):
    request.cls.result_significant_terms = {
        "chosen_metric": "Resolution Unresolved",
        "metrics": [
            "Resolution Unresolved",
            "Resolution Done",
            "Resolution Rejected",
            "Priority Minor",
            "Priority Major",
        ],
        "terms": {"description_tr": 0.0},
    }


@pytest.fixture(scope="class")
def settings_aot_metrics(request):
    request.cls.settings_for_aot = {
        "source_field": "Priority",
        "mark_up_entities": [
            {"area_of_testing": "AOT1", "entities": ["Major"]}
        ],
    }


@pytest.fixture(scope="class")
def report_fields(request):
    request.cls.report_fields = [
        "Project",
        "Key",
        "Status",
        "Priority",
        "Created",
        "Reporter",
        "Assignee",
    ]


@pytest.fixture(scope="class")
def chatbot_url(request):
    request.cls.chatbot_url = "http://localhost:5005/webhooks/rest/"


@pytest.fixture(scope="class")
def predictions_table_fields(request):
    request.cls.predictions_table_fields = [
        "Issue Key",
        "Priority",
        "Area of Testing",
        "Time to Resolve",
        "Summary",
        "Resolution: Done",
    ]


@pytest.fixture()
def qa_metrics_route(request):
    request.cls.qa_metrics_route = "qa_metrics/"


@pytest.fixture()
def analysis_and_training_route(request):
    request.cls.analysis_and_training_route = "analysis_and_training/"


@pytest.fixture()
def settings_route(request):
    request.cls.settings_route = "settings/"


@pytest.fixture()
def description_assessment_route(request):
    request.cls.description_assessment_route = "description_assessment/"


@pytest.fixture()
def auth_route(request):
    request.cls.auth_route = "auth/"
