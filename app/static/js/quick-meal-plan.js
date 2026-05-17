// JavaScript to handle the date change event on the quick meal plan form, and redirect to the same form with the selected date as a query parameter to pre-fill the form with existing meal plans for that date
document.addEventListener('DOMContentLoaded', function() {
    const mealDateInput = document.getElementById('meal_date');
        if (mealDateInput) {
            mealDateInput.addEventListener('change', function() {
                const selectedDate = this.value;

                if (selectedDate) {
                    const url = new URL(window.location.href);
                    url.searchParams.set('meal_date', selectedDate);
                    window.location.href = url.toString();
                }   
            });
        }
    }
);