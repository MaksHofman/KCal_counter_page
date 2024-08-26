import sqlite3
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def get_date_now() -> datetime:
    return datetime.now()


def get_kcal_goal_from_db(email, database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT goal FROM users WHERE email = "{email}";''')
    queary_output = cursor.fetchall()
    conn.close()
    return queary_output[0][0]


# zwraca wartosci
def get_progress_update(email: str, type: str, database_path) -> tuple[list, list]:
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT progress_update, progress_update_date FROM progress
                       WHERE user_id = "{email}" AND progress_type="{type}"
                       ORDER BY progress_update_date asc;''')
    queary_output = cursor.fetchall()
    conn.close()
    output_int = []
    output_date = []
    for out in queary_output:
        output_int.append(out[0])
        output_date.append(out[1])
    return output_int, output_date


def add_new_record_to_progress(email, int_record, type_record, database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    now = get_date_now()
    print(email)
    cursor.execute(f'''INSERT INTO progress (user_id, progress_update, progress_update_date, progress_type)
                        VALUES ('{email}','{int(int_record)}','{now}','{str(type_record)}');''')
    conn.commit()
    conn.close()


def make_graf_out_of_progress(output_int, output_date, type):
    dates = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f').date() for date in output_date]

    if not dates:
        # Generate a plot with a message indicating no data
        plt.figure(figsize=(10, 5), facecolor='#0f3057')

        # Set the background and title style
        plt.gca().set_facecolor('#ffffff')
        plt.text(0.5, 0.5, 'No data entered yet', horizontalalignment='center', verticalalignment='center',
                 fontsize=18, color='#ffffff', transform=plt.gca().transAxes,
                 fontname='Segoe UI')

        plt.title('Progress of Measurements Over Time', fontsize=20, color='#ffffff', fontname='Segoe UI')

        # Hide the axes
        plt.axis('off')

        # Save the plot
        plt.savefig(f'static/plots_saved_to_display/no_data_{type}.png', bbox_inches='tight', facecolor='#0f3057')
        return (f'no_data_{type}.png')

    plt.figure(figsize=(10, 5))
    plt.plot(dates, output_int, marker='o', linestyle='-', color='b')

    plt.gcf().autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))

    plt.title(f'Progress of {type} Measurements Over Time')
    plt.xlabel('Date')
    plt.ylabel(type)
    plt.grid(True)
    plt.savefig(f'static/plots_saved_to_display/{dates[-1]}{type}.png')
    return (f'{dates[-1]}{type}.png')


def calculate_bmr(weight, height, age, gender):
    """Calculate Basal Metabolic Rate (BMR) using Mifflin-St Jeor Equation"""
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        # raise ValueError("Gender not recognized. Use 'male' or 'female'.")
        # if gender is not set yet return 0
        return 0
    return int(round(bmr, 0))


def calculate_tdee(bmr, activity_level):
    """Calculate Total Daily Energy Expenditure (TDEE)"""

    if bmr == 0:
        return 'Not available yet. Visit <a href="/my_page">My Page</a> to update your account'

    activity_factors = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'super active': 1.9
    }

    if activity_level not in activity_factors:
        raise ValueError(
            "Activity level not recognized. Choose from 'sedentary', 'lightly active', 'moderately active', 'very active', 'super active'.")

    tdee = bmr * activity_factors[activity_level]
    return int(round(tdee, 0))


def calculate_bulking_calories(tdee, bulking_percentage):
    """Calculate calories for bulking phase"""
    bulking_calories = tdee + (tdee * bulking_percentage)
    return bulking_calories


def calculate_cutting_calories(tdee, cutting_percentage):
    """Calculate calories for cutting phase"""
    cutting_calories = tdee - (tdee * cutting_percentage)
    return cutting_calories


def kcal_calkulator(mass, height, age):
    print(mass, height, age)


if __name__ == "__main__":
    output_int, output_date = get_progress_update("qw.qw@gmail.com", "mass")
    make_graf_out_of_progress(output_int, output_date, "mass")
    print(output_int + output_date)
