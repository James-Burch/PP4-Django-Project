// -------------------------------- Code for booking page

// Function to display the availbale times for selected date on click
document.addEventListener("DOMContentLoaded" , function showAvailableTimes() {
    const date = document.getElementById('bookingDate').value;
    if (!date) return alert('Please select a date to proceed');

    // Fetch available times from the back end and implement here with the selected date
    const times = []
    const availableTimesList = document.getElementById('availableTimes');
    // Clear previous times
    availableTimesList.innerHTML = '';

    // Set the date in the time selection section to the selected one
    document.getElementById('selectedDate').textContent = date;

    // Append each booking time to the times list
    times.forEach(time => {
        const listItem = document.createElement('li');
        listItem.className = 'list-group-item d-flex justify-content-between align-items-center';
        listItem.textContent = time;

        // Add a button connected to each booking time
        const bookButton = document.createElement('button');
        bookButton.className = 'btn btn-sm btn-primary';
        bookButton.textContent = 'Book';
        bookButton.onclick = () => alert(`Booking for ${date} at ${time}`);

        listItem.appendChild(bookButton);
        availableTimesList.appendChild(listItem);
    });

    // Show the time selection and hide the date selection for booking
    document.getElementById("checkAvailabilityBtn").addEventListener("click", showAvailableTimes);
    document.getElementById("goBackBtn").addEventListener("click", goBack);
});

// Function to go back to date selection from time selection
function goBack() {
    document.getElementById('dateSelection').style.display = 'block';
    document.getElementById('timeSelection').style.display = 'none';
};

