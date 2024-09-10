
# Movie Recommendation System

This is a **Movie Recommendation System** built using **Streamlit**, **pandas**, and **pickle**. The system allows users to select a movie and receive a list of recommended movies based on similarity.

## Features

- **Movie Selection**: Users can select a movie from a dropdown list of available movie titles.
- **Recommendation Engine**: Based on the selected movie, the system recommends similar movies using precomputed similarity data.
- **Interactive UI**: The system provides an interactive user interface with a visually appealing design, including hover effects and responsive buttons.

## Tech Stack

- **Python**: The core programming language used for the backend logic.
- **Streamlit**: For creating the web application interface.
- **pandas**: For handling and manipulating the movie data.
- **pickle**: For loading precomputed movie data and similarity matrices.

## Prerequisites

Make sure you have the following installed:

- **Python 3.7+**
- **pip** (Python package installer)

### Required Python Libraries:

You can install the necessary libraries by running:

```bash
pip install streamlit pandas
```

If you're using a virtual environment, activate it before installing the dependencies.

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/movierec-system.git
   cd movierec-system
   ```

2. **Install the required libraries**:

   Run the following command to install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download/Place the Data Files**:

   - Ensure that `movie_dict.pkl` (which contains the movie data) and `similarity.pkl` (which contains the similarity matrix) are located in the root directory of your project.

4. **Run the Application**:

   You can run the app using Streamlit by running the following command:

   ```bash
   streamlit run app.py
   ```

5. **Access the Application**:

   Once the app is running, open your browser and navigate to `http://localhost:8501/` to interact with the Movie Recommendation System.

## Usage

1. **Select a Movie**: From the dropdown menu, choose a movie title.
2. **Get Recommendations**: Click the "Recommend" button, and the system will display a list of 5 movies similar to the one you selected.
3. **Responsive Design**: The interface includes hover effects and button animations for an enhanced user experience.

## Example

### Selecting a Movie:

- **Movie Selected**: Avatar

### Recommendations:

- Aliens vs Predator: Requiem
- Aliens
- Falcon Rising
- Independence Day
- Titan A.E.

## Customization

- **CSS Styling**: The application is styled using custom CSS to add hover effects, button transitions, and shadow effects for the recommended movies.
- **Movie Dataset**: You can modify the dataset by updating the `movie_dict.pkl` and `similarity.pkl` files with your own movie data.

## Future Enhancements

- Add support for personalized recommendations based on user preferences.
- Enhance the recommendation algorithm using more advanced techniques such as collaborative filtering or deep learning models.
- Implement additional filters such as genre, year, or rating to refine recommendations.

## Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to improve the Movie Recommendation System.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
