"""Tests for docs_handson functions and their invariants."""

from unittest.mock import Mock

import pytest
import requests

from daic_tutorial_python_envs import docs_handson


@pytest.mark.parametrize(
    ("weight_kg", "height_m"),
    [(50, 1.5), (70, 1.75), (90, 1.9)],
)
def test_calculate_bmi_matches_formula(weight_kg, height_m):
    assert docs_handson.calculate_bmi(weight_kg, height_m) == pytest.approx(
        weight_kg / height_m**2
    )


@pytest.mark.parametrize(
    ("weight_kg", "height_m", "scale"),
    [(50, 1.5, 0.5), (70, 1.75, 2), (90, 1.9, 3.5)],
)
def test_calculate_bmi_is_invariant_when_weight_and_height_scale_together(
    weight_kg, height_m, scale
):
    original_bmi = docs_handson.calculate_bmi(weight_kg, height_m)
    scaled_bmi = docs_handson.calculate_bmi(weight_kg * scale**2, height_m * scale)

    assert scaled_bmi == pytest.approx(original_bmi)


@pytest.mark.parametrize(
    ("weight_kg", "height_m"),
    [(50, 1.5), (70, 1.75), (90, 1.9)],
)
def test_calculate_bmi_scales_linearly_with_weight_and_quadratically_with_height(
    weight_kg, height_m
):
    bmi = docs_handson.calculate_bmi(weight_kg, height_m)

    assert docs_handson.calculate_bmi(2 * weight_kg, height_m) == pytest.approx(2 * bmi)
    assert docs_handson.calculate_bmi(weight_kg, 2 * height_m) == pytest.approx(bmi / 4)


@pytest.mark.parametrize(("weight_kg", "height_m"), [(-1, 1.75), (70, -1)])
def test_calculate_bmi_rejects_negative_inputs(weight_kg, height_m):
    with pytest.raises(ValueError, match="Weight and height must be positive"):
        docs_handson.calculate_bmi(weight_kg, height_m)


def test_calculate_bmi_is_zero_for_zero_weight():
    assert docs_handson.calculate_bmi(0, 1.75) == 0


def test_get_current_weather_requests_coordinates_and_returns_current_weather(
    monkeypatch,
):
    weather = {"temperature": 17.2, "windspeed": 8.3, "weathercode": 1}
    response = Mock()
    response.json.return_value = {"current_weather": weather}
    get = Mock(return_value=response)
    monkeypatch.setattr(docs_handson.requests, "get", get)

    result = docs_handson.get_current_weather(52.37, 4.89)

    get.assert_called_once_with(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": 52.37,
            "longitude": 4.89,
            "current_weather": "true",
        },
    )
    response.raise_for_status.assert_called_once_with()
    assert result == weather


def test_get_current_weather_returns_empty_dict_when_response_has_no_current_weather(
    monkeypatch,
):
    response = Mock()
    response.json.return_value = {}
    monkeypatch.setattr(docs_handson.requests, "get", Mock(return_value=response))

    assert docs_handson.get_current_weather(0, 0) == {}


def test_get_current_weather_propagates_http_errors(monkeypatch):
    response = Mock()
    error = requests.exceptions.HTTPError("request failed")
    response.raise_for_status.side_effect = error
    monkeypatch.setattr(docs_handson.requests, "get", Mock(return_value=response))

    with pytest.raises(requests.exceptions.HTTPError, match="request failed"):
        docs_handson.get_current_weather(52.37, 4.89)
