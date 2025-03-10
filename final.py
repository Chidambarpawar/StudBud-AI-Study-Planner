from datetime import datetime, timedelta

class StudBudAIStudyPlanner:
    def __init__(self, name, sleep_schedule, extracurriculars, school_time, weekly_study_hours):
        self.name = name
        self.sleep_schedule = sleep_schedule  # e.g., "11 PM - 7 AM"
        self.extracurriculars = extracurriculars  # e.g., ["Football", "Music"]
        self.school_time = school_time  # e.g., "8 AM - 3 PM, 1 hour travel"
        self.weekly_study_hours = weekly_study_hours  # e.g., 15 hours per week
        self.subjects = []  # List to store subjects e.g., ["Maths", "Science", "History"]

    def get_subjects(self, num_subjects):
        for i in range(num_subjects):
            subject = input(f"Enter subject {i + 1} (e.g., Maths, Science, History): ")
            self.subjects.append(subject)

    def generate_study_plan(self, start_date, end_date):
        study_plan = {}
        current_date = start_date
        delta = timedelta(days=1)

        day_counter = 1
        while current_date <= end_date:
            day_of_week = current_date.strftime("%A")
            study_plan[f"Day {day_counter} - {current_date.strftime('%Y-%m-%d')}"] = self._generate_daily_schedule(day_of_week, current_date)
            current_date += delta
            day_counter += 1

        return study_plan

    def _generate_daily_schedule(self, day_of_week, current_date):
        daily_schedule = []
        available_time = self._calculate_available_time(day_of_week)
        study_hours_per_day = self.weekly_study_hours / 7  # Distribute study hours evenly across the week
        start_time = datetime.strptime("7:00 PM", "%I:%M %p")  # Study starts at 7:00 PM

        # Assign subjects to individual days
        subject_index = (current_date.weekday()) % len(self.subjects)
        subject = self.subjects[subject_index]
        study_duration = min(study_hours_per_day, 4)  # Cap the study duration to 4 hours (7 PM to 11 PM)

        study_session = {
            "subject": subject,
            "duration": f"{study_duration:.1f} hours",
            "method": self._recommend_study_method(subject, current_date),
            "time": self._format_time(start_time),
            "end_time": self._format_time(start_time + timedelta(hours=study_duration))
        }

        # Increment the start time for the next session
        start_time += timedelta(hours=study_duration)
        daily_schedule.append(study_session)

        return daily_schedule

    def _calculate_available_time(self, day_of_week):
        # Assuming study time is fixed from 7 PM to 11 PM, always 4 hours
        return 4

    def _recommend_study_method(self, subject, current_date):
        # Define a list of study methods for each subject
        study_methods = {
            "Maths": [
                "Solve practice problems and review formulas",
                "Watch video tutorials on challenging topics",
                "Create flashcards for key concepts",
                "Work on past exam papers"
            ],
            "Science": [
                "Watch video lectures and conduct experiments",
                "Read and summarize textbook chapters",
                "Create mind maps for complex topics",
                "Discuss concepts with a study group"
            ],
            "History": [
                "Read textbooks and create timelines",
                "Watch historical documentaries",
                "Write essays on key events",
                "Quiz yourself on important dates and facts"
            ]
        }

        # Get the list of methods for the selected subject
        methods = study_methods.get(subject, ["Read and summarize notes"])

        # Use the day of the week to select a method (cycle through the list)
        day_index = current_date.weekday()  # Monday = 0, Sunday = 6
        method_index = day_index % len(methods)  # Ensure the index is within the list range
        return methods[method_index]

    def _format_time(self, start_time):
        return start_time.strftime("%I:%M %p")

    def display_study_plan(self, study_plan):
        print(f"\nHello, {self.name}! 🌟 Here's your personalized study plan to help you achieve your goals:\n")
        print("Here’s how your study plan is designed:")
        print("- It balances your study time with your daily routine.")
        print("- It assigns subjects to specific days to ensure a balanced workload.")
        print("- It recommends effective study methods to help you learn better.\n")

        # Generate output like the desired format
        for date, schedule in study_plan.items():
            print(f"📅 {date}:")
            print("----------------------------------------")
            for session in schedule:
                print(f"  - Subject: {session['subject']}")
                print(f"    Duration: {session['duration']}")
                print(f"    Method: {session['method']}")
                print(f"    Start Time: {session['time']}")
                print(f"    End Time: {session['end_time']}")
            print("\nKeep going! 🚀")

# Input from User
print("Welcome to StudBud AI Study Planner! 🎓")
print("Let's create a personalized study plan tailored just for you.\n")

name = input("Enter your name: ")
sleep_schedule = input("What does your usual sleep schedule look like? (e.g., 11 PM - 7 AM): ")
extracurriculars = input("Extra-curricular activities? (e.g., Football, Music): ").split(", ")
school_time = input("How long do you spend at, and travelling to/from school? (e.g., 8 AM - 3 PM, 1 hour travel): ")
weekly_study_hours = float(input("How long, weekly, do you want to dedicate towards study? (e.g., 15): "))

# Asking how many subjects to study
num_subjects = int(input("How many subjects do you want to study? "))
planner = StudBudAIStudyPlanner(name, sleep_schedule, extracurriculars, school_time, weekly_study_hours)

# Get subjects from the user
planner.get_subjects(num_subjects)

# Generate Study Plan
start_date = datetime(2025, 3, 9)  # Start date
end_date = datetime(2025, 3, 15)  # End date

study_plan = planner.generate_study_plan(start_date, end_date)
planner.display_study_plan(study_plan)

# Final Message
print(f"Thank you for using StudBud AI Study Planner, {name}! 🚀")
print("Remember, consistency is key to success! Keep pushing forward.")