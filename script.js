document.getElementById("study-planner-form").addEventListener("submit", function (e) {
    e.preventDefault();

    // Get form inputs
    const name = document.getElementById("name").value;
    const sleepSchedule = document.getElementById("sleep-schedule").value;
    const extracurriculars = document.getElementById("extracurriculars").value;
    const schoolTime = document.getElementById("school-time").value;
    const weeklyStudyHours = parseFloat(document.getElementById("weekly-study-hours").value);
    const numSubjects = parseInt(document.getElementById("num-subjects").value);
    const subjects = Array.from(document.querySelectorAll("#subjects-container input")).map(input => input.value);

    // Prepare data to send to the backend
    const data = {
        name,
        sleep_schedule: sleepSchedule,
        extracurriculars: extracurriculars,
        school_time: schoolTime,
        weekly_study_hours: weeklyStudyHours,
        subjects: subjects
    };

    // Send data to the backend
    fetch("http://127.0.0.1:5000/generate-plan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(studyPlan => {
            // Display study plan
            const outputDiv = document.getElementById("study-plan-output");
            outputDiv.innerHTML = `
                <h3>Hello, ${studyPlan.name}! 🌟</h3>
                <p>Here's your personalized study plan:</p>
                <ul>
                    ${Object.keys(studyPlan.plan).map(date => `
                        <li>
                            <strong>${date}:</strong>
                            <ul>
                                ${studyPlan.plan[date].map(session => `
                                    <li>
                                        <strong>Subject:</strong> ${session.subject}<br>
                                        <strong>Duration:</strong> ${session.duration}<br>
                                        <strong>Method:</strong> ${session.method}<br>
                                        <strong>Time:</strong> ${session.time} to ${session.end_time}
                                    </li>
                                `).join("")}
                            </ul>
                        </li>
                    `).join("")}
                </ul>
                <p>Keep going! 🚀</p>
            `;
        })
        .catch(error => console.error("Error:", error));
});