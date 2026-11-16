# Algae-Bioreactor-App

Algae Bioreactor Management App

A Django web application designed for students and teachers for managing algae bioreactors, algae strains, laboratory equipment, and nutrient feeding schedules.

## Prerequisites
- **Python 3.13.5** (or compatible Python 3.13+ version)
- **pip** (Python package installer)

## Installation & Setup

Follow these steps to set up and run the project locally:

1. **Get the Project Files**
Choose one of the following options to get the project locally:

* Option A: Download ZIP (Recommended for quick setup)
  1. Click the green **`<> Code`** button at the top of this GitHub repository.
  2. Select **`Download ZIP`** and extract the archive to a folder on your computer.
  3. Open the extracted folder in your IDE (e.g., PyCharm) or navigate to it in your terminal.


* Option B: Clone the Repository via Git
   ```bash
   git clone https://github.com/angelovan/Django-Basics-Retake-Exam---Algae-Bioreactor-App.git
   cd Django-Basics-Retake-Exam---Algae-Bioreactor-App
   ```

2. **Create and activate a virtual environment:**
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS / Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Features
- **Bioreactor Management:** Users can register or update individual bioreactor units, cabinet (classroom) locations, setup dates, and observation notes.
- **Search & Sorting:** Sort bioreactors by name or setup date directly from the list view.
- **Algae Strains:** Three specific algae cultures are available for selection when creating a bioreactor unit - *Chlorella vulgaris*, *Arthrospira platensis (Spirulina)*, and *Scenedesmus obliquus*.
- **Equipment:** Multiple pieces of lab equipment can be added and used for the created bioreactor units via Many-to-Many relationships.
- **Feeding Schedules:** Keep tabs on nutrient feed intervals, completion dates, and cycle notes. The next feeding due date is automatically calculated based on the selected algae strain's feed interval days once the current feed is completed.
- **Custom Template Filters & Reusable Partials:** Uses custom template filters for dynamic feeding status formatting and modular template partials for clean navigation and layout structure.

## Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (Time-zone aware dates using `DateField` and `timezone.localdate`)

## How to Use the App Efficiently

- **Add Algae Strains:** Start by adding your algae strain(s) and updating the optimal pH and temperature in the template (refer to the scientific notes below).
- **Add Equipment:** Log your equipment inventory. Examples include LED Growth Lights, Air Pumps, Submersible Mini Aquarium Heaters, Wide-Range pH Test Strips, Digital Aquarium Thermometers, Aquarium Airline Tubing & Check Valve, 10mL Plastic Syringes, and Pipettes.
- **Create a Bioreactor Unit:** Set up and register individual bioreactor units.
- **Manage Units:** Once created, bioreactor units can be easily edited or deleted. Use the "View" button to check their feeding schedule and any student observational notes.
- **Track Feedings:** Document completed feedings with optional notes. Once a feed is marked as completed, the app automatically calculates and displays the next scheduled feed date. 


## Algae Species Characteristics

- **Chlorella vulgaris** 
  * *Optimal Conditions:* Temperature 25°C – 30°C | pH 6.5 – 7.5 | Feeding interval: 5 days.
  * *Resilience:* Highly resilient. Can survive temperature drops down to 10°C and pH swings from 5.0 to 9.0 without dying.
  * *Description:* A unicellular, chlorophyte microalga characterized by its spherical morphology and efficient photosynthetic apparatus. Isolated in 1890, this organism served as a primary model for elucidating the light-independent reactions of photosynthesis.

- **Arthrospira platensis (Spirulina)** 
  * *Optimal Conditions:* Temperature 35°C – 38°C | pH 9.0 – 11.0 | Feeding interval: 7 days.
  * *Resilience:* High pH acts as a natural shield, preventing contamination from other algae or bacteria in a classroom setting.
  * *Description:* A filamentous, multicellular, photosynthetic cyanobacterium colloquially designated as Spirulina.

- **Scenedesmus obliquus** 
  * *Optimal Conditions:* Temperature 20°C – 28°C | pH 7.0 – 8.0 | Feeding interval: 10 days.
  * *Resilience:* Thrives at standard room temperature, making it excellent for cooler classrooms that turn off heating over the weekend.
  * *Description:* A highly adaptive freshwater green alga found globally in common ponds, lakes, and puddles, making it a staple organism for ecological studies. Rather than living as single cells, it organizes into distinct, symmetrical colonies called coenobia, where four or eight football-shaped cells align side-by-side like a tiny log raft.
  
## Feeding Schedule & Premature Feeding Validation

Each algae species has a configurable feeding interval (`feed_interval_days`, defaulting to 7 days). When a feeding record is created or updated for a bioreactor unit, the application dynamically calculates the next scheduled feeding date (`due_date`) based on the assigned species' interval.

To protect cultures from overfeeding, the feeding form enforces a validation check:
- If an attempt is made to log a new feeding record earlier than the calculated next due date, the submission is blocked.
- A descriptive warning banner is displayed to the user specifying the required feeding interval for that algae strain and reminding them of the exact next scheduled feeding date (`DD-MMM-YYYY`).

## Sample Images & Image Credits

For testing purposes, three sample algae culture images are provided in the `algae_culture_images/` directory at the root of the project. You can upload these files when creating or updating bioreactor units to test the file upload functionality:

- **`Chlorella_algae_culture.PNG`**
  Source: [Google Images / Algae Culture Reference](https://share.google/6Ii0lVzpeWwtS7G62)
- **`Scenedesmus_obliquus_culture.jpg`**
  Source: [Google Images / Scenedesmus obliquus Reference](https://share.google/oRm8opa9hzChYS7Qq)
- **`Spirulina_algae_culture.jpg`**  
  Source: [Grow Organic Spirulina (Algae Research Supply)](https://grow-organic-spirulina.com/shop/spirulina-culture-kit-algae-research-supply/)