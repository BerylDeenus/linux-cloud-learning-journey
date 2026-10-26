def check(percent: float) -> str:
    if percent < 0 or percent > 100:
        raise ValueError("the percent should be between 0 and 100")
    if percent >= 90:
        return "CRITICAL"
    if percent >= 75:
        return "WARNING"
    return "LOOKS FINE"
