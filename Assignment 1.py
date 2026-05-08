def main():
    # break down the tasks into multiple more manageable and smaller function
    average_sleep_time, sleep_interruptions, sleep_environment_quality, caffeine_consumption, exercise_duration, stress_level = get_user_details()

    sleep_quality_score = calculate_sleep_quality_score(average_sleep_time, sleep_interruptions)

    wsqi = calculate_weighted_sleep_quality_index(sleep_quality_score, sleep_environment_quality, caffeine_consumption, exercise_duration, stress_level)

    get_sleep_quality_group(wsqi, average_sleep_time, sleep_interruptions, caffeine_consumption, exercise_duration)

def get_user_details():
    average_sleep_time = float(input("Enter your average sleep time per night in hours: "))
    sleep_interruptions = int(input("Enter the number of times you wake up during the night: "))
    sleep_environment_quality = int(input("Rate your sleep environment quality on a scale from 1 (poor) to 10 (excellent): "))
    caffeine_consumption = int(input("Enter the average number of cups of coffee or caffeinated drinks you consume per day (0-10): "))
    exercise_duration = int(input("Enter the average number of minutes of exercise per day (0-200): "))
    stress_level = int(input("Rate your stress level on a scale from 1 (low) to 10 (high): "))
    
    return (average_sleep_time, sleep_interruptions, sleep_environment_quality, caffeine_consumption, exercise_duration, stress_level)

def calculate_sleep_quality_score(average_sleep_time, sleep_interruptions):
    sleep_quality_score = ((average_sleep_time - sleep_interruptions) / 8) * 100
    if sleep_quality_score < 0:
        sleep_quality_score = 0
    return sleep_quality_score

def calculate_weighted_sleep_quality_index(sleep_quality_score, sleep_environment_quality, caffeine_consumption, exercise_duration, stress_level):
    if sleep_quality_score == 0:
        wsqi = 0
    else:
        wsqi = (0.5 * sleep_quality_score) + (0.3 * sleep_environment_quality) + (0.2 * (10 - caffeine_consumption)) + (0.1 * (exercise_duration) / 15) - (0.1 * stress_level)
    
    # Replaced int() with round() based on your previous assignment instructions
    return round(wsqi)

def get_sleep_quality_group(wsqi, average_sleep_time, sleep_interruptions, caffeine_consumption, exercise_duration):
    group_value = ""
    advice = ""

    if 0 <= wsqi <= 30:
        group_value = "Poor"
        if average_sleep_time <= 7:
            hours_needed = 8 - average_sleep_time
        advice = f"Increase nightly sleep by {hours_needed} hour(s) to reach 8 hours. \n"
        if sleep_interruptions > 0:
            advice += "Reduce nighttime awakenings by optimizing your bedroom (make it darker, cooler, and quieter) and limiting fluids/alcohol before bed. \n"
        if caffeine_consumption >= 3:
            coffees_needed = caffeine_consumption - 2
            advice += f"Reduce caffeine by {coffees_needed}  to get below 3 cups/day, and avoid caffeine after mid‑afternoon \n"
        if exercise_duration < 15:
             minutes_needed = 15 - exercise_duration
             advice += f"Increase daily exercise by {minutes_needed} minute(s) (ideally earlier in the day) to reach or exceed 15 minutes"
    elif 31 <= wsqi <= 50:
        group_value = "Fair"
    elif 51 <= wsqi <= 70:
        group_value = "Good"
    elif 71 <= wsqi <= 100:
        group_value = "Excellent"

    
    print(f"\nYour Weighted Sleep Quality Index (WSQI) is {wsqi} and is considered {group_value}.")
    
    if advice:
        print(f"Please consider the following recommendation:\n{advice}")

main()