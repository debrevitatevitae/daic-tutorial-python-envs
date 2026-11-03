import requests  # noqa: D100


def get_current_weather(lat: float, lon: float, units: str = "metric") -> dict:  # noqa: ARG001
    """Retrieve current weather data from the Open-Meteo public API.

    Args:
        lat: Latitude of the location (e.g. 52.37 for Amsterdam).
        lon: Longitude of the location (e.g. 4.89 for Amsterdam).
        units: Unit system to use. Only "metric" is supported for now.

    Returns:
        Dictionary with current temperature (°C), windspeed (km/h), and weather code.

    Raises:
        requests.exceptions.RequestException: If the HTTP request fails.

    Example:
        ```python
        data = get_current_weather(52.37, 4.89)
        print(data["temperature"])  # e.g., 17.2
        ```
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": "true"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("current_weather", {})


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate the Body Mass Index (BMI) given weight and height.

    Args:
        weight_kg: Weight in kilograms.
        height_m: Height in meters.

    Returns:
        The calculated BMI.

    Raises:
        ValueError: If weight or height is negative.

    Example:
        ```python
        bmi = calculate_bmi(70, 1.75)
        print(bmi)  # e.g., 22.86
        ```
    """
    if weight_kg < 0 or height_m < 0:
        err_msg = "Weight and height must be positive."
        raise ValueError(err_msg)
    return weight_kg / (height_m**2)
