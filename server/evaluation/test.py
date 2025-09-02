import pathlib

import dotenv
from google.adk.evaluation import AgentEvaluator
import pytest


@pytest.fixture(scope="session", autouse=True)
def load_env():
    dotenv.load_dotenv()


def test_inspire():
    """Test the agent's basic ability on a few examples."""
    AgentEvaluator.evaluate(
        "travel_concierge",
        str(pathlib.Path(__file__).parent / "data/inspire.test.json"),
        num_runs=4,
        initial_session_file=str(pathlib.Path(__file__).parent
                                 / "itinerary_empty_default.json")
    )


def test_pretrip():
    """Test the agent's basic ability on a few examples."""
    AgentEvaluator.evaluate(
        "travel_concierge",
        str(pathlib.Path(__file__).parent / "data/pretrip.test.json"),
        num_runs=4,
        initial_session_file=str(pathlib.Path(__file__).parent
                                 / "itinerary_seattle_example.json")
    )


def test_intrip():
    """Test the agent's basic ability on a few examples."""
    AgentEvaluator.evaluate(
        "travel_concierge",
        str(pathlib.Path(__file__).parent / "data/intrip.test.json"),
        num_runs=4,
        initial_session_file=str(pathlib.Path(__file__).parent
                                 / "itinerary_seattle_example.json")
    )
    